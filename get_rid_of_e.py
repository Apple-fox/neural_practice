file = open("C:/Users/Мария/Desktop/not e.gcode")

file1 = open("C:/Users/Мария/Desktop/not_e.gcode", "w")
a = file.readline()
while(a):
    s = a.split("E")
    if len(s) > 1:
        file1.write("{}\n".format(s[0]))
    else:
        file1.write(s[0])
    a = file.readline()
file.close()
file1.close()
