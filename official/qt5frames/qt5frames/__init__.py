# -*- coding: utf-8 -*-
# Copyright (c) Sebastian Klaassen. All Rights Reserved.
# Distributed under the MIT License. See LICENSE file for more info.

import abc
import functools
import numbers
import quaternion
import re
from multipledispatch import dispatch
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QMainWindow, QDialog, QGroupBox, QTabWidget, QLayout, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QStackedLayout
from PyQt5.QtCore import Qt, QObject, QRect, QPointF, QRectF
from PyQt5.QtGui import QTransform, QPixmap
from asyncframes import Event, Frame, PFrame, FrameMeta, Primitive, hold, sleep, any_, find_parent
from .linalg import *
from .keys import Keys


__all__ = [
    # Widget Containers
    'Container', 'MainWindow', 'Dialog', 'Layout', 'HBoxLayout', 'VBoxLayout', 'GridLayout', 'FormLayout', 'StackedLayout', 'GroupBox', 'TabWidget', 'TabPage', 'CanvasLayer', 'Canvas', 'Pixmap',

    # Widgets
    'Widget', 'PushButton', 'Label', 'LCDNumber', 'ProgressBar', 'ComboBox', 'ListView', 'DialogButtonBox',

    # Shapes
    'Shape', 'Line', 'Lines', 'Polyline', 'Rect', 'Circle', 'Text', 'Image',

    # Other
    'StandardItemModel', 'StandardItem',
]
__version__ = '0.0.1'


class QtEvent(object):
    def __init__(self, sender, *args):
        self.sender = sender
        self.args = args

# ------------------------------------------------------------------------------
# Widget Containers
# ------------------------------------------------------------------------------

class QtFrame(type(QObject), FrameMeta):
    pass

class Container(Frame, metaclass=QtFrame):
    def __init__(self, size=None, layout=None):
        if not isinstance(self, QWidget): raise Exception("The Container class shouldn't be used directly. Use a layout class instead")
        super().__init__()
        if size:
            self.resize(*size)
        if layout is not None:
            self._layout = layout()
            self.setLayout(self._layout)
        else:
            self._layout = None

    def add_widget(self, widget, **kwargs):
        if self._layout is None: return
        if type(self._layout) == QGridLayout and 'row' in kwargs and 'col' in kwargs:
            self._layout.addWidget(
                widget,
                kwargs.get('row'),
                kwargs.get('col'),
                kwargs.get('rowspan', 1),
                kwargs.get('colspan', 1),
                kwargs.get('alignment', QtCore.Qt.Alignment())
            )
        elif type(self._layout) == QFormLayout and 'label' in kwargs:
            self._layout.addRow(kwargs.get('label'), widget)
        else:
            self._layout.addWidget(widget)
    def remove_widget(self, widget):
        if self._layout is None: return
        self._layout.removeWidget(widget)

    def setCurrentIndex(self, index):
        if type(self._layout) == QStackedLayout: self._layout.setCurrentIndex(index)
    def setCurrentWidget(self, widget):
        if type(self._layout) == QStackedLayout: self._layout.setCurrentWidget(widget)

class MainWindow(Container, QMainWindow):
    def __init__(self, size=None, title=None, modal=False):
        QMainWindow.__init__(self)
        Container.__init__(self)
        self.keys = Keys()
        if size:
            self.resize(*size)
        if title is not None:
            self.setWindowTitle(title)
        if modal:
            self.setWindowModality(Qt.ApplicationModal)
        self.closed = Event("MainWindow.closed")

    def create(self, framefunc, *frameargs, size=None, title=None, **framekwargs):
        if size:
            self.resize(*size)
        if title is not None:
            self.setWindowTitle(title)
        super().create(framefunc, *frameargs, **framekwargs)
        self.show()

    def _ondispose(self):
        self.deleteLater()

    def closeEvent(self, event):
        self.closed.send(event)
        if event.isAccepted(): # If event wasn't canceled by user
            self.remove()

    def add_widget(self, widget, **kwargs):
        self.setCentralWidget(widget)
    def remove_widget(self, widget):
        pass

    def keyPressEvent(self, event):
        self.keys._onkeyevent(event.key(), True, event)
    def keyReleaseEvent(self, event):
        self.keys._onkeyevent(event.key(), False, event)

