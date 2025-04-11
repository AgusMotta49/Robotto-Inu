print("hello world")
print("i am a dog")
from gpiozero import AngularServo
from time import sleep
# inicializar el servo en GPIO pin 14
# min_pulse_width y max_pulse_width van a nesesitar ajustes
servo = AngularServo(14,min_angle=0,max_angle=180,min_pulse_width=0.5/1000,max_pulse_width=2.5/1000)
# Funcion para el angulo del servo
def set_angle(angle):
    servo.angle = angle
    sleep(1)

#Main program loop
try:
    while True:
        angle = int(input("enter angle(0 y 180): "))
        set_angle(angle)
except KeyboardInterrupt:
    print("Programa detenido por el usuario")