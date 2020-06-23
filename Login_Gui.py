import sys,json,pdb,random,smtplib,socket
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import QMessageBox

class Forgot(qtw.QWidget):
    def __init__(self,parent = None):
        super(Forgot,self).__init__(parent)
        window = qtw.QWidget()
        layout = qtw.QVBoxLayout()
        sub_layout = qtw.QVBoxLayout()
        sub_sub_layout_1 = qtw.QHBoxLayout()
        sub_sub_layout_2 = qtw.QHBoxLayout()
        self.setLayout(layout)
        self.username = qtw.QLineEdit(self,placeholderText='Enter Your Username Here',clearButtonEnabled=True)
        self.t0 = qtw.QLabel("Username")
        self.t1 = qtw.QLabel("Email")
        self.email = qtw.QLineEdit(self,placeholderText='Enter Your Email Here',clearButtonEnabled=True)
        self.back = qtw.QPushButton("Back")
        self.back.clicked.connect(self.show_mainwindow)
        self.submit = qtw.QPushButton("Submit")
        self.submit.clicked.connect(self.send_email)
        sub_layout.addLayout(sub_sub_layout_1)
        sub_layout.addLayout(sub_sub_layout_2)
        sub_sub_layout_1.addWidget(self.t0)
        sub_sub_layout_1.addWidget(self.username)
        sub_sub_layout_2.addWidget(self.t1)
        sub_sub_layout_2.addWidget(self.email)
        layout.addLayout(sub_layout)
        layout.addWidget(self.submit)
        layout.addWidget(self.back)

    def show_mainwindow(self):
        self.hide()
        mw.show()

    def send_email(self):
        username = self.username.text()
        email = self.email.text()
        with open("C:\\Users\\M\\Desktop\\data.json", "r") as user_data:
            temp_dict = json.load(user_data)
            if username in temp_dict and email.lower() == temp_dict[username]["email"].lower():
                sender = "Ahmedazim7804@gmail.com"
                message = f"Thanks To Contact Us \nYour Password is {temp_dict[username]['password']}"
                password = "Azim!451/0"
                receiver = email
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, receiver, message)
                QMessageBox.about(self,"Forgot Password","Email Has Been Sent Successfully")
            else:
                QMessageBox.about(self,"Error","Incorrect Credentials")

class Signup(qtw.QWidget):
    def __init__(self,parent = None):
        super(Signup,self).__init__(parent)
        #Window
        window = qtw.QWidget()
        #Layout
        main_layout = qtw.QVBoxLayout()
        self.setLayout(main_layout)
        layout_1 = qtw.QHBoxLayout()
        layout_2 = qtw.QHBoxLayout()
        layout_3 = qtw.QHBoxLayout()
        #Widget
        self.username_label = qtw.QLabel("Username")
        self.password_label = qtw.QLabel("Password")
        self.email_label = qtw.QLabel("Email")
        self.username = qtw.QLineEdit(self,placeholderText='Enter Your Username',clearButtonEnabled=True)
        self.password = qtw.QLineEdit(self,placeholderText='Enter Your Passowrd',clearButtonEnabled=True)
        self.password.setEchoMode(qtw.QLineEdit.Password)
        self.email = qtw.QLineEdit(self,placeholderText='Enter Your Email',clearButtonEnabled=True)
        self.back = qtw.QPushButton("Back")
        self.submit = qtw.QPushButton("Submit")
        #Layout_add
        layout_1.addWidget(self.username_label)
        layout_1.addWidget(self.username)
        layout_2.addWidget(self.password_label)
        layout_2.addWidget(self.password)
        layout_3.addWidget(self.email_label)
        layout_3.addWidget(self.email)
        main_layout.addLayout(layout_1)
        main_layout.addLayout(layout_2)
        main_layout.addLayout(layout_3)
        main_layout.addWidget(self.submit)
        main_layout.addWidget(self.back)
        #Behaviour
        self.back.clicked.connect(self.f_back)
        self.submit.clicked.connect(self.f_submit)

    def f_back(self):
        mw.show()
        self.hide()

    def f_submit(self):
        username = self.username.text()
        password = self.password.text()
        email = self.email.text()
        with open("C:\\Users\\M\\Desktop\\data.json", "r+") as user_data:
            temp_dict = json.load(user_data)
            if username not in temp_dict and username != '' and password != '' and email != '':
                temp_dict[username] = {"password" : password, "email" : email, "stats" : {"r_p_s" : {"g_p" : 0,"g_w" : 0,"g_l" : 0,"g_t" : 0},"guess_num" : {"g_p" : 0,"g_w" : 0,"g_l" : 0} }}
                QMessageBox.about(self,"Signup","Account Created Successfully")
            elif username in temp_dict:
                QMessageBox.about(self,"Signup","Email Already Exist")
                return
            else:
                QMessageBox.about(self,"Signup","Invalid Credentials")
                return
        with open("C:\\Users\\M\\Desktop\\data.json", "r+") as user_data:
            json.dump(temp_dict, user_data)

