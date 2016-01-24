import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel)
from PyQt5.QtGui import QPixmap, QIcon
import urllib.request
import requests
import os


class XkcdViewer(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        xkcd_array = requests.get("http://dynamic.xkcd.com/api-0/jsonp/comic/").json()

        self.setGeometry(300, 300, 1000, 500)
        title = xkcd_array['title'].encode("latin-1").decode("utf-8")
        self.setWindowTitle('XKCD - '+title)
        print(type(title))

        alt = xkcd_array['alt'].encode("latin-1").decode("utf-8")

        self.setToolTip(alt)

        url = xkcd_array['img']
        data = urllib.request.urlopen(url).read()
        img = QPixmap()
        img.loadFromData(data)

        self.resize(img.width(), img.height())

        lbl2 = QLabel('asd', self)
        lbl2.setPixmap(img)

        self.show()

if __name__ == '__main__':

    dn = os.path.dirname(os.path.realpath(__file__))
    app = QApplication(sys.argv)
    view = XkcdViewer()
    app.setWindowIcon(QIcon(dn+'/xkcd.png'))
    sys.exit(app.exec_())
