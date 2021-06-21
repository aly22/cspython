from PIL import Image, ImageFilter, ImageFont, ImageDraw

# from IPython.display import display


file = r"F:\pythonalapok\pythonka\cspython\End_of_course_projects\msi_recruitment.gif"
image = Image.open(file).convert('RGBA')


def pixel_getter(image):
    images = []
    font = ImageFont.truetype(
        r"F:\pythonalapok\pythonka\cspython\End_of_course_projects\fanwood-webfont.ttf",
        50)
    k = 0
    for i in range(3):

        cnt = 0.1
        for j in range(3):

            newim2 = Image.new(image.mode, image.size)
            draw = ImageDraw.Draw(newim2)
            if i == 0:
                draw.text((15, 400), "channel {} intensity {}".format(k, cnt),
                          fill=(int(255 * cnt), 255, 255), font=font)
            elif i == 1:
                draw.text((15, 400), "channel {} intensity {}".format(k, cnt),
                          fill=(255, int(255 * cnt), 255), font=font)
            else:
                draw.text((15, 400), "channel {} intensity {}".format(k, cnt),
                          fill=(255, 255, int(255 * cnt)), font=font)

            newim = image.filter(ImageFilter.BoxBlur(0))
            for x in range(image.width):
                for y in range(image.height):

                    r = (image.getpixel((x, y)))[0]
                    g = (image.getpixel((x, y)))[1]
                    b = (image.getpixel((x, y)))[2]
                    if i == 0:

                        newim.putpixel((x, y), (int(r * cnt), g, b))
                    elif i == 1:
                        newim.putpixel((x, y), (r, int(g * cnt), b))
                    else:
                        newim.putpixel((x, y), (r, g, int(cnt * b)))
            blended_img = Image.composite(newim2, newim, newim2)
            cnt += 0.4
            images.append(blended_img)
        k += 1
    return (images)


images = pixel_getter(image)


def put_images(lst, image):
    newim = Image.new(image.mode, (image.width * 3, image.height * 3))
    x = 0
    y = 0
    i = 0.1
    cnt = 0
    for img in lst:

        newim.paste(img, (x, y))

        print(x, y)  # think Ali think
        print(i)
        if x + image.width == newim.width:
            x = 0
            y += image.height
            i = 0.1
            cnt += 1
        else:
            x += image.width
            i += .4

    return newim


newimage = put_images(images, image)
newimage.show()
newimage.save("assignment1.png")
