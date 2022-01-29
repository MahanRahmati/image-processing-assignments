import cv2
from matplotlib import pyplot
import pyvips

x = pyvips.Image.new_from_file("data.jpg")
x = x.hist_equal()
x.write_to_file("normalized_data.jpg")

img = cv2.imread("data.jpg", cv2.IMREAD_GRAYSCALE)
histogram = cv2.calcHist([img],[0],None,[256],[0,256]) 
normalized = cv2.imread("normalized_data.jpg", cv2.IMREAD_GRAYSCALE)
normalizedHistogram = cv2.calcHist([normalized],[0],None,[256],[0,256]) 
cv2.imshow("Base Image", img)
cv2.imshow("Normalized Image", normalized)
pyplot.plot(histogram)
pyplot.plot(normalizedHistogram)
pyplot.show()