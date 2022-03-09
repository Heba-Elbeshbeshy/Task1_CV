from utils import *
from filtering import *
from conv import *

# Read Image
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


#filtering
# medianFilter = median_filter(gauss_image)
# display_image(medianFilter, "Gray")
# gauss_kernal = gaussian_filter(3, 3, 2)
# convolved_image = convolve(gauss_image, gauss_kernal)
# display_image(convolved_image, "Gray")

avg_filter = average_filter(3, uniform_image)
display_image(avg_filter, "Gray")

medianFilter = median_filter(sp_image)
display_image(medianFilter, "Gray")

