import sys,sqlite3,time
from PyQt5 import QtGui
from PyQt5.QtWidgets import QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget, \
QPushButton, QApplication, QMainWindow,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit, QHBoxLayout
from PyQt5.QtCore import QCoreApplication

class DBHelper():
    def __init__(self):
        self.conn=sqlite3.connect("sdms.db")
        self.c=self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS student(sid INTEGER,Sname TEXT,dept INTEGER,year INTEGER,course_a INTEGER,course_b INTEGER,course_c INTEGER)")
        self.c.execute("CREATE TABLE IF NOT EXISTS faculty(fid INTEGER,f_name TEXT,course INTEGER,dept INTEGER,class_room INTEGER)")
        self.c.execute("CREATE TABLE IF NOT EXISTS Course(cid INTEGER,c_name INTEGER,faculty TEXT,credit INTEGER,type INTEGER,slot INTEGER,No_enrolled INTEGER)")

    def addStudent(self,sid ,Sname ,dept ,year ,course_a ,course_b ,course_c ):
        try:
            self.c.execute("INSERT INTO student(sid ,Sname ,dept ,year ,course_a ,course_b ,course_c) VALUES (?,?,?,?,?,?,?)",(sid ,Sname ,dept ,year ,course_a ,course_b ,course_c))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Student is added successfully to the database.')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add student to the database.')

    def searchStudent(self,sid):
       
        self.c.execute("SELECT * from student WHERE sid="+str(sid))
        self.data=self.c.fetchone()

        if not self.data:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find any student with roll no '+str(sid))
            return None
        self.list=[]
        for i in range(0,7):
            self.list.append(self.data[i])
        self.c.close()
        self.conn.close()
        showStudent(self.list)

    def deleteRecord(self,sid):
        try:
            self.c.execute("DELETE from student WHERE sid="+str(sid))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Student is deleted from the database.')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not delete student from the database.')

        

class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.userNameLabel=QLabel("Username")
        self.userPassLabel=QLabel("Password")
        self.textName = QLineEdit(self)
        self.textPass = QLineEdit(self)
        self.buttonLogin = QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QGridLayout(self)
        layout.addWidget(self.userNameLabel, 1, 1)
        layout.addWidget(self.userPassLabel, 2, 1)
        layout.addWidget(self.textName,1,2)
        layout.addWidget(self.textPass,2,2)
        layout.addWidget(self.buttonLogin,3,1,1,2)

        self.setWindowTitle("Login")


    def handleLogin(self):
        if (self.textName.text() == '' and
            self.textPass.text() == ''):
            self.accept()
        else:
            QMessageBox.warning(
                self, 'Error', 'Bad user or password')