class Menu(qtw.QWidget):
    def __init__(self,username,password):
        super(Menu,self).__init__()
        self.username = username
        self.password = password
        #Window
        window = qtw.QWidget()
        #Widgets
        self.rps = qtw.QPushButton("Rock Paper Scissor")
        self.guess_num = qtw.QPushButton("Guess The Number")
        self.stat = qtw.QPushButton("Statistics")
        self.back = qtw.QPushButton("Back")
        #Layout
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.rps)
        layout.addWidget(self.guess_num)
        layout.addWidget(self.stat)
        layout.addWidget(self.back)
        #Behaviour
        self.back.clicked.connect(self.f_back)
        self.rps.clicked.connect(self.f_rps)
        self.guess_num.clicked.connect(self.f_guess_num)
        self.stat.clicked.connect(self.f_stat)

    def f_back(self):
        self.d = Login()
        self.d.show()
        self.hide()

    def f_rps(self):
        self.t = RPS_Choose(self.username,self.password)
        self.hide()
        self.t.show()

    def f_guess_num(self):
        self.hide()
        self.z = Guess_num(self.username,self.password)
        self.z.show()

    def f_stat(self):
        username = self.username
        password = self.password
        self.hide()
        self.s = Stat(username,password)
        self.s.show()

class Stat(qtw.QWidget):
    def __init__(self,username,password):
        super().__init__()
        self.username = username
        self.password = password
        # Window
        window = qtw.QWidget()
        self.resize(553,160)
        # Widgets
        self.back = qtw.QPushButton("Back")
        self.back.clicked.connect(self.f_back)
        self.Table = qtw.QTableWidget()
        self.Table.setRowCount(2)
        self.Table.setColumnCount(4)
        self.Table.setHorizontalHeaderLabels(["Games Played", "Game Wins", "Game Loosed", "Game Tied"])
        self.Table.setVerticalHeaderLabels(["1. Rock Paper Scissor", "2. Guess The Number"])
        self.Table.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding)
        self.f_stat_data()
        # Layout
        layout = qtw.QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.Table, 0, 0)
        layout.addWidget(self.back, 2, 0)

    def f_stat_data(self):
        with open("C:\\users\\M\Desktop\\data.json", 'r') as userdata:
            temp_dict = json.load(userdata)
            self.Table.setItem(0, 0, qtw.QTableWidgetItem(str(temp_dict[self.username]["stats"]["r_p_s"]["g_p"])))
            self.Table.setItem(0, 1, qtw.QTableWidgetItem(str(temp_dict[self.username]["stats"]["r_p_s"]["g_w"])))
            self.Table.setItem(0, 2, qtw.QTableWidgetItem(str(temp_dict[self.username]["stats"]["r_p_s"]["g_l"])))
            self.Table.setItem(0, 3, qtw.QTableWidgetItem(str(temp_dict[self.username]["stats"]["r_p_s"]["g_t"])))
            self.Table.setItem(1, 0,qtw.QTableWidgetItem(str(temp_dict[self.username]["stats"]["guess_num"]["g_p"])))
            self.Table.setItem(1, 1,qtw.QTableWidgetItem(str(temp_dict[self.username]["stats"]["guess_num"]["g_w"])))
            self.Table.setItem(1, 2,qtw.QTableWidgetItem(str(temp_dict[self.username]["stats"]["guess_num"]["g_l"])))
            self.Table.setItem(1, 3, qtw.QTableWidgetItem("0"))

    def f_back(self):
        self.hide()
        self.l = Menu(self.username, self.password)
        self.l.show()

