#Write a Python program to convert a color image to a black and white image.
from images import Image
def blackwhite(image):
    width=image.getWidth()
    height=image.getHeight()
    new=Image(width,height)
    y=0
    while y<height:
        x=0
        while x<width:
            oldP=image.getPixel(x,y)
            r=oldP[0]
            g=oldP[1]
            b=oldP[2]
            avg=(r+g+b)//3
            if avg>128:
                #black
                new.setPixel(x,y,(0,0,0))
            else:
                #white
                new.setPixel(x,y,(255,255,255))
            x+=1
        y+=1
    new.draw()
image=Image("girl.gif")
image.draw()
blackwhite(image)