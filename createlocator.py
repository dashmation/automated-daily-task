import xml.dom.minidom
import os
import re
from lxml import etree
import subprocess

def takeXMLDOM(filename):
    os.system('rm *.xml')
    os.system('adb shell uiautomator dump /sdcard/DCIM/'+filename+'.xml')
    os.system('adb pull /sdcard/DCIM/'+filename+'.xml .')
    os.system('adb shell rm /sdcard/DCIM/'+filename+'.xml')
    return filename

def getTextFrom(filename):
    # Load the XML file into an ElementTree object
    tree = etree.parse(filename)

    # Use an XPath query to select the element that contains the text you're interested in
    element = tree.xpath('//example/element')[0]

    # Extract the text from the element
    text = element.text

    # Print the extracted text
    print(text)
    

# Define a recursive function to get all possible XPaths
def get_all_xpaths(node, path=""):
    with open('temp.xml', 'r') as file:
        # Load the XML output of "adb shell uiautomator dump" into a string
        xml_string = file.read()

    # Parse the XML string into an ElementTree object
    root = etree.fromstring(xml_string)

    # Get the XPath for this node
    xpath = node.getroottree().getpath(node)
    xpath = xpath.replace("[1]", "") # Remove index if it's the first element
    xpath = path + xpath # Combine with the path so far
    
    # Print the XPath
    print(xpath)
    
    # Recursively get XPaths for all child nodes
    for i, child in enumerate(node.getchildren()):
        get_all_xpaths(child, xpath + f"[{i+1}]")


def getDataFromXML(filename):
    doc = xml.dom.minidom.parse(filename+'.xml')
    # print(doc.nodeName)
    # print(doc.firstChild.tagName)

    node = doc.getElementsByTagName('node')
    print("%d nodes" % node.length)
    dict = {'index':'',
            'text':'',
            'class':'',
            'package':'',
            'content-desc':'',
            'checkable':'',
            'checked':'',
            'clickable':'',
            'enabled':'',
            'focusable':'',
            'focused':'',
            'scrollable':'',
            'long-clickable':'',
            'password':'',
            'selected':'',
            'bounds':''}
    xpath = ''
    dict_in_dict = []
    for item in node:
        dict['index'] = item.getAttribute('index')
        dict['text'] = item.getAttribute('text')
        dict['resource-id'] = item.getAttribute('resource-id')
        dict['class'] = item.getAttribute('class')
        dict['package'] = item.getAttribute('package')
        dict['content-desc'] = item.getAttribute('content-desc')
        dict['checkable'] = item.getAttribute('checkable')
        dict['checked'] = item.getAttribute('checked')
        dict['clickable'] = item.getAttribute('clickable')
        dict['enabled'] = item.getAttribute('enabled')
        dict['focusable'] = item.getAttribute('focusable')
        dict['focused'] = item.getAttribute('focused')
        dict['scrollable'] = item.getAttribute('scrollable')
        dict['long-clickable'] = item.getAttribute('long-clickable')
        dict['password'] = item.getAttribute('password')
        dict['selected'] = item.getAttribute('selected')
        dict['bounds'] = item.getAttribute('bounds')     
        if dict['resource-id'] != '':
            byName = dict['resource-id'][dict['resource-id'].find('/')+1:]
            xpath = 'By '+byName+' = By.xpath(\"//'+dict['class']+'[@resource-id,'+dict['resource-id']+'"]'
            # print('By '+byName+' = By.xpath(\"//'+dict['class']+'[@resource-id,'+dict['resource-id']+'"]')
        elif dict['text'] != '':
            byName = re.sub('[^a-zA-Z]','',dict['text'])
            xpath = 'By '+byName+' = By.xpath(\"//'+dict['class']+'[@resource-id,'+dict['resource-id']+'"]'
            # print('By '+byName+' = By.xpath(\"//'+dict['class']+'[@text,'+dict['text']+'"]')

        # print('#######################')
        
        if xpath not in dict_in_dict:
            dict_in_dict.append(xpath)
    
    # for i in dict_in_dict:
        # print(i)
        # print('#######################')
    
    # print(dict_in_dict)
    


def main():
    generateXPATH('com.airtel.tv')

if __name__ == '__main__':
    main()