import cv2
import numpy as np
digits = cv2.imread("digits.png",cv2.IMREAD_GRAYSCALE)
rows = np.vsplit(digits,50)
cells = []
for row in rows :
    row_cells=np.hsplit(row,50)
    for cell in row_cells:
        cells.append(cell)
cv2.imshow("cell",cells[2499])
cv2.waitKey(0)
cv2.DestroyAllWindows()
