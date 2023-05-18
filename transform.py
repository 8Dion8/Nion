from PIL import Image
import colorsys as cs
from math import floor

INPUTIMAGEPATH = "./test.png"

INPUTIMAGE = Image.open(INPUTIMAGEPATH)
INPUTIMAGEPIX = INPUTIMAGE.load()
WIDTH, HEIGHT = INPUTIMAGE.size

print(WIDTH, HEIGHT)

OUTPUTIMAGE = Image.new("RGB", (WIDTH, HEIGHT))
OUTPUTIMAGEPIX = OUTPUTIMAGE.load()

import configparser
config = configparser.ConfigParser()
config.read("colors.ini")

colors = config["gruvbox"]

print(colors)

def hex_to_rgb(hex_value):
    h = hex_value.strip("#") 
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return rgb


def frag(pix):
    hsv = cs.rgb_to_hsv(*[i/255 for i in pix])
    hue = hsv[0]
    sat = hsv[1]
    val = hsv[2]

    if val <= 0.3:
        home_hue = 0
        home_sat = 0
        home_val = 0

        target_hsv  = cs.rgb_to_hsv(*[i/255 for i in hex_to_rgb(colors["black"])])

    elif sat <= 0.3:
        home_hue = 0
        home_sat = 0
        home_val = 1
        
        target_hsv  = cs.rgb_to_hsv(*[i/255 for i in hex_to_rgb(colors["white"])])

    elif 0 <= hue * 360 < 15 or 330 <= hue * 360 <= 360:
        home_hue = 0
        home_sat = 1
        home_val = 1
        
        target_hsv  = cs.rgb_to_hsv(*[i/255 for i in hex_to_rgb(colors["red"])])

    elif 15 <= hue * 360 < 45:
        home_hue = 30/360
        home_sat = 1
        home_val = 1

        target_hsv  = cs.rgb_to_hsv(*[i/255 for i in hex_to_rgb(colors["orange"])])

    elif 45 <= hue * 360 < 90:
        home_hue = 60/360
        home_sat = 1
        home_val = 1

        target_hsv  = cs.rgb_to_hsv(*[i/255 for i in hex_to_rgb(colors["yellow"])])

    elif 90 <= hue * 360 < 150:
        home_hue = 120/360
        home_sat = 1
        home_val = 1

        target_hsv  = cs.rgb_to_hsv(*[i/255 for i in hex_to_rgb(colors["green"])])

    elif 150 <= hue * 360 < 210:
        home_hue = 180/360
        home_sat = 1
        home_val = 1

        target_hsv  = cs.rgb_to_hsv(*[i/255 for i in hex_to_rgb(colors["cyan"])])

    elif 210 <= hue * 360 < 270:
        home_hue = 240/360
        home_sat = 1
        home_val = 1

        target_hsv  = cs.rgb_to_hsv(*[i/255 for i in hex_to_rgb(colors["blue"])])

    elif 270 <= hue * 360 < 330:
        home_hue = 300/360
        home_sat = 1
        home_val = 1

        target_hsv  = cs.rgb_to_hsv(*[i/255 for i in hex_to_rgb(colors["magenta"])])

    #print(target_hsv)

    #return tuple([floor(i * 255) for i in cs.hsv_to_rgb(*target_hsv)])
    

    target_hue = target_hsv[0]
    target_sat = target_hsv[1]
    target_val = target_hsv[2]

    hue_dif = home_hue - target_hue
    new_hue = hue + hue_dif
    new_sat = home_sat * target_sat * sat
    new_val = home_val * target_val * val



        
 
    return tuple([floor(i * 255) for i in cs.hsv_to_rgb(new_hue, new_sat, new_val)])


for x in range(WIDTH):
    for y in range(HEIGHT):
        newval = frag(INPUTIMAGEPIX[x, y])
        
        OUTPUTIMAGEPIX[x, y] = newval 

OUTPUTIMAGE.save("out.png")
