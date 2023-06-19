from gpiozero import Motor, OutputDevice
import tty, sys, termios

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)


motor1 = Motor(24, 27)
motor1_enable = OutputDevice(5, initial_value=1)
motor2 = Motor(6, 22)
motor2_enable = OutputDevice(17, initial_value=1)
motor3 = Motor(23, 16)
motor3_enable = OutputDevice(12, initial_value=1)
motor4 = Motor(13, 18)
motor4_enable = OutputDevice(25, initial_value=1)

alma = True

while alma:
    bekert = sys.stdin.read(1)[0]
    if bekert == "w":
        print("Forward")
        for i in range(100):
            motor1.forward()
            motor2.forward()
            motor3.forward()
            motor4.forward()
    if bekert == "s":
        print("Backwards")
        for i in range(100):
            motor1.backward()
            motor2.backward()
            motor3.backward()
            motor4.backward()
    if bekert == "a":
        print("Left")
        for i in range(100):
            motor1.backward()
            motor2.backward()
            motor3.forward()
            motor4.forward()
    if bekert == "d":
        print("right")
        for i in range(100):
            motor1.forward()
            motor2.forward()
            motor3.backward()
            motor4.backward()
    if bekert == "q":
        print("Stopping")
        motor1.stop()
        motor2.stop()
        motor3.stop()
        motor4.stop()