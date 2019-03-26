# -*- coding: utf-8 -*-
# Copyright (c) Sebastian Klaassen. All Rights Reserved.
# Distributed under the MIT License. See LICENSE file for more info.

from asyncframes import Frame, hold, sleep
from qt5frames import *
from asyncframes.pyqt5_eventloop import EventLoop

@MainWindow(size=(200, 100), title="Central Layout Example")
async def layout_central():
    PushButton('1')
    await hold()

@MainWindow(size=(200, 100), title="HBox Layout Example")
async def layout_hbox():
    with HBoxLayout:
        PushButton('1')
        PushButton('2')
    await hold()

@MainWindow(size=(200, 100), title="VBox Layout Example")
async def layout_vbox():
    with VBoxLayout:
        PushButton('1')
        PushButton('2')
    await hold()

@MainWindow(size=(200, 100), title="Grid Layout Example")
async def layout_grid():
    with GridLayout:
        PushButton('1', row=0, col=0)
        PushButton('2', row=0, col=1)
        PushButton('3', row=1, col=0, colspan=2)
    await hold()

@MainWindow(size=(200, 100), title="Form Layout Example")
async def layout_form():
    with FormLayout:
        PushButton('2', label=PushButton('1'))
        PushButton('4', label='3')
    await hold()

@MainWindow(size=(200, 100), title="Stacked Layout Example")
async def layout_stacked():
    with StackedLayout as sl:
        PushButton('1')
        PushButton('2')
    while True:
        sl.setCurrentIndex(0)
        await sleep(1)
        sl.setCurrentIndex(1)
        await sleep(1)

@MainWindow(size=(200, 100), title="No Layout Example")
async def layout_none():
    with Layout:
        PushButton('1')
        PushButton('2').move(20, 20)
        await hold()

@MainWindow(size=(400, 400), title="Compound Layout Example")
async def layout_compound():
    with GridLayout:
        with HBoxLayout(row=0, col=0):
            PushButton('h1')
            PushButton('h2')
        with VBoxLayout(row=0, col=1):
            PushButton('v1')
            PushButton('v2')
        with GridLayout(row=1, col=0):
            PushButton('g1', row=0, col=0)
            PushButton('g2', row=0, col=1)
            PushButton('g3', row=1, col=0, colspan=2)
        with FormLayout(row=1, col=1):
            PushButton('f2', label=PushButton('f1'))
            PushButton('f4', label='f3')
        with Layout(row=2, col=0):
            PushButton('n1')
            PushButton('n2').move(20, 20)
        with StackedLayout(row=2, col=1) as sl:
            PushButton('s1')
            PushButton('s2')
        with GroupBox(row=3, col=0, title="GroupBox", layout=Layout.hbox):
            PushButton('1')
            PushButton('2')
        with TabWidget(row=3, col=1):
            with TabPage("hbox", layout=Layout.hbox):
                PushButton('1')
                PushButton('2')
            with TabPage("vbox", layout=Layout.vbox):
                PushButton('1')
                PushButton('2')
    while True:
        sl.setCurrentIndex(0)
        await sleep(1)
        sl.setCurrentIndex(1)
        await sleep(1)

loop = EventLoop()
loop.run(layout_compound)
