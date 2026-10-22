#!/bin/bash

export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$(id -u)/bus"

# Change this to your actual folder path
cd /home/xqzm/Remind_Homework

# This runs the 'show' part of your python script silently
MESSAGE=$(python3 hw.py show)

if [[ "$MESSAGE" != "Nothing to do!" ]]; then
    notify-send "⏰ PENDING HOMEWORK REMINDER" "$MESSAGE"
fi
