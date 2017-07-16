import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QVBoxLayout,QPushButton,QLineEdit,QLabel,QHBoxLayout)
import scrapper

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Enter Handle ")
        self.name_input = QLineEdit()
        self.button = QPushButton("Search")
        self.button.clicked.connect(self.clickedButton)

        h = QHBoxLayout()
        h.addWidget(self.label)
        h.addWidget(self.name_input)

        v = QVBoxLayout()
        v.addStretch(1)
        v.addLayout(h)
        v.addWidget(self.button)
        self.setLayout(v)
        self.setWindowTitle("Codechef Scrapper")
        self.show()

    def clickedButton(self):
        print("Entered")
        handle = self.name_input.text();
        print(handle)
        s=scrapper.Scrapper(handle)
        cnt=(s.ruu())
        self.button.setText(cnt)
       # print(main.cnt)
        #self.button.setText("your Rank is "+str(main.res))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=MainWindow()
    #print(main.cnt)
    sys.exit(app.exec_())