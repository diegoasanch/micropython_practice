from machine import Pin
from radio import get_radio
import time


null_char = b'\x00'.decode("UTF-8")


def rx():
    led = Pin('LED', Pin.OUT)
    try:
        nrf = get_radio()
    except OSError as e:
        print('Failed to initialize nRF24L01', e)
        led.on()
        return

    nrf.open_rx_pipe(1, 'PyPic')
    nrf.start_listening()

    led.off()
    success = 0
    miss = 0

    while True:
        if nrf.any():
            msg = nrf.recv().decode("UTF-8").replace(null_char, '').strip()
            if msg:
                print(f'RX {success}: msg {msg} - len {len(msg)}', )
                # nrf.flush_rx()
                success += 1
                led.value(1)
                time.sleep_ms(200)
                led.value(0)
                time.sleep_ms(200)
            else:
                print(f'RX miss {miss}')
                miss += 1
                led.value(1)
                time.sleep_ms(200)
                led.value(0)
                time.sleep_ms(200)
