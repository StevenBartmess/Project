from PyQt5.QtWidgets import *
from view import *
from PyQt5.QtGui import QPixmap

import random


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.Roll_button.clicked.connect(lambda: self.roll())

    def roll(self):
        dice_one = random.randint(1, 6)
        qpixmap = QPixmap(self.getdice(dice_one))
        self.Dice_oneimage.setPixmap(qpixmap)
        dice_two = random.randint(1, 6)
        qpixmap = QPixmap(self.getdice(dice_two))
        self.Dice_twoimage.setPixmap(qpixmap)
        dice_three = random.randint(1, 6)
        qpixmap = QPixmap(self.getdice(dice_three))
        self.Dice_threeimage.setPixmap(qpixmap)
        dice_four = random.randint(1, 6)
        qpixmap = QPixmap(self.getdice(dice_four))
        self.Dice_fourimage.setPixmap(qpixmap)
        dice_five = random.randint(1, 6)
        qpixmap = QPixmap(self.getdice(dice_five))
        self.Dice_fiveimage.setPixmap(qpixmap)
        dice_six = random.randint(1, 6)
        qpixmap = QPixmap(self.getdice(dice_six))
        self.Dice_six.setPixmap(qpixmap)
        dice_seven = random.randint(1, 6)
        qpixmap = QPixmap(self.getdice(dice_seven))
        self.Dice_seven.setPixmap(qpixmap)
        dice_eight = random.randint(1, 6)
        qpixmap = QPixmap(self.getdice(dice_eight))
        self.Dice_eight.setPixmap(qpixmap)
        dice_nine = random.randint(1, 6)
        qpixmap = QPixmap(self.getdice(dice_nine))
        self.Dice_nine.setPixmap(qpixmap)
        dice_ten = random.randint(1, 6)
        qpixmap = QPixmap(self.getdice(dice_ten))
        self.Dice_ten.setPixmap(qpixmap)

        subtotal = dice_one + dice_two + dice_three + dice_four + dice_five
        if dice_one == dice_two and dice_three and dice_four and dice_five:
            subtotal += 25
        elif dice_one == dice_two and dice_three and dice_four:
            subtotal += 20
        elif dice_one == dice_two and dice_three and dice_five:
            subtotal += 20
        elif dice_one == dice_three and dice_four and dice_five:
            subtotal += 20
        elif dice_two == dice_three and dice_four and dice_five:
            subtotal += 20
        elif dice_one == dice_two and dice_three:
            subtotal += 15
        elif dice_one == dice_two and dice_four:
            subtotal += 15
        elif dice_one == dice_two and dice_five:
            subtotal += 15
        elif dice_one == dice_three and dice_four:
            subtotal += 15
        elif dice_one == dice_three and dice_five:
            subtotal += 15
        elif dice_one == dice_four and dice_five:
            subtotal += 15
        elif dice_two == dice_three and dice_four:
            subtotal += 15
        elif dice_two == dice_three and dice_five:
            subtotal += 15
        elif dice_two == dice_four and dice_five:
            subtotal += 15
        elif dice_three == dice_four and dice_five:
            subtotal += 15
        yourscore = subtotal
        self.you_score_label.setText(str(yourscore))
        subtotal = dice_six + dice_seven + dice_eight + dice_nine + dice_ten
        if dice_six == dice_seven and dice_eight and dice_nine and dice_ten:
            subtotal += 25
        elif dice_six == dice_seven and dice_eight and dice_nine:
            subtotal += 20
        elif dice_six == dice_seven and dice_eight and dice_ten:
            subtotal += 20
        elif dice_six == dice_eight and dice_nine and dice_ten:
            subtotal += 20
        elif dice_seven == dice_eight and dice_nine and dice_ten:
            subtotal += 20
        elif dice_six == dice_seven and dice_eight:
            subtotal += 15
        elif dice_six == dice_seven and dice_nine:
            subtotal += 15
        elif dice_six == dice_seven and dice_ten:
            subtotal += 15
        elif dice_six == dice_eight and dice_nine:
            subtotal += 15
        elif dice_six == dice_eight and dice_ten:
            subtotal += 15
        elif dice_six == dice_nine and dice_ten:
            subtotal += 15
        elif dice_seven == dice_eight and dice_nine:
            subtotal += 15
        elif dice_seven == dice_eight and dice_ten:
            subtotal += 15
        elif dice_seven == dice_nine and dice_ten:
            subtotal += 15
        elif dice_eight == dice_nine and dice_ten:
            subtotal += 15
        opponentscore = subtotal
        self.opponent_score_label.setText(str(opponentscore))


    def getdice(self, dice):
        if dice == 1:
            return "images/one.jpg"
        if dice == 2:
            return "images/two.jpg"
        if dice == 3:
            return "images/three.jpg"
        if dice == 4:
            return "images/four.jpg"
        if dice == 5:
            return "images/five.jpg"
        if dice == 6:
            return "images/six.jpg"

    def setrolls(self):
        rolls = 3
        if rolls > 0:
            rolls -= 1
        self.Rolls_left_counter.setText(str(rolls))
        if rolls <= 0:
            self.Roll_button.hide()
