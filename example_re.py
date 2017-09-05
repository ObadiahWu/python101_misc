import re
# example: regexp
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-9999')
print("EX(regexp)",mo.group())
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print("EX(regexp)(findall)",mo)
import pyautogui
print ("EX(pyautogui): size is",pyautogui.size())
pyautogui.moveTo(800,500,duration=0.25)
print ("EX(pyautogui): current position is",pyautogui.position())
im = pyautogui.screenshot()
print("EX(pyautogui): current pixel value is",im.getpixel((pyautogui.position())))