class Guess_num(qtw.QWidget):

    def __init__(self,username,password):
        super().__init__()
        self.username = username
        self.password = password
        #window
        window = qtw.QWidget()
        #Widgets
        self.game_name = qtw.QLabel("GUESS THE NUMBER")
        self.myFont = qtg.QFont()
        self.myFont.setBold(True)
        self.myFont.setPixelSize(30)
        self.game_name.setFont(self.myFont)
        self.game_name.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding)
        self.game_name.setAlignment(qtc.Qt.AlignHCenter | qtc.Qt.AlignTop)
        self.back = qtw.QPushButton("Back")
        self.guess_label = qtw.QLabel("Guess Number")
        self.guess_label.setAlignment(qtc.Qt.AlignHCenter | qtc.Qt.AlignTop)
        self.guess_input = qtw.QLineEdit(self,clearButtonEnabled = True)
        self.submit = qtw.QPushButton("Enter")
        self.count = 5
        self.new_game = qtw.QPushButton("New Game")
        #Behaviour
        self.back.clicked.connect(self.f_back)
        self.submit.clicked.connect(self.f_submit)
        self.new_game.clicked.connect(self.f_new_game)
        #Layout
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.game_name)
        layout.addWidget(self.guess_label)
        layout.addWidget(self.guess_input)
        layout.addWidget(self.submit)
        layout.addWidget(self.new_game)
        layout.addWidget(self.back)
        #Game_code
        self.n = random.randint(0,50)

    def f_new_game(self):
        self.count = 5
        self.n = random.randint(0,50)
        self.submit.setEnabled(True)
        QMessageBox.about(self,"Guess The Number",f"Guess the number Between 0 and 50\nYou have {self.count} Chances")

    def f_submit(self):
        try:
            self.guess = int(self.guess_input.text())
        except ValueError:
            QMessageBox.about(self,"Guess Number","Input Only Numbers")
            self.submit.setEnabled(False)
            return
        if self.guess == self.n:
            QMessageBox.about(self,"Guess The Number","You Guess Correct")
            with open("C:\\users\\M\Desktop\\data.json","r") as user_data:
                temp_dict = json.load(user_data)
                temp_dict[self.username]["stats"]["guess_num"]["g_p"] = int(temp_dict[self.username]["stats"]["guess_num"]["g_p"]) + 1
                temp_dict[self.username]["stats"]["guess_num"]["g_w"] = int(temp_dict[self.username]["stats"]["guess_num"]["g_w"]) + 1
            with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                json.dump(temp_dict, user_data)
        elif self.guess < self.n:
            self.count -= 1
            if self.count < 1:
                QMessageBox.about(self, "Guess The Number", "You Lose")
                with open("C:\\users\\M\Desktop\\data.json", "r") as user_data:
                    temp_dict = json.load(user_data)
                    temp_dict[self.username]["stats"]["guess_num"]["g_p"] = int(temp_dict[self.username]["stats"]["guess_num"]["g_p"]) + 1
                    temp_dict[self.username]["stats"]["guess_num"]["g_l"] = int(temp_dict[self.username]["stats"]["guess_num"]["g_l"]) + 1
                with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                    json.dump(temp_dict,user_data)
                self.submit.setEnabled(False)
            else:
                QMessageBox.about(self, "Guess The Number",f"Your Guess is Lower Than Number\n{self.count} Chances Left")
        elif self.guess > self.n:
            self.count -= 1
            if self.count < 1:
                QMessageBox.about(self, "Guess The Number", "You Lose")
                with open("C:\\users\\M\Desktop\\data.json", "r") as user_data:
                    temp_dict = json.load(user_data)
                    temp_dict[self.username]["stats"]["guess_num"]["g_p"] = int(temp_dict[self.username]["stats"]["guess_num"]["g_p"]) + 1
                    temp_dict[self.username]["stats"]["guess_num"]["g_l"] = int(temp_dict[self.username]["stats"]["guess_num"]["g_l"]) + 1
                with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                    json.dump(temp_dict,user_data)
                self.submit.setEnabled(False)
            else:
                QMessageBox.about(self, "Guess The Number",f"Your Guess is Higher Than Number\n{self.count} Chances Left")

    def f_back(self):
        self.hide()
        self.x = Menu(self.username,self.password)
        self.x.show()

