from machine import Pin
import rp2

NUM_LEDS = 1


@rp2.asm_pio(
    sideset_init=rp2.PIO.OUT_LOW,
    out_shiftdir=rp2.PIO.SHIFT_LEFT,
    autopull=True,
    pull_thresh=24,
)
def ws2812():
    # pylint: disable=E,W,C,R
    wrap_target()
    nop()
    wrap()


sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(22))

sm.active(1)