class Dialog(Container, QDialog):
    def __init__(self, layout=None, size=None, title=None):
        QDialog.__init__(self)
        Container.__init__(self, layout=layout)
        self.keys = Keys()
        if size:
            self.resize(*size)
        if title is not None:
            self.setWindowTitle(title)
        self.closed = Event("Dialog.closed")
        def onfinished(result):
            self._result = result
            self.remove()
        self.finished.connect(onfinished)

    def create(self, framefunc, *frameargs, size=None, title=None, **framekwargs):
        if size:
            self.resize(*size)
        if title is not None:
            self.setWindowTitle(title)
        super().create(framefunc, *frameargs, **framekwargs)
        self.show()

    def _ondispose(self):
        self.deleteLater()

    def closeEvent(self, event):
        self.closed.send(event)
        if event.isAccepted(): # If event wasn't canceled by user
            self.remove()

    def keyPressEvent(self, event):
        self.keys._onkeyevent(event.key(), True, event)
    def keyReleaseEvent(self, event):
        self.keys._onkeyevent(event.key(), False, event)

class Layout(Container, QWidget):
    hbox = QHBoxLayout
    vbox = QVBoxLayout
    grid = QGridLayout
    form = QFormLayout
    stacked = QStackedLayout

    def __init__(self, layout=None, **kwargs):
        QWidget.__init__(self)
        Container.__init__(self, layout=layout)
        parent = find_parent(Container)
        if parent is None:
            raise Exception("Layouts need to be defined inside a MainWindow or Dialog")
        parent.add_widget(self, **kwargs)

class HBoxLayout(Layout):
    def __init__(self, **kwargs):
        super().__init__(Layout.hbox, **kwargs)

    def addStretch(self, stretch = 0):
        self._layout.addStretch(stretch)

class VBoxLayout(Layout):
    def __init__(self, **kwargs):
        super().__init__(Layout.vbox, **kwargs)

    def addStretch(self, stretch = 0):
        self._layout.addStretch(stretch)

class GridLayout(Layout):
    def __init__(self, **kwargs):
        super().__init__(Layout.grid, **kwargs)

class FormLayout(Layout):
    def __init__(self, **kwargs):
        super().__init__(Layout.form, **kwargs)

class StackedLayout(Layout):
    def __init__(self, **kwargs):
        super().__init__(Layout.stacked, **kwargs)

class GroupBox(Container, QGroupBox):
    def __init__(self, size=None, title=None, layout=None, **kwargs):
        QGroupBox.__init__(self)
        Container.__init__(self, layout=layout)
        parent = find_parent(Container)
        if parent is None:
            raise Exception("GroupBox needs to be defined inside a MainWindow or Dialog")
        parent.add_widget(self, **kwargs)
        if size:
            self.resize(*size)
        if title is not None:
            self.setTitle(title)

class TabWidget(Container, QTabWidget):
    def __init__(self, size=None, layout=None, **kwargs):
        QTabWidget.__init__(self)
        Container.__init__(self, layout=layout)
        parent = find_parent(Container)
        if parent is None:
            raise Exception("TabWidget needs to be defined inside a MainWindow or Dialog")
        parent.add_widget(self, **kwargs)
        if size:
            self.resize(*size)

class TabPage(Container, QWidget):
    @dispatch(QtGui.QIcon, str)
    def __init__(self, icon, label, layout=None):
        QWidget.__init__(self)
        Container.__init__(self, layout=layout)
        parent = find_parent(TabWidget)
        if parent is None:
            raise Exception("TabPage needs to be defined inside a TabWidget")
        parent.addTab(self, icon, label)
    @dispatch(str)
    def __init__(self, label, layout=None):
        QWidget.__init__(self)
        Container.__init__(self, layout=layout)
        parent = find_parent(TabWidget)
        if parent is None:
            raise Exception("TabPage needs to be defined inside a TabWidget")
        parent.addTab(self, label)

