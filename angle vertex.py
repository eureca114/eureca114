from machine import *
from time import *
x=Pin(12,Pin.OUT)
x=PWM(x)
y=PWM(Pin(2,Pin.OUT))
z=1
for i in range(17):
    sleep(0.5)
    print(z)
    x.duty_u16(z-1)
    y.duty_u16(z-1)
    z*=2
