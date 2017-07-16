import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QVBoxLayout,QPushButton,QLineEdit,QLabel,QHBoxLayout,QComboBox)
from  PyQt5.QtCore import Qt
import scrapper

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Enter Handle ")
        self.name_input = QLineEdit()
        self.button = QPushButton("Search")
        self.rating = QLabel("Codechef Rating :: ")
        self.countryRank = QLabel("Country Rank :: ")
        self.globalRank = QLabel("Global Rank :: ")
        self.ratingStars = QLabel("Rating Stars :: ")
        self.highestRating = QLabel("Highest Rating :: ")
        self.contestAttended = QLabel("Contest Attended :: ")
        self.cb= QComboBox()
        self.button.clicked.connect(self.clickedButton)
        #self.pb= QProgressBar(splash)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.lightGray)
        self.setPalette(p)
        h = QHBoxLayout()
        h.addWidget(self.label)
        h.addWidget(self.name_input)
        #h.addWidget(self.rating)
        v = QVBoxLayout()
        v.addStretch(1)
        v.addWidget(self.rating)
        v.addWidget(self.globalRank)
        v.addWidget(self.countryRank)
        v.addWidget(self.ratingStars)
        v.addWidget(self.highestRating)
        v.addWidget(self.contestAttended)
        v.addWidget(self.cb)
        v.addLayout(h)
        v.addWidget(self.button)
        self.setLayout(v)
        self.setWindowTitle("Codechef Scrapper")
        self.show()

    def clickedButton(self):
        print("Entered")
        handle = self.name_input.text();
        print(handle)
        try:
            s=scrapper.Scrapper(handle)
            list=s.problemsolved()
            for items in list:
                self.cb.addItem(items)
            self.rating.setText("Codechef Rating ::   "+s.overAllRating())
            self.countryRank.setText("Country Rank ::  "+s.countryRank())
            self.globalRank.setText("Global Rank ::   "+s.globalRank())
            self.ratingStars.setText("Rating Stars ::   "+s.ratingStars())
            self.highestRating.setText("Highest Rating ::   "+s.highestRating())
            self.contestAttended.setText("Contest Attended ::   "+str(s.contestAttended()))
        except:
            pri="NULL"
            self.button.setText(":( Invalid Input")
            self.rating.setText("Codechef Rating ::   " +pri)
            self.countryRank.setText("Country Rank ::  " + pri)
            self.globalRank.setText("Global Rank ::   " + pri)
            self.ratingStars.setText("Rating Stars ::   " + pri)
            self.highestRating.setText("Highest Rating ::   " + pri)
            self.contestAttended.setText("Contest Attended ::   " + pri)
            #self.button.setText("Search")
       # print(main.cnt)
        #self.button.setText("your Rank is "+str(main.res))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=MainWindow()
    #print(main.cnt)
    sys.exit(app.exec_())