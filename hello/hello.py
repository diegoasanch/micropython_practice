from machine import Pin
import uasyncio


async def blink(led: Pin, count: int, delay_ms: int) -> None:
    # for i in range(count):
    i = 0
    while True:
        led.toggle()
        print(f"Blink {i}")
        i += 1
        await uasyncio.sleep_ms(delay_ms)


async def greet(count: int, delay_ms: int) -> None:
    i = 0
    while True:
        # for i in range(count):
        print(f"Hello, world! {i}")
        i += 1
        await uasyncio.sleep_ms(delay_ms)


async def main() -> None:
    led = Pin('LED', Pin.OUT)

    task1 = uasyncio.create_task(blink(led, 20, 200))
    task2 = uasyncio.create_task(greet(20, 300))

    await uasyncio.gather(task1, task2)

uasyncio.run(main())