class RPS_Choose(qtw.QWidget):

    def __init__(self,username,password):
        super().__init__()
        self.username = username
        self.password = password
        #Window
        window = qtw.QWidget()
        #Widgets
        self.single_player = qtw.QPushButton("Single Player")
        self.multi_player = qtw.QPushButton("Multiplayer")
        self.back = qtw.QPushButton("Back")
        #Behaviour
        self.single_player.clicked.connect(self.f_single_player)
        self.multi_player.clicked.connect(self.f_multi_player)
        self.back.clicked.connect(self.f_back)
        #Layout
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.single_player)
        layout.addWidget(self.multi_player)
        layout.addWidget(self.back)

    def f_back(self):
        self.j = Menu(self.username,self.password)
        self.hide()
        self.j.show()

    def f_single_player(self):
        self.b = RPS_S(self.username,self.password)
        self.hide()
        self.b.show()

    def f_multi_player(self):
        self.g = RPS_M(self.username,self.password)
        self.hide()
        self.g.show()

class RPS_S(qtw.QWidget):

    def __init__(self,username,password):
        super().__init__()
        self.username = username
        self.password = password
        #Window
        window = qtw.QWidget()
        #Widget
        self.game_name = qtw.QLabel("ROCK PAPER SCISSOR")
        self.input = qtw.QLineEdit(self,clearButtonEnabled = True)
        self.back = qtw.QPushButton("Back")
        self.submit = qtw.QPushButton("Enter")
        self.new_game = qtw.QPushButton("New Game")
        self.cpu = random.choice(["Rock","Paper","Scissor"])
        #Behaviour
        self.font = qtg.QFont()
        self.font.setBold(True)
        self.font.setPixelSize(30)
        self.game_name.setFont(self.font)
        self.game_name.setAlignment(qtc.Qt.AlignTop | qtc.Qt.AlignHCenter)
        self.submit.setEnabled(False)
        self.back.clicked.connect(self.f_back)
        self.submit.clicked.connect(self.f_submit)
        self.new_game.clicked.connect(self.f_new_game)
        #Layout
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.game_name)
        layout.addWidget(self.input)
        layout.addWidget(self.submit)
        layout.addWidget(self.new_game)
        layout.addWidget(self.back)

    def f_back(self):
        self.i = RPS_Choose(self.username,self.password)
        self.hide()
        self.i.show()

    def f_new_game(self):
        self.submit.setEnabled(True)
        self.cpu = random.choice(["Rock","Paper","Scissor"])
        self.input.setText("")

    def f_submit(self):
        self.choose = (str(self.input.text())).lower()
        if self.choose.lower() not in ["rock","paper","scissor"]:
            QMessageBox.about(self,"Rock Paper Scissor",f"Choose 1 From Below\n1. Rock\n2. Paper\n3.Scissor")
            return
        elif self.choose == self.cpu.lower():
            QMessageBox.about(self, "Rock Paper Scissor", "Game Tied")
            with open("C:\\users\\M\Desktop\\data.json","r") as user_data:
                temp_dict = json.load(user_data)
                temp_dict[self.username]["stats"]["r_p_s"]["g_p"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_p"]) + 1
                temp_dict[self.username]["stats"]["r_p_s"]["g_t"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_t"]) + 1
            with open("C:\\users\\M\Desktop\\data.json","w") as user_data:
                json.dump(temp_dict,user_data)
            self.input.setText("")
            self.submit.setEnabled(False)
        elif self.cpu.lower() == "rock":
            if self.choose == "paper":
                QMessageBox.about(self, "Rock Paper Scissor", "You Win")
                with open("C:\\users\\M\Desktop\\data.json", "r") as user_data:
                    temp_dict = json.load(user_data)
                    temp_dict[self.username]["stats"]["r_p_s"]["g_p"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_p"]) + 1
                    temp_dict[self.username]["stats"]["r_p_s"]["g_w"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_w"]) + 1
                with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                    json.dump(temp_dict, user_data)
                self.input.setText("")
                self.submit.setEnabled(False)
            elif self.choose == "scissor":
                QMessageBox.about(self, "Rock Paper Scissor", "You Lose")
                with open("C:\\users\\M\Desktop\\data.json", "r") as user_data:
                    temp_dict = json.load(user_data)
                    temp_dict[self.username]["stats"]["r_p_s"]["g_p"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_p"]) + 1
                    temp_dict[self.username]["stats"]["r_p_s"]["g_l"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_l"]) + 1
                with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                    json.dump(temp_dict, user_data)
                self.input.setText("")
                self.submit.setEnabled(False)
        elif self.cpu.lower() == "paper":
            if self.choose == "rock":
                QMessageBox.about(self, "Rock Paper Scissor", "You Lose")
                with open("C:\\users\\M\Desktop\\data.json", "r") as user_data:
                    temp_dict = json.load(user_data)
                    temp_dict[self.username]["stats"]["r_p_s"]["g_p"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_p"]) + 1
                    temp_dict[self.username]["stats"]["r_p_s"]["g_l"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_l"]) + 1
                with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                    json.dump(temp_dict, user_data)
                self.input.setText("")
                self.submit.setEnabled(False)
            elif self.choose == "scissor":
                QMessageBox.about(self, "Rock Paper Scissor", "You Win")
                with open("C:\\users\\M\Desktop\\data.json", "r") as user_data:
                    temp_dict = json.load(user_data)
                    temp_dict[self.username]["stats"]["r_p_s"]["g_p"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_p"]) + 1
                    temp_dict[self.username]["stats"]["r_p_s"]["g_w"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_w"]) + 1
                with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                    json.dump(temp_dict, user_data)
                self.input.setText("")
                self.submit.setEnabled(False)
        elif self.cpu.lower() == "scissor":
            if self.choose == "rock":
                QMessageBox.about(self, "Rock Paper Scissor", "You Win")
                with open("C:\\users\\M\Desktop\\data.json", "r") as user_data:
                    temp_dict = json.load(user_data)
                    temp_dict[self.username]["stats"]["r_p_s"]["g_p"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_p"]) + 1
                    temp_dict[self.username]["stats"]["r_p_s"]["g_w"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_w"]) + 1
                with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                    json.dump(temp_dict, user_data)
                self.input.setText("")
                self.submit.setEnabled(False)
            elif self.choose == "paper":
                QMessageBox.about(self, "Rock Paper Scissor", "You Lose")
                with open("C:\\users\\M\Desktop\\data.json", "r") as user_data:
                    temp_dict = json.load(user_data)
                    temp_dict[self.username]["stats"]["r_p_s"]["g_p"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_p"]) + 1
                    temp_dict[self.username]["stats"]["r_p_s"]["g_l"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_l"]) + 1
                with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                    json.dump(temp_dict, user_data)
                self.input.setText("")
                self.submit.setEnabled(False)

class RPS_M(qtw.QWidget):
    def __init__(self,username,password):
        super().__init__()
        self.username = username
        self.password = password
        #Window
        window = qtw.QWidget()
        #Widgets
        self.game_name = qtw.QLabel("ROCK PAPER SCISSOR")
        self.game_name_1 = qtw.QLabel("MULTIPLAYER")
        self.input = qtw.QComboBox(self,editable = False)
        self.input.addItem("Select","Select")
        self.input.addItem("Rock", "Rock")
        self.input.addItem("Paper", "Paper")
        self.input.addItem("Scissor", "Scissor")
        self.input.model().item(0).setEnabled(False)
        self.submit = qtw.QPushButton("Enter")
        self.ip_label = qtw.QLabel("IP")
        self.ip = qtw.QLineEdit(self,clearButtonEnabled = True)
        self.port_label = qtw.QLabel("Port")
        self.port = qtw.QLineEdit(self)
        self.back = qtw.QPushButton("Back")
        self.se = qtw.QRadioButton("Server",self,checkable = True,checked = False)
        self.cl = qtw.QRadioButton("Client",self,checkable = True,checked = False)
        self.new_game = qtw.QPushButton("New Game")
        self.new_game.setDisabled(True)
        #Font and Style
        self.font = qtg.QFont()
        self.font.setBold(True)
        self.font.setPixelSize(30)
        self.game_name.setFont(self.font)
        self.game_name_1.setFont(self.font)
        self.game_name.setAlignment(qtc.Qt.AlignHCenter | qtc.Qt.AlignTop)
        self.game_name_1.setAlignment(qtc.Qt.AlignHCenter | qtc.Qt.AlignTop)
        #Layout
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.game_name)
        layout.addWidget(self.game_name_1)
        layout.addWidget(self.input)
        #Layout_IP
        layout_1 = qtw.QHBoxLayout()
        layout_1.addWidget(self.ip_label)
        layout_1.addWidget(self.ip)
        layout.addLayout(layout_1)
        #Layout_PORT
        layout_2 = qtw.QHBoxLayout()
        layout_2.addWidget(self.port_label)
        layout_2.addWidget(self.port)
        layout.addLayout(layout_2)
        #Layout_3
        layout_3 = qtw.QHBoxLayout()
        layout_3.addWidget(self.se)
        layout_3.addWidget(self.cl)
        layout.addLayout(layout_3)
        #Layout
        layout.addWidget(self.new_game)
        layout.addWidget(self.submit)
        #Layout_4
        layout_4 = qtw.QGridLayout()
        layout_4.addWidget(self.back,0,3)
        layout.addLayout(layout_4)
        #Behaviour
        self.back.clicked.connect(self.f_back)
        self.submit.clicked.connect(self.f_submit)
        self.new_game.clicked.connect(self.f_new_game)
        #####
        self.count_server = 0
        self.count_client = 0

    def f_back(self):
        self.o = RPS_Choose(self.username,self.password)
        self.hide()
        self.o.show()

    def f_new_game(self):
        self.count_client = 0
        self.count_server = 0
        self.submit.setEnabled(True)
        self.se.setEnabled(True)
        self.cl.setEnabled(True)

    def client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_1 = self.ip.text()
        self.port_1 = int(self.port.text())
        s.connect((self.host_1,self.port_1))
        x = self.input.currentText()
        msg = str(x)
        print(f"You Have Choosed {msg}")
        s.send(msg.encode())
        s.close()

    def server(self):
        global data
        print("Waiting for other user input...")
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = self.ip.text()
        port = int(self.port.text())
        serversocket.bind((host, port))

        serversocket.listen(5)
        (clientsocket, address) = serversocket.accept()
        data = clientsocket.recv(1024).decode()

    def f_result(self,user,cpu):
        self.choose = str(user.lower())
        self.cpu = str(cpu.lower())
        if self.choose.lower() not in ["rock","paper","scissor"]:
            QMessageBox.about(self,"Rock Paper Scissor",f"Choose 1 From Below\n1. Rock\n2. Paper\n3.Scissor")
            return
        elif self.choose == self.cpu.lower():
            QMessageBox.about(self, "Rock Paper Scissor", "Game Tied")
            with open("C:\\users\\M\Desktop\\data.json","r") as user_data:
                temp_dict = json.load(user_data)
                temp_dict[self.username]["stats"]["r_p_s"]["g_p"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_p"]) + 1
                temp_dict[self.username]["stats"]["r_p_s"]["g_t"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_t"]) + 1
            with open("C:\\users\\M\Desktop\\data.json","w") as user_data:
                json.dump(temp_dict,user_data)
        elif self.cpu.lower() == "rock":
            if self.choose == "paper":
                QMessageBox.about(self, "Rock Paper Scissor", "You Win")
                with open("C:\\users\\M\Desktop\\data.json", "r") as user_data:
                    temp_dict = json.load(user_data)
                    temp_dict[self.username]["stats"]["r_p_s"]["g_p"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_p"]) + 1
                    temp_dict[self.username]["stats"]["r_p_s"]["g_w"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_w"]) + 1
                with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                    json.dump(temp_dict, user_data)
            elif self.choose == "scissor":
                QMessageBox.about(self, "Rock Paper Scissor", "You Lose")
                with open("C:\\users\\M\Desktop\\data.json", "r") as user_data:
                    temp_dict = json.load(user_data)
                    temp_dict[self.username]["stats"]["r_p_s"]["g_p"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_p"]) + 1
                    temp_dict[self.username]["stats"]["r_p_s"]["g_l"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_l"]) + 1
                with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                    json.dump(temp_dict, user_data)
        elif self.cpu.lower() == "paper":
            if self.choose == "rock":
                QMessageBox.about(self, "Rock Paper Scissor", "You Lose")
                with open("C:\\users\\M\Desktop\\data.json", "r") as user_data:
                    temp_dict = json.load(user_data)
                    temp_dict[self.username]["stats"]["r_p_s"]["g_p"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_p"]) + 1
                    temp_dict[self.username]["stats"]["r_p_s"]["g_l"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_l"]) + 1
                with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                    json.dump(temp_dict, user_data)
            elif self.choose == "scissor":
                QMessageBox.about(self, "Rock Paper Scissor", "You Win")
                with open("C:\\users\\M\Desktop\\data.json", "r") as user_data:
                    temp_dict = json.load(user_data)
                    temp_dict[self.username]["stats"]["r_p_s"]["g_p"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_p"]) + 1
                    temp_dict[self.username]["stats"]["r_p_s"]["g_w"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_w"]) + 1
                with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                    json.dump(temp_dict, user_data)
        elif self.cpu.lower() == "scissor":
            if self.choose == "rock":
                QMessageBox.about(self, "Rock Paper Scissor", "You Win")
                with open("C:\\users\\M\Desktop\\data.json", "r") as user_data:
                    temp_dict = json.load(user_data)
                    temp_dict[self.username]["stats"]["r_p_s"]["g_p"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_p"]) + 1
                    temp_dict[self.username]["stats"]["r_p_s"]["g_w"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_w"]) + 1
                with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                    json.dump(temp_dict, user_data)
            elif self.choose == "paper":
                QMessageBox.about(self, "Rock Paper Scissor", "You Lose")
                with open("C:\\users\\M\Desktop\\data.json", "r") as user_data:
                    temp_dict = json.load(user_data)
                    temp_dict[self.username]["stats"]["r_p_s"]["g_p"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_p"]) + 1
                    temp_dict[self.username]["stats"]["r_p_s"]["g_l"] = int(temp_dict[self.username]["stats"]["r_p_s"]["g_l"]) + 1
                with open("C:\\users\\M\Desktop\\data.json", "w") as user_data:
                    json.dump(temp_dict, user_data)

    def f_submit(self):
        if self.se.isChecked():
            self.server()
            self.count_server = 1
            self.cpu = data
            print(f"Cpu Have Choosed {self.cpu}")
            self.se.setEnabled(False)
            self.cl.setChecked(True)
            if self.count_server == 1 and self.count_client == 1:
                self.new_game.setEnabled(True)
                self.submit.setDisabled(True)
                self.se.setEnabled(False)
                self.cl.setEnabled(False)
                self.user = self.input.currentText()
                self.f_result(self.user,self.cpu)
        elif self.cl.isChecked():
            self.client()
            self.count_client = 1
            self.cl.setEnabled(False)
            self.se.setChecked(True)
            if self.count_server == 1 and self.count_client == 1:
                self.new_game.setEnabled(True)
                self.submit.setDisabled(True)
                self.se.setEnabled(False)
                self.cl.setEnabled(False)
                self.user = self.input.currentText()
                self.f_result(self.user,self.cpu)

class Login(qtw.QWidget):
    def __init__(self,parent = None):
        super(Login,self).__init__(parent)
        #Window
        window = qtw.QWidget()
        #Widgets
        self.username_label = qtw.QLabel("Username")
        self.password_label = qtw.QLabel("Password")
        self.username = qtw.QLineEdit(self,placeholderText = "Enter Your Username",clearButtonEnabled = True)
        self.password = qtw.QLineEdit(self,placeholderText = "Enter Your Password",clearButtonEnabled = True)
        self.login = qtw.QPushButton("Login")
        self.back = qtw.QPushButton("Back")
        #Layout
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)
        layout_1 = qtw.QHBoxLayout()
        layout_2 = qtw.QHBoxLayout()
        layout.addLayout(layout_1)
        layout.addLayout(layout_2)
        layout_1.addWidget(self.username_label)
        layout_1.addWidget(self.username)
        layout_2.addWidget(self.password_label)
        layout_2.addWidget(self.password)
        layout.addWidget(self.login)
        layout.addWidget(self.back)
        #Behaviour
        self.back.clicked.connect(self.f_back)
        self.login.clicked.connect(self.f_login)

    def f_back(self):
        mw.show()
        self.hide()

    def f_login(self):
        username = self.username.text()
        password = self.password.text()
        with open("C:\\users\\M\\Desktop\\data.json","r") as user_data:
            temp_dict = json.load(user_data)
            if username in temp_dict and temp_dict[username]["password"] == password:
                QMessageBox.about(self,"Login","You Have Loged in")
                self.f = Menu(username,password)
                self.hide()
                self.f.show()
            elif username not in temp_dict:
                QMessageBox.about(self,"Login","Incorrect Username")
            elif username in temp_dict and temp_dict[username]["password"] != password:
                QMessageBox.about(self,"Login","Incorrect Password")
            elif username == '':
                QMessageBox.about(self,"Login","Enter Username")
            elif password == '':
                QMessageBox.about(self,"Login","Enter Password")
            else:
                QMessageBox.about(self,"Login","Something Went Wrong")

class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()
        #WINDOW
        window = qtw.QWidget()
        self.resize(600,480)
        self.setWindowTitle("Login")
        #Layout
        main_layout = qtw.QVBoxLayout()
        self.setLayout(main_layout)
        #Buttons
        self.login = qtw.QPushButton("Login")
        self.signup = qtw.QPushButton("Sign Up")
        self.forgot = qtw.QPushButton("Forgot Password")
        self.quit = qtw.QPushButton("Quit")
        self.login.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding)
        self.signup.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding)
        self.forgot.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding)
        self.quit.setSizePolicy(qtw.QSizePolicy.Expanding,qtw.QSizePolicy.Expanding)
        main_layout.addWidget(self.login)
        main_layout.addWidget(self.signup)
        main_layout.addWidget(self.forgot)
        main_layout.addWidget(self.quit)
        #Behaviour
        self.quit.clicked.connect(self.f_quit)
        self.forgot.clicked.connect(self.f_forgot)
        self.signup.clicked.connect(self.f_signup)
        self.login.clicked.connect(self.f_login)
        #Show
        self.show()

    def f_quit(self):
        self.quit()

    def f_forgot(self):
        self.a = Forgot()
        self.hide()
        self.a.show()

    def f_signup(self):
        self.b = Signup()
        self.hide()
        self.b.show()

    def f_login(self):
        self.c = Login()
        self.hide()
        self.c.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())