# XP Pen buttons / pad / keyboard configuration on Linux

These python scripts are designed to assign custom keys to the XP Pen Artist Pro 13.3 Tablet as no driver is able to handle the device "pad" in order to use it with xsetwacom commands. I think it can be used to configure other non working keyboard tablets

To make your tablet work you must premilinarily :
_ Install the digimend driver : https://github.com/DIGImend
_ Install the xf86-input-wacom and set the xorg.conf : https://digimend.github.io/support/howto/drivers/wacom/
_ Having python installed
_ Install your Linux Headers
_ Get the pyhon-evdev package : https://python-evdev.readthedocs.io/

Once this done, I have my pen directly recognised and setted up (without having to approach it near the tablet to set up it). You should be able to configure your pen and display with the xsetwacom command (take a look at the init_tablet.sh)

Nevertheless there are limitations on the pen :
_ My second button just doesn't work
_ The tilt

So, to set up the keyboard, there are 3 scripts to help you :

## init_pad.py

This is the main script, I start it as a Linux Service (it should be better with udev rules) and it must executable and run with administrator privileges. It captures the buttons events and emulate your key configuration (see below). It must be configured to match yout tablet keyboard device, your tablet buttons inputs and to match what keys (or shortcuts) you want to trigger with them.

### Adapt "DevName" variable

Change the DevName matching your Tablet KeyBoard Name. You can find it's name with :
  xinput

Find your tablet keyboard name and replace the DevName variable
  DevName = "YOUR TABLET KEYBOARD NAME HERE"

### Adapt "Inputs" array : key events sent by the tablet

There values are the values captured from the XP Pen Artist 13.3 Pro. It assigns the sequence of key event codes provided by you tablet when pressing a button. On my XP Pen Artist 13.3 Pro tablet I have 8 buttons (that I have named from K1 to K8) and a scroll wheel that is triggering two buttons (named KL and KR). Feel free to adapt this array to match your number of buttons and keys codes sequences. The button event codes can be captured from the catch_buttons.py script (see below).

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

### Adapt "Outputs" array : your desired keys matching your buttons

The Output array must have the same key names (K1, K2 ...) as the Inputs array. The key names make the match between inputs and outputs in the script. These are example for custom shortcuts. You can set how many KEY you want to make shortcuts. All the output keys are pressed and released simultanously. Use the catch_keys.py script to know your keycodes because it depends on your keyboard layout (in french keyboard standard layout the letter "w" is KEY_Z : look at he K5 button wich trigger CTRL+Z)


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

## catch_buttons.py

This script is designed to help you to capture your tablet buttons key events to fill the "Inputs" array. Beware some buttons triggers multiple key events code so you have to report them sequentially in the array of your input.

  Inputs['K8'] = [29, 56, 49]

Here : the input named "K8" triggers 3 key events : 29, 56 and 49

Note : this script must be set as executable and run with administrator privileges

## catch_keys.py

This script is designed to help you to capture your desired keys configuration for a button. Run this script and type with your main keyboard the keys you want. Report the values shown on screen to the relative Output button. As sayed previously, KEY_Q is letter "a" in french so your keyboard layout is not taken (that's why I have written this script)

  Outputs['K1'] = ["KEY_LEFTCTRL", "KEY_W"]

Here, the button K1 will trigger the shortcut CTRL+Z (undo, KEY_W is Z in my french keyboard layout)

Note : again, this script must be set as executable and run with administrator privileges
