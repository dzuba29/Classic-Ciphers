from PIL import Image, ImageMath
import numpy as np

def extract(img,bits):
    img=np.array(img)
    mask=2**bits-1
    extracted_img=(img & mask) << (8 - bits)
    image = Image.fromarray(extracted_img)

    return image

def insert_resized(img,watermark,bits):
    watermark=watermark.resize(img.size)
    img=np.array(img)
    watermark=np.array(watermark)
 
    mask = 256 - 2**bits
    hidden_img = (img & mask) | (watermark >> (8 - bits))

    image = Image.fromarray(hidden_img)
    
    return image


def insert_crop(img,watermark,bits):
    width_img,height_img = img.size
    width_wm,height_wm = watermark.size

    coef_w = np.ceil(width_img/width_wm)
    coef_h = np.ceil(height_img/height_wm)


    lst_w=[]
    watermark=np.array(watermark)
    for i in range(int(coef_h)):
        lst_w.append(watermark)
    horizon=np.concatenate(lst_w, axis=0 )

    lst_h=[]
    for j in range(int(coef_w)):
        lst_h.append(horizon)

    vertical=np.concatenate(lst_h, axis=1 )

    img=np.array(img)
    
    croped_arr=vertical[:height_img,:width_img ,:]
    

    mask = 256 - 2**bits

    hidden_img = (img & mask) | (croped_arr >> (8 - bits))

    image = Image.fromarray(hidden_img)
    
    return image
    
def main():
    #resize watermark to image sizes
    image=Image.open("img.bmp") 
    watermark=Image.open("secret.jpg") 

    encoded_img=insert_resized(image,watermark,4)
    encoded_img.save("/1/encoded_img.bmp")

    decoded_img=Image.open("/1/encoded_img.bmp")
    decoded_img=extract(decoded_img,4)
    decoded_img.resize(watermark.size).save("/1/EXTRACTED.bmp")

    #crop watermark many times to image sizes
    image=Image.open("img.bmp") 
    watermark=Image.open("secret.jpg") 
    width_wm,height_wm = watermark.size

    encoded_img=insert_crop(image,watermark,4)
    encoded_img.save("/2/encoded_img.bmp")

    decoded_img=Image.open("/2/encoded_img.bmp")
    decoded_img=extract(decoded_img,4).crop((0, 0, width_wm, height_wm )).save("/2/EXTRACTED.bmp")

  




main()
