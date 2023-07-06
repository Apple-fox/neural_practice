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

        if o == 50:
            cv2.imwrite("camera{}.png".format(n), img)
            break

    cap.release()
    cv2.destroyAllWindows()
    return


# Установка соединения через последовательный порт
ser = serial.Serial('COM3', 115200)
time.sleep(2)

f = open("b.gcode")
a = f.readline()
n = 0
com = ["0", "0", "0", "0"]

while (a):
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
        while b != b'ok 0\r\n' and b != b'ok\r\n' and b != b'wait\r\n':
            print(b)
            b = ser.readline()

        print(a)
    else:
        if ";MESH:NONMESH" in a:  # если попадается строка означающая смену слоя
            command = "G1 F1500 E{}\r\n".format(str(float(com[3]) - 9.5))
            open("filik.txt", "a").write(command)
            ser.write(command.encode())
            b = ser.readline()
            while b != b'ok 0\r\n' and b != b'ok\r\n' and b != b'wait\r\n':
                print(b)
                b = ser.readline()
            command = "G0 X0 Y220; injected\r\n"  # отправляем команду на выдвигание стола
            open("filik.txt", "a").write(command)
            ser.write(command.encode())
            b = ser.readline()
            while b != b'ok 0\r\n' and b != b'ok\r\n' and b != b'wait\r\n':
                print(b)
                b = ser.readline()
            take_photo(n)  # делаем снимок
            n += 1
            command = "G1 X{} Y{} Z{} E{}\r\n".format(com[0], com[1], com[2], com[3])
            ser.write(command.encode())
            open("filik.txt", "a").write(command)
            b = ser.readline()
            while b != b'ok 0\r\n' and b != b'ok\r\n' and b != b'wait\r\n':
                print(b)
                b = ser.readline()

    a = f.readline()

f.close()
ser.close()
