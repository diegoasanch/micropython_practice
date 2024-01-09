import uasyncio as asyncio
import utime

from lib.nrf24l01.nrf24l01 import NRF24L01


class AsyncRadio:
    def __init__(
        self,
        radio: NRF24L01,
        poll_interval_ms: int = 1,
    ):
        self.radio = radio
        self.poll_interval_ms = poll_interval_ms

    async def send(self, buff: bytearray, timeout: int = 1000):
        '''
        Send a buffer of data asynchronously over the radio.
        raises `OSError` if the send times out or if the send fails.
        '''
        self.radio.send_start(buff)
        start = utime.ticks_ms()
        send_result = self.radio.send_done()
        while send_result is None and utime.ticks_diff(utime.ticks_ms(), start) < timeout:
            # Sleep for poll_interval_ms to yield to other coroutines
            await asyncio.sleep_ms(self.poll_interval_ms)
            send_result = self.radio.send_done()
        if send_result == None:
            raise OSError("Send timed out")
        elif send_result == 2:
            raise OSError("Send failed")
