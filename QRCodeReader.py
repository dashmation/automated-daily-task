import os
import cv2
import pandas as pd
import datetime
import time
from tabulate import tabulate

def decode(input):
    if input == '!':
        return 0
    else:
        if input == '"':
            return 1
        else:
            if input == '#':
                return 3
            else:
                if input == '$':
                    return 5
                else:
                    if input == '%':
                        return 7
                    else:
                        if input == '&':
                            return 9
                        else:
                            if input == "'":
                                return 11
                            else:
                                if input == '(':
                                    return 13
                                else:
                                    return ord(input)-26
                
def CODE(input):
    return ''.join(filter(lambda i: i.isdigit(), input))

def read_qr_code(filename):
    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        # value = 'b3c225ff-1;5efa03bd;-VvZjZnZjZnV^V^VnVnVZVZV^V^V^VFVFVjVZVb'
        return value
    except:
        return

def takeXMLDOM(filename):
    os.system('rm *.xml')
    os.system('adb shell uiautomator dump /sdcard/DCIM/'+filename+'.xml')
    os.system('adb pull /sdcard/DCIM/'+filename+'.xml .')
    os.system('adb shell rm /sdcard/DCIM/'+filename+'.xml')
    return filename

def search_string_in_file(file_name, string_to_search):
    line_number = 0
    results = False
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then return TRUE
                results = True
    return results

def goToTPDiagnostics():
    os.system('adb shell input keyevent 3')

    os.system('adb shell input keyevent 22')
    os.system('adb shell input keyevent 22')
    os.system('adb shell input keyevent 22')
    os.system('adb shell input keyevent 22')
    os.system('adb shell input keyevent 22')
    os.system('adb shell input keyevent 22')
    os.system('adb shell input keyevent 22')
    os.system('adb shell input keyevent 22')
    os.system('adb shell input keyevent 22')

    os.system('adb shell input keyevent 23')

    os.system('adb shell input keyevent 20')
    os.system('adb shell input keyevent 20')
    os.system('adb shell input keyevent 20')
    os.system('adb shell input keyevent 20')
    os.system('adb shell input keyevent 20')

    os.system('adb shell input keyevent 23')

    os.system('adb shell input keyevent 20')
    os.system('adb shell input keyevent 20')

def clickOnSCANALLTP():
    os.system('adb shell input keyevent 22')
    os.system('adb shell input keyevent 22')

    os.system('adb shell input keyevent 23')

def generateQRCode():
    os.system('adb shell input keyevent 22')

    os.system('adb shell input keyevent 23')

def clickOnOK():
    os.system('adb shell input keyevent 23')

def takeScreenshot(name):
    os.system('adb shell screencap -p /sdcard/DCIM/'+name+'.png')
    os.system('adb pull /sdcard/DCIM/'+name+'.png .')
    os.system('adb shell rm /sdcard/DCIM/'+name+'.png')
    return name

def getQRCodeDecodeValue(filename):
    value = read_qr_code(filename+'.png')
    print(value)

    df = pd.DataFrame(columns=['', 'QR Code','',value])

    df.loc[1] = ['','No. of char in QR code',len(value),'']
    df.loc[2] = ['','CRC (2-Byte)','PASS','']
    df.loc[3] = ['','Customer ID',str(int(value[:8], 16))+''+value[8:10],'']
    df.loc[4] = ['','Current Time (IST)',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'']

    df.loc[5] = ['','Number Of Transponders',decode(value[20:21]),'']

    index = 6
    count = 1
    while index < 44 or count < 20:
        df.loc[index] = ['Transponder '+str(count), 'Signal Strength', decode(value[index+15:index+16]),'']
        df.loc[index+1] = ['Transponder '+str(count), 'Signal Quality', decode(value[index+1+15:index+1+16]),'']
        index = index + 2
        count = count + 1

    df.to_csv('result.csv', index = False, encoding='utf-8')
    os.system('open result.csv')
    print(tabulate(df, headers='keys', tablefmt='psql'))

def mains():
    goToTPDiagnostics()
    clickOnSCANALLTP()
    time.sleep(117.8)
    for retry in range(1,11):
        filename = takeXMLDOM('temp')
        status = search_string_in_file(filename+'.xml','text="GENERATE QR CODE"')
        if status == True:
            try:
                generateQRCode()
                takeScreenshot('image')
                clickOnOK()
                getQRCodeDecodeValue('image')
                os.system('rm *.png')
                os.system('rm *.xml') 
            except:
                print('Unable to perform')
            break;
        time.sleep(3)
        retry = retry + 1

def main():
    getQRCodeDecodeValue('image')

if __name__ == '__main__':
    main()