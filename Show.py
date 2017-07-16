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
        self.rating = QLabel("Codechef Rating :: ")
        self.countryRank = QLabel("Country Rank :: ")
        self.globalRank = QLabel("Global Rank :: ")
        self.ratingStars = QLabel("Rating Stars :: ")
        self.highestRating = QLabel("Highest Rating :: ")
        self.contestAttended = QLabel("Contest Attended :: ")
        self.button.clicked.connect(self.clickedButton)

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
            cnt=(s.overAllRating())
            self.button.setText(cnt)
            self.rating.setText("Codechef Rating ::   "+s.overAllRating())
            self.countryRank.setText("Country Rank ::  "+s.countryRank())
            self.globalRank.setText("Global Rank ::   "+s.globalRank())
            self.ratingStars.setText("Rating Stars ::   "+s.ratingStars())
            self.highestRating.setText("Highest Rating ::   "+s.highestRating())
            self.contestAttended.setText("Contest Attended ::   "+str(s.contestAttended()))
        except:
            self.button.setText(":( Invalid Input")
       # print(main.cnt)
        #self.button.setText("your Rank is "+str(main.res))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=MainWindow()
    #print(main.cnt)
    sys.exit(app.exec_())