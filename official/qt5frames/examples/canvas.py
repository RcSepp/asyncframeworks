# -*- coding: utf-8 -*-
# Copyright (c) Sebastian Klaassen. All Rights Reserved.
# Distributed under the MIT License. See LICENSE file for more info.

from asyncframes import Frame, hold
from qt5frames import *
from qt5frames.linalg import *
from asyncframes.pyqt5_eventloop import EventLoop
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen

@MainWindow(size=(200, 100), title="Simple Canvas Example")
async def canvas_simple():
    with Canvas:
        Line(vec2(0, 0), vec2(100, 100), QPen(Qt.red))
        Circle(vec2(50, 50), 50, QPen(Qt.green))
        Text(vec2(20, 20), vec2(100, 50), Qt.AlignLeft, "Text", QPen(Qt.blue))
    await hold()

loop = EventLoop()
loop.run(canvas_simple)
