import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import math
import cv2  # hnshelha b3d borha

def generate_noise(image, noise_type):
    if noise_type == "gaussian_noise":

        gaussian_noise = np.random.normal(0,10,(image.shape[0], image.shape[1]))
        save_image("Gaussian random noise.jpg", gaussian_noise)
    
        return gaussian_noise

    if noise_type == "uniform_noise":

        uniform_noise =  np.random.uniform(0,50,(image.shape[0], image.shape[1]))
        save_image("Uniform random noise.jpg", uniform_noise)

        return uniform_noise

# Add salt and pepper noise to image , prob: Probability of the noise
def sp_noise(image,prob):

    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

# adding noisy image to original image gaussian & uniform
def image_plus_noise(image, noise_image):

    noisy_image = np.add(image, noise_image)
    return noisy_image


def display_image(image_to_display, type):

    if type == "Gray":
        imgplot = plt.imshow(image_to_display, cmap='gray')
    else:
        imgplot = plt.imshow(image_to_display)

    plt.show()


def from_RGB_to_GS(image):

    R, G, B = image[:,:,0], image[:,:,1], image[:,:,2]
    imgGray = (0.2989 * R + 0.5870 * G + 0.1140 * B).astype(np.uint8)

    return imgGray

def save_image(image_name, image_to_save):

    mpimg.imsave(image_name, image_to_save)


# Histogram function
def HistDistFun(GreyScaleImg):
    Frequencies=[]
    PixelValues=[]

    for s in range(0,256,1):
        PixelValues.append(s)
        
    for k in range(0,256,1):
        Frequencies.append(0)
        
    imgShape=GreyScaleImg.shape
    cols,rows=imgShape
    for i in range(0,cols,1):
        for j in range(0,rows,1):
            value=GreyScaleImg[i,j]         
            Frequencies[value]=Frequencies[value]+1        

    return Frequencies 

# image equalization
# cumulative distribution frequency
def cdf(histogram):  
    cdf = [0] * len(histogram)   #len=256
    #print (cdf)
    cdf[0] = histogram[0]
    for i in range(1, len(histogram)):

        cdf[i]= cdf[i-1]+histogram[i]

    cdf = [n*255/cdf[-1] for n in cdf]     

    return cdf

# to get new pixel values (linear interpolation) 
def image_equalization(image):

    img_cdf = cdf(HistDistFun(image))
    equalized_img = np.interp(image, range(0,256), img_cdf)

    return equalized_img

#Image normalization
def normalization(cols, rows, x_max, x_min, x_new_max, x_new_min, Greyimg):
 
    img = cv2.resize (Greyimg,(cols, rows))

    img_norm_list = []
    for i in range(0, cols):
        img_norm_list_rows = []
        for j in range(0, rows):
            #normalization folmula is: x_norm = (x - x_new_min) / (x_max - x_min)) * (x_new_max - x_new_min)
            x_norm = ((img[i][j] - x_new_min) / (x_max - x_min)) * (x_new_max - x_new_min)
            img_norm_list_rows.append(math.ceil(x_norm))
        img_norm_list.append(img_norm_list_rows)

    array = np.array(img_norm_list)
    h, w = array.shape
    mat = np.reshape(array, (h, w))
    img_norm = Image.fromarray(mat)

    return img_norm





    
