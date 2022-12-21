import time
import numpy as np
import pyscreenshot as ImageGrab
import cv2
from datetime import datetime
import serial
import os
import pytesseract
from word2number import w2n

pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'
serial_port = serial.Serial('COM9', 9600)
filename = 'kek.png'
txs = "0"
serial_port.write(txs.encode())

cap = cv2.VideoCapture(0)
crange = [0, 0, 0, 0, 0, 0]
text = 'three'
while True:
    flag, img = cap.read()
    height, widht = img.shape[:2]
    Centr_X = int(widht / 2)
    Centr_Y = int(height / 2)
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    screen = np.array(ImageGrab.grab(bbox=(cv2.imshow('Origin', img))))
    last_time = time.time()
    # cv2.imshow('window', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    cv2.imwrite(filename, img)
    # x = x + 1
    img = cv2.imread('kek.png')
    text = pytesseract.image_to_string(img).lower()
    print(text)
    f = open('log.txt', 'a')

    numb_arr = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    b = ""
    status = ""
    for i in numb_arr:
        b = i.lower()
        i = text.find(i)
        if i == -1:
            txs = "0"
            serial_port.write(txs.encode())
        if i != -1 and "one" in b:
            txs = "1"
            serial_port.write(txs.encode())
            temp = serial_port.read_all().decode()[0:1]
            print(f"----{temp}----")
            f.write(f"Time: {datetime.now()} Mess: {b} Status: {temp}\n")
            time.sleep(1)
        if i != -1 and "two" in b:
            txs = "2"
            serial_port.write(txs.encode())
            temp = serial_port.read_all().decode()[0:1]
            print(f"----{temp}----")
            f.write(f"Time: {datetime.now()} Mess: {b} Status: {temp}\n")
            time.sleep(1)
        if i != -1 and "three" in b:
            txs = "3"
            serial_port.write(txs.encode())
            temp = serial_port.read_all().decode()[0:1]
            print(f"----{temp}----")
            f.write(f"Time: {datetime.now()} Mess: {b} Status: {temp}\n")
            time.sleep(1)
        if i != -1 and "four" in b:
            txs = "4"
            serial_port.write(txs.encode())
            temp = serial_port.read_all().decode()[0:1]
            print(f"----{temp}----")
            f.write(f"Time: {datetime.now()} Mess: {b} Status: {temp}\n")
            time.sleep(1)
        if i != -1 and b == "five":
            txs = "5"
            serial_port.write(txs.encode())
            temp = serial_port.read_all().decode()[0:1]
            print(f"----{temp}----")
            f.write(f"Time: {datetime.now()} Mess: {b} Status: {temp}\n")
            time.sleep(1)
        if i != -1 and "six" in b:
            txs = "6"
            serial_port.write(txs.encode())
            temp = serial_port.read_all().decode()[0:1]
            print(f"----{temp}----")
            f.write(f"Time: {datetime.now()} Mess: {b} Status: {temp}\n")
            time.sleep(1)
        if i != -1 and "seven" in b:
            txs = "7"
            serial_port.write(txs.encode())
            temp = serial_port.read_all().decode()[0:1]
            print(f"----{temp}----")
            f.write(f"Time: {datetime.now()} Mess: {b} Status: {temp}\n")
            time.sleep(1)
        if i != -1 and "eight" in b:
            txs = "8"
            serial_port.write(txs.encode())
            temp = serial_port.read_all().decode()[0:1]
            print(f"----{temp}----")
            f.write(f"Time: {datetime.now()} Mess: {b} Status: {temp}\n")
            time.sleep(1)
        if i != -1 and "nine" in b:
            txs = "9"
            serial_port.write(txs.encode())
            temp = serial_port.read_all().decode()[0:1]
            print(f"----{temp}----")
            f.write(f"Time: {datetime.now()} Mess: {b} Status: {temp}\n")
            time.sleep(1)
        if text != '':
            try:
                if w2n.word_to_num(text) is not None:
                    if w2n.word_to_num(text) >= 10:
                        print(f"NOT IN BASE: {w2n.word_to_num(text)}")
                        txs = "w"
                        serial_port.write(txs.encode())
                        time.sleep(1)
            except:
                print()
    f.close()
    ch = cv2.waitKey(5)
    if ch == 3:
        break
