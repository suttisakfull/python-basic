import cv2
vdo = cv2.VideoCapture("vv.mp4")

while True:
    _,frame = vdo.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(27) & 0xFF == ord("q"):
        break
vdo.release()
cv2.destroyAllWindows()
 