def showStudent(list):
    sid=0
    dept = ""
    year = ""
    sname = ""
    course_a = ""
    course_b = ""
    course_c = ""

    sid=list[0]
    sname=list[1]

    if list[2]==0:
        dept="Mechanical Engineering"
    elif list[2]==1:
        dept="Chemical Engineering"
    elif list[2]==2:
        dept="Software Engineering"
    elif list[2]==3:
        dept="Biotech Engineering"
    elif list[2]==4:
        dept="Computer Science and Engineering"
    elif list[2]==5:
        dept="Information Technology"

    if list[3]==0:
        year="1st"
    elif list[3]==1:
        year="2nd"
    elif list[3]==2:
        year="3rd"
    elif list[3]==3:
        year="4th"

    if list[4]==0:
        course_a="DBMS"
    elif list[4]==1:
        course_a="OS"
    elif list[4]==2:
        course_a="CN"
    elif list[4]==3:
        course_a="C++"
    elif list[4]==4:
        course_a="JAVA"
    elif list[4]==5:
        course_a="PYTHON"
    elif list[4]==6:
        course_a="THERMO"
    elif list[4]==7:
        course_a="MACHINE"
    elif list[4]==8:
        course_a="CELLS"
    elif list[4]==9:
        course_a="DS"
    elif list[4]==10:
        course_a="CRE"
    elif list[4]==11:
        course_a="MICROBES"
    elif list[4]==12:
        course_a="FERTILIZER"

    if list[5]==0:
        course_b="DBMS"
    elif list[5]==1:
        course_b="OS"
    elif list[5]==2:
        course_b="CN"
    elif list[5]==3:
        course_b="C++"
    elif list[5]==4:
        course_b="JAVA"
    elif list[5]==5:
        course_b="PYTHON"
    elif list[5]==6:
        course_b="THERMO"
    elif list[5]==7:
        course_b="MACHINE"
    elif list[5]==8:
        course_b="CELLS"
    elif list[5]==9:
        course_b="DS"
    elif list[5]==10:
        course_b="CRE"
    elif list[5]==11:
        course_b="MICROBES"
    elif list[5]==12:
        course_b="FERTILIZER"

    if list[6]==0:
        course_c="DBMS"
    elif list[6]==1:
        course_c="OS"
    elif list[6]==2:
        course_c="CN"
    elif list[6]==3:
        course_c="C++"
    elif list[6]==4:
        course_c="JAVA"
    elif list[6]==5:
        course_c="PYTHON"
    elif list[6]==6:
        course_c="THERMO"
    elif list[6]==7:
        course_c="MACHINE"
    elif list[6]==8:
        course_c="CELLS"
    elif list[6]==9:
        course_c="DS"
    elif list[6]==10:
        course_c="CRE"
    elif list[6]==11:
        course_c="MICROBES"
    elif list[6]==12:
        course_c="FERTILIZER"
    elif list[6]==13:
        course_c="PLANTS"
    elif list[6]==14:
        course_c="MOBLIE APP"


    table=QTableWidget()
    tableItem=QTableWidgetItem()
    table.setWindowTitle("Student Details")
    table.setRowCount(7)
    table.setColumnCount(2)

    table.setItem(0, 0, QTableWidgetItem("Roll"))
    table.setItem(0, 1, QTableWidgetItem(str(sid)))
    table.setItem(1, 0, QTableWidgetItem("Name"))
    table.setItem(1, 1, QTableWidgetItem(str(sname)))
    table.setItem(2, 0, QTableWidgetItem("Department"))
    table.setItem(2, 1, QTableWidgetItem(str(dept)))
    table.setItem(3, 0, QTableWidgetItem("Year"))
    table.setItem(3, 1, QTableWidgetItem(str(year)))
    table.setItem(4, 0, QTableWidgetItem("Slot A"))
    table.setItem(4, 1, QTableWidgetItem(str(course_a)))
    table.setItem(5, 0, QTableWidgetItem("Slot B"))
    table.setItem(5, 1, QTableWidgetItem(str(course_b)))
    table.setItem(6, 0, QTableWidgetItem("Slot C"))
    table.setItem(6, 1, QTableWidgetItem(str(course_c)))
    table.horizontalHeader().setStretchLastSection(True)
    table.show()
    dialog=QDialog()
    dialog.setWindowTitle("Student Details")
    dialog.resize(500,300)
    dialog.setLayout(QVBoxLayout())
    dialog.layout().addWidget(table)
    dialog.exec()


