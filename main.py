from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout
import random
app = QApplication([])
window = QWidget()
window.show()
window.setWindowTitle("DJ Arbus")
push = qPushButton('Winner')
Text = QLabel('?')
Text2 = QLabel('Press to calcylaite')
Line =QVBoxLayout
Line.addWidget(Text2,aligment=Qt.AllignHCenter)
Line.addWidget(Text,aligment=Qt.AllignHCenter)
Line.addWidget(push,aligment=Qt.AllignHCenter)
window.setLayout(Line)
def pushbutton():
    number = random.randint(0, 100)
    text.setText(str(number))
    push.clicked.connect(pushbutton)

app.exec_()
print('я незнаю что написать')