from PyQt5.QtWidgets import *
from view import *
from PyQt5.QtGui import QPixmap

import random


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.Roll_button.clicked.connect(lambda: self.roll())
        self.again_button.clicked.connect(lambda: self.reset())
        self.you_score_label.setText(str(0))
        self.opponent_score_label.setText(str(0))
        self.again_button.hide()

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
        dicegroup = [dice_one, dice_two, dice_three, dice_four, dice_five]
        if dicegroup[0] == dicegroup[1] and dicegroup[0] == dicegroup[2] and dicegroup[0] == dicegroup[3] and dicegroup[0] == dicegroup[4]:
            subtotal += 25
        elif dicegroup[0] == dicegroup[1] and dicegroup[0] == dicegroup[2] and dicegroup[0] == dicegroup[3]:
            subtotal += 20
        elif dicegroup[0] == dicegroup[1] and dicegroup[0] == dicegroup[2] and dicegroup[0] == dicegroup[4]:
            subtotal += 20
        elif dicegroup[0] == dicegroup[1] and dicegroup[0] == dicegroup[3] and dicegroup[0] == dicegroup[4]:
            subtotal += 20
        elif dicegroup[1] == dicegroup[2] and dicegroup[1] == dicegroup[3] and dicegroup[1] == dicegroup[4]:
            subtotal += 20
        elif dicegroup[0] == dicegroup[1] and dicegroup[0] == dicegroup[2]:
            subtotal += 15
            if dicegroup[3] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[1] and dicegroup[0] == dicegroup[3]:
            subtotal += 15
            if dicegroup[2] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[1] and dicegroup[0] == dicegroup[4]:
            subtotal += 15
            if dicegroup[2] == dicegroup[3]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[2] and dicegroup[0] == dicegroup[3]:
            subtotal += 15
            if dicegroup[1] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[2] and dicegroup[0] == dicegroup[4]:
            subtotal += 15
            if dicegroup[1] == dicegroup[3]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[3] and dicegroup[0] == dicegroup[4]:
            subtotal += 15
            if dicegroup[1] == dicegroup[2]:
                subtotal += 10
        elif dicegroup[1] == dicegroup[2] and dicegroup[1] == dicegroup[3]:
            subtotal += 15
            if dicegroup[0] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[1] == dicegroup[2] and dicegroup[1] == dicegroup[4]:
            subtotal += 15
            if dicegroup[0] == dicegroup[3]:
                subtotal += 10
        elif dicegroup[1] == dicegroup[3] and dicegroup[1] == dicegroup[4]:
            subtotal += 15
            if dicegroup[0] == dicegroup[2]:
                subtotal += 10
        elif dicegroup[2] == dicegroup[3] and dicegroup[2] == dicegroup[4]:
            subtotal += 15
            if dicegroup[0] == dicegroup[1]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[1]:
            subtotal += 10
            if dicegroup[2] == dicegroup[3]:
                subtotal += 10
            elif dicegroup[2] == dicegroup[4]:
                subtotal += 10
            elif dicegroup[3] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[2]:
            subtotal += 10
            if dicegroup[1] == dicegroup[3]:
                subtotal += 10
            elif dicegroup[1] == dicegroup[4]:
                subtotal += 10
            elif dicegroup[3] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[3]:
            subtotal += 10
            if dicegroup[1] == dicegroup[2]:
                subtotal += 10
            elif dicegroup[1] == dicegroup[4]:
                subtotal += 10
            elif dicegroup[2] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[4]:
            subtotal += 10
            if dicegroup[1] == dicegroup[2]:
                subtotal += 10
            elif dicegroup[1] == dicegroup[3]:
                subtotal += 10
            elif dicegroup[2] == dicegroup[3]:
                subtotal += 10
        elif dicegroup[1] == dicegroup[2]:
            subtotal += 10
            if dicegroup[0] == dicegroup[3]:
                subtotal += 10
            elif dicegroup[0] == dicegroup[4]:
                subtotal += 10
            elif dicegroup[3] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[1] == dicegroup[3]:
            subtotal += 10
            if dicegroup[0] == dicegroup[2]:
                subtotal += 10
            elif dicegroup[0] == dicegroup[4]:
                subtotal += 10
            elif dicegroup[2] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[1] == dicegroup[4]:
            subtotal += 10
            if dicegroup[0] == dicegroup[2]:
                subtotal += 10
            elif dicegroup[0] == dicegroup[3]:
                subtotal += 10
            elif dicegroup[2] == dicegroup[3]:
                subtotal += 10
        elif dicegroup[2] == dicegroup[3]:
            subtotal += 10
            if dicegroup[0] == dicegroup[1]:
                subtotal += 10
            elif dicegroup[0] == dicegroup[4]:
                subtotal += 10
            elif dicegroup[1] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[2] == dicegroup[4]:
            subtotal += 10
            if dicegroup[0] == dicegroup[1]:
                subtotal += 10
            elif dicegroup[0] == dicegroup[3]:
                subtotal += 10
            elif dicegroup[1] == dicegroup[3]:
                subtotal += 10
        elif dicegroup[3] == dicegroup[4]:
            subtotal += 10
            if dicegroup[0] == dicegroup[1]:
                subtotal += 10
            elif dicegroup[0] == dicegroup[2]:
                subtotal += 10
            elif dicegroup[1] == dicegroup[2]:
                subtotal += 10
        challenger = subtotal
        currentmax = self.you_score_label.text()
        if int(currentmax) < challenger:
            currentmax = challenger
        self.you_score_label.setText(str(currentmax))
        subtotal = dice_six + dice_seven + dice_eight + dice_nine + dice_ten
        dicegroup = [dice_six, dice_seven, dice_eight, dice_nine, dice_ten]
        if dicegroup[0] == dicegroup[1] and dicegroup[0] == dicegroup[2] and dicegroup[0] == dicegroup[3] and dicegroup[
            0] == dicegroup[4]:
            subtotal += 25
        elif dicegroup[0] == dicegroup[1] and dicegroup[0] == dicegroup[2] and dicegroup[0] == dicegroup[3]:
            subtotal += 20
        elif dicegroup[0] == dicegroup[1] and dicegroup[0] == dicegroup[2] and dicegroup[0] == dicegroup[4]:
            subtotal += 20
        elif dicegroup[0] == dicegroup[1] and dicegroup[0] == dicegroup[3] and dicegroup[0] == dicegroup[4]:
            subtotal += 20
        elif dicegroup[1] == dicegroup[2] and dicegroup[1] == dicegroup[3] and dicegroup[1] == dicegroup[4]:
            subtotal += 20
        elif dicegroup[0] == dicegroup[1] and dicegroup[0] == dicegroup[2]:
            subtotal += 15
            if dicegroup[3] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[1] and dicegroup[0] == dicegroup[3]:
            subtotal += 15
            if dicegroup[2] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[1] and dicegroup[0] == dicegroup[4]:
            subtotal += 15
            if dicegroup[2] == dicegroup[3]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[2] and dicegroup[0] == dicegroup[3]:
            subtotal += 15
            if dicegroup[1] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[2] and dicegroup[0] == dicegroup[4]:
            subtotal += 15
            if dicegroup[1] == dicegroup[3]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[3] and dicegroup[0] == dicegroup[4]:
            subtotal += 15
            if dicegroup[1] == dicegroup[2]:
                subtotal += 10
        elif dicegroup[1] == dicegroup[2] and dicegroup[1] == dicegroup[3]:
            subtotal += 15
            if dicegroup[0] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[1] == dicegroup[2] and dicegroup[1] == dicegroup[4]:
            subtotal += 15
            if dicegroup[0] == dicegroup[3]:
                subtotal += 10
        elif dicegroup[1] == dicegroup[3] and dicegroup[1] == dicegroup[4]:
            subtotal += 15
            if dicegroup[0] == dicegroup[2]:
                subtotal += 10
        elif dicegroup[2] == dicegroup[3] and dicegroup[2] == dicegroup[4]:
            subtotal += 15
            if dicegroup[0] == dicegroup[1]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[1]:
            subtotal += 10
            if dicegroup[2] == dicegroup[3]:
                subtotal += 10
            elif dicegroup[2] == dicegroup[4]:
                subtotal += 10
            elif dicegroup[3] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[2]:
            subtotal += 10
            if dicegroup[1] == dicegroup[3]:
                subtotal += 10
            elif dicegroup[1] == dicegroup[4]:
                subtotal += 10
            elif dicegroup[3] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[3]:
            subtotal += 10
            if dicegroup[1] == dicegroup[2]:
                subtotal += 10
            elif dicegroup[1] == dicegroup[4]:
                subtotal += 10
            elif dicegroup[2] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[0] == dicegroup[4]:
            subtotal += 10
            if dicegroup[1] == dicegroup[2]:
                subtotal += 10
            elif dicegroup[1] == dicegroup[3]:
                subtotal += 10
            elif dicegroup[2] == dicegroup[3]:
                subtotal += 10
        elif dicegroup[1] == dicegroup[2]:
            subtotal += 10
            if dicegroup[0] == dicegroup[3]:
                subtotal += 10
            elif dicegroup[0] == dicegroup[4]:
                subtotal += 10
            elif dicegroup[3] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[1] == dicegroup[3]:
            subtotal += 10
            if dicegroup[0] == dicegroup[2]:
                subtotal += 10
            elif dicegroup[0] == dicegroup[4]:
                subtotal += 10
            elif dicegroup[2] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[1] == dicegroup[4]:
            subtotal += 10
            if dicegroup[0] == dicegroup[2]:
                subtotal += 10
            elif dicegroup[0] == dicegroup[3]:
                subtotal += 10
            elif dicegroup[2] == dicegroup[3]:
                subtotal += 10
        elif dicegroup[2] == dicegroup[3]:
            subtotal += 10
            if dicegroup[0] == dicegroup[1]:
                subtotal += 10
            elif dicegroup[0] == dicegroup[4]:
                subtotal += 10
            elif dicegroup[1] == dicegroup[4]:
                subtotal += 10
        elif dicegroup[2] == dicegroup[4]:
            subtotal += 10
            if dicegroup[0] == dicegroup[1]:
                subtotal += 10
            elif dicegroup[0] == dicegroup[3]:
                subtotal += 10
            elif dicegroup[1] == dicegroup[3]:
                subtotal += 10
        elif dicegroup[3] == dicegroup[4]:
            subtotal += 10
            if dicegroup[0] == dicegroup[1]:
                subtotal += 10
            elif dicegroup[0] == dicegroup[2]:
                subtotal += 10
            elif dicegroup[1] == dicegroup[2]:
                subtotal += 10
        challenger = subtotal
        currentmax = self.opponent_score_label.text()
        if int(currentmax) < challenger:
            currentmax = challenger
        self.opponent_score_label.setText(str(currentmax))

        self.setrolls()

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
        rolls = int(self.Rolls_left_counter.text())
        rolls -= 1
        self.Rolls_left_counter.setText(str(rolls))
        if rolls == 0:
            self.Roll_button.hide()
            self.again_button.show()
            opponentscore = int(self.opponent_score_label.text())
            youscore = int(self.you_score_label.text())
            if youscore > opponentscore:
                self.result_label.setText("You win!")
            else:
                self.result_label.setText("You lose!")



    def reset(self):
        self.again_button.hide()
        self.Roll_button.show()
        self.Rolls_left_counter.setText("3")
        self.result_label.setText("")
        self.opponent_score_label.setText("0")
        self.you_score_label.setText("0")