#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.1
#  in conjunction with Tcl version 8.6
#    Mar 30, 2022 08:17:38 PM -03  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import snowpois0n

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = snowpois0n.Snowpois0n(_top1)
    root.mainloop()

def fastboot(*args):
    if platform.system() == "Darwin":
        os.system("./bin/darwin-x86/adb reboot recovery")

    elif platform.system() == "Linux":
        os.system("./bin/linux-amd64 reboot recovery")

    elif platform.system() == "Windows":
        os.system("start bin\\win32\\adb.exe reboot recovery")

    sys.stdout.flush()

def jailbreak(*args):
    if platform.system() == "Darwin":
        os.system("./bin/darwin-x86/adb install bin/acmarket_4.8.7_27.apk") #&& ./bin/darwin-x86/adb reboot")

    elif platform.system() == "Linux":
        os.system("./bin/linux-amd64/adb install bin/acmarket_4.8.7_27.apk") #&& ./bin/linux-amd64/adb reboot")

    elif platform.system() == "Windows":
        os.system("start bin\\win32\\adb.exe install bin\\acmarket_4.8.7_27.apk")

    sys.stdout.flush()

def reboot_device(*args):
    if platform.system() == "Darwin":
        os.system("./bin/darwin-x86/adb reboot")

    elif platform.system() == "Linux":
        os.system("./bin/linux-amd64 reboot")

    elif platform.system() == "Windows":
        os.system("start bin\\win32\\adb.exe reboot")

    sys.stdout.flush()

if __name__ == '__main__':
    snowpois0n.start_up()



