#删除  肯定是需要进行， 今天下午  把这些  功能实现一下 ， 删除操作，

from pyecharts .render import make_snapshot
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.Qt import *
import numpy as np
from PyQt5.QtWebEngineWidgets import QWebEngineView
import codecs
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

class kr:
    def __init__(self, new_file):
        self.m = None
        self.n = None
        self.value = []
        self.dict = {}
        self.matrix = None  # 储存
        self.place_name = []
        # self.init_graph(new_file)
        self.file = file

    def init_graph(self):
        new_file = self.file
        with open(new_file, 'r', True, 'utf-8') as f:
            self.m, self.n = map(int, f.readline().replace('\n', '').split(' '))
            self.place_name.extend(f.readline().replace('\n', '').split(' '))
            self.dict = dict(zip(self.place_name, range(self.m)))
            self.matrix = np.full((self.m, self.m), np.nan)

            for line in f.readlines():
                list2 = line.replace('\n', '').split(' ')
                i, j, value = self.dict[list2[0]], self.dict[list2[1]], int(list2[2])
                self.matrix[i][j] = value
        f.close()
        # print(self.m, self.n)
        # print(self.place_name)
        # print(self.dict)

    def updata_edge(self, from2, to1, value1):                                                                          #边的更新
        if np.isnan(self.matrix[from2][to1]):
            self.n += 1
        if np.isnan(self.matrix[from2][to1]):
            self.matrix[from2][to1] = value1
        else:
            self.matrix[from2][to1] = min(self.matrix[from2][to1], value1)
        print(self.matrix)
        print(self.n)

    def updata_node(self, kongjian):                                                                                    #点的更新
        self.place_name.append(kongjian.text())
        self.matrix = np.vstack([self.matrix, np.full((self.matrix.shape[1]), np.nan)])
        self.matrix = np.hstack([self.matrix, np.full((self.matrix.shape[0]), np.nan).reshape(-1, 1)])
        self.dict[kongjian.text()] = self.m
        self.m += 1
        print(self.dict)

    def prime(self):                                                                                                    #进行更新，点击
        pass





