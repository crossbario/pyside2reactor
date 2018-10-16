
Using the Pyside2Reactor
------------------------

Before running / importing any other Twisted code, invoke:

::

    app = QApplication(sys.argv) # your code to init QtCore
    from twisted.application import reactors
    reactors.installReactor('pyside2')


Testing
~~~~~~~

::

   trial --reactor=pyside2 twisted


If you're writing a conventional Qt application and just want twisted as
an addon, you can get that by calling reactor.runReturn() instead of
run(). This call needs to occur after your installation of of the
reactor and after QApplication.exec\_() (or QCoreApplication.exec\_()
whichever you are using.

reactor.run() will also work as expected in a typical twisted
application

Note that if a QApplication or QCoreApplication instance isn't
constructed prior to calling reactor run, an internally owned
QCoreApplication is created and destroyed. This won't work if you call
runReturn instead of run unless you take responsibility for destroying
QCoreApplication yourself...

However, most users want this reactor to do gui stuff so this shouldn't
be an issue.

Performance impact of Qt has been reduced by minimizing use of signaling
which is expensive.
