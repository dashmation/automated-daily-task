import os

# os.system('pip3 install opencv-python')
# os.system('pip3 install pytesseract')

import cv2
import pytesseract
import traceback
import json

def takeScreenshot(name):
    os.system('adb shell screencap -p /sdcard/DCIM/'+name+'.png')
    os.system('adb pull /sdcard/DCIM/'+name+'.png .')
    os.system('adb shell rm /sdcard/DCIM/'+name+'.png')

#Get The GrayScale Image
def getGrayScale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Remove Noise
def removeNoise(image):
    return cv2.medianBlur(image,5) 

#Thresholding
def thresholding(image):
    return cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def getInfo(image):
    img1 = cv2.imread(image)
    # img2 = getGrayScale(img1)
    # img3 = thresholding(img2)
    # img4 = removeNoise(img3)   
    text = pytesseract.image_to_string(img1)
    # print(text)
    content_list = []
    content_list = text.split('\n')
    # print(content_list)
    return content_list

def goToAccountInfoPage():
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

def goToSoftwareInfoPage():
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
    os.system('adb shell input keyevent 20')
    os.system('adb shell input keyevent 20')
    
def getDetails():
    try:
        goToAccountInfoPage()
        takeScreenshot('accountinfopage')
        goToSoftwareInfoPage()
        takeScreenshot('softwareinfopage')
        account_Info_list = getInfo('accountinfopage.png')
        software_Info_list = getInfo('softwareinfopage.png')
        details_dict = {'customerid':'','rtn':'','account_balance':'','due_date':'','monthly_rent':'','cdsn':'','build':'','fw':''}

        try:
            details_dict['customerid'] = account_Info_list[3][14:]
        except:
            details_dict['customerid'] = 'not_found'
        try:
            details_dict['rtn'] = account_Info_list[5][30:]
        except:
            details_dict['rtn'] = 'not_found'
        try:
            details_dict['account_balance'] = account_Info_list[7][21:]
        except:
            details_dict['account_balance'] = 'not_found'
        try:
            details_dict['due_date'] = account_Info_list[9][21:]
        except:
            details_dict['due_date'] = 'not_found'
        try:
            details_dict['monthly_rent'] = account_Info_list[11][18:]
        except:
            details_dict['monthly_rent'] = 'not_found'
        try:
            details_dict['cdsn'] = software_Info_list[23]
        except:
            details_dict['cdsn'] = 'not_found'
        try:
            details_dict['build'] = software_Info_list[19]
        except:
            details_dict['build'] = 'not_found'
        try:
            details_dict['fw'] = software_Info_list[22]
        except:
            details_dict['fw'] = 'not_found'

        # print(details_dict)
        print('')
        print('')
        print('')
        print('')
        details_json = json.dumps(details_dict,indent=4)
        print(details_json)
    except:
        print(traceback.format_exc())
    finally:
        os.system('rm *.png')
        print('')


getDetails()