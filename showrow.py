import cv2
import numpy as np
digits = cv2.imread("digits.png",cv2.IMREAD_GRAYSCALE)
rows = np.vsplit(digits,50)
cv2.imshow("row 0",rows[0])
cv2.waitKey(0)
cv2.DestroyAllWindows()
