#!/usr/bin/env python3
import os
import evdev
import asyncio
from evdev import ecodes, InputDevice, categorize, UInput

#DevName as shown with xinput under keyboard section
DevName = "UGTABLET 13.3 inch PenDisplay Keyboard"

#Input codes from your tablet buttons. See the catch_buttons.py script to capture them
Inputs = dict();
Inputs['K1'] = [48]
Inputs['K2'] = [18]
Inputs['K3'] = [56]
Inputs['K4'] = [57]
Inputs['K5'] = [47]
Inputs['K6'] = [29, 31]
Inputs['K7'] = [29, 44]
Inputs['K8'] = [29, 56, 49]
Inputs['KL'] = [29, 74]
Inputs['KR'] = [29, 78]

#Desired keys to be handled by the button. See the catch_keycodes.py script to capture them
Outputs = dict();
Outputs['K1'] = ["KEY_LEFTSHIFT", "KEY_LEFTCTRL", "KEY_P"]
Outputs['K2'] = ["KEY_LEFTSHIFT", "KEY_LEFTCTRL", "KEY_E"]
Outputs['K3'] = ["KEY_LEFTSHIFT", "KEY_LEFTCTRL", "KEY_H"]
Outputs['K4'] = ["KEY_LEFTCTRL", "KEY_S"]
Outputs['K5'] = ["KEY_LEFTCTRL", "KEY_W"]
Outputs['K6'] = ["KEY_LEFTCTRL", "KEY_Y"]
Outputs['K7'] = ["KEY_PAGEDOWN"]
Outputs['K8'] = ["KEY_LEFTCTRL", "KEY_D"]
Outputs['KL'] = ["KEY_LEFTCTRL", "KEY_KPMINUS"]
Outputs['KR'] = ["KEY_LEFTCTRL", "KEY_KPPLUS"]

def trigger_output(Input,Outputs, ui):
    for key in Outputs[Input]:
        ui.write(ecodes.EV_KEY, ecodes.ecodes[key], 1)

    Outputs[Input].reverse();

    for key in Outputs[Input]:
        ui.write(ecodes.EV_KEY, ecodes.ecodes[key], 0)

    Outputs[Input].reverse();

    ui.syn()

def catch_input(ev, Inputs, UniqueInputs, InputStack, Outputs, ui):
    if ev.value == 1:
        if ev.code in UniqueInputs:
            InputStack.append(ev.code)
            if InputStack in Inputs.values():
                Input = list(Inputs.keys())[list(Inputs.values()).index(InputStack)]
                trigger_output(Input, Outputs, ui)
                InputStack. clear()

UniqueInputs = dict();

for key in Inputs:
    for el in Inputs[key]:
        UniqueInputs[el] = 1

#UKeys = dict();

InputStack = []

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
        print("Tablet Keyboard Found")
        ui = UInput()
        keyboard.grab()
        async def helper(keyboard):
            async for ev in keyboard.async_read_loop():
                catch_input(ev, Inputs, UniqueInputs, InputStack, Outputs, ui)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(helper(keyboard))
        ui.close()