class Ui_MainWindow(object):
    def setupUi(self, MainWindow, init_kr):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1000)
        self.new_kr = init_kr
        self.new_kr.init_graph()
        with open("Qobject.qss", "r") as f:
            qApp.setStyleSheet(f.read())




        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 190, 291, 651))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label3 = QtWidgets.QLabel(self.widget)
        self.label3.setObjectName("label")
        self.verticalLayout.addWidget(self.label3)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_4)
        self.listWidget_2 = QtWidgets.QListWidget(self.widget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)




        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 30, 441, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 90, 441, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 190, 191, 651))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)






        self.stackedWidget = QtWidgets.QStackedWidget(MainWindow)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setGeometry(600, 10, 1300, 950)
        self.browser = QWebEngineView(self.stackedWidget)




        self.browser.setGeometry(0,0,1300,950)              # 这个是我生成的一个   小浏览器，然后就是，小的浏览器
        self.browser.load(QUrl("file:///D:/pycharm/untitled/GUI/图.html"))




        # 首先是    将所有的文本中的数据  加入到list 中,
        with open(self.new_kr.file, 'r', True, 'utf-8') as f:
            f.readline()
            f.readline()
            for line in f.readlines():
                list= line.replace('\n', '')
                item=QListWidgetItem()
                item.setText(list)
                self.listWidget_2.addItem(item)

        for i in range(len(self.new_kr.place_name)):
            item=QListWidgetItem()
            item.setText(self.new_kr.place_name[i])
            self.listWidget.addItem(item)



        # self.pyecharts_update()
        self.pushButton_5.pressed.connect(self.update1)                          #插入

        # self.listWidget.clicked.connect(self.dele_item_dian)                     #删除点
        # self.listWidget_2.clicked.connect(self.dele_item_bian)                   #删除边


        # self.a=pyqtSignal()                 #一个是选中  widget 中的item
        # self.b=pyqtSignal()                 #一个是 push，pushbottem
        # self.a.connect(lambda:())
        # self.a.connect(self.pushButton_3)

        # self.pushButton_3.clicked.connect(self.dele_item_dian())
        # self.pushButton_3.clicked.connect(self.dele_item_bian())

        self.listWidget.clicked.connect(self.check)
        self.pushButton_3.clicked.connect(self.remove)
        self.listWidget_2.clicked.connect(self.check1)
        self.pushButton_3.clicked.connect(self.remove1)
        self.mouse=QMouseEvent



        # 鼠标点击空白  使得选中效果消失     点击
    def quxiao_dele(self,mylistqwidge):
        # self.mouse.
        pass

    def check(self,index):
        r=index.row()
        self.f=r
    def remove(self):
        items = self.listWidget.selectedIndexes()
        if items:
            self.listWidget.removeItemWidget(self.listWidget.takeItem(self.f))
    def check1(self,index):
        r=index.row()
        self.f1=r
    def remove1(self):
        items = self.listWidget_2.selectedIndexes()
        if items:
            self.listWidget_2.removeItemWidget(self.listWidget_2.takeItem(self.f1))
    def quxiao_zhuangtai(self,event):
        pass






    # def dele_item_dian1(self,item):                                      #我只想删除当前 所选的 item，不是
    #     # item = self.listWidget.setcurrentItem()
    #     # self.listWidget.takeItem(self.listWidget.row(item))
    #     print(self.listWidget.setCurrentItem())
    #
    # def dele_item_dian(self):                       #
    #     self.pushButton_3.clicked.connect(self.dele_item_dian1)
    #
    #
    #
    # def dele_item_bian1(self):
    #     item = self.listWidget_2.setcurrentItem()
    #     self.listWidget_2.takeItem(self.listWidget_2.row(item))
    #
    # def dele_item_bian(self):
    #     self.pushButton_3.clicked.connect(self.dele_item_bian1)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "起始点"))
        self.label_2.setText(_translate("MainWindow", "终点"))
        self.label_3.setText(_translate("MainWindow", "权值"))
        self.pushButton_5.setText(_translate("MainWindow", "插入"))
        self.pushButton_3.setText(_translate("MainWindow", "删除"))
        self.pushButton_2.setText(_translate("MainWindow", "prim算法"))
        self.pushButton.setText(_translate("MainWindow", "可视化"))
        self.label3.setText(_translate("MainWindow", "点"))
        self.label_4.setText(_translate("MainWindow", "边"))

    def update1(self):                                                                                                  #更新点，边
        if (self.lineEdit.text()) and (self.lineEdit_2.text()) and (self.lineEdit_3.text()):
            if self.lineEdit.text() not in self.new_kr.place_name:  #
                item1=QListWidgetItem()
                item1.setText(self.lineEdit.text())
                self.listWidget.addItem(item1)
                self.new_kr.updata_node(self.lineEdit)


            if self.lineEdit_2.text() not in self.new_kr.place_name:
                item2 = QListWidgetItem()
                item2.setText(self.lineEdit_2.text())
                self.listWidget.addItem(item2)
                self.new_kr.updata_node(self.lineEdit_2)

            from1 = self.new_kr.dict[self.lineEdit.text()]
            to = self.new_kr.dict[self.lineEdit_2.text()]
            value = self.lineEdit_3.text()
            value = int(value)
            if np.isnan(self.new_kr.matrix[from1][to]):
                string=self.lineEdit.text()+' '+self.lineEdit_2.text()+' '+self.lineEdit_3.text()
                item = QListWidgetItem()
                item.setText(string)
                self.listWidget_2.addItem(item)
                self.new_kr.updata_edge(from1, to, value)


            print(self.new_kr.matrix[from1][to],value,'-----')
            if not np.isnan(self.new_kr.matrix[from1][to]) and self.new_kr.matrix[from1][to]>value:               #这个是删除边
                for item3 in self.listWidget_2.selectedItems():
                    a,b=[(item3.text()).split(' ')][:2]
                    print(a,b)
                    if a==self.listWidget.text() and b==self.listWidget_2.text() :
                        self.listWidget_2.takeItem(self.listWidget_2.row(item3))
                        break



        else:
            pass




    def update_browser_init(self):                                                                                      #图片的更新
        pass

    def update2(self):                                                                                                  # 删除点
        pass

    def update3(self):                                                                                                  # prim算法
        pass

    def pyecharts_update(self):                                                                                         # 可视化
        # node_show=list(zip(self.))

        geo = (
             Geo(init_opts = {"width":1300,"bg_color":"#2a59"})

                .add_schema(
                maptype="china",
                itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#211"),
            )
                .add(
                "城市交通图",
                [("广州", 55), ("北京", 66), ("杭州", 77), ("重庆", 88),('上海',100),('任县',123),('太原',12)],           #把这改了
                type_=ChartType.EFFECT_SCATTER,
                color="red",
            )
                .add(
                "城市交通图",
                [("广州", "上海"), ("广州", "北京"), ("广州", "杭州"), ("广州", "重庆")],
                type_=ChartType.LINES,
                effect_opts=opts.EffectOpts(
                    symbol=SymbolType.ARROW, symbol_size=6, color="blue"
                ),
                linestyle_opts=opts.LineStyleOpts(curve=0.2),
            )

                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(title_opts=opts.TitleOpts(title="城市交通图"))

        )
        geo.render(path='D:/pycharm/untitled/GUI/图.html')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    file = "oo.txt"
    now = kr(file)

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, now)
    MainWindow.show()

    sys.exit(app.exec_())
