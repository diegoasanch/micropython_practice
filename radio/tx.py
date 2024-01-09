
from machine import Pin
from async_radio import AsyncRadio
from radio import get_radio
import uasyncio as asyncio


async def tx():
    led = Pin('LED', Pin.OUT)
    try:
        nrf = get_radio()
    except OSError as e:
        print('Failed to initialize nRF24L01', e)
        led.on()
        return

    i = 0
    nrf.open_tx_pipe('PyPic')

    radio = AsyncRadio(nrf, 0)

    while True:
        try:
            print(f'Sending {i}')
            # nrf.send(f"Packet {i}", 3000)
            await radio.send(f"Packet {i}", 3000)
            print('Sent')
            for _ in range(3):
                led.value(1)
                await asyncio.sleep_ms(100)
                led.value(0)
                await asyncio.sleep_ms(100)
        except OSError as e:
            # print(f'Message {i} lost', e)
            led.value(1)
            await asyncio.sleep_ms(600)

        i += 1
        led.value(0)
        await asyncio.sleep_ms(400)
