import cv2
img = cv2.imread("OpenCv.png")
img_size = cv2.resize(img,(500,500)) 
cv2.imshow("frame",img_size)
cv2.waitKey(0)