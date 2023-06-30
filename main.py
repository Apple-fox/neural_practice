import time
import serial
import cv2

def take_photo(n):
    cap = cv2.VideoCapture(0)  # захват камеры
    o = 0
    while True:  # цикл позволяет снимать видео

        o += 1
        ret, img = cap.read()
        if ret:
            cv2.imshow("camera", img)

        else:
            print("error")

        if o == 50:
            cv2.imwrite("camera{}.png".format(n), img)
            break

    cap.release()
    cv2.destroyAllWindows()
    return

# Установка соединения через последовательный порт
ser = serial.Serial('COM5', 115200)
time.sleep(2)

# # примеры комманд
# command = "G28\r\n"
# ser.write(command.encode())

f = open("ear.gcode")
a = f.readline()
n = 0
while(a):
    s = a.split(":")
    if a[0] != ";":
        command = a.strip("\n")
        command = "{}\r\n".format(command)
        ser.write(command.encode())
        b = ser.readline()
        while(b != b'ok 0\r\n' and b != b'ok\r\n' and b != b'wait\r\n'):
            print(b)
            b = ser.readline()

        print(a)
    #else:
        # if (("LAYER" in s[0]) and ("LAYER_COUNT" not in s[0]) and (s[1] != "0\n")):  # если попадается строка означающая смену слоя
        #     command = "G0 X0 Y220\r\n"  # отправляем команду на выдвигание стола
        #     ser.write(command.encode())
        #     #take_photo(n)  # делаем снимок
        #     n += 1
        # elif(s[0] == ";TIME_ELAPSED"):
        #     time.sleep(float(s[1]))
    a = f.readline()

f.close()
time.sleep(30)
ser.close()
