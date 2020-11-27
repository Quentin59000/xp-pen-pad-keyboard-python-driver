#!/usr/bin/env python3
import os
import evdev
from evdev import InputDevice, ecodes
from select import select

if os.geteuid() != 0:
    print("Please run with administrator privileges")
    sys.exit()
else:
    devices = [InputDevice(path) for path in evdev.list_devices()]
    devices = {dev.fd: dev for dev in devices}

    print("CTRL+C to abort")
    while True:
        r, w, x = select(devices, [], [])
        for fd in r:
            for event in devices[fd].read():
                if event.type == ecodes.EV_KEY:
                    key = evdev.categorize(event)
                    if key.keystate == 1:
                        print("\n---------")
                        print(key.keycode)
                    if key.keystate == 0:
                        print("\n---------")