class CanvasLayer(Frame):
    def __init__(self, pos=None, rot=None, scl=None):
        super().__init__()
        self._pos = vec2(0, 0) if pos is None else pos
        self._rot = quat() if rot is None else rot
        self._scl = vec2(1, 1) if scl is None else scl

        if isinstance(self, Canvas) or isinstance(self, Pixmap):
            self._canvas = self
        else:
            # Find parent frame of class Canvas
            self._canvas = find_parent((Canvas, Pixmap))
            if self._canvas is None:
                raise Exception("CanvasLayer can't be defined outside Canvas")

            self._canvas.layers.append(self)

    def _ondispose(self):
        self._canvas.layers.remove(self)

    def create(self, framefunc, *frameargs, pos=None, rot=None, scl=None, **framekwargs):
        self.transform = QTransform()

        if pos is not None: self._pos = pos
        if rot is not None: self._rot = rot
        if scl is not None: self._scl = scl

        if isinstance(self._rot, numbers.Number): self._rot = quat(self._rot)
        if isinstance(self._scl, numbers.Number): self._scl = vec2(self._scl, self._scl)

        self._update_transform() # Update transform matrix to reflect self._pos, self._rot and self._scl

        super().create(framefunc, *frameargs, **framekwargs)

    def _update_transform(self):
        rmat = quaternion.as_rotation_matrix(self._rot)

        self.transform.setMatrix(
            rmat[0, 0] * self._scl.x, rmat[1, 0],               rmat[2, 0],
            rmat[0, 1],               rmat[1, 1] * self._scl.y, rmat[2, 1],
            rmat[0, 2] + self._pos.x, rmat[1, 2] + self._pos.y, rmat[2, 2]
        )

        #TODO: Recursively update child transform's

        self._canvas.update()

    @property
    def pos(self):
        return self._pos
    @pos.setter
    def pos(self, value):
        self._pos = value # Set new self._pos
        self._update_transform() # Update self.transform

    @property
    def rot(self):
        return self._rot
    @rot.setter
    def rot(self, value):
        self._rot = value # Set new self._rot
        self._update_transform()

    @property
    def scl(self):
        return self._scl
    @scl.setter
    def scl(self, value):
        self._scl = value # Set new self._scl
        self._update_transform() # Update self.transform

class Canvas(CanvasLayer, QWidget, metaclass=QtFrame):
    def __init__(self, size=None, pos=None, rot=None, scl=None, **kwargs):
        CanvasLayer.__init__(self, pos, rot, scl)
        QWidget.__init__(self)
        parent = find_parent(Container)
        if parent is None:
            raise Exception("StackedLayout needs to be defined inside a MainWindow or Dialog")
        parent.add_widget(self, **kwargs)
        if size is not None:
            self.resize(*size)
        self.layers = [self]
        self.setBackgroundRole(QtGui.QPalette.Base)
        self.setAutoFillBackground(True)
        self.show()
    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        #painter.setBrush(QtGui.QBrush(Qt.red))
        #painter.drawRect(QRect(0, 0, self.width() - 1, self.height() - 1))
        #painter.setPen(QtGui.QPen(Qt.blue))
        #painter.drawLine(0, 0, 100, 100)
        for layer in self.layers:
            for primitive in layer._primitives:
                primitive.draw(painter)
        painter.end()
    def _remove_stage2(self, *args, **kwargs):
        parent = find_parent(Container)
        parent.remove_widget(self)
        self.setParent(None)
        self.deleteLater()
        super()._remove_stage2(*args, **kwargs)

class Pixmap(CanvasLayer, QPixmap, metaclass=QtFrame):
    def __init__(self, width=None, height=None, pos=None, rot=None, scl=None, **kwargs):
        CanvasLayer.__init__(self, pos, rot, scl)
        self._width = width
        self._height = height
        self.layers = [self]
    def create(self, framefunc, *frameargs, width=None, height=None, **framekwargs):
        QPixmap.__init__(self, width or self._width, height or self._height)
        super().create(framefunc, *frameargs, **framekwargs)
    def draw(self):
        painter = QtGui.QPainter()
        painter.begin(self)
        for layer in self.layers:
            for primitive in layer._primitives:
                primitive.draw(painter)
        painter.end()
    def update(self):
        pass #self.draw()

