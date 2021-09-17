# Demo generative art project designed to provide a solid foundation for creating generative art in Python

import cairo
import math
import random
from datetime import datetime


def draw_background(cr, colour, image_width, image_height):
    cr.set_source_rgb(colour[0], colour[1], colour[2])
    cr.rectangle(0, 0, image_width, image_height)
    cr.fill()


def draw_shape(
        cr,
        colour,
        position,
        rotation,
        square_size,
        line_thickness
):
    cr.set_source_rgb(colour[0], colour[1], colour[2])
    cr.set_line_width(line_thickness)
    # Rotate the shape by moving to the centre point and rotating the whole screen, then moving back
    cr.translate(position[0], position[1])
    cr.rotate(rotation * math.pi / 180)
    cr.translate(-position[0], -position[1])

    # Draw a rectangle at the specified location and with the specified size
    cr.rectangle(
        position[0] - square_size / 2,
        position[1] - square_size / 2,
        square_size,
        square_size
    )
    cr.stroke()

    # Rotate back to the original rotation
    cr.translate(position[0], position[1])
    cr.rotate(-rotation * math.pi / 180)
    cr.translate(-position[0], -position[1])


def generate_image():
    start = datetime.now()
    print("Generating art")

    # Image Variable Constraints
    image_size = 1000
    squares_across = 10
    background_colour = (0, 0, 0)
    colours_min_max = [(0, 0, 0), (1, 1, 0)]
    size_min_max = [0, 1]
    rotation_min_max = [0, 90]
    line_thickness_min_max = [1, 5]

    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, image_size, image_size)
    cr = cairo.Context(ims)
    draw_background(cr, background_colour, image_size, image_size)

    # Loop through and draw every square
    for y in range(0, squares_across):
        for x in range(0, squares_across):
            # Specify the size of the squares in pixels determined by image_size
            max_square_size = image_size / squares_across
            size_multiplier = random.uniform(size_min_max[0], size_min_max[1])
            square_size = size_multiplier * max_square_size
            # Set the position of the square in pixels, calculated from the image size
            position = [
                x * max_square_size + max_square_size / 2,
                y * max_square_size + max_square_size / 2
            ]
            # Select a random colour from the specified range
            colour = (
                random.uniform(colours_min_max[0][0], colours_min_max[1][0]),
                random.uniform(colours_min_max[0][1], colours_min_max[1][1]),
                random.uniform(colours_min_max[0][2], colours_min_max[1][2])
            )
            # Set the rotation from the specified range
            rotation = random.uniform(rotation_min_max[0], rotation_min_max[1])
            # Set line thickness from the specified range
            line_thickness = random.uniform(line_thickness_min_max[0], line_thickness_min_max[1])
            draw_shape(
                cr,
                colour,
                position,
                rotation,
                square_size,
                line_thickness
            )

    ims.write_to_png('Generated_Image.png')
    print("Finished: " + str(datetime.now() - start))


if __name__ == '__main__':
    generate_image()
