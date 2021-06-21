path = r"C:\Users\ALI-Gsus\Downloads\PsViragokSzurkeKicsi.jpg"
#image.getpixel# First, lets import all of the library functions we need
import PIL
import numpy as np
from PIL import Image
from PIL import ImageFilter
# from IPython.display import display

# And lets load the image we were working, and we can just convert it to RGB inline
file="msi_recruitment.gif"
image=Image.open(file).convert('RGB')
def pixel_getter(image):
    images=[]

    for i in range(3):
        #i=0
        cnt=0.1
        for j in range(3):
            pixels=image.load()
            #j=0
            newim=image.filter(ImageFilter.BoxBlur(0))
            for x in range(image.width):
                for y in range(image.height):
    # for color in image.getdata():
    #     images.append((color))
                    r=(image.getpixel((x,y)))[0]
                    g=(image.getpixel((x,y)))[1]
                    b=(image.getpixel((x,y)))[2]
                    if i ==0:

                        newim.putpixel((x,y),(int(r*cnt),g,b))
                    elif i==1:
                        newim.putpixel((x,y),(r,int(g*cnt),b))
                    else:
                        newim.putpixel((x,y),(r,g,int(cnt*b)))
            cnt+=0.4
            images.append(newim)
    return (images)
def image_changer(lst):
    newimdatas=[]
    for i in range(3):
        cnt=0.1

        for j in range(3):
            newimdata=[]
            for color in lst:
                r,g,b=color[0],color[1],color[2]
                if i==0:
                    newimdata.append((int(r*cnt),g,b))
                elif i==1:
                    newimdata.append((r,int(g*cnt),b))
                else:
                    newimdata.append((r,g,int(b*cnt)))
            newimdatas.append(newimdata)
            cnt+=.4

    return newimdatas


images=pixel_getter(image)
print(images)
for img in images:
    img.show(           )
# def put_images(lst,image):
#     newim=Image.new(image.mode,(image.width*3,image.height*3))
#     x=0
#     y=0
#
#     # for img in lst:
#     #     newim.paste(img,(x,y))
#
#         if x+image.width==newim.width:
#             x=0
#             y+=image.height
#         else:
#             x+=image.width
#     return newim
# images2=image_changer(images)
# images3=[]
# for img in images2:
    # images3.append(Image.new(image.mode,image.size).putdata(img).copy())

# final_image=put_images(images3,image)
# newim.putdata((images2))
# newim.show()
# final_image.show()