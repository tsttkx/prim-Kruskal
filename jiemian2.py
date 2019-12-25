from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtWidgets import qApp,QListWidgetItem,QApplication,QMainWindow
import numpy as np
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.Qt import QUrl
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
from pyecharts import options as opts

#封装一个关于图的信息
class kr:
    def __init__(self, new_file):
        self.m = None
        self.n = None
        self.dict = {}
        self.dict1={}
        self.matrix = None
        self.place_name = []
        # self.init_graph(new_file)
        self.file = file

    def init_graph(self):
        new_file = self.file
        with open(new_file, 'r', True, 'utf-8') as f:
            line1=f.readline()
            if line1:
                self.m, self.n = map(int, line1.replace('\n', '').split(' '))
                self.place_name.extend(f.readline().replace('\n', '').split(' '))
                self.dict = dict(zip(self.place_name, range(self.m)))
                self.dict1=dict(zip(range(self.m),self.place_name))
                self.matrix = np.full((self.m, self.m), float('inf'))
                for line in f.readlines():
                    list2 = line.replace('\n', '').split(' ')
                    i, j, value = self.  dict[list2[0]], self.dict[list2[1]], float(list2[2])
                    self.matrix[i][j] = value
                    self.matrix[j][i]=value
            else:
                self.m=self.n=0
                self.matrix=None
        # print (self.matrix)
        # print(self.m, self.n)
        # print(self.place_name)
        # print(self.dict)
        # print(self.dict1)


    #边的更新
    def updata_edge(self, from2, to1, value1):
        if self.matrix[from2][to1]==float('inf'):
            self.n += 1
        self.matrix[from2][to1]=min(self.matrix[from2][to1], value1)
        self.matrix[to1][from2] = min(self.matrix[from2][to1], value1)
        #
        #     self.matrix[from2][to1] = value1
        #     self.matrix[to1][from2]=value1
        # else:
        #     self.matrix[from2][to1] = min(self.matrix[from2][to1], value1)
        #     self.matrix[to1][from2]=min(self.matrix[from2][to1], value1)

        # print(self.matrix)
        # print(self.n)

    #点的更新
    def updata_node(self, kongjian):
        self.place_name.append(kongjian.text())
        if self.matrix is None:
            self.matrix=np.full((1,1),float('inf'))
        else:
            self.matrix = np.vstack([self.matrix, np.full((self.matrix.shape[1]), float('inf'))])
            self.matrix = np.hstack([self.matrix, np.full((self.matrix.shape[0]), float('inf')).reshape(-1, 1)])
        self.dict[kongjian.text()] = self.m
        self.dict1[self.m]=kongjian.text()
        self.m += 1
        # print(self.dict)


