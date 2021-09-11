import time
from machine import Pin, PWM

# going to fade in/out onboard led
pwm = PWM(Pin(25))

pwm.freq(1000)

# oscillate duty cycle over time
duty = 0
direction = 1
for _ in range(8 * 256):
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)
