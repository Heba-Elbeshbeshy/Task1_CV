from utils import *

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
