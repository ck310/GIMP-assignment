# !/usr/bin/env python
from gimpfu import *


'''
write the python function to achieve filterin
'''

def Jazz_Poster(file1, file2, file3, file4, file5, str1, font1, str2, font2, str3, font3):# args are following soon
       # Make a new image background
       posterW, posterH = 2480, 3508
       posterImage = gimp.Image(posterW, posterH, RGB)
       gimp.Display(posterImage)
              
       # Make the colors
       bgcolor = gimpcolor.RGB(0,0,0)
       gimp.set_background(bgcolor)
       fcolor = gimpcolor.RGB(0,0,0)

       # Make background
       backLayer = gimp.Layer(posterImage, "background",posterW, posterH, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(backLayer)
       pdb.gimp_drawable_fill(backLayer, 1)

       # Image 1 - load, scale, copy, make_layer, paste, anchor, translate
       image1 = pdb.file_jpeg_load(file1, file1)
       pdb.gimp_image_rotate(image1, 0)
       pdb.gimp_image_scale(image1, posterW-216, posterH-113)
       pdb.gimp_edit_copy(image1.layers[0])
       layer1 = gimp.Layer(posterImage, "image1",posterW-216, posterH-113, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer1)
       floatingLayer = pdb.gimp_edit_paste(layer1, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer1.translate(posterW/25, posterH/50)

       # Image 2 - load, scale, copy, make_layer, paste, anchor, translate
       image2 = pdb.file_png_load(file2, file2)
       pdb.gimp_image_scale(image2, posterW-1034, posterH-1325)
       pdb.gimp_edit_copy(image2.layers[0])
       layer2 = gimp.Layer(posterImage, "image2",posterW-1034, posterH-1325 , RGBA_IMAGE, 48.0, NORMAL_MODE)
       posterImage.add_layer(layer2)
       floatingLayer = pdb.gimp_edit_paste(layer2, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       # code for adjusting color level - 
       pdb.gimp_desaturate_full(layer2, 1)
       pdb.gimp_drawable_levels(layer2, 0, 0, 1, True, 1.00 , 0, 0, True)
       layer2.translate(915,1281)
       
       # Image 3 - load, scale, copy, make_layer, paste, anchor, translate
       image3 = pdb.file_png_load(file3, file3)
       pdb.gimp_image_scale(image3, posterW-1466, posterH-1978)
       pdb.gimp_edit_copy(image3.layers[0])
       layer3 = gimp.Layer(posterImage, "image3",posterW-1466, posterH-1978, RGBA_IMAGE, 48.0, NORMAL_MODE)
       posterImage.add_layer(layer3)
       floatingLayer = pdb.gimp_edit_paste(layer3, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       # code for fliping and adjusting color level -
       pdb.gimp_item_transform_flip_simple(layer3, 0, False, 507.0)
       pdb.gimp_desaturate_full(layer3, 1)
       pdb.gimp_drawable_levels(layer3, 0, 0, 1, True, 1.00 , 0, 0, True)
       layer3.translate(98,1939)
       
       # Image 4 - load, scale, copy, make_layer, paste, anchor, translate
       image4 = pdb.file_png_load(file4, file4)
       pdb.gimp_image_scale(image4, posterW-667, posterH-751)
       pdb.gimp_edit_copy(image4.layers[0])
       layer4 = gimp.Layer(posterImage, "image4",posterW-667, posterH-751, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer4)
       floatingLayer = pdb.gimp_edit_paste(layer4, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       # Saturation and Color balancing code
       # pdb.gimp_color_balance(drawable, transfer_mode, preserve_lum, cyan_red, magenta_green, yellow_blue)
       pdb.gimp_desaturate_full(layer4, 1)
       pdb.gimp_color_balance(layer4, 1, True, 52.9, 17.3, -10.6)
       layer4.translate(546, 246)

       # Image 5 - load, scale, copy, make_layer, paste, anchor, translate
       image5 = pdb.file_png_load(file5, file5)
       pdb.gimp_image_scale(image5, posterW-1760, posterH-2848)
       pdb.gimp_edit_copy(image5.layers[0])
       layer5 = gimp.Layer(posterImage, "image5",posterW-1760, posterH-2848, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer5)
       floatingLayer = pdb.gimp_edit_paste(layer5, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer5.translate(154,561)

       # code for text layer
       # text_layer = pdb.gimp_text_fontname(image, drawable, x, y, text, border, antialias, size, size_type, fontname)
       # text 1
       textLayer1 = pdb.gimp_text_fontname(posterImage, None, 386, 1099, str1, 5, True, 117, PIXELS, font1)
       pdb.gimp_text_layer_set_color(textLayer1, fcolor)
       justify = pdb.gimp_text_layer_set_justification(textLayer1, 0)
       # text 2
       textLayer2 = pdb.gimp_text_fontname(posterImage, None, 462, 2435, str2, 5, True, 115, PIXELS, font2)
       pdb.gimp_text_layer_set_color(textLayer2, fcolor)
       justify = pdb.gimp_text_layer_set_justification(textLayer2, 0)
       # text 3
       textLayer3 = pdb.gimp_text_fontname(posterImage, None, 462, 2730, str3, 5, True, 95, PIXELS, font3)
       pdb.gimp_text_layer_set_color(textLayer3, fcolor)
       justify = pdb.gimp_text_layer_set_justification(textLayer3, 0)
       gimp.message("JAZZ Poster Created")


register(
     "python_fu_Jazz_Poster",
     "JAZZ Themed Poster",
     "Poster Maker with some UI",
     "ST",
     "Copyright@ST",
     "2021",
     "Poster",
     "",
     [# add input arguments
         (PF_FILE, "file1", "Choose Image 1",""),
         (PF_FILE, "file2", "Choose Image 2",""),
         (PF_FILE, "file3", "Choose Image 3",""),
         (PF_FILE, "file4", "Choose Image 4",""),
         (PF_FILE, "file5", "Choose Image 5",""),
         (PF_STRING, "str1", "Text 1",'''Live Music
Festival'''),
         (PF_FONT, "font1", "Font Used", "Book Antiqua Bold Italic"),
         (PF_STRING, "str2", "Text 2",'''OCTOBER
22-25'''),
         (PF_FONT, "font2", "Font Used", "Times New Roman, Bold"),
         (PF_STRING, "str3", "Text 3",'''9:00 PM Music Hall
Doors Open At 7PM'''),
         (PF_FONT, "font3", "Font Used", "Book Antiqua Bold Italic")



     ],
     [],
     Jazz_Poster,
     menu = "<Image>/File/Create/JAZZ/"
)
 
main()





         
