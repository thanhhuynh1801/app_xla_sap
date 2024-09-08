## Software built by thanhhuynh 27/08/2024
## check quantity SAP

from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QRect,Qt)
from PySide6.QtGui import (QAction,
    QFont, QImage, 
    QPainter, QPixmap)
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QTextEdit, QVBoxLayout, QScrollBar,QHBoxLayout,
    QToolBar, QWidget,QFileDialog, QMessageBox ,QGraphicsScene,QGraphicsPixmapItem)
import cv2
import numpy as np
from math import atan2, cos, sin, sqrt, pi
import datetime
import serial
import os
import multiprocessing
from multiprocessing import Process, Event, Queue
from pypylon import pylon

def task1(event, exit_event, auto_event,ketquaxuly, datacom, connectcom,capture_img,auto_run,stop_event,stop_runcalib):
    print("Task 1 assigned to process: {}".format(os.getpid())) 
    class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
            if not MainWindow.objectName():
                MainWindow.setObjectName(u"MainWindow")
            MainWindow.resize(1529, 935)
            font = QFont()
            font.setBold(False)
            font.setKerning(True)
            MainWindow.setFont(font)
            MainWindow.setAcceptDrops(False)
            MainWindow.setAutoFillBackground(False)
            MainWindow.setStyleSheet(u"")
            self.action_connect_cam = QAction(MainWindow)
            self.action_connect_cam.setObjectName(u"action_connect_cam")
            self.action_disconnect_cam = QAction(MainWindow)
            self.action_disconnect_cam.setObjectName(u"action_disconnect_cam")
            self.action_runcalib = QAction(MainWindow)
            self.action_runcalib.setObjectName(u"action_runcalib")
            self.action_stopcalib = QAction(MainWindow)
            self.action_stopcalib.setObjectName(u"action_stopcalib")
            self.action_connect_com = QAction(MainWindow)
            self.action_connect_com.setObjectName(u"action_connect_com")
            self.action_disconnect_com = QAction(MainWindow)
            self.action_disconnect_com.setObjectName(u"action_disconnect_com")
            self.save_img = QAction(MainWindow)
            self.save_img.setObjectName(u"save_img")
            self.save_as_img = QAction(MainWindow)
            self.save_as_img.setObjectName(u"save_as_img")
            self.open_img = QAction(MainWindow)
            self.open_img.setObjectName(u"open_img")
            self.actionSp2 = QAction(MainWindow)
            self.actionSp2.setObjectName(u"actionSp2")
            self.bankinhnho = QAction(MainWindow)
            self.bankinhnho.setObjectName(u"bankinhnho")
            self.bankinhnho.setText("Cắt mẫu")
            self.bankinhlon = QAction(MainWindow)
            self.bankinhlon.setObjectName(u"bankinhlon")
            self.bankinhlon.setText("Vẽ khung")
            self.test_sp1 = QAction(MainWindow)
            self.test_sp1.setObjectName(u"test_sp1")
            self.test_sp2 = QAction(MainWindow)
            self.test_sp2.setObjectName(u"test_sp2")
            self.centralwidget = QWidget(MainWindow)
            self.centralwidget.setObjectName(u"centralwidget")
            self.groupBox = QGroupBox(self.centralwidget)
            self.groupBox.setObjectName(u"groupBox")
            self.groupBox.setGeometry(QRect(1160, 660, 331, 81))
            font1 = QFont()
            font1.setPointSize(9)
            font1.setBold(False)
            font1.setKerning(True)
            self.groupBox.setFont(font1)
            self.groupBox.setStyleSheet(u"")
            self.cambien = QLabel(self.groupBox)
            self.cambien.setObjectName(u"cambien")
            self.cambien.setGeometry(QRect(30, 40, 25, 25))
            self.cambien.setStyleSheet(u"QLabel#cambien {\n"
    "    background-color: gray;\n"
    "    border-radius: 12px;\n"
    "    min-width: 25px;\n"
    "    min-height: 25px;\n"
    "    max-width: 25px;\n"
    "    max-height:25px;\n"
    "}")
            self.label_2 = QLabel(self.groupBox)
            self.label_2.setObjectName(u"label_2")
            self.label_2.setGeometry(QRect(70, 40, 71, 31))
            self.label_2.setFont(font1)
            self.xylanh = QLabel(self.groupBox)
            self.xylanh.setObjectName(u"xylanh")
            self.xylanh.setGeometry(QRect(200, 40, 25, 25))
            self.xylanh.setStyleSheet(u"QLabel#xylanh {\n"
    "    background-color: gray;\n"
    "    border-radius: 12px;\n"
    "    min-width: 25px;\n"
    "    min-height: 25px;\n"
    "    max-width: 25px;\n"
    "    max-height:25px;\n"
    "}")
            self.label_4 = QLabel(self.groupBox)
            self.label_4.setObjectName(u"label_4")
            self.label_4.setGeometry(QRect(240, 40, 51, 31))
            self.label_4.setFont(font1)
            self.groupBox_2 = QGroupBox(self.centralwidget)
            self.groupBox_2.setObjectName(u"groupBox_2")
            self.groupBox_2.setGeometry(QRect(810, 160, 341, 221))
            self.groupBox_2.setFont(font1)
            self.groupBox_2.setStyleSheet(u"")
            self.led_sp_dat = QLabel(self.groupBox_2)
            self.led_sp_dat.setObjectName(u"led_sp_dat")
            self.led_sp_dat.setGeometry(QRect(50, 60, 50, 50))
            self.led_sp_dat.setStyleSheet(u"QLabel#led_sp_dat{\n"
    "    background-color: gray;\n"
    "    border-radius: 25px;\n"
    "    min-width: 50px;\n"
    "    min-height: 50px;\n"
    "    max-width: 50px;\n"
    "    max-height:50px;\n"
    "}")
            self.led_sp_kodat = QLabel(self.groupBox_2)
            self.led_sp_kodat.setObjectName(u"led_sp_kodat")
            self.led_sp_kodat.setGeometry(QRect(50, 140, 50, 50))
            self.led_sp_kodat.setStyleSheet(u"QLabel#led_sp_kodat{\n"
    "    background-color: gray;\n"
    "    border-radius: 25px;\n"
    "    min-width: 50px;\n"
    "    min-height: 50px;\n"
    "    max-width: 50px;\n"
    "    max-height:50px;\n"
    "}")
            self.label_6 = QLabel(self.groupBox_2)
            self.label_6.setObjectName(u"label_6")
            self.label_6.setGeometry(QRect(120, 70, 91, 31))
            font2 = QFont()
            font2.setPointSize(14)
            font2.setBold(False)
            font2.setKerning(True)
            self.label_6.setFont(font2)
            self.label_7 = QLabel(self.groupBox_2)
            self.label_7.setObjectName(u"label_7")
            self.label_7.setGeometry(QRect(120, 150, 171, 41))
            self.label_7.setFont(font2)
            self.groupBox_3 = QGroupBox(self.centralwidget)
            self.groupBox_3.setObjectName(u"groupBox_3")
            self.groupBox_3.setGeometry(QRect(60, 150, 731, 671))
            self.groupBox_3.setFont(font1)
            self.groupBox_3.setStyleSheet(u"")
            self.hienthianh = QGraphicsView(self.groupBox_3)
            self.hienthianh.setObjectName(u"hienthianh")
            self.hienthianh.setGeometry(QRect(20, 30, 691, 621))
            self.hienthianh.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.groupBox_4 = QGroupBox(self.centralwidget)
            self.groupBox_4.setObjectName(u"groupBox_4")
            self.groupBox_4.setGeometry(QRect(1160, 320, 331, 331))
            self.groupBox_4.setFont(font1)
            self.groupBox_4.setStyleSheet(u"")
            self.chupanh = QPushButton(self.groupBox_4)
            self.chupanh.setObjectName(u"chupanh")
            self.chupanh.setGeometry(QRect(70, 190, 81, 41))
            self.chupanh.setFont(font1)
            self.chupanh.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.onxylanh = QPushButton(self.groupBox_4)
            self.onxylanh.setObjectName(u"onxylanh")
            self.onxylanh.setGeometry(QRect(200, 190, 81, 41))
            self.onxylanh.setFont(font1)
            self.onxylanh.setStyleSheet(u"background-color: rgb(255, 255, 255);")

            self.button_exit = QPushButton(MainWindow)
            self.button_exit.setObjectName(u"button_exit")
            self.button_exit.setGeometry(QRect(1400, 50, 81, 31))
            self.button_exit.setStyleSheet("font-size: 30px;")
            # self.button_exit.setFont(font1)
            self.button_exit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

            self.label_8 = QLabel(self.groupBox_4)
            self.label_8.setObjectName(u"label_8")
            self.label_8.setGeometry(QRect(30, 40, 51, 21))
            font3 = QFont()
            font3.setPointSize(12)
            font3.setBold(False)
            font3.setKerning(True)
            self.label_8.setFont(font3)
            self.label_9 = QLabel(self.groupBox_4)
            self.label_9.setObjectName(u"label_9")
            self.label_9.setGeometry(QRect(30, 140, 71, 31))
            self.label_9.setFont(font3)
            self.chay = QPushButton(self.groupBox_4)
            self.chay.setObjectName(u"chay")
            self.chay.setGeometry(QRect(70, 80, 81, 41))
            self.chay.setFont(font1)
            self.chay.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.dung = QPushButton(self.groupBox_4)
            self.dung.setObjectName(u"dung")
            self.dung.setGeometry(QRect(200, 80, 71, 41))
            self.dung.setFont(font1)
            self.dung.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.groupBox_5 = QGroupBox(self.centralwidget)
            self.groupBox_5.setObjectName(u"groupBox_5")
            self.groupBox_5.setGeometry(QRect(810, 390, 341, 351))
            self.groupBox_5.setFont(font1)
            self.groupBox_5.setStyleSheet(u"")
            self.hienthitrangthai = QTextEdit(self.groupBox_5)
            self.hienthitrangthai.setObjectName(u"hienthitrangthai")
            self.hienthitrangthai.setGeometry(QRect(10, 30, 321, 221))
            self.hienthitrangthai.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.led_connect_cam = QLabel(self.groupBox_5)
            self.led_connect_cam.setObjectName(u"led_connect_cam")
            self.led_connect_cam.setGeometry(QRect(30, 310, 25, 25))
            self.led_connect_cam.setStyleSheet(u"QLabel#led_connect_cam{\n"
    "    background-color: gray;\n"
    "    border-radius: 12px;\n"
    "    min-width: 25px;\n"
    "    min-height: 25px;\n"
    "    max-width: 25px;\n"
    "    max-height:25px;\n"
    "}")
            self.label_10 = QLabel(self.groupBox_5)
            self.label_10.setObjectName(u"label_10")
            self.label_10.setGeometry(QRect(70, 310, 61, 21))
            self.label_10.setFont(font1)
            self.led_connect_com = QLabel(self.groupBox_5)
            self.led_connect_com.setObjectName(u"led_connect_com")
            self.led_connect_com.setGeometry(QRect(200, 310, 25, 25))
            self.led_connect_com.setStyleSheet(u"QLabel#led_connect_com {\n"
    "    background-color: gray;\n"
    "    border-radius: 12px;\n"
    "    min-width: 25px;\n"
    "    min-height: 25px;\n"
    "    max-width: 25px;\n"
    "    max-height:25px;\n"
    "}")
            self.label_11 = QLabel(self.groupBox_5)
            self.label_11.setObjectName(u"label_11")
            self.label_11.setGeometry(QRect(240, 310, 81, 21))
            self.label_11.setFont(font1)
            self.label_12 = QLabel(self.groupBox_5)
            self.label_12.setObjectName(u"label_12")
            self.label_12.setGeometry(QRect(10, 280, 131, 21))
            self.label_12.setFont(font1)
            self.clearbox = QPushButton(self.groupBox_5)
            self.clearbox.setObjectName(u"clearbox")
            self.clearbox.setGeometry(QRect(270, 260, 61, 31))
            self.groupBox_6 = QGroupBox(self.centralwidget)
            self.groupBox_6.setObjectName(u"groupBox_6")
            self.groupBox_6.setGeometry(QRect(1160, 160, 331, 151))
            self.groupBox_6.setFont(font1)
            self.groupBox_6.setStyleSheet(u"")
            self.label_13 = QLabel(self.groupBox_6)
            self.label_13.setObjectName(u"label_13")
            self.label_13.setGeometry(QRect(40, 100, 71, 41))
            self.label_13.setFont(font1)
            self.label_14 = QLabel(self.groupBox_6)
            self.label_14.setObjectName(u"label_14")
            self.label_14.setGeometry(QRect(140, 110, 61, 21))
            self.label_14.setFont(font1)
            self.label_15 = QLabel(self.groupBox_6)
            self.label_15.setObjectName(u"label_15")
            self.label_15.setGeometry(QRect(250, 110, 47, 21))
            self.label_15.setFont(font1)
            self.led_start = QLabel(self.groupBox_6)
            self.led_start.setObjectName(u"led_start")
            self.led_start.setGeometry(QRect(40, 40, 50, 50))
            self.led_start.setStyleSheet(u"QLabel#led_start{\n"
    "    background-color: gray;\n"
    "    border-radius: 25px;\n"
    "    min-width: 50px;\n"
    "    min-height: 50px;\n"
    "    max-width: 50px;\n"
    "    max-height:50px;\n"
    "}")
            self.led_stop = QLabel(self.groupBox_6)
            self.led_stop.setObjectName(u"led_stop")
            self.led_stop.setGeometry(QRect(140, 40, 50, 50))
            self.led_stop.setStyleSheet(u"QLabel#led_stop{\n"
    "    background-color: red;\n"
    "    border-radius: 25px;\n"
    "    min-width: 50px;\n"
    "    min-height: 50px;\n"
    "    max-width: 50px;\n"
    "    max-height:50px;\n"
    "}")
            self.led_loi = QLabel(self.groupBox_6)
            self.led_loi.setObjectName(u"led_loi")
            self.led_loi.setGeometry(QRect(230, 40, 50, 50))
            self.led_loi.setStyleSheet(u"QLabel#led_loi{\n"
    "    background-color: gray;\n"
    "    border-radius: 25px;\n"
    "    min-width: 50px;\n"
    "    min-height: 50px;\n"
    "    max-width: 50px;\n"
    "    max-height:50px;\n"
    "}")
            self.groupBox_7 = QGroupBox(self.centralwidget)
            self.groupBox_7.setObjectName(u"groupBox_7")
            self.groupBox_7.setGeometry(QRect(630, 10, 451, 81))
            self.groupBox_7.setToolTip(u"")
            self.groupBox_7.setStatusTip(u"")
            self.groupBox_7.setWhatsThis(u"")
            self.groupBox_7.setAccessibleDescription(u"")
            self.groupBox_7.setAutoFillBackground(True)
            self.groupBox_7.setStyleSheet(u"")
            self.groupBox_7.setFlat(False)
            self.label_17 = QLabel(self.groupBox_7)
            self.label_17.setObjectName(u"label_17")
            self.label_17.setGeometry(QRect(40, 10, 361, 51))
            font4 = QFont()
            font4.setPointSize(24)
            font4.setBold(False)
            font4.setKerning(True)
            self.label_17.setFont(font4)
            self.label_17.setAutoFillBackground(True)
            self.groupBox_8 = QGroupBox(self.centralwidget)
            self.groupBox_8.setObjectName(u"groupBox_8")
            self.groupBox_8.setGeometry(QRect(60, 70, 521, 71))
            font5 = QFont()
            font5.setPointSize(9)
            self.groupBox_8.setFont(font5)
            self.groupBox_8.setStyleSheet(u"")
            self.label_5 = QLabel(self.groupBox_8)
            self.label_5.setObjectName(u"label_5")
            self.label_5.setGeometry(QRect(10, 30, 161, 21))
            self.label_5.setFont(font1)
            self.chon_com = QLineEdit(self.groupBox_8)
            self.chon_com.setObjectName(u"chon_com")
            self.chon_com.setGeometry(QRect(150, 20, 81, 31))
            self.chon_com.setFont(font1)
            self.chon_com.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.label_16 = QLabel(self.groupBox_8)
            self.label_16.setObjectName(u"label_16")
            self.label_16.setGeometry(QRect(250, 30, 171, 16))
            self.label_16.setFont(font1)
            self.chon_sp = QComboBox(self.groupBox_8)
            self.chon_sp.addItem("")
            self.chon_sp.addItem("")
            self.chon_sp.setObjectName(u"chon_sp")
            self.chon_sp.setGeometry(QRect(420, 20, 81, 31))
            self.chon_sp.setFont(font1)
            self.chon_sp.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QMenuBar(MainWindow)
            self.menubar.setObjectName(u"menubar")
            self.menubar.setGeometry(QRect(0, 0, 1529, 26))
            self.menucamera = QMenu(self.menubar)
            self.menucamera.setObjectName(u"menucamera")
            self.menuCalib_Camera = QMenu(self.menubar)
            self.menuCalib_Camera.setObjectName(u"menuCalib_Camera")
            self.menuConnect_Com = QMenu(self.menubar)
            self.menuConnect_Com.setObjectName(u"menuConnect_Com")
            self.menuC_i_t_th_ng_s = QMenu(self.menubar)
            self.menuC_i_t_th_ng_s.setObjectName(u"menuC_i_t_th_ng_s")
            self.menuSP1 = QMenu(self.menuC_i_t_th_ng_s)
            self.menuSP1.setObjectName(u"menuSP1")
            self.menuFile = QMenu(self.menubar)
            self.menuFile.setObjectName(u"menuFile")
            self.menuKi_m_tra_ch_ng_tr_nh = QMenu(self.menubar)
            self.menuKi_m_tra_ch_ng_tr_nh.setObjectName(u"menuKi_m_tra_ch_ng_tr_nh")
            MainWindow.setMenuBar(self.menubar)
            self.toolBar = QToolBar(MainWindow)
            self.toolBar.setObjectName(u"toolBar")
            MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

            self.menubar.addAction(self.menuFile.menuAction())
            self.menubar.addAction(self.menucamera.menuAction())
            self.menubar.addAction(self.menuCalib_Camera.menuAction())
            self.menubar.addAction(self.menuConnect_Com.menuAction())
            self.menubar.addAction(self.menuC_i_t_th_ng_s.menuAction())
            self.menubar.addAction(self.menuKi_m_tra_ch_ng_tr_nh.menuAction())
            self.menucamera.addAction(self.action_connect_cam)
            self.menucamera.addAction(self.action_disconnect_cam)
            self.menuCalib_Camera.addAction(self.action_runcalib)
            self.menuCalib_Camera.addAction(self.action_stopcalib)
            self.menuConnect_Com.addAction(self.action_connect_com)
            self.menuConnect_Com.addAction(self.action_disconnect_com)
            self.menuC_i_t_th_ng_s.addAction(self.menuSP1.menuAction())
            self.menuC_i_t_th_ng_s.addAction(self.actionSp2)
            self.menuSP1.addAction(self.bankinhnho)
            self.menuSP1.addAction(self.bankinhlon)
            self.menuFile.addAction(self.save_img)
            self.menuFile.addAction(self.save_as_img)
            self.menuFile.addAction(self.open_img)
            self.menuKi_m_tra_ch_ng_tr_nh.addAction(self.test_sp1)
            self.menuKi_m_tra_ch_ng_tr_nh.addAction(self.test_sp2)

            self.retranslateUi(MainWindow)

            QMetaObject.connectSlotsByName(MainWindow)
            # setupUi


            self.save_img.triggered.connect(self.save_image)
            self.save_as_img.triggered.connect(self.save_image_as)
            self.open_img.triggered.connect(self.open_image)
            self.actionSp2.triggered.connect(self.open_new_gui)
            self.bankinhnho.triggered.connect(self.crop_img)
            self.bankinhlon.triggered.connect(self.meg_infor_vekhung)
            # Khởi tạo giá trị bán kính
            self.radius_large = 42  # Giá trị mặc định
            self.radius_small = 37  # Giá trị mặc định
            # khởi tạo giá trị diện tích
            self.area_max = 6500  # Giá trị mặc định
            self.area_min = 5000  # Giá trị mặc định
            self.offset = 230 # giá trị ban đầu của offset
            self.width = 520 # giá trị ban đầu chiều dài khung cắt
            self.height = 70 # giá trị ban đầu chiều rộng khung cắt
            # ảnh sau khi cắt
            self.cropped_image=None
            ## các thông số vẽ các khung khe
            self.x1_1 = int(28)
            self.y1_1 = int(0)
            self.x2_1 = int(75)
            self.y2_1 = int(69)
            self.khoancach= 70
            self.blocksize=13   # số lẻ
            self.constant=2

            self.cap=None
            # các hàm 
            self.action_runcalib.triggered.connect(self.action_runcalib_triggered)
            self.action_stopcalib.triggered.connect(self.stop_calibcamera)
            self.action_connect_com.triggered.connect(self.connect_com)
            self.action_disconnect_com.triggered.connect(self.disconnect_com)
            self.action_connect_cam.triggered.connect(self.connect_cam)
            self.action_disconnect_cam.triggered.connect(self.disconnect_cam)
            self.chupanh.clicked.connect(self.capture_photo)
            self.onxylanh.clicked.connect(self.on_xylanh)
            self.chay.clicked.connect(self.run_auto)
            self.dung.clicked.connect(self.stop_auto)
            self.button_exit.clicked.connect(self.close_application)
            self.clearbox.clicked.connect(self.xoakhungthongbao)
            self.chon_sp.activated.connect(self.on_combobox_activated)

            # các biến đa luồng
            self.event = multiprocessing.Event()
            self.exit_event = multiprocessing.Event()
            self.ang_queue = Queue()
            self.point_queue = Queue()
            self.point_queue1 = Queue()

            self.p1 = None
            self.p2 = None
            self.status_connectcom=False
            self.status_connectcam=False
            self.stop_event = stop_event

            self.luachonsp = 0

        def retranslateUi(self, MainWindow):
            MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
            MainWindow.setWindowFilePath("")
            self.action_connect_cam.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
            self.action_disconnect_cam.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
            self.action_runcalib.setText(QCoreApplication.translate("MainWindow", u"Run Calib", None))
            self.action_stopcalib.setText(QCoreApplication.translate("MainWindow", u"Stop Calib", None))
            self.action_connect_com.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
            self.action_disconnect_com.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
            self.save_img.setText(QCoreApplication.translate("MainWindow", u"Save image", None))
            self.save_as_img.setText(QCoreApplication.translate("MainWindow", u"Save As image", None))
            self.open_img.setText(QCoreApplication.translate("MainWindow", u"Open image", None))
            self.actionSp2.setText(QCoreApplication.translate("MainWindow", u"Sp2", None))
            self.bankinhnho.setText(QCoreApplication.translate("MainWindow", u"Cắt mẫu", None))
            self.bankinhlon.setText(QCoreApplication.translate("MainWindow", u"Vẽ khung", None))
            self.test_sp1.setText(QCoreApplication.translate("MainWindow", u"SP1", None))
            self.test_sp2.setText(QCoreApplication.translate("MainWindow", u"SP2", None))
            self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i IO/ DO", None))
            self.cambien.setText("")
            self.label_2.setText(QCoreApplication.translate("MainWindow", u"c\u1ea3m bi\u1ebfn", None))
            self.xylanh.setText("")
            self.label_4.setText(QCoreApplication.translate("MainWindow", u"Xylanh", None))
            self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3 ki\u1ec3m tra", None))
            self.led_sp_dat.setText("")
            self.led_sp_kodat.setText("")
            self.label_6.setText(QCoreApplication.translate("MainWindow", u"SP \u0110\u1ea0T", None))
            self.label_7.setText(QCoreApplication.translate("MainWindow", u"SP KH\u00d4NG \u0110\u1ea0T", None))
            self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Hi\u1ec3n th\u1ecb \u1ea3nh", None))
            self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"B\u1ea3ng \u0111i\u1ec1u khi\u1ec3n", None))
            self.chupanh.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee5p \u1ea3nh", None))
            self.onxylanh.setText(QCoreApplication.translate("MainWindow", u"On Xylanh", None))
            self.button_exit.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
            self.label_8.setText(QCoreApplication.translate("MainWindow", u"Auto:", None))
            self.label_9.setText(QCoreApplication.translate("MainWindow", u"Manual:", None))
            self.chay.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
            self.dung.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
            self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Hi\u1ec3n th\u1ecb th\u00f4ng b\u00e1o", None))
            self.led_connect_cam.setText("")
            self.label_10.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
            self.led_connect_com.setText("")
            self.label_11.setText(QCoreApplication.translate("MainWindow", u"Com port", None))
            self.label_12.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i k\u1ebft n\u1ed1i:", None))
            self.clearbox.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
            self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u0110\u00e8n b\u00e1o", None))
            self.label_13.setText(QCoreApplication.translate("MainWindow", u"Led Start", None))
            self.label_14.setText(QCoreApplication.translate("MainWindow", u"Led Stop", None))
            self.label_15.setText(QCoreApplication.translate("MainWindow", u"L\u1ed7i", None))
            self.led_start.setText("")
            self.led_stop.setText("")
            self.led_loi.setText("")
            self.groupBox_7.setTitle("")
            self.label_17.setText(QCoreApplication.translate("MainWindow", u"Ki\u1ec3m S\u1ed1 L\u01b0\u1ee3ng S\u00e1p ", None))
            self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"L\u1ef1a Ch\u1ecdn", None))
            self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn c\u1ed5ng Com Port:", None))
            self.label_16.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn s\u1ea3n ph\u1ea9m ki\u1ec3m tra:", None))
            self.chon_sp.setItemText(0, QCoreApplication.translate("MainWindow", u"Sp1", None))
            self.chon_sp.setItemText(1, QCoreApplication.translate("MainWindow", u"Sp2", None))

            self.menucamera.setTitle(QCoreApplication.translate("MainWindow", u"Connect Camera", None))
            self.menuCalib_Camera.setTitle(QCoreApplication.translate("MainWindow", u"Calib Camera", None))
            self.menuConnect_Com.setTitle(QCoreApplication.translate("MainWindow", u"Connect Com", None))
            self.menuC_i_t_th_ng_s.setTitle(QCoreApplication.translate("MainWindow", u"C\u00e0i \u0111\u1eb7t th\u00f4ng s\u1ed1", None))
            self.menuSP1.setTitle(QCoreApplication.translate("MainWindow", u"SP1", None))
            self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
            self.menuKi_m_tra_ch_ng_tr_nh.setTitle(QCoreApplication.translate("MainWindow", u"Ki\u1ec3m tra ch\u01b0\u01a1ng tr\u00ecnh", None))
            self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        # retranslateUi
        def save_image_as(self):
            scene = self.hienthianh.scene()
            if scene:
                    items = scene.items()
                    if items:
                            pixmap = items[0].pixmap()
                            
                            # Hiển thị hộp thoại "Save As"
                            file_dialog = QFileDialog()
                            file_dialog.setDefaultSuffix("png")
                            file_dialog.setNameFilter("Image files (*.png *.jpg *.jpeg)")
                            file_dialog.setWindowTitle("Save Image")
                            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
                            if file_dialog.exec_():
                                    selected_file = file_dialog.selectedFiles()[0]
                                    try:
                                            pixmap.save(selected_file)
                                            QMessageBox.information(self, "Save Image", f"Image saved to {selected_file}")
                                    except Exception as e:
                                            QMessageBox.critical(self, "Error", f"Failed to save image: {str(e)}")
            else:
                    QMessageBox.warning(self.hienthianh, "No Image", "Please open an image first before saving.")
        def save_image(self):
            print('1')
            scene = self.hienthianh.scene()
            if scene:
                    items = scene.items()
                    if items:
                            pixmap = items[0].pixmap()
                            
                            # Hiển thị hộp thoại "Save"
                            file_dialog = QFileDialog()
                            file_dialog.setDefaultSuffix("png")
                            file_dialog.setNameFilter("Image files (*.png *.jpg *.jpeg)")
                            file_dialog.setWindowTitle("Save Image")
                            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
                            if file_dialog.exec_():
                                    selected_file = file_dialog.selectedFiles()[0]
                                    try:
                                            pixmap.save(selected_file)
                                            QMessageBox.information(self, "Save Image", f"Image saved to {selected_file}")
                                    except Exception as e:
                                            QMessageBox.critical(self, "Error", f"Failed to save image: {str(e)}")
            else:
                    QMessageBox.warning(self.hienthianh, "No Image", "Please open an image first before saving.")
        def open_image(self):
            # Hiển thị hộp thoại mở file
            file_dialog = QFileDialog()
            file_dialog.setDefaultSuffix("png")
            file_dialog.setNameFilter("Image files (*.png *.jpg *.jpeg)")
            file_dialog.setWindowTitle("Open Image")
            file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
            if file_dialog.exec_():
                    selected_file = file_dialog.selectedFiles()[0]
                    
                    try:
                            # Tạo pixmap từ ảnh được chọn
                            pixmap = QPixmap(selected_file)
                            
                            # Tạo một scene mới và thêm pixmap vào đó
                            scene = QGraphicsScene()
                            scene_item = QGraphicsPixmapItem(pixmap)
                            scene.addItem(scene_item)
                            
                            # Thiết lập kích thước của scene để vừa với khung hienthianh
                            scene.setSceneRect(0, 0, self.hienthianh.width(), self.hienthianh.height())
                            
                            # Hiển thị scene lên self.hienthianh
                            self.hienthianh.setScene(scene)
                            self.hienthianh.setAlignment(Qt.AlignCenter)
                            self.hienthianh.setTransformationAnchor(QGraphicsView.AnchorViewCenter)
                            self.hienthianh.setResizeAnchor(QGraphicsView.AnchorViewCenter)
                            self.hienthianh.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                            self.hienthianh.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                            self.hienthianh.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
                            self.hienthianh.setRenderHint(QPainter.Antialiasing)
                            self.hienthianh.setRenderHint(QPainter.SmoothPixmapTransform)
                            self.hienthianh.setInteractive(False)
                            self.hienthianh.setDragMode(QGraphicsView.NoDrag)
                            
                            # Điều chỉnh kích thước của ảnh để hiển thị full khung hienthianh
                            scene_item.setScale(min(self.hienthianh.width() / pixmap.width(), self.hienthianh.height() / pixmap.height()))
                            
                            QMessageBox.information(self, "Open Image", f"Image opened from {selected_file}")
                    except Exception as e:
                            QMessageBox.critical(self, "Error", f"Failed to open image: {str(e)}")
            
        def open_new_gui(self):
            # Tạo một widget mới
            self.new_widget = QWidget()  # Lưu widget vào biến instance
            self.new_widget.setWindowTitle("Cài bán kính ")  # Đổi tiêu đề

            # Thiết lập kích thước cho widget mới
            self.new_widget.resize(300, 200)  # Kích thước lớn hơn

            # Tạo layout
            layout = QVBoxLayout()

            # Tạo thanh cuộn cho bán kính lớn
            self.scroll_bar_large = QScrollBar()
            self.scroll_bar_large.setOrientation(Qt.Horizontal)
            self.scroll_bar_large.setRange(0, 100)
            self.scroll_bar_large.setValue(self.radius_large)  # Đặt giá trị khởi đầu
            self.scroll_bar_large.setStyleSheet("""
                    QScrollBar:horizontal {
                    height: 20px;           /* Chiều cao của thanh cuộn */
                    }
                    QScrollBar::handle:horizontal {
                    min-width: 20px;        /* Chiều rộng tối thiểu của thanh cuộn */
                    }
            """)

            # Tạo nhãn hiển thị giá trị của thanh cuộn bán kính lớn
            self.label_large = QLabel("Bán kính lớn: 0")
            self.scroll_bar_large.valueChanged.connect(lambda value: self.update_label_lon(value, self.label_large))

            # Tạo thanh cuộn cho bán kính nhỏ
            self.scroll_bar_small = QScrollBar()
            self.scroll_bar_small.setOrientation(Qt.Horizontal)
            self.scroll_bar_small.setRange(0, 100)
            self.scroll_bar_small.setValue(self.radius_small)  # Đặt giá trị khởi đầu
            self.scroll_bar_small.setStyleSheet("""
                    QScrollBar:horizontal {
                    height: 20px;           /* Chiều cao của thanh cuộn */
                    }
                    QScrollBar::handle:horizontal {
                    min-width: 20px;        /* Chiều rộng tối thiểu của thanh cuộn */
                    }
            """)

            # Tạo nhãn hiển thị giá trị của thanh cuộn bán kính nhỏ
            self.label_small = QLabel("Bán kính nhỏ: 0")
            self.scroll_bar_small.valueChanged.connect(lambda value: self.update_label_nho(value, self.label_small))

            # Thêm các widget vào layout
            layout.addWidget(self.scroll_bar_large)
            layout.addWidget(self.label_large)
            layout.addWidget(self.scroll_bar_small)
            layout.addWidget(self.label_small)
            # Tạo nút nhấn
            self.button = QPushButton("Test mẫu SP1")
            self.button.clicked.connect(self.process_image)  # Kết nối nút nhấn với hàm xử lý

            # Thêm nút nhấn vào layout
            layout.addWidget(self.button, alignment=Qt.AlignRight)  # Đặt nút ở góc phải

            self.new_widget.setLayout(layout)
            self.new_widget.show()  # Hiển thị widget mới

        def update_label_lon(self, value, label):
            self.radius_large = value  # Cập nhật giá trị bán kính lớn
            label.setText(f"Bán kính lớn: {value}")

        def update_label_nho(self, value, label):
            self.radius_small = value  # Cập nhật giá trị bán kính nhỏ
            label.setText(f"Bán kính nhỏ: {value}")

        def process_image(self):
            scene = self.hienthianh.scene()
            if scene:
                    # Load the image
                    # image = cv2.imread(r'D:\sapmau\image_test\10.png')
                    item = scene.items()[0]  # Giả sử chỉ có một item
                    pixmap = item.pixmap()
                    image = pixmap.toImage()

                    # Chuyển đổi QImage sang định dạng OpenCV
                    image = image.convertToFormat(QImage.Format.Format_RGB888)
                    width = image.width()
                    height = image.height()

                    # Chuyển đổi QImage thành mảng NumPy
                    ptr = image.bits()
                    frame = np.array(ptr).reshape(height, width, 2)  # Chuyển đổi sang mảng NumPy

                    # Kiểm tra xem dữ liệu có hợp lệ không
                    if frame is None or frame.size == 0:
                            print("Không thể lấy ảnh từ QGraphicsView.")
                            return
                    # Convert the image to grayscale
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    # Resize image
                    new_width = 800
                    new_height = int(gray.shape[0] * new_width / gray.shape[1])
                    gray = cv2.resize(gray, (new_width, new_height))

                    # Apply Gaussian Blur
                    blur = cv2.GaussianBlur(gray, (3, 3), 0)

                    # Find circles using the radii from the scroll bars
                    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 10,
                                            param1=10, param2=20,
                                            minRadius=self.radius_small,
                                            maxRadius=self.radius_large)

                    # Display number of circles found
                    if circles is not None:
                            num_circles = len(circles[0])
                            cv2.putText(gray, f"Circles: {num_circles}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
                            

                    # Draw the detected circles
                    circles = np.uint16(np.around(circles))
                    for i in circles[0, :]:
                            cv2.circle(gray, (i[0], i[1]), i[2], (0, 255, 0), 2)  # Draw circle outline
                            cv2.circle(gray, (i[0], i[1]), 2, (0, 0, 255), 3)  # Draw center

                    cv2.imshow("image test", gray)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
            else:
                    QMessageBox.warning(self.hienthianh, "No Image", "Please open an image.")

        def crop_img(self):
            # Tạo một widget mới
            self.new_widget = QWidget()  # Lưu widget vào biến instance
            self.new_widget.setWindowTitle("Crop Image")  # Đổi tiêu đề

            # Thiết lập kích thước cho widget mới
            self.new_widget.resize(400, 200)  # Kích thước lớn hơn

            # Tạo layout
            layout = QVBoxLayout()

            # Tạo thanh cuộn cho diện tích nhỏ nhất
            self.scroll_bar_large = QScrollBar()
            self.scroll_bar_large.setOrientation(Qt.Horizontal)
            self.scroll_bar_large.setRange(0, 10000)  # Phạm vi từ 0 đến 10,000
            self.scroll_bar_large.setSingleStep(50) 
            self.scroll_bar_large.setValue(self.area_min)  # Đặt giá trị khởi đầu
            self.scroll_bar_large.setStyleSheet("""
                    QScrollBar:horizontal {
                    height: 20px;           /* Chiều cao của thanh cuộn */
                    }
                    QScrollBar::handle:horizontal {
                    min-width: 20px;        /* Chiều rộng tối thiểu của thanh cuộn */
                    }
            """)

            # Tạo nhãn hiển thị giá trị của thanh cuộn diện tích nhỏ nhất
            self.label_large = QLabel(f"Diện tích nhỏ nhất: {self.area_min}")
            self.scroll_bar_large.valueChanged.connect(lambda value: self.update_label_dientich_min(value, self.label_large))

            # Tạo layout ngang cho diện tích nhỏ nhất
            h_layout_large = QHBoxLayout()
            h_layout_large.addWidget(self.scroll_bar_large)
            h_layout_large.addWidget(self.label_large)

            # Thêm layout ngang vào layout chính
            layout.addLayout(h_layout_large)

            # Tạo thanh cuộn cho diện tích lớn nhất
            self.scroll_bar_small = QScrollBar()
            self.scroll_bar_small.setOrientation(Qt.Horizontal)
            self.scroll_bar_small.setRange(0, 10000)  # Phạm vi từ 0 đến 10,000
            self.scroll_bar_small.setSingleStep(50)  # Độ nhảy là 100
            self.scroll_bar_small.setValue(self.area_max)  # Đặt giá trị khởi đầu
            self.scroll_bar_small.setStyleSheet("""
                    QScrollBar:horizontal {
                    height: 20px;           /* Chiều cao của thanh cuộn */
                    }
                    QScrollBar::handle:horizontal {
                    min-width: 20px;        /* Chiều rộng tối thiểu của thanh cuộn */
                    }
            """)

            # Tạo nhãn hiển thị giá trị của thanh cuộn diện tích lớn nhất
            self.label_small = QLabel(f"Diện tích lớn nhất: {self.area_max}")
            self.scroll_bar_small.valueChanged.connect(lambda value: self.update_label_dientich_max(value, self.label_small))

            # Tạo layout ngang cho offset
            h_layout_small = QHBoxLayout()
            h_layout_small.addWidget(self.scroll_bar_small)
            h_layout_small.addWidget(self.label_small)

            # Thêm layout ngang vào layout chính
            layout.addLayout(h_layout_small)

            ####
            # Tạo thanh cuộn cho offset
            self.scroll_bar_offset = QScrollBar()
            self.scroll_bar_offset.setOrientation(Qt.Horizontal)
            self.scroll_bar_offset.setRange(0, 600)  # Phạm vi từ 0 đến 10,000
            self.scroll_bar_offset.setSingleStep(3) 
            self.scroll_bar_offset.setValue(self.offset)  # Đặt giá trị khởi đầu
            self.scroll_bar_offset.setStyleSheet("""
                    QScrollBar:horizontal {
                    height: 20px;           /* Chiều cao của thanh cuộn */
                    }
                    QScrollBar::handle:horizontal {
                    min-width: 20px;        /* Chiều rộng tối thiểu của thanh cuộn */
                    }
            """)

            # Tạo nhãn hiển thị giá trị của thanh cuộn diện tích lớn nhất
            self.label_offset = QLabel(f"Giá trị offset: {self.offset}")
            self.scroll_bar_offset.valueChanged.connect(lambda value: self.update_label_offset(value, self.label_offset))

            # Tạo layout ngang cho offset
            h_layout_offset = QHBoxLayout()
            h_layout_offset.addWidget(self.scroll_bar_offset)
            h_layout_offset.addWidget(self.label_offset)

            # Thêm layout ngang vào layout chính
            layout.addLayout(h_layout_offset)
            ####
            # Tạo thanh cuộn cho offset
            self.scroll_bar_width = QScrollBar()
            self.scroll_bar_width.setOrientation(Qt.Horizontal)
            self.scroll_bar_width.setRange(0, 1000)  # Phạm vi từ 0 đến 10,000
            self.scroll_bar_width.setSingleStep(2) 
            self.scroll_bar_width.setValue(self.width)  # Đặt giá trị khởi đầu
            self.scroll_bar_width.setStyleSheet("""
                    QScrollBar:horizontal {
                    height: 20px;           /* Chiều cao của thanh cuộn */
                    }
                    QScrollBar::handle:horizontal {
                    min-width: 20px;        /* Chiều rộng tối thiểu của thanh cuộn */
                    }
            """)

            # Tạo nhãn hiển thị giá trị của thanh cuộn diện tích lớn nhất
            self.label_width = QLabel(f"Chiều dài khung: {self.width}")
            self.scroll_bar_width.valueChanged.connect(lambda value: self.update_label_width(value, self.label_width))

            # Tạo layout ngang cho offset
            h_layout_width = QHBoxLayout()
            h_layout_width.addWidget(self.scroll_bar_width)
            h_layout_width.addWidget(self.label_width)

            # Thêm layout ngang vào layout chính
            layout.addLayout(h_layout_width)

            ####
            # Tạo thanh cuộn cho offset
            self.scroll_bar_height = QScrollBar()
            self.scroll_bar_height.setOrientation(Qt.Horizontal)
            self.scroll_bar_height.setRange(0, 500)  # Phạm vi từ 0 đến 10,000
            self.scroll_bar_height.setSingleStep(2) 
            self.scroll_bar_height.setValue(self.height)  # Đặt giá trị khởi đầu
            self.scroll_bar_height.setStyleSheet("""
                    QScrollBar:horizontal {
                    height: 20px;           /* Chiều cao của thanh cuộn */
                    }
                    QScrollBar::handle:horizontal {
                    min-width: 20px;        /* Chiều rộng tối thiểu của thanh cuộn */
                    }
            """)

            # Tạo nhãn hiển thị giá trị của thanh cuộn diện tích lớn nhất
            self.label_height = QLabel(f"Chiều rộng khung: {self.height}")
            self.scroll_bar_height.valueChanged.connect(lambda value: self.update_label_height(value, self.label_height))

            # Tạo layout ngang cho offset
            h_layout_height = QHBoxLayout()
            h_layout_height.addWidget(self.scroll_bar_height)
            h_layout_height.addWidget(self.label_height)

            # Thêm layout ngang vào layout chính
            layout.addLayout(h_layout_height)
            ####

            # Tạo layout ngang cho các nút nhấn
            h_layout_buttons = QHBoxLayout()

            # Tạo nút nhấn crop img
            self.button = QPushButton("Crop img")
            self.button.setFixedSize(80, 30)
            self.button.clicked.connect(self.button_cropimg)  # Kết nối nút nhấn với hàm xử lý
            h_layout_buttons.addWidget(self.button)  # Thêm nút vào layout ngang

            # Tạo nút nhấn lưu ảnh và thông số
            self.button_save = QPushButton("Save img")
            self.button_save.setFixedSize(80, 30)
            self.button_save.clicked.connect(self.button_save_infor)  # Kết nối nút nhấn với hàm xử lý
            h_layout_buttons.addWidget(self.button_save)  # Thêm nút vào layout ngang

            # Thêm layout ngang vào layout chính
            layout.addLayout(h_layout_buttons)  # Đặt ở góc phải

            self.new_widget.setLayout(layout)
            self.new_widget.show()  # Hiển thị widget mới

        def update_label_dientich_min(self, value, label):
            self.area_min = value  # Cập nhật giá trị diện tích nhỏ nhất
            label.setText(f"Diện tích nhỏ nhất: {value}")
        def update_label_dientich_max(self, value, label):
            self.area_max = value  # Cập nhật giá trị diện tích lớn nhất
            label.setText(f"Diện tích lớn nhất: {value}")
        def update_label_offset(self, value, label):
            self.offset = value  # Cập nhật giá trị diện tích lớn nhất
            label.setText(f"Giá trị offset: {value}")
        def update_label_width(self, value, label):
            self.width = value  # Cập nhật giá trị diện tích lớn nhất
            label.setText(f"Chiều dài khung: {value}")
        def update_label_height(self, value, label):
            self.height = value  # Cập nhật giá trị diện tích lớn nhất
            label.setText(f"Chiều rộng khung: {value}")
        
        def getOrientation(self,pts, img): 
            sz = len(pts)
            data_pts = np.empty((sz, 2), dtype=np.float64)
            for i in range(data_pts.shape[0]):
                    data_pts[i,0] = pts[i,0,0]
                    data_pts[i,1] = pts[i,0,1]      
            # Perform PCA analysis
            mean = np.empty((0))
            mean, eigenvectors, eigenvalues = cv2.PCACompute2(data_pts, mean)      
            # Store the center of the object
            cntr = (int(mean[0,0]), int(mean[0,1]))     
            cv2.circle(img, cntr, 3, (255, 0, 255), 2)
            p1 = (cntr[0] + 0.02 * eigenvectors[0,0] * eigenvalues[0,0], cntr[1] + 0.02 * eigenvectors[0,1] * eigenvalues[0,0])
            p2 = (cntr[0] - 0.02 * eigenvectors[1,0] * eigenvalues[1,0], cntr[1] - 0.02 * eigenvectors[1,1] * eigenvalues[1,0])    
            angle = atan2(eigenvectors[0,1], eigenvectors[0,0]) # orientation in radians
            angle = angle*180/pi
            
            return angle,cntr

        def button_cropimg(self):
            scene = self.hienthianh.scene()
            if scene:
                    # Load the image
                    # image = cv2.imread(r'D:\sapmau\image_test\10.png')
                    item = scene.items()[0]  # Giả sử chỉ có một item
                    pixmap = item.pixmap()
                    image = pixmap.toImage()

                    # Chuyển đổi QImage sang định dạng OpenCV
                    image = image.convertToFormat(QImage.Format.Format_RGB888)
                    width = image.width()
                    height = image.height()

                    # Chuyển đổi QImage thành mảng NumPy
                    ptr = image.bits()
                    frame = np.array(ptr).reshape(height, width, 3)  # Chuyển đổi sang mảng NumPy

                    # Kiểm tra xem dữ liệu có hợp lệ không
                    if frame is None or frame.size == 0:
                            print("Không thể lấy ảnh từ QGraphicsView.")
                            return
                    # Convert the image to grayscale
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    height, width= gray.shape
                    # Định nghĩa kích thước mới mong muốn
                    new_width = 800
                    new_height = int(height * new_width / width)
                    # Resize ảnh giữ tỉ lệ
                    gray = cv2.resize(gray, (new_width, new_height))
                    image_rotation=gray

                    # Apply Gaussian blur to reduce noise
                    blur = cv2.GaussianBlur(gray, (9,9), 0)

                    # Apply Canny edge detection
                    edges = cv2.Canny(blur, 100, 200)
                    # cv2.imshow('canny',edges)
                    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

                    for i, c in enumerate(contours):
                            # Calculate the area of each contour
                            area = cv2.contourArea(c)
                            # Ignore contours that are too small or too large
                            if area <self.area_min or self.area_max < area:
                                    continue   
                            angle,centr = self.getOrientation(c,gray)
                            print('angle', angle, 'position', centr)

                    # Tính toán ma trận xoay
                    rows, cols= gray.shape
                    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)

                    # Xoay ảnh
                    rotated_image = cv2.warpAffine(image_rotation, M, (cols, rows))

                    edges1 = cv2.Canny(rotated_image, 100, 200)
                    # cv2.imshow('img_canny1', edges1)
                    contours1, _ = cv2.findContours(edges1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
                    # print(contours1)
                    for i, c in enumerate(contours1):
                            # Calculate the area of each contour
                            area = cv2.contourArea(c)
                            # Ignore contours that are too small or too large
                            if area <self.area_min or self.area_max < area:
                                    continue   
                            # Draw each contour only for visualisation purposes
                            cv2.drawContours(rotated_image, contours1, i, (0, 0, 255), 1)
                            # Find the orientation of each shape
                            angle1,centr1 = self.getOrientation(c,rotated_image)
                            print('angle_rotation', angle1, 'position_rotation', centr1)

                    # Tính toán chiều rộng và chiều cao của hình chữ nhật
                    print(edges.shape)
                    # self.width = 520
                    # self.height = 70  # Chọn chiều cao tùy ý
                    # self.offset=230
                    if centr1[1] >= 300: # chiều dài khung*3/4/2
                            y1_rect = int(centr1[1] - self.offset - self.height / 2)
                            y2_rect = int(centr1[1] - self.offset + self.height / 2)
                    else:
                            y1_rect = int(centr1[1] + self.offset - self.height / 2)
                            y2_rect = int(centr1[1] + self.offset + self.height / 2)

                    x1_rect = int(centr1[0] - self.width / 2)
                    x2_rect = int(centr1[0] + self.width / 2)

                    # Cắt ảnh trong vùng hình chữ nhật
                    self.cropped_image = rotated_image[y1_rect:y2_rect, x1_rect:x2_rect]
                    cv2.imshow("Crop image", self.cropped_image)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
            else:
                    QMessageBox.warning(self.hienthianh, "No Image", "Chưa mở ảnh.")
            
        
        def button_save_infor(self):
            # Kiểm tra xem ảnh đã được cắt chưa
            if self.cropped_image is not None:
                    # Hiển thị hộp thoại "Save"
                    file_dialog = QFileDialog()
                    file_dialog.setDefaultSuffix("png")
                    file_dialog.setNameFilter("Image files (*.png *.jpg *.jpeg)")
                    file_dialog.setWindowTitle("Save Cropped Image")
                    file_dialog.setAcceptMode(QFileDialog.AcceptSave)

                    if file_dialog.exec_():
                            selected_file = file_dialog.selectedFiles()[0]
                            try:
                                    # Lưu ảnh đã cắt
                                    cv2.imwrite(selected_file, self.cropped_image)
                                    QMessageBox.information(self, "Save Image", f"Cropped image saved to {selected_file}")
                            except Exception as e:
                                    QMessageBox.critical(self, "Error", f"Failed to save image: {str(e)}")
            else:
                    QMessageBox.warning(self.hienthianh, "No Image", "Chưa có ảnh cắt mẫu.")

        def meg_infor_vekhung(self):
            # Tạo một widget mới
            self.new_widget = QWidget()  # Lưu widget vào biến instance
            self.new_widget.setWindowTitle("Thông số tạo khung khe")  # Đổi tiêu đề

            # Thiết lập kích thước cho widget mới
            self.new_widget.resize(400, 200)  # Kích thước lớn hơn

            # Tạo layout
            layout = QVBoxLayout()

            # Tạo thanh cuộn cho vị trí x1_1
            self.scroll_bar_large = QScrollBar()
            self.scroll_bar_large.setOrientation(Qt.Horizontal)
            self.scroll_bar_large.setRange(0, 500)  # Phạm vi từ 0 đến 10,000
            self.scroll_bar_large.setSingleStep(2) 
            self.scroll_bar_large.setValue(self.x1_1)  # Đặt giá trị khởi đầu
            self.scroll_bar_large.setStyleSheet("""
                    QScrollBar:horizontal {
                    height: 20px;           /* Chiều cao của thanh cuộn */
                    }
                    QScrollBar::handle:horizontal {
                    min-width: 20px;        /* Chiều rộng tối thiểu của thanh cuộn */
                    }
            """)

            # Tạo nhãn hiển thị giá trị của thanh cuộn diện tích nhỏ nhất
            self.label_large = QLabel(f"X1_1: {self.x1_1}")
            self.scroll_bar_large.valueChanged.connect(lambda value: self.update_label_x1_1(value, self.label_large))

            # Tạo layout ngang cho diện tích nhỏ nhất
            h_layout_large = QHBoxLayout()
            h_layout_large.addWidget(self.scroll_bar_large)
            h_layout_large.addWidget(self.label_large)

            # Thêm layout ngang vào layout chính
            layout.addLayout(h_layout_large)

            # Tạo thanh cuộn cho y1_1
            self.scroll_bar_small = QScrollBar()
            self.scroll_bar_small.setOrientation(Qt.Horizontal)
            self.scroll_bar_small.setRange(0, 500)  # Phạm vi từ 0 đến 10,000
            self.scroll_bar_small.setSingleStep(2)  # Độ nhảy là 100
            self.scroll_bar_small.setValue(self.y1_1)  # Đặt giá trị khởi đầu
            self.scroll_bar_small.setStyleSheet("""
                    QScrollBar:horizontal {
                    height: 20px;           /* Chiều cao của thanh cuộn */
                    }
                    QScrollBar::handle:horizontal {
                    min-width: 20px;        /* Chiều rộng tối thiểu của thanh cuộn */
                    }
            """)

            # Tạo nhãn hiển thị giá trị của thanh cuộn diện tích lớn nhất
            self.label_small = QLabel(f"Y1_1: {self.y1_1}")
            self.scroll_bar_small.valueChanged.connect(lambda value: self.update_label_y1_1(value, self.label_small))

            # Tạo layout ngang cho offset
            h_layout_small = QHBoxLayout()
            h_layout_small.addWidget(self.scroll_bar_small)
            h_layout_small.addWidget(self.label_small)

            # Thêm layout ngang vào layout chính
            layout.addLayout(h_layout_small)

            ####
            # Tạo thanh cuộn cho x2_1
            self.scroll_bar_offset = QScrollBar()
            self.scroll_bar_offset.setOrientation(Qt.Horizontal)
            self.scroll_bar_offset.setRange(0, 500)  # Phạm vi từ 0 đến 10,000
            self.scroll_bar_offset.setSingleStep(2) 
            self.scroll_bar_offset.setValue(self.x2_1)  # Đặt giá trị khởi đầu
            self.scroll_bar_offset.setStyleSheet("""
                    QScrollBar:horizontal {
                    height: 20px;           /* Chiều cao của thanh cuộn */
                    }
                    QScrollBar::handle:horizontal {
                    min-width: 20px;        /* Chiều rộng tối thiểu của thanh cuộn */
                    }
            """)

            # Tạo nhãn hiển thị giá trị của thanh cuộn diện tích lớn nhất
            self.label_offset = QLabel(f"X2_1: {self.x2_1}")
            self.scroll_bar_offset.valueChanged.connect(lambda value: self.update_label_x2_1(value, self.label_offset))

            # Tạo layout ngang cho x2_1
            h_layout_offset = QHBoxLayout()
            h_layout_offset.addWidget(self.scroll_bar_offset)
            h_layout_offset.addWidget(self.label_offset)

            # Thêm layout ngang vào layout chính
            layout.addLayout(h_layout_offset)
            ####
            # Tạo thanh cuộn cho y2_1
            self.scroll_bar_width = QScrollBar()
            self.scroll_bar_width.setOrientation(Qt.Horizontal)
            self.scroll_bar_width.setRange(0, 500)  # Phạm vi từ 0 đến 10,000
            self.scroll_bar_width.setSingleStep(2) 
            self.scroll_bar_width.setValue(self.y2_1)  # Đặt giá trị khởi đầu
            self.scroll_bar_width.setStyleSheet("""
                    QScrollBar:horizontal {
                    height: 20px;           /* Chiều cao của thanh cuộn */
                    }
                    QScrollBar::handle:horizontal {
                    min-width: 20px;        /* Chiều rộng tối thiểu của thanh cuộn */
                    }
            """)

            # Tạo nhãn hiển thị giá trị của thanh cuộn diện tích lớn nhất
            self.label_width = QLabel(f"Y2_1: {self.y2_1}")
            self.scroll_bar_width.valueChanged.connect(lambda value: self.update_label_y2_1(value, self.label_width))

            # Tạo layout ngang cho offset
            h_layout_width = QHBoxLayout()
            h_layout_width.addWidget(self.scroll_bar_width)
            h_layout_width.addWidget(self.label_width)

            # Thêm layout ngang vào layout chính
            layout.addLayout(h_layout_width)

            ####
            # Tạo thanh cuộn cho blocksize
            self.scroll_bar_height = QScrollBar()
            self.scroll_bar_height.setOrientation(Qt.Horizontal)
            self.scroll_bar_height.setRange(1, 200)  # Phạm vi từ 0 đến 10,000
            self.scroll_bar_height.setSingleStep(2) 
            self.scroll_bar_height.setValue(self.blocksize)  # Đặt giá trị khởi đầu
            self.scroll_bar_height.setStyleSheet("""
                    QScrollBar:horizontal {
                    height: 20px;           /* Chiều cao của thanh cuộn */
                    }
                    QScrollBar::handle:horizontal {
                    min-width: 20px;        /* Chiều rộng tối thiểu của thanh cuộn */
                    }
            """)

            # Tạo nhãn hiển thị giá trị của thanh cuộn diện tích lớn nhất
            self.label_height = QLabel(f"Blocksize: {self.blocksize}")
            self.scroll_bar_height.valueChanged.connect(lambda value: self.update_label_blocksize(value, self.label_height))

            # Tạo layout ngang cho blocksize
            h_layout_height = QHBoxLayout()
            h_layout_height.addWidget(self.scroll_bar_height)
            h_layout_height.addWidget(self.label_height)

            # Thêm layout ngang vào layout chính
            layout.addLayout(h_layout_height)
            ####
            # Tạo thanh cuộn cho constant
            self.scroll_bar_constant = QScrollBar()
            self.scroll_bar_constant.setOrientation(Qt.Horizontal)
            self.scroll_bar_constant.setRange(0, 250)  # Phạm vi từ 0 đến 10,000
            self.scroll_bar_constant.setSingleStep(1) 
            self.scroll_bar_constant.setValue(self.constant)  # Đặt giá trị khởi đầu
            self.scroll_bar_constant.setStyleSheet("""
                    QScrollBar:horizontal {
                    height: 20px;           /* Chiều cao của thanh cuộn */
                    }
                    QScrollBar::handle:horizontal {
                    min-width: 20px;        /* Chiều rộng tối thiểu của thanh cuộn */
                    }
            """)

            # Tạo nhãn hiển thị giá trị của thanh cuộn diện tích lớn nhất
            self.label_constant = QLabel(f"Constant: {self.constant}")
            self.scroll_bar_constant.valueChanged.connect(lambda value: self.update_label_constant(value, self.label_constant))

            # Tạo layout ngang cho blocksize
            h_layout_constant = QHBoxLayout()
            h_layout_constant.addWidget(self.scroll_bar_constant)
            h_layout_constant.addWidget(self.label_constant)

            # Thêm layout ngang vào layout chính
            layout.addLayout(h_layout_constant)
            ####
            # Tạo thanh cuộn cho khoản cách
            self.scroll_bar_khoancach = QScrollBar()
            self.scroll_bar_khoancach.setOrientation(Qt.Horizontal)
            self.scroll_bar_khoancach.setRange(0, 300)  # Phạm vi từ 0 đến 10,000
            self.scroll_bar_khoancach.setSingleStep(1) 
            self.scroll_bar_khoancach.setValue(self.khoancach)  # Đặt giá trị khởi đầu
            self.scroll_bar_khoancach.setStyleSheet("""
                    QScrollBar:horizontal {
                    height: 20px;           /* Chiều cao của thanh cuộn */
                    }
                    QScrollBar::handle:horizontal {
                    min-width: 20px;        /* Chiều rộng tối thiểu của thanh cuộn */
                    }
            """)

            # Tạo nhãn hiển thị giá trị của khoan cách
            self.label_khoancach = QLabel(f"Khoảng cách: {self.khoancach}")
            self.scroll_bar_khoancach.valueChanged.connect(lambda value: self.update_label_khoancach(value, self.label_khoancach))

            # Tạo layout ngang cho blocksize
            h_layout_khoancach = QHBoxLayout()
            h_layout_khoancach.addWidget(self.scroll_bar_khoancach)
            h_layout_khoancach.addWidget(self.label_khoancach)

            # Thêm layout ngang vào layout chính
            layout.addLayout(h_layout_khoancach)
            ####
            # Tạo layout ngang cho các nút nhấn
            h_layout_buttons = QHBoxLayout()

            # Tạo nút nhấn crop img
            self.button = QPushButton("Draw khung")
            self.button.setFixedSize(80, 30)
            self.button.clicked.connect(self.ve_khung)  # Kết nối nút nhấn với hàm xử lý
            h_layout_buttons.addWidget(self.button)  # Thêm nút vào layout ngang

            # Thêm layout ngang vào layout chính
            layout.addLayout(h_layout_buttons)  # Đặt ở góc phải

            self.new_widget.setLayout(layout)
            self.new_widget.show()  # Hiển thị widget mới

        def update_label_x1_1(self, value, label):
            self.x1_1 = value  # Cập nhật giá trị diện tích nhỏ nhất
            label.setText(f"X1_1: {value}")
        def update_label_y1_1(self, value, label):
            self.y1_1 = value  # Cập nhật giá trị diện tích lớn nhất
            label.setText(f"Y1_1: {value}")
        def update_label_x2_1(self, value, label):
            self.x2_1 = value  # Cập nhật giá trị diện tích lớn nhất
            label.setText(f"X2_1: {value}")
        def update_label_y2_1(self, value, label):
            self.y2_1 = value  # Cập nhật giá trị diện tích lớn nhất
            label.setText(f"Y2_1: {value}")
        def update_label_blocksize(self, value, label):
            self.blocksize = value  # Cập nhật giá trị diện tích lớn nhất
            label.setText(f"Blocksize: {value}")
        def update_label_constant(self, value, label):
            self.constant = value  # Cập nhật giá trị diện tích lớn nhất
            label.setText(f"Constant: {value}")
        def update_label_khoancach(self, value, label):
            self.khoancach = value  # Cập nhật giá trị diện tích lớn nhất
            label.setText(f"Khoảng cách: {value}")


        def ve_khung(self):
            if self.cropped_image is not None:
                    image_khung=self.cropped_image.copy()
                    blur_cut_img = cv2.GaussianBlur(image_khung, (13,13), 0)
                    thresh = cv2.adaptiveThreshold(blur_cut_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                            cv2.THRESH_BINARY_INV, self.blocksize, self.constant)
                    cv2.imshow("thes",thresh)
                    x1_1 = self.x1_1
                    y1_1 = self.y1_1
                    x2_1 = self.x2_1
                    y2_1 = self.y2_1
                    khoancach= self.khoancach
                    conter=0
                    # Vẽ hình chữ nhật các khe
                    for i in range(0, 7):
                            x1 = int((x1_1+x2_1)/2)-6 + i * khoancach
                            x2 = int((x1_1+x2_1)/2)+8 + i * khoancach
                            img_cut = thresh[y1_1:y2_1, x1:x2]
                            white_pixels = np.sum(img_cut == 255)
                            black_pixels = np.sum(img_cut == 0)
                            ratio = white_pixels / (white_pixels + black_pixels)
                            print(f"Hình chữ nhật {i+1}: Tỷ lệ pixel trắng/đen = {ratio:.2f}")
                            cv2.rectangle(image_khung, (x1, y1_1), (x2, y2_1), (0, 255, 255), 1)
                            # In giá trị tỷ lệ lên hình
                            cv2.putText(image_khung, f"{ratio:.2f}", (x1, y2_1 - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                            # if ratio <=0.15:
                            #         conter=conter+1
                            #         cv2.putText(gray, f"error (DK1)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.imshow('draw khung',image_khung)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
            else:
                    QMessageBox.warning(self.hienthianh, "No Image", "Chưa có ảnh cắt mẫu.")

        def xoakhungthongbao(self):
            self.hienthitrangthai.clear()
            pass

        ####
        # xử các hàm
        def connect_com(self):
            try:
                port = self.chon_com.text()
                if not port:
                    current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                    self.hienthitrangthai.append(f"{current_time} :  Vui lòng nhập cổng serial.")
                    return
                # gửi tên cổng com qua task2
                datacom.put(port)
                connectcom.put('connectcom')

                # self.ser = serial.Serial(
                #     port=port,
                #     baudrate=9600,
                #     parity=serial.PARITY_NONE,
                #     stopbits=serial.STOPBITS_ONE,
                #     bytesize=serial.EIGHTBITS,
                #     timeout=1
                # )
                self.status_connectcom=True
                current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                self.hienthitrangthai.append(f"{current_time} :  Connected Com Serial")
                self.led_connect_com.setStyleSheet(u"QLabel#led_connect_com{\n"
                                                "    background-color: green;\n"
                                                "    border-radius: 12px;\n"
                                                "    min-width: 25px;\n"
                                                "    min-height: 25px;\n"
                                                "    max-width: 25px;\n"
                                                "    max-height:25px;\n"
                                                "}")
                # Thêm các xử lý khác sau khi kết nối thành công
            except serial.SerialException as e:
                current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                self.hienthitrangthai.append(f"{current_time} :  Can not connect Com Serial" + str(e))
        
        def disconnect_com(self):
            # self.ser.close()
            exit_event.set()
            self.status_connectcom=False
            current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            self.hienthitrangthai.append(f"{current_time} :  Disconnected Com Serial")
            self.led_connect_com.setStyleSheet(u"QLabel#led_connect_com{\n"
                                                "    background-color: gray;\n"
                                                "    border-radius: 12px;\n"
                                                "    min-width: 25px;\n"
                                                "    min-height: 25px;\n"
                                                "    max-width: 25px;\n"
                                                "    max-height:25px;\n"
                                                "}")
            
        def connect_cam(self):
            self.status_connectcam=True
            if not self.cap == None:
                current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                self.hienthitrangthai.append(f"{current_time} :  Connected Camera.")
                self.led_connect_cam.setStyleSheet(u"QLabel#led_connect_cam{\n"
                                                    "    background-color: green;\n"
                                                    "    border-radius: 12px;\n"
                                                    "    min-width: 25px;\n"
                                                    "    min-height: 25px;\n"
                                                    "    max-width: 25px;\n"
                                                    "    max-height:25px;\n"
                                                    "}")
            else:
                self.scene = QGraphicsScene()
                # Khởi tạo trình tìm kiếm camera
                tlFactory = pylon.TlFactory.GetInstance()
                # Lấy danh sách tất cả các thiết bị
                devices = tlFactory.EnumerateDevices()
                if len(devices) == 0:
                    print("Không tìm thấy camera")
                    current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                    self.hienthitrangthai.append(f"{current_time} :  Không tìm thấy cam.")
                    # exit(1)
                else:
                    # In ra dòng "Khởi tạo thành công camera" trong self.hienthitrangthai
                    current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                    self.hienthitrangthai.append(f"{current_time} :  Connected Camera.")
                    # Chọn camera đầu tiên
                    first_camera = devices[0]
                    # Khởi tạo camera
                    self.cap = pylon.InstantCamera(tlFactory.CreateDevice(first_camera))
                    # Kích hoạt camera
                    self.cap.Open()
                    # Hiển thị thông tin camera
                    print("Model:", self.cap.GetDeviceInfo().GetModelName())
                    print("Serial number:", self.cap.GetDeviceInfo().GetSerialNumber())
                    # Bắt đầu quá trình chụp nếu chưa bắt đầu
                    if not self.cap.IsGrabbing():
                        self.cap.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

                    grabResult = self.cap.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
                    if grabResult.GrabSucceeded():
                        # Chuyển đổi kết quả sang ảnh OpenCV       
                        img = grabResult.Array
                        # Chuyển đổi khung hình sang định dạng phù hợp với QGraphicsView
                        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        h, w, ch = image.shape
                        bytesPerLine = ch * w
                        qImg = QImage(image.data, w, h, bytesPerLine, QImage.Format_RGB888)

                        # Tạo pixmap và điều chỉnh kích thước để vừa với QGraphicsView
                        pixmap = QPixmap.fromImage(qImg)
                        pixmap = pixmap.scaled(self.hienthianh.width(), self.hienthianh.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)

                        # Hiển thị khung hình lên QGraphicsView
                        self.scene.clear()
                        self.scene.addPixmap(pixmap)
                        self.hienthianh.setScene(self.scene)
                        self.hienthianh.show()

                        # Đổi màu của LED
                        self.led_connect_cam.setStyleSheet(u"QLabel#led_connect_cam{\n"
                                                        "    background-color: green;\n"
                                                        "    border-radius: 12px;\n"
                                                        "    min-width: 25px;\n"
                                                        "    min-height: 25px;\n"
                                                        "    max-width: 25px;\n"
                                                        "    max-height:25px;\n"
                                                        "}")
                
        def disconnect_cam(self):
            self.status_connectcam=False
            stop_runcalib.set()
            self.cap.Close()
            cv2.destroyAllWindows()
            current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            self.hienthitrangthai.append(f"{current_time} :  Disconnected Camera.")
            self.led_connect_cam.setStyleSheet(u"QLabel#led_connect_cam{\n"
                                                "    background-color: gray;\n"
                                                "    border-radius: 12px;\n"
                                                "    min-width: 25px;\n"
                                                "    min-height: 25px;\n"
                                                "    max-width: 25px;\n"
                                                "    max-height:25px;\n"
                                                "}")
            
        def capture_photo(self):
            if  not self.cap == None:
                grabResult = self.cap.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
                if grabResult.GrabSucceeded():
                    img = grabResult.Array
                    # Chụp ảnh và hiển thị lên QGraphicsView
                    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    h, w, ch = image.shape
                    bytesPerLine = ch * w
                    qImg = QImage(image.data, w, h, bytesPerLine, QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(qImg)
                    pixmap = pixmap.scaled(self.hienthianh.width(), self.hienthianh.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
                    self.scene.clear()
                    self.scene.addPixmap(pixmap)
                    self.hienthianh.setScene(self.scene)
                    self.hienthianh.show()
                    current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                    self.hienthitrangthai.append(f"{current_time} :  Captured photo.")
            else:
                current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                self.hienthitrangthai.append(f"{current_time} :  Camera chưa được kết nối.")

        def action_runcalib_triggered(self):
            # self.run_calib()
            self.status_connectcam=True
            self.scene = QGraphicsScene()
            if not self.cap == None:
                # In ra dòng "Khởi tạo thành công camera" trong self.hienthitrangthai
                current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                self.hienthitrangthai.append(f"{current_time} :  Connected Camera. Calib Camera.")
                self.led_connect_cam.setStyleSheet(u"QLabel#led_connect_cam{\n"
                                                "    background-color: green;\n"
                                                "    border-radius: 12px;\n"
                                                "    min-width: 25px;\n"
                                                "    min-height: 25px;\n"
                                                "    max-width: 25px;\n"
                                                "    max-height:25px;\n"
                                                "}")
                if not self.cap.IsGrabbing():
                    self.cap.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
                while True:
                    grabResult = self.cap.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
                    if grabResult.GrabSucceeded():
                        # Chuyển đổi kết quả sang ảnh OpenCV       
                        img = grabResult.Array
                        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        h, w, ch = image.shape
                        bytesPerLine = ch * w
                        qImg = QImage(image.data, w, h, bytesPerLine, QImage.Format_RGB888)
                        pixmap = QPixmap.fromImage(qImg)
                        pixmap = pixmap.scaled(self.hienthianh.width(), self.hienthianh.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
                        self.scene.clear()
                        self.scene.addPixmap(pixmap)
                        self.hienthianh.setScene(self.scene)
                        self.hienthianh.show()
                        cv2.waitKey(10)
                        if stop_runcalib.is_set():
                             stop_runcalib.clear()
                             break
            else:
                 # Khởi tạo trình tìm kiếm camera
                tlFactory = pylon.TlFactory.GetInstance()
                # Lấy danh sách tất cả các thiết bị
                devices = tlFactory.EnumerateDevices()
                if len(devices) == 0:
                    print("Không tìm thấy camera")
                    current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                    self.hienthitrangthai.append(f"{current_time} :  Không tìm thấy cam.")
                    # exit(1)
                # Chọn camera đầu tiên
                first_camera = devices[0]
                # Khởi tạo camera
                self.cap = pylon.InstantCamera(tlFactory.CreateDevice(first_camera))
                # Kích hoạt camera
                self.cap.Open()
                # Bắt đầu quá trình chụp nếu chưa bắt đầu
                if not self.cap.IsGrabbing():
                    self.cap.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

                # In ra dòng "Khởi tạo thành công camera" trong self.hienthitrangthai
                current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                self.hienthitrangthai.append(f"{current_time} :  Connected Camera. Calib Camera.")
                # Đổi màu của LED
                self.led_connect_cam.setStyleSheet(u"QLabel#led_connect_cam{\n"
                                                "    background-color: green;\n"
                                                "    border-radius: 12px;\n"
                                                "    min-width: 25px;\n"
                                                "    min-height: 25px;\n"
                                                "    max-width: 25px;\n"
                                                "    max-height:25px;\n"
                                                "}")
                while True:
                    grabResult = self.cap.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
                    if grabResult.GrabSucceeded():
                        # Chuyển đổi kết quả sang ảnh OpenCV       
                        img = grabResult.Array
                        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        h, w, ch = image.shape
                        bytesPerLine = ch * w
                        qImg = QImage(image.data, w, h, bytesPerLine, QImage.Format_RGB888)
                        pixmap = QPixmap.fromImage(qImg)
                        pixmap = pixmap.scaled(self.hienthianh.width(), self.hienthianh.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
                        self.scene.clear()
                        self.scene.addPixmap(pixmap)
                        self.hienthianh.setScene(self.scene)
                        self.hienthianh.show()
                        cv2.waitKey(10)
                        if stop_runcalib.is_set():
                             stop_runcalib.clear()
                             break

        def stop_calibcamera(self):
            self.status_connectcam=False
            stop_runcalib.set()
            self.cap.Close()
            cv2.destroyAllWindows()
            current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            self.hienthitrangthai.append(f"{current_time} :  Stop Calib Camera. Disconnected Camera.")
            self.led_connect_cam.setStyleSheet(u"QLabel#led_connect_cam{\n"
                                                "    background-color: gray;\n"
                                                "    border-radius: 12px;\n"
                                                "    min-width: 25px;\n"
                                                "    min-height: 25px;\n"
                                                "    max-width: 25px;\n"
                                                "    max-height:25px;\n"
                                                "}")
        
        # Hàm để gửi dữ liệu qua cổng serial
        # def send_data(self,data):
        #     self.ser.write(data.encode())

        # # Hàm để đọc dữ liệu từ cổng serial
        # def read_data(self):
        #     return self.ser.read_all().decode().strip()
        
        def on_xylanh(self):
            if self.status_connectcom == True:
                try:
                    # self.send_data('222')  # Gửi số 2 xuống cổng COM
                    event.set()
                    current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                    self.hienthitrangthai.append(f"{current_time} :  On Xy lanh.")
                except serial.SerialException as e:
                    current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                    self.hienthitrangthai.append(f"{current_time} :  Error sending data to COM: {e}")
            else:
                current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                self.hienthitrangthai.append(f"{current_time} :  Cổng COM chưa được kết nối.")
        
        def run_auto(self):
            data=None
            if self.status_connectcom == True: 
                if self.status_connectcam == True:
                    current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                    self.hienthitrangthai.append(f"{current_time} :  Running Auto.")
                    self.led_start.setStyleSheet(u"QLabel#led_start{\n"
                                                "    background-color: green;\n"
                                                "    border-radius: 25px;\n"
                                                "    min-width: 50px;\n"
                                                "    min-height: 50px;\n"
                                                "    max-width: 50px;\n"
                                                "    max-height:50px;\n"
                                                "}")
                    self.led_stop.setStyleSheet(u"QLabel#led_stop{\n"
                                                "    background-color: gray;\n"
                                                "    border-radius: 25px;\n"
                                                "    min-width: 50px;\n"
                                                "    min-height: 50px;\n"
                                                "    max-width: 50px;\n"
                                                "    max-height:50px;\n"
                                                "}")
                    if not self.cap.IsGrabbing():
                        self.cap.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
                    while True:
                        cv2.waitKey(10)
                        # Kiểm tra xem có nhận được giá trị '1' từ cổng COM không
                        if not capture_img.empty():
                            data = capture_img.get()
                            if data == '1':
                                # Đọc một khung hình từ camera
                                grabResult = self.cap.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
                                if grabResult.GrabSucceeded():
                                    # Chuyển đổi kết quả sang ảnh OpenCV       
                                    img = grabResult.Array
                                    #### xử lý ảnh ở đây
                                    if self.luachonsp == 0:
                                        # Convert the image to grayscale
                                        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                                        # Resize image
                                        gray=img.copy()
                                        new_width = 800
                                        new_height = int(gray.shape[0] * new_width / gray.shape[1])
                                        gray = cv2.resize(gray, (new_width, new_height))

                                        # Apply Gaussian Blur
                                        blur = cv2.GaussianBlur(gray, (3, 3), 0)

                                        # Find circles using the radii from the scroll bars
                                        circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 10,
                                                                param1=10, param2=20,
                                                                minRadius=self.radius_small,
                                                                maxRadius=self.radius_large)

                                        # Display number of circles found
                                        if circles is not None:
                                                num_circles = len(circles[0])
                                                cv2.putText(gray, f"Circles: {num_circles}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
                                                if num_circles==24:
                                                    self.led_sp_kodat.setStyleSheet(u"QLabel#led_sp_kodat{\n"
                                                    "    background-color: gray;\n"
                                                    "    border-radius: 25px;\n"
                                                    "    min-width: 50px;\n"
                                                    "    min-height: 50px;\n"
                                                    "    max-width: 50px;\n"
                                                    "    max-height:50px;\n"
                                                    "}")
                                                    self.led_sp_dat.setStyleSheet(u"QLabel#led_sp_dat{\n"
                                                    "    background-color: green;\n"
                                                    "    border-radius: 25px;\n"
                                                    "    min-width: 50px;\n"
                                                    "    min-height: 50px;\n"
                                                    "    max-width: 50px;\n"
                                                    "    max-height:50px;\n"
                                                    "}")
                                                else:
                                                    self.led_sp_kodat.setStyleSheet(u"QLabel#led_sp_kodat{\n"
                                                    "    background-color: red;\n"
                                                    "    border-radius: 25px;\n"
                                                    "    min-width: 50px;\n"
                                                    "    min-height: 50px;\n"
                                                    "    max-width: 50px;\n"
                                                    "    max-height:50px;\n"
                                                    "}")
                                                    self.led_sp_dat.setStyleSheet(u"QLabel#led_sp_dat{\n"
                                                    "    background-color: gray;\n"
                                                    "    border-radius: 25px;\n"
                                                    "    min-width: 50px;\n"
                                                    "    min-height: 50px;\n"
                                                    "    max-width: 50px;\n"
                                                    "    max-height:50px;\n"
                                                    "}")
                                                     
                                        # Draw the detected circles
                                        circles = np.uint16(np.around(circles))
                                        for i in circles[0, :]:
                                                cv2.circle(gray, (i[0], i[1]), i[2], (0, 255, 0), 2)  # Draw circle outline
                                                cv2.circle(gray, (i[0], i[1]), 2, (0, 0, 255), 3)  # Draw center
                                        image = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
                                        h, w, ch = image.shape
                                        bytesPerLine = ch * w
                                        qImg = QImage(image.data, w, h, bytesPerLine, QImage.Format_RGB888)

                                        # Tạo pixmap và điều chỉnh kích thước để vừa với QGraphicsView
                                        pixmap = QPixmap.fromImage(qImg)
                                        pixmap = pixmap.scaled(self.hienthianh.width(), self.hienthianh.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)

                                        # Hiển thị khung hình lên QGraphicsView
                                        self.scene.clear()
                                        self.scene.addPixmap(pixmap)
                                        self.hienthianh.setScene(self.scene)
                                        self.hienthianh.show()
                                        
                                    else:
                                         pass                                   
                                    ####
                                    
                                cv2.waitKey(40)
                                #####
                                # xử lý ảnh ở đây


                                ####
                                # trả kết quả xử lý:
                                if True: # điều kiện sp lỗi kích xylanh
                                    ketquaxuly.set()

                        if auto_event.is_set():
                            auto_event.clear()
                            ketquaxuly.clear()
                            current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                            self.hienthitrangthai.append(f"{current_time} :  Stop Auto.")
                            break

                else:
                    current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                    self.hienthitrangthai.append(f"{current_time} :  Camera chưa được kết nối.")
            else:
                current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                self.hienthitrangthai.append(f"{current_time} :  Cổng COM chưa được kết nối.")

        def stop_auto(self):
            auto_event.set()
            self.led_stop.setStyleSheet(u"QLabel#led_stop{\n"
                                                "    background-color: red;\n"
                                                "    border-radius: 25px;\n"
                                                "    min-width: 50px;\n"
                                                "    min-height: 50px;\n"
                                                "    max-width: 50px;\n"
                                                "    max-height:50px;\n"
                                                "}")
            self.led_start.setStyleSheet(u"QLabel#led_start{\n"
                                                "    background-color: gray;\n"
                                                "    border-radius: 25px;\n"
                                                "    min-width: 50px;\n"
                                                "    min-height: 50px;\n"
                                                "    max-width: 50px;\n"
                                                "    max-height:50px;\n"
                                                "}")
            pass
        def close_application(self):
            self.stop_event.set()  # Đặt sự kiện để dừng cả task1 và task2
            print('Closing tasks...')
            cv2.waitKey(5)
            QApplication.exit()


        def on_combobox_activated(self, index):
            if index == 0:
                self.luachonsp =0
                current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                self.hienthitrangthai.append(f"{current_time} :  Chọn SP1")
            elif index == 1:
                self.luachonsp =1
                current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
                self.hienthitrangthai.append(f"{current_time} :  Chọn SP2")

      
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)

        def closeEvent(self, event):
            stop_event.set()  # Đặt cờ dừng
            print('ketthuc')
            event.accept()   
    # if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

def task2(event, exit_event,auto_event,ketquaxuly, datacom, connectcom,capture_img,auto_run,stop_event,stop_runcalib):
    print("Task 2 assigned to process: {}".format(os.getpid()))
    auto_event.clear()
    event.clear()
    exit_event.clear()
    while True:
        if stop_event.is_set():  # Kiểm tra nếu sự kiện dừng đã được thiết lập
            print("close task2")
            break
        if not connectcom.empty():
            received_data = connectcom.get()
            if received_data == 'connectcom':
                namecom=datacom.get()
                # Cấu hình cổng serial
                try:
                    ser = serial.Serial(
                        port=namecom,
                        baudrate=9600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=1
                    )
                    print("Kết nối cổng serial thành công!")
                except serial.SerialException as e:
                    print("Không thể kết nối cổng serial:", e)
                    exit()

                # Hàm để gửi dữ liệu qua cổng serial
                def send_data(data):
                    ser.write(data.encode())

                # Hàm để đọc dữ liệu từ cổng serial
                def read_data():
                    return ser.read_all().decode().strip()

                # Vòng lặp chính để đọc và gửi dữ liệu, nếu chưa có auto thì chạy và cập nhật io/do thôi
                while True:
                    if stop_event.is_set():  # Kiểm tra nếu sự kiện dừng đã được thiết lập
                        # print("close task2")
                        break
                    # Đọc dữ liệu từ cổng serial
                    readdata = read_data()
                    # print(readdata)
                    # Kiểm tra nếu dữ liệu đọc được là '1' thì xử lý chụp ảnh####
                    if readdata == '1':
                        # Gửi lại dữ liệu là '2'
                        capture_img.put('1')
                        # send_data('2')
            
                    elif readdata == '2':
                        # Kết thúc vòng lặp nếu nhận được '2'
                        print("Kết thúc vòng lặp")
                        break
                    if exit_event.is_set():   # disconnect cổng com
                        # Đóng cổng serial khi kết thúc
                        ser.close()
                        print("disconnect com")
                        exit_event.clear()
                        break
                    if event.is_set():   # xử lý bật xylanh manual
                        print("on xy lanh")
                        event.clear()
                        send_data('33')
                    if ketquaxuly.is_set():
                        ketquaxuly.clear()
                        send_data('33')
                        print("kích xy lanh")
                    
                    # if auto_event.is_set(): # kích hoạt chế độ auto
                    #     if readdata == '1':
                    #         capture_img.put('1')
                    #         print('capture image')
                        # if ketquaxuly.is_set():
                        #     ketquaxuly.clear()
                        #     send_data('33')
                        #     print('on xylanh')

                    # if auto_run.get()=='run': # kích hoạt chế độ auto
                    #     if readdata == '1':
                    #         capture_img.put('1')
                    #         print('capture image')

if __name__ == "__main__":
    event = Event()
    exit_event = Event()
    auto_event= Event()
    ketquaxuly= Event()
    datacom = Queue()
    connectcom = Queue()
    capture_img = Queue()
    auto_run= Queue()
    stop_event = Event()
    stop_runcalib = Event()

    # Tạo các tiến trình
    p1 = Process(target=task1, args=(event, exit_event,auto_event,ketquaxuly, datacom, connectcom,capture_img,auto_run,stop_event,stop_runcalib))
    p2 = Process(target=task2, args=(event, exit_event,auto_event,ketquaxuly, datacom, connectcom,capture_img,auto_run,stop_event,stop_runcalib))

    p1.start()
    p2.start()

    p1.join()
    p2.join()