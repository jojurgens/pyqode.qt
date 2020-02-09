import logging
logging.basicConfig(level=logging.INFO)
import os
os.environ['QT_API'] = 'pyside2'
from pyqode.qt import QtCore, QtGui, QtWidgets, QtWebWidgets
print('Qt version:%s' % QtCore.__version__)
print(QtCore.QEvent)
print(QtGui.QPainter)
print(QtWidgets.QWidget)