#!/usr/bin/env python3
import os
import evdev
import asyncio
from evdev import ecodes, InputDevice, categorize

#DevName as shown with xinput under keyboard section
DevName = "UGTABLET 13.3 inch PenDisplay Keyboard"

if os.geteuid() != 0:
    print("Please run with administrator privileges")
    sys.exit()
else:
    devices = [InputDevice(path) for path in evdev.list_devices()]
    keyboard = False
    for device in devices:
        if device.name == DevName:
            keyboard = device
            break

    if keyboard != False:
        print("CTRL+C to abort")
        print("Tablet Keyboard Found")
        keyboard.grab()
        async def helper(keyboard):
            async for ev in keyboard.async_read_loop():
                if ev.value == 1:
                    print(str(ev.code)+" found")

        loop = asyncio.get_event_loop()
        loop.run_until_complete(helper(keyboard))