# ------------------------------------------------------------------------------
# Widgets
# ------------------------------------------------------------------------------

def _create_properties(src, dest):
    """
    Substitude getter/setter pairs with Python properties

    Find callable attributes of the form 'foo' (getter) and 'setFoo' (setter) in class src and replace them with properties in class dest.
    """
    setters = {}
    setter_regex = re.compile(r"set[A-Z]\w*")
    for key in dir(src):
        try:
            setter = getattr(src, key)
        except TypeError:
            continue
        if callable(setter) and setter_regex.match(key):
            setters[key[3].lower() + key[4:]] = setter
    for key in dir(src):
        try:
            getter = getattr(src, key)
        except TypeError:
            continue
        if callable(getter) and key in setters:
            setattr(dest, key, property(getter, setters[key])) # Overwrite getter with property

def _convert_all_signals_to_awaitables(obj):
    for key in dir(obj.__class__):
        try:
            signal = getattr(obj, key)
        except TypeError:
            continue
        if type(signal) == QtCore.pyqtBoundSignal:
            awaitable = Event("{}.{}".format(obj.__class__.__name__, key))
            #signal.connect(functools.partial(awaitable.post, obj))
            def sig(awaitable, obj, *args):
                awaitable.post(QtEvent(obj, *args))
            signal.connect(functools.partial(sig, awaitable, obj))
            awaitable.connect = signal.connect # Preserve pyqtBoundSignal.connect()
            awaitable.emit = signal.emit # Preserve pyqtBoundSignal.emit()
            setattr(obj, key, awaitable)

class Widget(Primitive):
    def __init__(self):
        super().__init__(Container)
        self.double_clicked = Event("{}.double_clicked".format(self.__class__.__name__))

    def remove(self):
        self._owner.remove_widget(self)
        self.setParent(None)
        self.deleteLater()
        super().remove()

    def _show(self, kwargs):
        self.resize(self.sizeHint())
        self._owner.add_widget(self, **kwargs)
        self.show()

    def mouseDoubleClickEvent(self, event):
        self.double_clicked.send(event)

class PushButton(Widget, QtWidgets.QPushButton):
    @dispatch(QtGui.QIcon, str)
    def __init__(self, icon, text, **kwargs):
        super().__init__()
        QtWidgets.QPushButton.__init__(self, text, self._owner)
        _convert_all_signals_to_awaitables(self)
        self._show(kwargs)
    @dispatch(str)
    def __init__(self, text, **kwargs):
        super().__init__()
        QtWidgets.QPushButton.__init__(self, text, self._owner)
        _convert_all_signals_to_awaitables(self)
        self._show(kwargs)
    @dispatch()
    def __init__(self, **kwargs):
        super().__init__()
        QtWidgets.QPushButton.__init__(self, self._owner)
        _convert_all_signals_to_awaitables(self)
        self._show(kwargs)
_create_properties(QtWidgets.QPushButton, PushButton)

class Label(Widget, QtWidgets.QLabel):
    @dispatch(str)
    def __init__(self, text, **kwargs):
        super().__init__()
        QtWidgets.QLabel.__init__(self, text, self._owner)
        _convert_all_signals_to_awaitables(self)
        self._show(kwargs)
    @dispatch()
    def __init__(self, **kwargs):
        super().__init__()
        QtWidgets.QLabel.__init__(self, self._owner)
        _convert_all_signals_to_awaitables(self)
        self._show(kwargs)
_create_properties(QtWidgets.QLabel, Label)

class LCDNumber(Widget, QtWidgets.QLCDNumber):
    @dispatch(int)
    def __init__(self, num_digits, **kwargs):
        super().__init__()
        QtWidgets.QLCDNumber.__init__(self, num_digits, self._owner)
        _convert_all_signals_to_awaitables(self)
        self._show(kwargs)
    @dispatch()
    def __init__(self, **kwargs):
        super().__init__()
        QtWidgets.QLCDNumber.__init__(self, self._owner)
        _convert_all_signals_to_awaitables(self)
        self._show(kwargs)
