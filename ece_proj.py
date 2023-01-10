import speech_recognition as sr
from gpiozero import AngularServo
from time import sleep

servo=AngularServo(21, min_angle=0,max_angle=270,min_pulse_width=0.0006, max_pulse_width=0.002)


    #speech recognition
a=sr.Recognizer()
with sr.Microphone() as source:
    audio=a.listen(source)
    data=a.recognize_google(audio)
    print(data)

    #servo motor
        

d=list(map(str, data.split()))
print(d)
l=["1",'2','3','4','5','6','7','8','9','10']
y=""
for i in range(len(d)):
    if d[i] in l:
        y=str(d[i])
if(y=='1' or y=='one'):
    y=1
    servo.angle=60
    print(y)
elif(y=='2' or y=='two'):
    y=2
    servo.angle=80
    print(y)
elif(y=='3' or y=='three'):
    y=3
    servo.angle=100
    print(y)
elif(y=='4' or y=='four'):
    y=4
    servo.agnle=120
    print(y)
elif(y=='5' or y=='five'):
    y=5
    servo.angle=140
    print(y)
elif(y=='6' or y=='six'):
    y=6
    servo.angle=160
    print(y)
elif(y=='7' or y=='seven'):
    y=7
    servo.angle=180
    print(y)
elif(y=='8' or y=='eight'):
    y=8
    servo.angle=200
    print(y)
elif(y=='9' or y=='nine'):
    y=9
    servo.angle=220
    print(y)
elif(y=='10' or y=='ten'):
    y=10
    servo.angle=240
    print(y)
else:
    print("can't provide more than 10Volts")

