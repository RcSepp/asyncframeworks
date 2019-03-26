# -*- coding: utf-8 -*-
# Copyright (c) Sebastian Klaassen. All Rights Reserved.
# Distributed under the MIT License. See LICENSE file for more info.

from asyncframes import *
from qt5frames import *

__all__ = [
    'MessageBox', 'InputBox', 'ProgressBox'
]

@Dialog(layout=Layout.vbox)
async def MessageBox(self, message):
    Label(message)
    self._layout.addStretch(1)
    DialogButtonBox(DialogButtonBox.StandardButton.Ok)
    await hold()

@Dialog(layout=Layout.vbox)
async def InputBox(self, message, buttons=(DialogButtonBox.StandardButton.Yes | DialogButtonBox.StandardButton.No)):
    Label(message)
    self._layout.addStretch(1)
    DialogButtonBox(buttons)
    await hold()

# @Dialog(layout=Layout.vbox)
# async def ProgressBox(self, message, minimum=None, maximum=None):
#     if message is not None: Label(message)
#     self.pb = ProgressBar()
#     if minimum is not None:
#         self.pb.setMinimum(minimum)
#     if maximum is not None:
#         self.pb.setMaximum(maximum)
#     self.pb.setValue(self.pb.value)
#     DialogButtonBox(DialogButtonBox.StandardButton.Cancel)

#     Dialog.minimum = property(lambda self: self.pb.minimum, lambda self, value: self.pb.setMinimum(value))
#     Dialog.maximum = property(lambda self: self.pb.maximum, lambda self, value: self.pb.setMaximum(value))

#     def set_value(self, value):
#         value = max(self.pb.minimum, min(self.pb.maximum, value))
#         self.pb.setValue(value)
#         if value >= self.pb.maximum:
#             self.remove()
#     Dialog.value = property(lambda self: self.pb.value, set_value)

#     await hold()

@Dialog(layout=Layout.vbox)
async def ProgressBox(self, message, minimum=None, maximum=None):
    if message is not None: Label(message)
    self.pb = ProgressBar()
    DialogButtonBox(DialogButtonBox.StandardButton.Cancel)

    self.progress = Event("ProgressBox.progress")
    self.set_value = Event("ProgressBox.set_value")
    self.set_minimum = Event("ProgressBox.set_minimum")
    self.set_maximum = Event("ProgressBox.set_maximum")

    if minimum is not None:
        self.pb.setMinimum(minimum)
    if maximum is not None:
        self.pb.setMaximum(maximum)
    self.pb.setValue(self.pb.value)

    Dialog.value = property(lambda self: self.pb.value, lambda self, value: self.set_value.post(value))
    Dialog.minimum = property(lambda self: self.pb.minimum, lambda self, value: self.set_minimum.post(value))
    Dialog.maximum = property(lambda self: self.pb.maximum, lambda self, value: self.set_maximum.post(value))

    while True:
        event, value = await any_(self.progress, self.set_value, self.set_minimum, self.set_maximum)
        if event == self.progress:
            value = self.pb.value + (1 if value is None else value)
            value = max(self.pb.minimum, min(self.pb.maximum, value))
            self.pb.setValue(value)
            if value >= self.pb.maximum:
                break
        elif event == self.set_value:
            value = max(self.pb.minimum, min(self.pb.maximum, value))
            self.pb.setValue(value)
            if value >= self.pb.maximum:
                break
        elif event == self.set_minimum:
            self.pb.setMinimum(value)
        elif event == self.set_maximum:
            self.pb.setMaximum(value)

    Dialog.value = property(lambda self: 0, lambda self, value: None)
    Dialog.minimum = property(lambda self: 0, lambda self, value: None)
    Dialog.maximum = property(lambda self: 0, lambda self, value: None)