_create_properties(QtWidgets.QLCDNumber, LCDNumber)

class ProgressBar(Widget, QtWidgets.QProgressBar):
    @dispatch()
    def __init__(self, **kwargs):
        super().__init__()
        QtWidgets.QProgressBar.__init__(self, self._owner)
        _convert_all_signals_to_awaitables(self)
        self._show(kwargs)
_create_properties(QtWidgets.QProgressBar, ProgressBar)

class ComboBox(Widget, QtWidgets.QComboBox):
    @dispatch()
    def __init__(self, **kwargs):
        super().__init__()
        QtWidgets.QComboBox.__init__(self, self._owner)
        _convert_all_signals_to_awaitables(self)
        self._show(kwargs)
_create_properties(QtWidgets.QComboBox, ComboBox)

class ListView(Widget, QtWidgets.QListView):
    @dispatch(str)
    def __init__(self, text, **kwargs):
        super().__init__()
        QtWidgets.QListView.__init__(self, text, self._owner)
        _convert_all_signals_to_awaitables(self)
        self.current_changed = Event("ListView.current_changed")
        self._show(kwargs)
    @dispatch()
    def __init__(self, **kwargs):
        super().__init__()
        QtWidgets.QListView.__init__(self, self._owner)
        _convert_all_signals_to_awaitables(self)
        self.current_changed = Event("ListView.current_changed")
        self._show(kwargs)
    def currentChanged(self, current, previous):
        self.current_changed.send(QtEvent(self, current, previous))
_create_properties(QtWidgets.QListView, Label)

class StandardItemModel(PFrame, QtGui.QStandardItemModel, metaclass=QtFrame):
    @dispatch(int, int)
    def __init__(self, rows, columns):
        QtGui.QStandardItemModel.__init__(self, rows, columns)
        Frame.__init__(self)
    @dispatch()
    def __init__(self):
        QtGui.QStandardItemModel.__init__(self)
        Frame.__init__(self)

class StandardItem(Primitive, QtGui.QStandardItem):
    @dispatch(str)
    def __init__(self, text):
        QtGui.QStandardItem.__init__(self, text)
        Primitive.__init__(self, StandardItemModel)
        self._owner.appendRow(self)
    @dispatch(QtGui.QIcon, str)
    def __init__(self, icon, text):
        QtGui.QStandardItem.__init__(self, icon, text)
        Primitive.__init__(self, StandardItemModel)
        self._owner.appendRow(self)
    @dispatch(int)
    def __init__(self, rows, columns=1):
        QtGui.QStandardItem.__init__(self, rows, columns)
        Primitive.__init__(self, StandardItemModel)
        self._owner.appendRow(self)
    @dispatch()
    def __init__(self):
        QtGui.QStandardItem.__init__(self)
        Primitive.__init__(self, StandardItemModel)
        self._owner.appendRow(self)

class DialogButtonBox(Widget, QtWidgets.QDialogButtonBox):
    @dispatch(Qt.Orientation)
    def __init__(self, orientation, **kwargs):
        self._init(orientation, **kwargs)
    @dispatch(QtWidgets.QDialogButtonBox.StandardButton)
    def __init__(self, button, **kwargs):
        self._init(button, **kwargs)
    @dispatch(QtWidgets.QDialogButtonBox.StandardButtons)
    def __init__(self, buttons, **kwargs):
        self._init(buttons, **kwargs)
    @dispatch(QtWidgets.QDialogButtonBox.StandardButton, Qt.Orientation)
    def __init__(self, button, orientation, **kwargs):
        self._init(button, orientation, **kwargs)
    @dispatch(QtWidgets.QDialogButtonBox.StandardButtons, Qt.Orientation)
    def __init__(self, buttons, orientation, **kwargs):
        self._init(buttons, orientation, **kwargs)
    @dispatch()
    def __init__(self, **kwargs):
        self._init(**kwargs)
    def _init(self, *args, **kwargs):
        super().__init__()
        QtWidgets.QDialogButtonBox.__init__(self, *args, self._owner)
        dialog = find_parent(Dialog)
        if dialog is None:
            raise Exception("DialogButtonBox needs to be defined inside a Dialog")
        self.accepted.connect(dialog.accept)
        self.rejected.connect(dialog.reject)
        _convert_all_signals_to_awaitables(self)
        self._show(kwargs)
