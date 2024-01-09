import time
from machine import Pin, SPI
from lib.nrf24l01.nrf24l01 import NRF24L01


def get_radio(max_attempts=100) -> NRF24L01:
    led = Pin('LED', Pin.OUT)
    spi = SPI(0, baudrate=4000000, polarity=0, phase=0,
              sck=Pin(6), mosi=Pin(7), miso=Pin(4))

    attempt = 0
    nrf = None

    while nrf == None and attempt < max_attempts:
        try:
            nrf = NRF24L01(spi, Pin(14), Pin(17))
        except OSError as e:
            nrf = None
            print(f'Attempt {attempt} Failed to initialize nRF24L01', e)
            short_blink(led)
            time.sleep_ms(500)
        finally:
            attempt += 1

    if nrf == None:
        raise OSError('Failed to initialize nRF24L01')
    print('nRF24L01 initialized')
    return nrf


def short_blink(led: Pin):
    for _ in range(2):
        led.value(1)
        time.sleep_ms(100)
        led.value(0)
        time.sleep_ms(100)
