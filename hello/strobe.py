from machine import Pin
from time import sleep_ms


def strobe(led: Pin, count: int, delay_ms: int) -> None:
    for _ in range(count):
        led.toggle()
        sleep_ms(delay_ms)
