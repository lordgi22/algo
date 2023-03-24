#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QApplication, QWidget, QPushButton, QHBoxLayout,QVBoxLayout,QLabel,QMessageBox, QRadioButton, QGroupBox, QRadioButton
from random import shuffle
#создание приложения и главного окна
class Question():   
    def __init__(self,questions,prav_otvet,otv2,otv3,otv4,dop5):
        self.questions = questions
        self.prav_otvet = prav_otvet
        self.otv2 = otv2
        self.otv3 = otv3
        self.otv4 = otv4
        self.dop5 = dop5


qwert = Question('какой национальности не существует?', 'негретяне','алексеи','дуб','стыцамен','это:')

questions_list = []
questions_list.append(Question('Кто ты','Я','ДА','о','о','p'))
app = QApplication([])
okno = QWidget()
okno.setWindowTitle('Memory Card')

que = QLabel('Как национальности не существует?')
lm = QVBoxLayout()
lm.addWidget(que, alignment = Qt.AlignCenter)
k = QPushButton('Ответить')



RadioGroupBox = QGroupBox('Варианты ответов')
bt1q = QRadioButton('Энцы')
bt2q = QRadioButton('Чулымцы')
bt3q = QRadioButton('Алексеи')
bt4q = QRadioButton('Алеуты')
lay1o = QHBoxLayout()
lay2o = QVBoxLayout()
lay3o = QVBoxLayout()

lay2o.addWidget(bt1q)
lay2o.addWidget(bt2q)
lay3o.addWidget(bt3q)
lay3o.addWidget(bt4q)

lay1o.addLayout(lay2o)
lay1o.addLayout(lay3o)

a = QGroupBox('Результат теста')
bt1 = QLabel('Ответ:')
bt2 = QLabel('Это:')
bt3 = QLabel('прав ответ')

l1 = QHBoxLayout()
l2 = QVBoxLayout()
l2.addWidget(bt1)
l2.addWidget(bt2,alignment = Qt.AlignCenter)
l2.addWidget(bt3,alignment = Qt.AlignCenter)

l1.addLayout(l2)




RadioGroupBox.setLayout(lay1o)
lm.addWidget(RadioGroupBox)
a.setLayout(l1)
lm.addWidget(a)
RadioGroupBox
lm.addWidget(k)
okno.setLayout(lm)

RadioGroup = QButtonGroup()
RadioGroup.addButton(bt1q)
RadioGroup.addButton(bt2q)
RadioGroup.addButton(bt3q)
RadioGroup.addButton(bt4q)

a.hide()


def show_question():
    RadioGroupBox.show()
    a.hide()
    RadioGroup.setExclusive(False)
    bt1q.setChecked(False)
    bt2q.setChecked(False)
    bt3q.setChecked(False)
    bt4q.setChecked(False)

    RadioGroup.setExclusive(True)

    k.setText('Ответить')
def start_test():
    if k.text() == 'Ответить':
        show_result()
    elif k.text() == 'Следующий вопрос':
        show_question()
    
def show_result():
    RadioGroupBox.hide()
    a.show()
    k.setText('Следующий вопрос')

sp_otv = [bt1q, bt2q, bt3q,  bt4q]


def ask(q: Question):
    shuffle(sp_otv)
    sp_otv[0].setText(q.prav_otvet)
    sp_otv[1].setText(q.otv2)
    sp_otv[2].setText(q.otv3)
    sp_otv[3].setText(q.otv4)
    que.setText(q.questions)
    bt2.setText(q.dop5)
    bt3.setText(q.prav_otvet)
    show_question()

def show_correct(res):
    bt3.setText(res)
    show_result()

def check_answer():
    if sp_otv[0].isChecked():
        show_correct('Правильно')
    else:
        if sp_otv[1].isChecked() or sp_otv[2].isChecked() or sp_otv[3].isChecked():
            show_correct('Неправильно')
okno.l = -1

def next_questions():
    okno.l += 1
    if okno.l == len(questions_list):
        l = 0
    ask(questions_list[okno.l])




k.clicked.connect(check_answer)
okno.show()
app.exec_()