import random

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


class Smaile(QWidget):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 500, 400)
        self.setWindowTitle('Квадрат-объектив 1')

        uic.loadUi('UI.ui', self)

        self.btn_paint.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.Round(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def Round(self, qp):
        for i in range(random.randint(1, 15)):
            qp.setBrush(QColor(212, 212, 0))
            size = random.randint(50, 150)
            qp.drawEllipse(random.randint(1, 600), random.randint(1, 600), size,
                       size)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Smaile()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
