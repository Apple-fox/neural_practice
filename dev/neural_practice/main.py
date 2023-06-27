import cv2
import time

cap = cv2.VideoCapture(0)  # захват камеры

while True:  # цикл позволяет снимать видео

    ret, img = cap.read()
    if ret:
        cv2.imshow("camera", img)

    else:
        print("error")

    if cv2.waitKey(10) == 27:
        cv2.imwrite("camera.png", img)
        break

cap.release()
cv2.destroyAllWindows()


