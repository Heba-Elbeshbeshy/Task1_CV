from utils import *
import cv2
# Let's first create a zero image with the same dimensions of the loaded image
image = mpimg.imread('apple.jpeg')
gray_image = from_RGB_to_GS(image)


    
# 1- Adding noise to Image [Gaussian noise, Uniform noise, Salt & Pepper]
gaussian_noise = generate_noise(image, "gaussian_noise")
uniform_noise = generate_noise(image, "uniform_noise")

gauss_image = image_plus_noise(gray_image, gaussian_noise)
display_image(gauss_image, "Gray")

uniform_image = image_plus_noise(gray_image, uniform_noise)
display_image(uniform_image, "Gray")

sp_image = sp_noise(gray_image,0.00000025)
display_image(sp_image, "Gray")


# fadel taka feha
# 4- Draw histogram and distribution curve
#PixelValues,Frequencies=HistDistFun(gray_image)
#fig, axs = plt.subplots(2)
#fig.suptitle('Histogram & Distribution Curve')
#axs[0].bar(PixelValues,Frequencies)
#axs[1].plot(PixelValues,Frequencies)        
#plt.show()

# 5- Equalize the image
equalized_image = image_equalization(gray_image)
display_image(equalized_image, "Gray")

# 6- Normalize the image
normalized_image= normalization(cols=333, rows=333, x_min=0, x_max=255, x_new_min=0, x_new_max=33, Greyimg=gray_image)
display_image(normalized_image, "Gray")

