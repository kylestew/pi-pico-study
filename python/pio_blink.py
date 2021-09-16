import time
import rp2
from machine import Pin


@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink():
    wrap_target()
    set(pins, 1)
    nop()[31]
    nop()[31]
    nop()[31]
    set(pins, 0)
    nop()[31]
    nop()[31]
    nop()[31]
    wrap()


# bind one GPIO to output on LED pin running blink program above
sm = rp2.StateMachine(0, blink, freq=2000, set_base=Pin(25))

sm.active(1)
time.sleep(3)
sm.active(0)
