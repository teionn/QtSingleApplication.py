# -*- coding: utf-8 -*-
import sys
import uuid
from Qt.QtWidgets import QWidget
import QtSingleApplication

appGuid = str(uuid.uuid5(uuid.NAMESPACE_DNS,__file__))
app = QtSingleApplication.QSingleApplication(appGuid, sys.argv)
if app.isRunning():
    print("The window is already displayed.")
    sys.exit(0)

w = QWidget()
w.show()
app.setActivationWindow(w)
sys.exit(app.exec_())
