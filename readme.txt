ASSIGNMENT 02
MODULE CODE = CS6102
MODULE NAME = Graphics For Interactive Media


ASSIGNMENT TOPIC:
A4 poster composition on the theme 'JAZZ' using GIMP image editor along with a python script to generate the same.

- MY THEME

1. My poster is based on a vintage theme. Instead of having multiple images, I chose to have two main images, one as a background having a vintage texture and one of a jazz artist playing saxophone, rest of the images have been used for giving the bottom side of the poster, a subtle musical texture and for the text part. This will give the viewer an instant impression of the theme, the poster is based on.

2. All the images have been pre processed using GIMP only. This includes Rotation, Flip, Saturation, Color Balance and Level.

3. For the UI interface part, users can only choose the provided images in order to generate the poster, the text and font is already specified according to the theme and the aesthetics of the poster, but still can be changed according to one's preference.

- FILTERS AND TOOLS USED (My contribution)

1. ROTATION code = pdb.gimp_image_rotate(image, rotate_type) #used for Image 01

2. FLIP code = pdb.gimp_item_transform_flip_simple(item, flip_type, auto_center, axis) #used for Image 03

3. DESATURATE code = pdb.gimp_desaturate_full(drawable, desaturate_mode) #used for Image 02, 03 and 04

4. COLOR LEVELS code = pdb.gimp_drawable_levels(drawable, channel, low_input, high_input, clamp_input, gamma, low_output, high_output, clamp_output) #used for Image 02 and 03

5. COLOR BALANCE code = pdb.gimp_color_balance(drawable, transfer_mode, preserve_lum, cyan_red, magenta_green, yellow_blue) #used for Image 04

6. TEXT JUSTIFICATION code = pdb.gimp_text_layer_set_justification(layer, justify) #used for the text layers