#界面设计封装类
class Ui_MainWindow(object):
    def setupUi(self, MainWindow, init_kr):
        self.bian=[]
        self.ans_path=[]
        self.ans_path2=[]

        self.flag1=1
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1000)
        self.new_kr = init_kr
        self.new_kr.init_graph()
        with open("Qobject.qss", "r") as f:
            qApp.setStyleSheet(f.read())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #  左边的点和边 listQwidget
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


        #上面的插入模块
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


        #右边的一列按钮操作
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setGeometry(QtCore.QRect(400, 190, 191, 651))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_3.addWidget(self.pushButton_9)


        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        MainWindow.setCentralWidget(self.centralwidget)


        #这个是最下面最小生成树的代价
        self.widget1 = QtWidgets.QWidget(MainWindow)
        self.widget1.setGeometry(QtCore.QRect(30, 890, 261, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget1)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)

        self.widget2 = QtWidgets.QWidget(MainWindow)
        self.widget2.setGeometry(QtCore.QRect(300, 890, 261, 41))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout2 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.label_6 = QtWidgets.QLabel(self.widget2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout2.addWidget(self.label_6)
        self.textBrowser2 = QtWidgets.QTextBrowser(self.widget2)
        self.textBrowser2.setObjectName("textBrowser2")
        self.horizontalLayout2.addWidget(self.textBrowser2)



        #右边的浏览器加载 html 文件
        self.stackedWidget = QtWidgets.QStackedWidget(MainWindow)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setGeometry(600, 10, 1300, 950)
        self.browser = QWebEngineView(self.stackedWidget)
        self.browser.setGeometry(0, 0, 1300, 950)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



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
        self.pyecharts_update()

        #插入操作
        self.pushButton_5.clicked.connect(self.update1)

        #删除操作
        self.listWidget.clicked.connect(self.check)
        self.pushButton.clicked.connect(self.remove)
        self.listWidget_2.clicked.connect(self.check1)
        self.pushButton_2.clicked.connect(self.remove1)

        #可视化
        self.pushButton_4.clicked.connect(self.pyecharts_update)

        # 进行写文件
        self.pushButton_6.clicked.connect(self.write)

        #prim 算法
        self.pushButton_3.clicked.connect(self.prim)

        #显示路径向量，然后就是一点的是，肯定是知道  能不能形成一个  最小生成树然后再进行  显示路径向量
        self.pushButton_7.clicked.connect(self.prim_show_path)

        self.pushButton_8.clicked.connect(self.Kruskal_show)
        self.pushButton_9.clicked.connect(self.Kruskal)



    #删除点
    def check(self,index):
        self.listWidget_2.clearSelection()
    def remove(self):
        if self.listWidget.selectedItems():
            # print(self.listWidget.currentItem().text())
            item = self.listWidget.currentItem()
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget.clearSelection()

            self.new_kr.matrix=np.delete(self.new_kr.matrix,self.new_kr.dict[item.text()],0)
            self.new_kr.matrix = np.delete(self.new_kr.matrix, self.new_kr.dict[item.text()], 1)
            self.new_kr.place_name.remove(item.text())
            self.new_kr.m-=1
            self.new_kr.n= int(np.sum(self.new_kr.matrix!=float('inf'))/2)
            self.new_kr.dict = dict(zip(self.new_kr.place_name, range(self.new_kr.m)))
            self.new_kr.dict1=dict(zip( range(self.new_kr.m),self.new_kr.place_name))

            # print(self.new_kr.m,self.new_kr.n)
            # print(self.new_kr.matrix)
            # print(self.new_kr.place_name)
            # print(self.new_kr.dict)

            data=[]
            for i in range(self.listWidget_2.count()):
                if item.text() in self.listWidget_2.item(i).text().split(' '):
                    if i not in data:
                        data.append(i)
            data=np.array(data)
            for i in data:
                self.listWidget_2.takeItem(i)
                data-=1
        self.bian = list((self.new_kr.place_name[x], self.new_kr.place_name[y]) for x in range(self.new_kr.m) for y in
                         range(x + 1, self.new_kr.m) if self.new_kr.matrix[x][y] != float('inf'))

    #删除边的
    def check1(self,index):
        self.listWidget.clearSelection()
    def remove1(self):
        if self.listWidget_2.selectedItems():
            # print(self.listWidget_2.currentItem().text())
            item = self.listWidget_2.currentItem()
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            self.listWidget_2.clearSelection()
            #先进行判断处理, 点可以影响边
            if item.text().split(' ')[0] in self.new_kr.place_name and item.text().split(' ')[1] in self.new_kr.place_name :
                a,b=self.new_kr.dict[item.text().split(' ')[0]],self.new_kr.dict[item.text().split(' ')[1]]
                self.new_kr.matrix[a][b]=float('inf')
                self.new_kr.matrix[b][a]=float('inf')
                self.new_kr.n-=1
                # print(self.new_kr.matrix)
        self.bian = list((self.new_kr.place_name[x], self.new_kr.place_name[y]) for x in range(self.new_kr.m) for y in
                     range(x + 1, self.new_kr.m) if self.new_kr.matrix[x][y] != float('inf'))

    #每一个的显示问题
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "起始点"))
        self.label_2.setText(_translate("MainWindow", "终点"))
        self.label_3.setText(_translate("MainWindow", "权值"))
        self.label3.setText(_translate("MainWindow", "点"))
        self.label_4.setText(_translate("MainWindow", "边"))
        self.pushButton_5.setText(_translate("MainWindow", "插入"))
        self.pushButton.setText(_translate("MainWindow", "删除点"))
        self.pushButton_2.setText(_translate("MainWindow", "删除边"))
        self.pushButton_3.setText(_translate("MainWindow", "prim"))
        self.pushButton_4.setText(_translate("MainWindow", "可视化"))
        self.pushButton_6.setText(_translate("MainWindow", "记录到文件"))
        self.label_5.setText(_translate("MainWindow", "prim代价为"))
        self.label_6.setText(_translate("MainWindow", "Kruskal代价为"))
        self.pushButton_7.setText(_translate("MainWindow", "prim路径"))
        self.pushButton_8.setText(_translate("MainWindow", "Kruskal路径"))
        self.pushButton_9.setText(_translate("MainWindow", "Kruskal"))

    #插入点更新
    def update1(self):
        if (self.lineEdit.text()) and (self.lineEdit_2.text()) and (self.lineEdit_3.text()):
            if self.lineEdit.text() not in self.new_kr.place_name:
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
            value = float(value)
            if self.new_kr.matrix[from1][to]==float('inf'):
                string=self.lineEdit.text()+' '+self.lineEdit_2.text()+' '+self.lineEdit_3.text()
                item = QListWidgetItem()
                item.setText(string)
                self.listWidget_2.addItem(item)
                self.new_kr.updata_edge(from1, to, value)


            # print(self.new_kr.matrix[from1][to],value,'-----')
            if  self.new_kr.matrix[from1][to]>value:
                self.new_kr.matrix[from1][to]=value
                self.new_kr.matrix[to][from1]=value
                for item3 in self.listWidget_2.selectedItems():
                    a,b=[(item3.text()).split(' ')][:2]
                    # print(a,b)
                    if a==self.listWidget.text() and b==self.listWidget_2.text() :
                        self.listWidget_2.takeItem(self.listWidget_2.row(item3))
                        break

                for i in range(self.listWidget_2.count()):
                    if self.lineEdit.text() in self.listWidget_2.item(i).text().split(' ') and self.lineEdit_2.text() in self.listWidget_2.item(i).text().split(' '):
                        self.listWidget_2.takeItem(i)
                        break
                string = self.lineEdit.text() + ' ' + self.lineEdit_2.text() + ' ' + self.lineEdit_3.text()
                item = QListWidgetItem()
                item.setText(string)
                self.listWidget_2.addItem(item)

        else:
            pass

        # print(self.new_kr.m, self.new_kr.n)
        # print(self.new_kr.matrix)
        self.bian = list((self.new_kr.place_name[x], self.new_kr.place_name[y]) for x in range(self.new_kr.m) for y in
                         range(x + 1, self.new_kr.m) if self.new_kr.matrix[x][y] != float('inf'))

        # print(self.new_kr.m,self.new_kr.n)
        # print(self.new_kr.place_name)
        # print(self.new_kr.dict)
        # print(self.new_kr.matrix)
        # print(self.new_kr.dict1)




    #克鲁斯卡尔算法
    def Kruskal(self):
        self.ans_path2=[]

        def q_sort(L, left, right):
            if left < right:
                pivot = Partition(L, left, right)

                q_sort(L, left, pivot - 1)
                q_sort(L, pivot + 1, right)
            return L

        def Partition(L, left, right):
            pivotkey = L[left]

            while left < right:
                while left < right and L[right][2] >= pivotkey[2]:
                    right -= 1
                L[left] = L[right]
                while left < right and L[left][2] <= pivotkey[2]:
                    left += 1
                L[right] = L[left]

            L[left] = pivotkey
            return left

        def find(x):
            if x==child[x]:
                # print(x)
                return x

            else:
                child[x]=find(child[x])
                return child[x]

        edge=[]
        child=list(range(self.new_kr.m))

        # for i in range(self.listWidget_2.count()):
        #     item=self.listWidget_2.item(i).text().split(' ')
        #     x=int(self.new_kr.dict[item[0]])
        #     y=int(self.new_kr.dict[item[1]])
        #     z=float(item[2])
        #     edge1.append((x,y,z))

        edge= list((x, y,self.new_kr.matrix[x][y]) for x in range(self.new_kr.m) for y in
                         range(x + 1, self.new_kr.m) if self.new_kr.matrix[x][y] != float('inf'))

        q_sort(edge,0,len(edge)-1)
        # print(edge)
        ans = 0
        k=self.new_kr.m-1

        # print(child)

        for i in range(len(edge)):
            f1=find(edge[i][0])
            f2=find(edge[i][1])
            if  f1!=f2:
                k-=1
                # print(k)
                child[f1]=f2
                ans+=edge[i][2]
                self.ans_path2.append((self.new_kr.dict1[edge[i][0]],self.new_kr.dict1[edge[i][1]]))
        if k<=0:
            self.textBrowser2.setText(str(ans))
        else:
            self.textBrowser2.setText('构不成最小生成树')
            self.ans_path2.clear()


    #prim算法
    def prim(self):
        self.flag1=1
        ans=0
        self.ans_path=[]
        dis=[0]*100
        vis=[0]*100
        pre=[0]*100
        for i in range(self.new_kr.m):
                dis[i]=self.new_kr.matrix[0][i]
        vis[0]=1
        for i in range(1,self.new_kr.m):
            minv=float('inf')
            pos=-1
            for j in range(self.new_kr.m):
                if(not vis[j] and dis[j] <minv):
                    minv=dis[j]
                    pos=j
            if pos==-1:
                self.textBrowser.setText('构不成最小生成树')
                self.flag1=0
                break
            ans+=minv

            self.ans_path.append((self.new_kr.dict1[pre[pos]],self.new_kr.dict1[pos]))

            vis[pos]=1

            for j in range(self.new_kr.m):
                if(not vis[j] and  dis[j]>self.new_kr.matrix[pos][j] ):
                    dis[j]=self.new_kr.matrix[pos][j]
                    pre[j]=pos
        if self.flag1:
            self.textBrowser.setText(str(ans))





    #进行写入文件
    def write(self):
        k=0
        with open("in.txt",'w',encoding='utf-8') as f:
            f.write(str(self.new_kr.m)+' '+str(self.new_kr.n)+'\n')
            for i in range(self.listWidget.count()):
                if k:
                    f.write(' ')
                k=1
                f.write(self.listWidget.item(i).text())
            f.write('\n')
            for i in range(self.listWidget_2.count()):
                f.write(self.listWidget_2.item(i).text()+'\n')


    #克鲁斯卡尔显示路径
    def Kruskal_show(self):
        place = list(zip(self.new_kr.place_name, range(self.new_kr.m)))
        if len(self.ans_path2):
            attr2 = self.ans_path2
        else:
            attr2=[]
        def diff_set(a, b):
            a_, b_ = map(lambda x: {frozenset(k): k for k in x}, [a, b])
            return [a_[k] for k in a_.keys() - b_.keys()]
        attr1=diff_set(self.bian,attr2)

        # print(attr1)
        # print(attr2)

        geo = (
            Geo(init_opts={"width": 1300, "bg_color": "#2a59"})
                .add_schema(
                maptype="china",
                itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),
            )
                .add(
                "",
                place,
                type_=ChartType.EFFECT_SCATTER,
                color="green",
            )
                .add(
                "",
                attr1,
                type_=ChartType.LINES,
                linestyle_opts=opts.LineStyleOpts(curve=0.2, color='red'),
            )
                .add(
                "",  # 这个就是我设置的路径，最后生成的路径使用另一种颜色完成
                attr2,
                type_=ChartType.LINES,
                linestyle_opts=opts.LineStyleOpts(curve=0.2, color='white'),
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(title_opts=opts.TitleOpts(title="城市交通图"))
        )
        geo.render(path='D:/pycharm/untitled/GUI/图.html')
        self.browser.load(QUrl("file:///D:/pycharm/untitled/GUI/图.html"))



    #prim显示路径
    def prim_show_path(self):
        place = list(zip(self.new_kr.place_name, range(self.new_kr.m)))

        if self.flag1:
            attr2=self.ans_path
        else:
            attr2=[]

        def diff_set(a, b):
            a_, b_ = map(lambda x: {frozenset(k): k for k in x}, [a, b])
            return [a_[k] for k in a_.keys() - b_.keys()]
        attr1=diff_set(self.bian,attr2)

        # print(attr1)
        # print(attr2)

        geo = (
            Geo(init_opts={"width": 1300, "bg_color": "#2a59"})
                .add_schema(
                maptype="china",
                itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),
            )
                .add(
                "",
                place,
                type_=ChartType.EFFECT_SCATTER,
                color="green",
            )
                .add(
                "",
                attr1,
                type_=ChartType.LINES,
                linestyle_opts=opts.LineStyleOpts(curve=0.2, color='red'),
            )
                .add(
                "",
                     attr2,
                    type_=ChartType.LINES,
                     linestyle_opts=opts.LineStyleOpts(curve=0.2,color='white'),
                )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(title_opts=opts.TitleOpts(title="城市交通图"))
        )
        geo.render(path='D:/pycharm/untitled/GUI/图.html')
        self.browser.load(QUrl("file:///D:/pycharm/untitled/GUI/图.html"))



    #进行可视化
    def pyecharts_update(self):
        place=list(zip(self.new_kr.place_name,range(self.new_kr.m)))
        self.bian=list((self.new_kr.place_name[x],self.new_kr.place_name[y]) for x in range(self.new_kr.m) for y in range(x+1,self.new_kr.m) if self.new_kr.matrix[x][y]!=float('inf'))

        # for i in range(self.listWidget_2.count()):
        #     item=self.listWidget_2.item(i).text().split(' ')
        #     self.bian.append((item[0],item[1]))
        # print(self.bian)

        geo = (
             Geo(init_opts = {"width":1300,"bg_color":"#2a59"})
                .add_schema(
                maptype="china",
                itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),
                 # label_opts=opts.LabelOpts(is_show=True)
            )
                .add(
                "",
                 place,
                type_=ChartType.EFFECT_SCATTER,
                color="green",
                label_opts=opts.LabelOpts(is_show=True)
            )
                .add(
                "",
                 self.bian,
                 type_=ChartType.LINES,
                linestyle_opts=opts.LineStyleOpts(curve=0.2, color='red'),


            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(title_opts=opts.TitleOpts(title="城市交通图"))
        )
        geo.render(path='D:/pycharm/untitled/GUI/图.html')
        self.browser.load(QUrl("file:///D:/pycharm/untitled/GUI/图.html"))



#主函数
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    file = "oo.txt"
    now = kr(file)

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, now)
    MainWindow.show()

    sys.exit(app.exec_())
