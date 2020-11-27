#!/bin/sh
#Change HEAD-4 to the monitor you want
MONITOR="HEAD-4"
PAD_NAME='UGTABLET 13.3 inch PenDisplay stylus'
PAD_KEY_NAME='UGTABLET 13.3 inch PenDisplay Keyboard'

ID_STYLUS=`/usr/bin/xinput | grep "$PAD_NAME" | cut -f 2 | cut -c 4-5`
ID_KEY_NAME=`/usr/bin/xinput | grep "$PAD_KEY_NAME" | cut -f 2 | cut -c 4-5`
/usr/bin/xsetwacom set $ID_STYLUS MapToOutput $MONITOR
/usr/bin/xsetwacom set $ID_STYLUS Button 2 3
