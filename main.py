import time
import serial
import cv2

def take_photo():
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
            cv2.imwrite("camera.png", img)
            break

    cap.release()
    cv2.destroyAllWindows()
    return

# Установка соединения через последовательный порт
ser = serial.Serial('COM3', 115200)
time.sleep(2)

# примеры комманд
command = "G28\r\n"
ser.write(command.encode())
command = "G0 X100 Y100\r\n"
ser.write(command.encode())
command = "G0 X0 Y220\r\n"  # выдвигаем стол для фото
ser.write(command.encode())

# делаем фото
take_photo()

# продолжаем команды
command = "G4 S2\r\n"
ser.write(command.encode())
command = "G0 X110 Y110\r\n"
ser.write(command.encode())

time.sleep(20)

ser.close()