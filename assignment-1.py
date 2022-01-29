import numpy as np
import cv2

img = cv2.imread("data.jpg", cv2.IMREAD_GRAYSCALE)

img_inter = cv2.resize(img, (600, 600), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Linear Interpolated Image", img_inter)

img_inter = cv2.resize(img, (600, 600), interpolation=cv2.INTER_NEAREST)
cv2.imshow("Nearest Interpolated Image", img_inter)

img_inter = cv2.resize(img, (600, 600), interpolation=cv2.INTER_CUBIC)
cv2.imshow("Cubic Interpolated Image", img_inter)

cv2.waitKey(0)
cv2.destroyAllWindows()