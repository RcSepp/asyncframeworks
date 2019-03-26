# -*- coding: utf-8 -*-
# Copyright (c) Sebastian Klaassen. All Rights Reserved.
# Distributed under the MIT License. See LICENSE file for more info.

from asyncframes import Frame, Event, hold, sleep
from qt5frames import MainWindow, dialogs, DialogButtonBox
from asyncframes.pyqt5_eventloop import EventLoop

@MainWindow
async def main_frame():
    if await dialogs.InputBox("Will it rain tomorrow?") == 1:
        await dialogs.MessageBox("Better pack an umbrella!")

loop = EventLoop()
loop.run(main_frame)
