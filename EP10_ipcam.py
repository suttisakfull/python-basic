import cv2
# url ='http://192.168.1.38:4747/video'
url='http://192.168.1.38:4747/video'

vdo_c = cv2.VideoCapture(0)

while True:
    _,frame = vdo_c.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(27) & 0xFF == ord("q"):
        break
vdo_c.release()
cv2.destroyAllWindows()