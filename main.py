import time
import serial
import cv2


def is_number(stroka: str):
    try:
        float(stroka)
        return True
    except ValueError:
        return False


def take_photo(n):
    cap = cv2.VideoCapture(0)  # захват камеры
    o = 0
    while True:  # цикл позволяет снимать видео

        o += 1
        ret, img = cap.read()
        # if ret:
        #     cv2.imshow("camera", img)

        # else:
        #     print("error")

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

f = open("helicopter.gcode")
a = f.readline()
n = 0
com = ["0","0", "0","0"]

while(a):
    s = a.split(":")

    if a[0] != ";":
        if "X" in a or "Y" in a or "Z" in a or "E" in a:
            s = a.split(" ")
            for i in range(len(s)):
                if "X" in s[i] and s[i].split("X")[1] != com[0]:
                    com[0] = s[i].split("X")[1].strip("\n")
                if "Y" in s[i] and s[i].split("Y")[1] != com[1]:
                    com[1] = s[i].split("Y")[1].strip("\n")
                if "Z" in s[i] and s[i].split("Z")[1] != com[2]:
                    com[2] = s[i].split("Z")[1].strip("\n")
                if "E" in s[i] and s[i].split("E")[1] != com[3] and is_number(s[i].split("E")[1]):
                    com[3] = s[i].split("E")[1].strip("\n")

        command = a.strip("\n")
        command = "{}\r\n".format(command)
        ser.write(command.encode())
        open("filik.txt", "a").write(command)
        b = ser.readline()
        while(b != b'ok 0\r\n' and b != b'ok\r\n' and b != b'wait\r\n'):
            print(b)
            b = ser.readline()

        print(a)
    else:
        if ";MESH:NONMESH" in a:  # если попадается строка означающая смену слоя
            command = "G0 X0 Y220" + " E" + com[3] + "; injected\r\n"  # отправляем команду на выдвигание стола
            open("filik.txt", "a").write(command)
            ser.write(command.encode())
            b = ser.readline()
            while (b != b'ok 0\r\n' and b != b'ok\r\n' and b != b'wait\r\n'):
                print(b)
                b = ser.readline()
            take_photo(n)  # делаем снимок
            n += 1
            command = "G1 X" + com[0] + " Y" + com[1] + " Z" + com[2] + " E" + com[3] + "\r\n"
            ser.write(command.encode())
            open("filik.txt", "a").write(command)
            b = ser.readline()
            while (b != b'ok 0\r\n' and b != b'ok\r\n' and b != b'wait\r\n'):
                print(b)
                b = ser.readline()

    a = f.readline()

f.close()
time.sleep(30)
ser.close()
