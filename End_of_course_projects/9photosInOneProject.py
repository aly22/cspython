path = r"C:\Users\ALI-Gsus\Downloads\PsViragokSzurkeKicsi.jpg"
# image.getpixel# First, lets import all of the library functions we need
import PIL
import numpy as np
from PIL import Image
from PIL import ImageFilter
from PIL import ImageFont, ImageDraw

# from IPython.display import display

# And lets load the image we were working, and we can just convert it to RGB inline
file = r"F:\pythonalapok\pythonka\cspython\End_of_course_projects\msi_recruitment.gif"
image = Image.open(file).convert('RGBA')


def pixel_getter(image):
    images = []

    for i in range(3):
        # i=0
        cnt = 0.1
        for j in range(3):
            pixels = image.load()
            # j=0
            newim = image.filter(ImageFilter.BoxBlur(0))
            for x in range(image.width):
                for y in range(image.height):
                    # for color in image.getdata():
                    #     images.append((color))
                    r = (image.getpixel((x, y)))[0]
                    g = (image.getpixel((x, y)))[1]
                    b = (image.getpixel((x, y)))[2]
                    if i == 0:

                        newim.putpixel((x, y), (int(r * cnt), g, b))
                    elif i == 1:
                        newim.putpixel((x, y), (r, int(g * cnt), b))
                    else:
                        newim.putpixel((x, y), (r, g, int(cnt * b)))
            cnt += 0.4
            images.append(newim)
    return (images)


def image_changer(lst):
    newimdatas = []
    for i in range(3):
        cnt = 0.1

        for j in range(3):
            newimdata = []
            for color in lst:
                r, g, b = color[0], color[1], color[2]
                if i == 0:
                    newimdata.append((int(r * cnt), g, b))
                elif i == 1:
                    newimdata.append((r, int(g * cnt), b))
                else:
                    newimdata.append((r, g, int(b * cnt)))
            newimdatas.append(newimdata)
            cnt += .4

    return newimdatas


images = pixel_getter(image)


def put_images(lst, image):
    font=ImageFont.truetype(r"F:\pythonalapok\pythonka\cspython\End_of_course_projects\fanwood-webfont.ttf",50)

    newim = Image.new(image.mode, (image.width * 3, image.height * 3))
    x = 0
    y = 0
    i=0.1
    cnt=0
    lst2=[]
    # for img in lst:


        # blended_img=Image.merge("RGB",(newim2,img))
        # blended_img=Image.composite(newim2,,)
        # lst2.append(blended_img)
        # blended_img.show()
    for img in lst:
        newim2=Image.new(img.mode,img.size)
        draw=ImageDraw.Draw(newim2)
        draw.text((15,400),"channel {} intensity {}".format(cnt,i),fill=(255,255,255),font=font)
        blended_img=Image.composite(newim2,img,newim2)
        newim.paste(blended_img, (x, y))


        print(x, y)  # think Ali think
        print(i)
        if x + image.width == newim.width:
            x = 0
            y += image.height
            i=0.1
            cnt+=1
        else:
            x += image.width
            i+=.4

    return newim


newimage = put_images(images, image)
newimage.show()
newimage.save("assignment1.png")