import cv2
import numpy as np
digits = cv2.imread("digits.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow("diigts",digits)
cv2.waitKey(0)
cv2.DestroyAllWindows()