_create_properties(QtWidgets.QDialogButtonBox, DialogButtonBox)

# ------------------------------------------------------------------------------
# Shapes
# ------------------------------------------------------------------------------

class Shape(Primitive, metaclass=abc.ABCMeta):
    def __init__(self):
        super().__init__(CanvasLayer)

        # Find parent frame of class Canvas
        self._canvas = find_parent(Canvas)

    @abc.abstractmethod
    def draw(self, painter):
        raise NotImplementedError

class Line(Shape):
    def __init__(self, v0, v1, pen=None):
        super().__init__()
        self.v0 = v0
        self.v1 = v1
        self.pen = pen

    def draw(self, painter):
        if self.pen is not None: painter.setPen(self.pen)
        painter.setWorldTransform(self._owner.transform)
        painter.drawLine(self.v0.x, self.v0.y, self.v1.x, self.v1.y)

class Lines(Shape):
    def __init__(self, points, pen=None):
        super().__init__()
        self.points = points
        self.pen = pen

    def draw(self, painter):
        if self.pen is not None: painter.setPen(self.pen)
        painter.setWorldTransform(self._owner.transform)
        painter.drawLines(*(QPointF(*p) for p in self.points))

class Polyline(Shape):
    def __init__(self, points, pen=None):
        super().__init__()
        self.points = points
        self.pen = pen

    def draw(self, painter):
        if self.pen is not None: painter.setPen(self.pen)
        painter.setWorldTransform(self._owner.transform)
        painter.drawPolyline(*(QPointF(*p) for p in self.points))

class Rect(Shape):
    def __init__(self, pos, size, pen=None, brush=None):
        super().__init__()
        self.pos = pos
        self.size = size
        self.pen = pen
        self.brush = brush

    def draw(self, painter):
        if self.pen is not None:
            painter.setPen(self.pen)
        else:
            painter.setPen(Qt.NoPen)
        if self.brush is not None: painter.setBrush(self.brush)
        painter.setWorldTransform(self._owner.transform)
        painter.drawRect(self.pos.x, self.pos.y, self.size.x, self.size.y)

class Circle(Shape):
    def __init__(self, pos, radius, pen=None, brush=None):
        super().__init__()
        self.pos = pos
        self.radius = radius
        self.pen = pen
        self.brush = brush

    def draw(self, painter):
        if self.pen is not None:
            painter.setPen(self.pen)
        else:
            painter.setPen(Qt.NoPen)
        if self.brush is not None: painter.setBrush(self.brush)
        painter.setWorldTransform(self._owner.transform)
        painter.drawEllipse(QPointF(*self.pos), self.radius, self.radius)

class Text(Shape):
    def __init__(self, pos, size, alignment, text, pen=None, font=None):
        super().__init__()
        self.pos = pos
        self.size = size
        self.alignment = alignment
        self.text = text
        self.pen = pen
        self.font = font

    def draw(self, painter):
        if self.pen is not None: painter.setPen(self.pen)
        if self.font is not None: painter.setFont(self.font)
        painter.setWorldTransform(self._owner.transform)
        painter.drawText(self.pos.x, self.pos.y, self.size.x, self.size.y, self.alignment, self.text)

class Image(Shape):
    def __init__(self, pos, size, image, srcpos=vec2(0, 0), srcsize=None):
        super().__init__()
        self.pos = pos
        self.image = image
        self.srcpos = srcpos
        self.srcsize = vec2(image.width(), image.height()) if srcsize is None else srcsize
        self.size = vec2(self.srcsize) if size is None else size

    def draw(self, painter):
        painter.setWorldTransform(self._owner.transform)
        painter.drawPixmap(QRectF(*self.pos, *self.size), self.image, QRectF(*self.srcpos, *self.srcsize))