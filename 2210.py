from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
                    QApplication, 
                    QWidget,
                    QPushButton,
                    QLabel,
                    QVBoxLayout,
                    QHBoxLayout )
app = QApplication([])
window = QWidget()                    
window.resize(360, 600)
window.setWindowTitle("Калькулятор")
window.setStyleSheet('''
*{
    font-size: 24px;
}
QWidget{
    background-color: rgba(0,0,0,0.5);
}
QPushButton{
    height: 70px;
    }''')

main_layout = QVBoxLayout()
h1_layout = QHBoxLayout()
h2_layout = QHBoxLayout()
h3_layout = QHBoxLayout()
h4_layout = QHBoxLayout()
h5_layout = QHBoxLayout()
h6_layout = QHBoxLayout()

total = QLabel('')
total_str = ''
h1_layout.addWidget(total, alignment= Qt.AlignRight)
total.setStyleSheet('''background-color: transparent;
font-size: 28px;
color: white;
''')
button_C = QPushButton('C')
button_AC = QPushButton('AC')
button_percent = QPushButton('%')
button_devision = QPushButton('/')
button_multi = QPushButton('*') # 2
button_minus = QPushButton('-') # 3
button_plus = QPushButton('+') # 4
button_dot = QPushButton('.') # 6
button_equals = QPushButton('=') # 6
button_devision.setStyleSheet('''background-color: #EBAD1C;''')
button_multi.setStyleSheet('''background-color: #EBAD1C;''')
button_minus.setStyleSheet('''background-color: #EBAD1C;''')
button_plus.setStyleSheet('''background-color: #EBAD1C;''')
button_equals.setStyleSheet('''background-color: #EBAD1C;''')
button_dot.setStyleSheet('''background-color: #7D7D7D;''')


h2_layout.addWidget(button_C)
h2_layout.addWidget(button_AC)
h2_layout.addWidget(button_percent)
h2_layout.addWidget(button_devision)
numbers = []
for number in range(10):
    numbers.append(QPushButton(str(number)))
    numbers[-1].setStyleSheet('''
    background-color: #7D7D7D; ''')
numbers[0].setStyleSheet('''width: 150px;
background-color: #7D7D7D;''')
k = 1
h6_layout.addWidget(numbers[0])
for  i in range(3):
    h5_layout.addWidget(numbers[k])
    k += 1
for i in range(3):
    h4_layout.addWidget(numbers[k])
    k += 1  
for i in range(3):
    h3_layout.addWidget(numbers[k])
    k += 1

h3_layout.addWidget(button_multi)
h4_layout.addWidget(button_minus)
h5_layout.addWidget(button_plus)
h6_layout.addWidget(button_dot)
h6_layout.addWidget(button_equals)

main_layout.addLayout(h1_layout)
main_layout.addLayout(h2_layout)
main_layout.addLayout(h3_layout)
main_layout.addLayout(h4_layout)
main_layout.addLayout(h5_layout)
main_layout.addLayout(h6_layout)



def a1():
    global total_str
    total_str += str(i)
    total.setText(total_str)
def a2():
    global total_str
    total_str += '2'
    total.setText(total_str)
def a3():
    global total_str
    total_str += '3'
    total.setText(total_str)
def a4():
    global total_str
    total_str += '4'
    total.setText(total_str)
def a5():
    global total_str
    total_str += '5'
    total.setText(total_str)
def a6():
    global total_str
    total_str += '6'
    total.setText(total_str)
def a7():
    global total_str
    total_str += '7'
    total.setText(total_str)
def a8():
    global total_str
    total_str += '8'
    total.setText(total_str)
def a9():
    global total_str
    total_str += '9'
    total.setText(total_str)
def a0():
    global total_str
    total_str += '0'
    total.setText(total_str)
def a_plus():
    global total_str
    total_str += '+'
    total.setText(total_str)
defs_numbers = {}
defs_numbers['1'] = a1
defs_numbers['2'] = a2
defs_numbers['3'] = a3
defs_numbers['4'] = a4
defs_numbers['5'] = a5
defs_numbers['6'] = a6
defs_numbers['7'] = a7
defs_numbers['8'] = a8
defs_numbers['9'] = a9
defs_numbers['0'] = a0

for i in range(0, 10):
    numbers[i].clicked.connect(defs_numbers[str(i)])

button_plus.clicked.connect(a_plus)

def a_equals():
    global total_str
    total_int = 0
    total_list = total_str.split('+')
    for i in total_list:
        total_int += int(i)
    total.setText(str(total_int))
button_equals.clicked.connect(a_equals)


window.setLayout(main_layout)
window.show()
app.exec_()
