import numpy as np
import cv2

img = cv2.imread("data.jpg", cv2.IMREAD_GRAYSCALE)

rows, cols = img.shape

M = np.float32([[1, 0, 50],
                [0, 1, 50],
                [0, 0, 1]])

translated_img = cv2.warpPerspective(img, M, (cols, rows))
cv2.imshow("Translated Image", translated_img)

M = np.float32([[1.5, 0  , 0],
            	[0,   1.8, 0],
            	[0,   0,   1]])
scaled_img = cv2.warpPerspective(img,M,(cols*2,rows*2))
cv2.imshow("Scaled Image", scaled_img)

# x-axis
M = np.float32([[1, 0.5, 0],
             	[0, 1  , 0],
            	[0, 0  , 1]])
# y-axis
# M = np.float32([[1,   0, 0],
#             	  [0.5, 1, 0],
#             	  [0,   0, 1]])          
sheared_img = cv2.warpPerspective(img,M,(int(cols*1.5),int(rows*1.5)))
cv2.imshow("Sheared Image", sheared_img)

# x-axis
M = np.float32([[1,  0, 0   ],
                [0, -1, rows],
                [0,  0, 1   ]])
# y-axis
# M = np.float32([[-1, 0, cols],
#                 [ 0, 1, 0   ],
#                 [ 0, 0, 1   ]])
reflected_img = cv2.warpPerspective(img,M,(int(cols),int(rows)))
cv2.imshow("Reflected Image", reflected_img)


angle = np.radians(10)
M = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
            	[np.sin(angle), np.cos(angle), 0],
            	[0, 0, 1]])
rotated_img = cv2.warpPerspective(img, M, (int(cols),int(rows)))
cv2.imshow("Rotated Image", rotated_img)

cropped_img = img[50:100, 50:100]
cv2.imshow("Cropped Image", cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()