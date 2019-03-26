# -*- coding: utf-8 -*-
# Copyright (c) Sebastian Klaassen. All Rights Reserved.
# Distributed under the MIT License. See LICENSE file for more info.

from asyncframes import Frame, hold, sleep
from qt5frames import *
from asyncframes.pyqt5_eventloop import EventLoop

@MainWindow(size=(200, 100), title="Simple Canvas Example")
async def keys_any(self):
    key = None
    while key != self.keys.escape:
        key, keyevent = await self.keys.anykey
        print(str(key))

loop = EventLoop()
loop.run(keys_any)
