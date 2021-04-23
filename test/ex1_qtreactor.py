# works:
# from PySide2 import QtCore, QtWidgets

# works:
from PySide6 import QtCore, QtWidgets

import sys
app = QtWidgets.QApplication(sys.argv)

import qt5reactor
qt5reactor.install()

from twisted.internet import reactor
from twisted.internet.task import LoopingCall

mywindow = QtWidgets.QWidget()
mywindow.resize(600, 400)
mywindow.setWindowTitle('Hello, World!')

mylabel = QtWidgets.QLabel(mywindow)
mylabel.setGeometry(QtCore.QRect(200, 200, 200, 200))

count = 0

def set_label():
    global count
    global mylabel
    count += 1
    msg = 'Hello, World [count={}]!'.format(count)
    print(msg)
    mylabel.setText(msg)

lc = LoopingCall(set_label)
lc.start(1.)

mywindow.show()
app.exec_()

# reactor.run()
reactor.runReturn()
