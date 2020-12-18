# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testing_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from tensorflow import keras
import pandas as pd
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Load Models...
        self.low_model = keras.models.load_model('low_model')
        self.high_model = keras.models.load_model('high_model')
        self.current_model = 'LSTM'

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.app_title = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_title.sizePolicy().hasHeightForWidth())
        self.app_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.app_title.setFont(font)
        self.app_title.setObjectName("app_title")
        self.verticalLayout.addWidget(self.app_title)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.text_input_file_path = QtWidgets.QLineEdit(self.centralwidget)
        self.text_input_file_path.setObjectName("text_input_file_path")
        self.verticalLayout.addWidget(self.text_input_file_path)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.cb_select_model = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_select_model.sizePolicy().hasHeightForWidth())
        self.cb_select_model.setSizePolicy(sizePolicy)
        self.cb_select_model.setObjectName("cb_select_model")
        self.verticalLayout.addWidget(self.cb_select_model)
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_run.sizePolicy().hasHeightForWidth())
        self.btn_run.setSizePolicy(sizePolicy)
        self.btn_run.setObjectName("btn_run")
        self.verticalLayout.addWidget(self.btn_run)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayout.addWidget(self.table)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Changed Things
        self.btn_run.clicked.connect(self.predict)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.app_title.setText(_translate("MainWindow", "Intraday Stock Price Prediction Application"))
        self.label_2.setText(_translate("MainWindow", "CSV input file path"))
        self.label.setText(_translate("MainWindow", "Select Model"))
        self.btn_run.setText(_translate("MainWindow", "Run"))
        self.label_3.setText(_translate("MainWindow", "Output"))


    def load_models(self):
        text = self.cb_select_model.currentText()
        
        if text != self.current_model:
            if text == 'LSTM':
                low_path = 'low_model'
                high_path ='high_model'
            elif text == 'Linear Regression':
                 low_path = 'lr_low_model'
                high_path ='lr_high_model'

             # Load Models...
            self.low_model = keras.models.load_model('low_model')
            self.high_model = keras.models.load_model('high_model')
 
            self.current_model = text
  
        
    def predict(self):
        text = self.text_input_file_path.text().strip()
        
        df = pd.read_csv(text, header=None)
        
        for row in df.iterrows():
            name = row[0]
            numbers = row[1:]
            
            scaler = MinMaxScaler()
            new_data = scaler.fit_transform(np.reshape(np.asarray(numbers),(-1,1)).astype(np.float32))
            
            pred_low = self.low_model.predict(new_data)[0]
            pred_high =self.high_model.predict(new_data)[0]
            
            pred_low = scaler.inverse_transform([pred_low])[0]
            pred_high = scaler.inverse_transform([pred_low])[0]
            
            row_count = self.table.rowCount()
            self.table.insertRow(row_count)
            
            self.table.setItem(row_count , 0, name)
            self.table.setItem(row_count , 1, pre_low)
            self.table.setItem(row_count , 2, pred_high)
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

