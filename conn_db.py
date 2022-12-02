import serial

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from tire import save_result

import tensorflow.keras
import numpy as np
import cv2

# Set a PORT Number & baud rate
PORT = 'COM3'
BaudRate = 9600

ARD= serial.Serial(PORT,BaudRate)

def Decode(int_sum):
    int_sum = int_sum.decode()
    int_sum = str(int_sum)
    if int_sum[0]=='Q':                       
        Ard1=str(int_sum[1:2])
        Ard2=str(int_sum[3:5])
        result= [Ard1, Ard2]
        return result
    
def Ardread(): # return list [Ard1,Ard2]
        if ARD.readable():
            LINE = ARD.readline()
            code=Decode(LINE) 
            return code
        else : 
            print("읽기 실패 from _Ardread_")

model = tensorflow.keras.models.load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
size = (224, 224)
classes = ['normal tire', 'level 1 tire', 'level 2 tire']

cred = credentials.Certificate("mssb-80c93-firebase-adminsdk-vak81-60cdb63f5c.json")
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://mssb-80c93-default-rtdb.firebaseio.com'})

result = save_result()

temp = Ardread()
result1 = float(temp[0]) + (float(temp[1]) * 0.01)

dir = db.reference()
dir.update({'타이어 손상도':result})
dir.update({'마모도':result1})