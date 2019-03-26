# -*- coding: utf-8 -*-
# Copyright (c) Sebastian Klaassen. All Rights Reserved.
# Distributed under the MIT License. See LICENSE file for more info.

from asyncframes import Frame, hold
from qt5frames import *
from qt5frames.linalg import *
from asyncframes.pyqt5_eventloop import EventLoop
from PyQt5 import QtWidgets, QtGui, QtCore

@MainWindow(size=(200, 100), title="Simple ListView Example")
async def listview_simple():
    model = QtGui.QStandardItemModel(4, 4)
    for row in range(4):
        for column in range(4):
            item = QtGui.QStandardItem("item " + str(row))

            if column == 0:
                with Pixmap(256, 256) as pixmap:
                    Rect(vec2(0, 0), vec2(256, 256), None, QtGui.QBrush(QtCore.Qt.gray))
                    Circle(vec2(100, 100), 100, None, QtGui.QBrush(QtCore.Qt.red))
                pixmap.draw()
                item.setIcon(QtGui.QIcon(pixmap))

            model.setItem(row, column, item)

    lv = ListView()
    lv.setModel(model)
    lv.setViewMode(ListView.ViewMode.IconMode)
    lv.setMovement(ListView.Static)

    await hold()

loop = EventLoop()
loop.run(listview_simple)