class AddStudent(QDialog):
    def __init__(self):
        super().__init__()

        self.dept=-1
        self.year=-1
        self.sid=-1
        self.sname=""
        self.course_a=-1
        self.course_b=-1
        self.course_c=-1

        self.btnCancel=QPushButton("Cancel",self)
        self.btnReset=QPushButton("Reset",self)
        self.btnAdd=QPushButton("Add",self)

        self.btnCancel.setFixedHeight(30)
        self.btnReset.setFixedHeight(30)
        self.btnAdd.setFixedHeight(30)

        self.yearCombo=QComboBox(self)
        self.yearCombo.addItem("1st")
        self.yearCombo.addItem("2nd")
        self.yearCombo.addItem("3rd")
        self.yearCombo.addItem("4th")      

        self.branchCombo = QComboBox(self)
        self.branchCombo.addItem("Mechanical")
        self.branchCombo.addItem("Chemical")
        self.branchCombo.addItem("Software")
        self.branchCombo.addItem("Biotech")
        self.branchCombo.addItem("Computer Science")
        self.branchCombo.addItem("Information Technology")

        self.cACombo = QComboBox(self)
        self.cACombo.addItem("DBMS")
        self.cACombo.addItem("OS")
        self.cACombo.addItem("CN")
        self.cACombo.addItem("C++")
        self.cACombo.addItem("JAVA")
        self.cACombo.addItem("PYTHON")
        self.cACombo.addItem("THERMO")
        self.cACombo.addItem("MACHINE")
        self.cACombo.addItem("CELLS")
        self.cACombo.addItem("DS")
        self.cACombo.addItem("CRE")
        self.cACombo.addItem("MICROBES")
        self.cACombo.addItem("FERTILIZER")
        self.cACombo.addItem("PLANTS")

        self.cBCombo = QComboBox(self)
        self.cBCombo.addItem("DBMS")
        self.cBCombo.addItem("OS")
        self.cBCombo.addItem("CN")
        self.cBCombo.addItem("C++")
        self.cBCombo.addItem("JAVA")
        self.cBCombo.addItem("PYTHON")
        self.cBCombo.addItem("THERMO")
        self.cBCombo.addItem("MACHINE")
        self.cBCombo.addItem("CELLS")
        self.cBCombo.addItem("DS")
        self.cBCombo.addItem("CRE")
        self.cBCombo.addItem("MICROBES")
        self.cBCombo.addItem("FERTILIZER")
        self.cBCombo.addItem("PLANTS")

        self.cCCombo = QComboBox(self)
        self.cCCombo.addItem("DBMS")
        self.cCCombo.addItem("OS")
        self.cCCombo.addItem("CN")
        self.cCCombo.addItem("C++")
        self.cCCombo.addItem("JAVA")
        self.cCCombo.addItem("PYTHON")
        self.cCCombo.addItem("THERMO")
        self.cCCombo.addItem("MACHINE")
        self.cCCombo.addItem("CELLS")
        self.cCCombo.addItem("DS")
        self.cCCombo.addItem("CRE")
        self.cCCombo.addItem("MICROBES")
        self.cCCombo.addItem("FERTILIZER")
        self.cCCombo.addItem("PLANTS")
        self.cCCombo.addItem("MOBILE APP")

        self.rollLabel=QLabel("Roll No")
        self.nameLabel=QLabel("Name")
        self.cALabel = QLabel("Slot A")
        self.yearLabel = QLabel("Current Year")
        self.cBLabel = QLabel("Slot B")
        self.branchLabel = QLabel("Branch")
        self.cCLabel=QLabel("Slot C")
   
        self.rollText=QLineEdit(self)
        self.nameText=QLineEdit(self)

        self.grid=QGridLayout(self)
        self.grid.addWidget(self.rollLabel,1,1)
        self.grid.addWidget(self.nameLabel,2,1)
        self.grid.addWidget(self.yearLabel, 3, 1)
        self.grid.addWidget(self.branchLabel, 4, 1)
        self.grid.addWidget(self.cALabel, 5, 1)
        self.grid.addWidget(self.cBLabel, 6, 1)
        self.grid.addWidget(self.cCLabel,7,1)
        
        self.grid.addWidget(self.rollText,1,2)
        self.grid.addWidget(self.nameText,2,2)
        self.grid.addWidget(self.yearCombo, 3, 2)
        self.grid.addWidget(self.branchCombo, 4, 2)
        self.grid.addWidget(self.cACombo, 5, 2)
        self.grid.addWidget(self.cBCombo, 6, 2)
        self.grid.addWidget(self.cCCombo,7,2)
       
        self.grid.addWidget(self.btnReset,9,1)
        self.grid.addWidget(self.btnCancel,9,3)
        self.grid.addWidget(self.btnAdd,9,2)

        self.btnAdd.clicked.connect(self.addStudent)
        self.btnCancel.clicked.connect(self.Close)
        self.btnReset.clicked.connect(self.reset)
        
        self.setLayout(self.grid)
        self.setWindowTitle("Add Student Details")
        self.resize(500,300)

    def Close(self):
    	self.close()

    def reset(self):
        self.rollText.setText("")
        self.nameText.setText("")
        
    def addStudent(self):
        self.year=self.yearCombo.currentIndex()
        self.dept=self.branchCombo.currentIndex()
        self.sid=int(self.rollText.text())
        self.sname=self.nameText.text()
        self.course_a=self.cACombo.currentIndex()
        self.course_b=self.cBCombo.currentIndex()
        self.course_c=self.cCCombo.currentIndex()

        self.dbhelper=DBHelper()
        self.dbhelper.addStudent(self.sid,self.sname,self.dept ,self.year ,self.course_a ,self.course_b ,self.course_c )


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rollToBeSearched=0
        self.vbox = QVBoxLayout()
        self.text = QLabel("Enter the roll no of the student")
        self.editField = QLineEdit()
        self.btnSearch = QPushButton("Search", self)
        self.btnSearch.clicked.connect(self.showStudent)
        self.vbox.addWidget(self.text)
        self.vbox.addWidget(self.editField)
        self.vbox.addWidget(self.btnSearch)
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Enter Roll No")
        self.dialog.setLayout(self.vbox)

        self.rollForDelete = 0
        self.vboxDelete = QVBoxLayout()
        self.textDelete = QLabel("Enter the roll no of the student")
        self.editFieldDelete = QLineEdit()
        self.btnSearchDelete = QPushButton("Search", self)
        self.btnSearchDelete.clicked.connect(self.deleteRecord)                       
        self.vboxDelete.addWidget(self.textDelete)
        self.vboxDelete.addWidget(self.editFieldDelete)
        self.vboxDelete.addWidget(self.btnSearchDelete)
        self.dialogDelete = QDialog()
        self.dialogDelete.setWindowTitle("Delete Record")
        self.dialogDelete.setLayout(self.vboxDelete)

        layout = QGridLayout() # Using a GridLayout to allow the widget to be resized 

        self.btnEnterStudent=QPushButton("Enter Student Details",self)
        self.btnShowStudentDetails=QPushButton("Show Student Details",self)
        self.btnDeleteRecord=QPushButton("Delete record",self)

        self.picLabel=QLabel(self)
        self.picLabel.resize(150,150)
        self.picLabel.move(120,10)
        self.picLabel.setScaledContents(True)
        self.picLabel.setPixmap(QtGui.QPixmap("user.png"))
        layout.addWidget(self.picLabel, 0, 0) # Choose row and column for every widget

        self.btnEnterStudent.move(15,170)
        self.btnEnterStudent.resize(180,40)
        self.btnEnterStudentFont=self.btnEnterStudent.font()
        self.btnEnterStudentFont.setPointSize(13)
        self.btnEnterStudent.setFont(self.btnEnterStudentFont)
        self.btnEnterStudent.clicked.connect(self.enterstudent)
        layout.addWidget(self.btnEnterStudent, 1, 0) 

        self.btnDeleteRecord.move(205,170)
        self.btnDeleteRecord.resize(180, 40)
        self.btnDeleteRecordFont = self.btnEnterStudent.font()
        self.btnDeleteRecordFont.setPointSize(13)
        self.btnDeleteRecord.setFont(self.btnDeleteRecordFont)

        self.btnDeleteRecord.clicked.connect(self.showDeleteDialog)  
        layout.addWidget(self.btnDeleteRecord, 1, 1)                                 #2222


        self.btnShowStudentDetails.move(15, 220)
        self.btnShowStudentDetails.resize(180, 40)
        self.btnShowStudentDetailsFont = self.btnEnterStudent.font()
        self.btnShowStudentDetailsFont.setPointSize(13)
        self.btnShowStudentDetails.setFont(self.btnShowStudentDetailsFont)
        self.btnShowStudentDetails.clicked.connect(self.showStudentDialog)
        layout.addWidget(self.btnShowStudentDetails, 2, 0)
        
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w) # setting the layout to central window

        self.setFixedSize(400,280)
        self.setWindowTitle("Student Database Management System")

    def enterstudent(self):
        enterStudent=AddStudent()
        enterStudent.exec()

    def showStudentDialog(self):
        self.dialog.exec()

    def showDeleteDialog(self):
        self.dialogDelete.exec()
    
    def showStudent(self):
        if self.editField.text() is "":
            QMessageBox.warning(QMessageBox(), 'Error','You must give the roll number to show the results for.')
            return None
        showstudent = DBHelper()
        showstudent.searchStudent(int(self.editField.text()))

    def deleteRecord(self):
        if self.editField.text() is "":
            QMessageBox.warning(QMessageBox(), 'Error','You must give the roll number to show the results for.')
            return None
        delrecord = DBHelper()
        delrecord.deleteRecord(int(self.editFieldDelete.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()

    if login.exec_() == QDialog.Accepted:
        window = Window()
        window.show()
    sys.exit(app.exec_())      



