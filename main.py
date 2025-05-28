# File:     Automated-OCT.py
# Version:  0.0.01
# Author:   Susan Haynes
# Comments/Notes:
#   (0,0) coordinates are the top left corner of the screen for 1920x1080
#   (0,0) coordinates are the bottom right corner of the screen for 1919x1079
# To find the location on a screen open IDLE
# >>> import pyautogui      <- this allows us to use pyautogui prompts
# >>> pyautogui.size()    <- this returns the size of the monitor
# >>> pyautogui.position()  <- this returns the exact location of where the mouse pointer is

import configparser                                     # parsing multiple GUI's
import datetime as dt                                   # Date library
import keyboard                                         # windows right key
import os                                               # closing an executable
import pyautogui                                        # automating screen clicks
import pymem                                            # checking if .exe is open
import pymem.process                                    # checking if .exe is open
import pywinauto                                        # bringing an .exe to the foreground
import subprocess                                       # open an executable
import time                                             # call time to count/pause
import tkinter as tk                                    # Tkinter's Tk class
import tkinter.ttk as ttk                               # Tkinter's Tkk class
import win32con                                         # justify right or left the GUI.
import win32gui                                         # bring apps to front foreground

from functools import partial                           # freezing one function while executing another
from openpyxl import *                                  # Write to excel
from pathlib import PureWindowsPath                     # library that cleans up windows path extensions
from PIL import ImageTk, Image                          # Displaying LAL background photo
from python_imagesearch.imagesearch import imagesearch  # opening images, pip package
from tkinter import messagebox                          # Exit standard message box
from win32gui import GetWindowText, GetForegroundWindow # check position of a window

config = configparser.ConfigParser()
samp_arr_raw =[]
btn_pres_cnt = 1                # setting count to 0 to be able to call it a global variable within the function

###########################################       Temporary variables for testing            ##################################################  
opcred = "SH"                                          # Main.opcred
work_order = "L00-TEST"                                 # Main.WO
#dio_sz = "4.5D"                                             # Dioptics.dio_sz
#lns_type = " 040"                                           # Main.lns_type    --> Do we need this since we are always going to both 040 and 015??
#oct_eq = "OCT 1"                                            # Main.eq_num_oct  --> Do we need this? Or was it only for folder
#entry_pr = "02"                                             # Main.entry_pr    --> Do we need this?

fill_arr = 30                   # TEST VALUE
samp_arr_raw = []               # TEST VALUE
for fa in range(fill_arr):      # TEST VALUE
    samp_arr_raw.append(fa)     # TEST VALUE
print("Sample Array Raw is: ", samp_arr_raw)    # TEST
        
##########################################################################################################################################
#################################################    KINESIS & LUMEDICA     ##############################################################
##########################################################################################################################################
#opcred = Main.opcred
#work_order = Main.WO

###########################################      Assign Screenshots to Variables      ################################################
path = r"C:\Users\shaynes\OneDrive - RxSight, Inc\Desktop\OCT XY-Stage\ThorLabs Kinesis/"
k_allchecked    = "Kin-AllChecked.png"
k_allunchecked  = "Kin-AllUnChecked.png"
k_arrow         = "Kin-Arrow.png"
k_arrowns       = "Kin-ArrowNS.png"
k_cancel        = "Kin-Cancel.png"
k_check         = "Kin-Chk.png"
k_conn          = "Kin-Conn.png"
k_connn         = "Kin-Connn.png"
k_connxy        = "Kin-ConnXY.png"
k_connyx        = "Kin-ConnYX.png"
k_drag          = "Kin-Drag.png"
k_home          = "Kin-Home.png"
k_home_cls      = "Kin-HomeClose.png"
k_home_dpdn     = "Kin-HomeDpDn.png"
k_not_homed     = "Kin-HomeNot.png"
k_notallconn    = "Kin-NoAllConnected.png"
k_nodevices     = "Kin-NoDevices.png"
k_nousb         = "Kin-NoUSB.png"
k_noxconn       = "Kin-NoXConn.png"
k_noxnoyconn    = "Kin-NoXNoYConn.png"
k_noyconn       = "Kin-NoYConn.png"
k_resume        = "Kin-Resume.png"
k_run           = "Kin-Run.png"
k_seqopt        = "Kin-SeqOpt.png"
k_pause         = "Kin-SeqPause.png"
k_start_cls     = "Kin-StartClose.png"
k_start_dpdn    = "Kin-StartDpDn.png" 
k_start         = "Kin-StartSeq.png"
k_stop          = "Kin-Stop.png"
k_testseq       = "Kin-TestSeq.png"
k_tseq_dpdn     = "Kin-TestSeqDpDn.png"
k_tseq_cls      = "Kin-TSeqClose.png"
k_x_sn          = "Kin-XandSN.png"
k_xdis_h        = "Kin-XDisHome.png"
k_xdis_nh       = "Kin-XDisNotHome.png"
k_xen_h         = "Kin-XEnHome.png"
k_xen_nh        = "Kin-XEnNotHome.png"
k_x_nh          = "Kin-XNotHome.png"
k_xzero         = "Kin-XHome.png"
k_xsn           = "Kin-XSN.png"
k_xstart        = "Kin-Xstart.png"
k_y_sn          = "Kin-YandSN.png"
k_ydis_h        = "Kin-YDisHome.png"
k_ydis_nh       = "Kin-YDisNotHome.png"
k_yen_h         = "Kin-YEnHome.png"
k_yen_nh        = "Kin-YEnNotHome.png"
k_y_nh          = "Kin-YNotHome.png"
k_yzero         = "Kin-YHome.png"
k_ysn           = "Kin-YSN.png"
k_ystart        = "Kin-Ystart.png"
k_thorlabs      = "Thorlabs.png"

###########################################     Assign Lumedica Screenshots to Variables      #################################################
l_path = r"O:\Lumedica OCT Data Backup\Notes to File\Lumedica Screenshots/"
l_cnf_015       = "Lum-Cnfg-015.png"
l_cnf_040       = "Lum-Cnfg-040.png"
l_cnf_100       = "Lum-Cnfg-100.png"
l_cnf_crss      = "Lum-Cnfg-Cross.png"
l_cnf_circ      = "Lum-Cnfg-Circle.png"
l_fil_att       = "Lum-FileAtt.png"
l_fil_att_cls   = "Lum-FilAttCls.png"
l_fil_att_pop   = "Lum-FileAttPop.png"
l_fold          = "Lum-Folder.png"
l_saveB         = "Lum-SaveBimg.png"
l_scn_type      = "Lum-Alin-Type.png"       # not using this yet. For circle and picking type.
l_start         = "Lum-StartScn.png"
l_stop          = "Lum-StopScn.png"
l_tab_cnfg      = "Lum-TabCnfg.png"
l_tab_main      = "Lum-TabMain.png"

##############################   Functions to bring to foreground and right/left justify & full screen   ######################################  
#def kin_main():                                                             # bring Kinesis to the main screen, we will need this multiple times.
#    kin_title = 'Kinesis'
#    kin_app = pywinauto.Application().connect(title=kin_title)
#    kin_win = kin_app[kin_title]
#    kin_win.set_focus()
#    print('Kinesis is in the foreground now.')

#def kin_pop():                                                              # bring Kinesis POPUP to the main screen, we will need this multiple times.
#    pop_title = 'Sequence Options'                                          # DOUBLE CHECK THIS IS THE POPUP WINDOW NAME!!!!!!!!!!!!!!!!!!!!!!!!!!!
#    pop_app = pywinauto.Application().connect(title=pop_title)
#    pop_win = pop_app[pop_title]
#    pop_win.set_focus()
#    print('Kinesis Pop-up is in the foreground now.')

#def right_kin():                                                                # Right justify Kinesis
#    kin_main()                                                                  # Bring Kinesis to main foreground
#    time.sleep(1)                                                               # pause to allow to come to foreground
#    rkin = win32gui.GetForegroundWindow()                                       # grab the window in the foreground
#    r_rect = win32gui.GetWindowRect(rkin)                                       # assign window rectangle coordinates to an array
#    a = r_rect[0]                                                               # a=upper left corner positon of the Kinesis window in the X coordinates of the screen
#    b = r_rect[1]                                                               # b=upper left corner positon of the Kinesis window in the Y coordinates of the screen
#    c = r_rect[2] - a                                                           # c is the length of the kinesis window, should be half the length of the screen 1920/2=960
#    d = r_rect[3] - b                                                           # d is the height of the kinesis window, should be the entire height of the screen 1080
#    if b != 0:                                                                  # if b is not equal to 0 (Y in the 0 location)
#        win32gui.SetWindowPos(rkin, win32con.HWND_TOP, 960, 0, 960, 1080, 0)    # set to this location; X=960, Y=0, L=960, H=1080 
#        print('Kinesis is not right justified... from the if statement.')       # X,Y,L,H. X&Y are top left corner position. L&W of the GUI window
#        time.sleep(1)
#    else:                                                                       # else, right justify anyways
#        win32gui.SetWindowPos(rkin, win32con.HWND_TOP, 960, 0, 960, 1080, 0)    # Y may be at 0, but some of the other coordinates might not be.
#        print('Kinesis seems to be right justified... from the else statement.')
#        time.sleep(1)

def lum_main():                                                                 # bring Lumedica to the main screen, we will need this multiple times.
    lum_title = 'Lumedica OQ PathScope'
    lum_app = pywinauto.Application().connect(title=lum_title)
    lum_win = lum_app[lum_title]
    lum_win.set_focus()
    print('Lumedica is in the foreground.')

def lum_file_att():                                                             # bring Lumedica to the main screen, we will need this multiple times.
    lum_fil_att = 'File Attributes'                                             # Find a window named File Attributes
    lum_app_filatt = pywinauto.Application().connect(title=lum_fil_att)         # Connect to the app
    lum_filatt_set = lum_app_filatt[lum_fil_att]
    lum_filatt_set.set_focus()
    print('File Attributes is in the foreground.')
    time.sleep(1)                                                               # pause to allow to come to foreground
    lum_filatt_get = win32gui.GetForegroundWindow()                             # grab the window in the foreground
    lum_filatt_rec = win32gui.GetWindowRect(lum_filatt_get)                     # assign window rectangle coordinates to an array
    i = lum_filatt_rec[0]                                                       # i=upper left corner positon of File Attributes window in the X coordinates of the screen
    j = lum_filatt_rec[1]                                                       # j=upper left corner positon of File Attributes window in the Y coordinates of the screen
    k = lum_filatt_rec[2] - i                                                   # k is the length of the File Attributes window, should be half the length of the screen 1920/2=960
    l = lum_filatt_rec[3] - j                                                   # l is the height of the File Attributes window, should be the entire height of the screen 1080
    if j != 0:                                                                  # if b is not equal to 0 (Y in the 0 location)
        win32gui.SetWindowPos(lum_filatt_get, win32con.HWND_TOP, 393, 24, 609, 271, 0) # set to this location; X=393, Y=24, L=609, H=271 
        print('Lumedica is not right justified... from the if statement.')      # X,Y,L,H. X&Y are top left corner position. L&W of the GUI window
    else:                                                                       # else, left justify anyways
        win32gui.SetWindowPos(lum_filatt_get, win32con.HWND_TOP, 393, 24, 609, 271, 0) # Y may be at 0, but some of the other coordinates might not be.
        print('Lumedica seems to be right justified... from the else statement.')

def lum_mini():                                                                 # minimize Lumedica, we will need this multiple times.
    lum_main()                                                                  # Bring Lumedica to main foreground
    time.sleep(1)                                                               # pause to allow to come to foreground
    lum_minimize = win32gui.GetForegroundWindow()                               # grab the window in the foreground
    win32gui.ShowWindow(lum_minimize, win32con.SW_MINIMIZE)                     # minimize lumedica
    print('Lumedica is minimized.')

def left_lum():                                                                 # Left justify Lumedica
    lum_main()                                                                  # Bring Lumedica to main foreground
    time.sleep(1)                                                               # pause to allow to come to foreground
    llum = win32gui.GetForegroundWindow()                                       # grab the window in the foreground
    l_rect = win32gui.GetWindowRect(llum)                                       # assign window rectangle coordinates to an array
    e = l_rect[0]                                                               # e=upper left corner positon of Lumedica window in the X coordinates of the screen
    f = l_rect[1]                                                               # f=upper left corner positon of Lumedica window in the Y coordinates of the screen
    g = l_rect[2] - e                                                           # g is the length of the Lumedica window, should be half the length of the screen 1920/2=960
    h = l_rect[3] - f                                                           # h is the height of the Lumedica window, should be the entire height of the screen 1080
    if f != 0:                                                                  # if b is not equal to 0 (Y in the 0 location)
        win32gui.SetWindowPos(llum, win32con.HWND_TOP, 0, 0, 960, 1080, 0)      # set to this location; X=0, Y=0, L=960, H=1080 
        print('Lumedica is not right justified... from the if statement.')      # X,Y,L,H. X&Y are top left corner position. L&W of the GUI window
    else:                                                                       # else, left justify anyways
        win32gui.SetWindowPos(llum, win32con.HWND_TOP, 0, 0, 960, 1080, 0)      # Y may be at 0, but some of the other coordinates might not be.
        print('Lumedica seems to be right justified... from the else statement.')

def full_lum():                                                                 # Make Lumedica Full Screen
    lum_main()                                                                  # Bring Lumedica to main foreground
    time.sleep(1)                                                               # pause to allow to come to foreground
    llum = win32gui.GetForegroundWindow()                                       # grab the window in the foreground         
    win32gui.SetWindowPos(llum, win32con.HWND_TOP, 0, 0, 1760, 1035, 0)         # set to this location; X=0, Y=0, L=1760, H=1035 
    print('Lumedica is the full screen.')                                       # X,Y,L,H. X&Y are top left corner position. L&W of the GUI window

def lum_save():
    print("Do Lumedica save stuff here.")

def data_fexp():
    subprocess.Popen('explorer "C:\\Users\\Public\\Documents\\Lumedica\\OctEngine\\Data\\' + work_order + '\\"') # open file explorer
    time.sleep(1)
    fexp = win32gui.GetForegroundWindow()                                       # grab the window in the foreground         
    win32gui.SetWindowPos(fexp, win32con.HWND_TOP, 1761, 0, 158, 1035, 0)       # set to this location; X=1761, Y=0, L=158, H=1035 
    print('File Explorer Data is far right justified.')                         # X,Y,L,H. X&Y are top left corner position. L&W of the GUI window

############################################            Open Kinesis and Lumedica             ##################################################  
#try:                                                                                        # Try: check if Kinesis is already open.                
#    kin_pm = pymem.Pymem('Kinesis.exe')
#except:                                                                                     # Except, if not open, then open it.
#    print('Except: Kinesis is not running, lets open it!!!')
#    subprocess.Popen('C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.Kinesis.exe', shell=True) # Open Kinesis sw
#    time.sleep(8)                                                                           # wait 8 seconds for kinesis to open fully
#else:
#    print('Else: Kinesis is already open.')

try:                                                                                        # Try: check if Lumedica is already open.                
    lum_pm = pymem.Pymem('OctEngine.exe')
except:                                                                                     # Exception executed, if not open, then open it.
    print('Except: Lumedica is not running, lets open it!!!')
    subprocess.Popen('C:\\Program Files (x86)\\Lumedica\\OctEngine\\OctEngine.exe', shell=True) # Lumedica sw
    time.sleep(7)                                                                           # wait 8 seconds for Lumedica to open fully           
else:
    print('Else: Lumedica is already open.')

#kin_main()                                                                                  # kinesis into the foreground
#right_kin()                                                                                 # right justify kinesis
#time.sleep(1)
#############################################           ALIGNMENT LUMEDICA, DO FIRST           ##################################################  
full_lum()                                                                                  # lumedica full screen
time.sleep(1)                                                                            # pause to full screen

afold, bfold = pyautogui.locateCenterOnScreen(l_path + f'{l_fold}')                         # assign X,Y coordinates of image to variables
pyautogui.moveTo(x=afold, y=bfold)                                                          # move to x,y coordinates of empty folder entry
pyautogui.moveRel(xOffset=50, yOffset=-5)                                                   # move to "Folder" entry box
pyautogui.click()                                                                           # click in the entry box to become the focus
time.sleep(1)           
pyautogui.hotkey('ctrl', 'a')                                                               # select all hotkey
pyautogui.press('backspace')                                                                # backspace to clear whatever is in there
time.sleep(1)   
pyautogui.typewrite(work_order)                                                             # paste work order entry string from main GUI
time.sleep(2)   
print("Entered work_order: ", work_order)
time.sleep(1)   

try:                                                                                        # try to find the lumdedica popup screen
    a_att_pop, b_att_pop = pyautogui.locateCenterOnScreen(l_path + f'{l_fil_att_pop}')      # assign x,y coordinates of file attributes popup
except:                                                                                     # exception excuted if can't find try image
    print("exception executed, can't find file attribute popup. Open it.")
    pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_fil_att}'))                # click on file attributes to get the pop up
    time.sleep(1)                                                                           # pause to allow to open
    a_att_pop, b_att_pop = pyautogui.locateCenterOnScreen(l_path + f'{l_fil_att_pop}')      # assign x,y coordinates of file attributes popup
else:                                                                                       # else excuted if was able to find try image
    print("else statement, was able to find file attribute popup.")                         # X,Y Coordinates written to the variables

lum_file_att()                                                                              # move file attribute to specific location
time.sleep(1) 
data_fexp()                                                                                 # move file explorer to specific location
time.sleep(1) 

pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                                  # move to x,y coordinates of file attributes 
pyautogui.moveRel(xOffset=150, yOffset=18)                                                  # move to "Operator" entry box
pyautogui.click()                                                                           # click in the entry box to become the focus
time.sleep(1)           
pyautogui.hotkey('ctrl', 'a')                                                               # select all hotkey
pyautogui.typewrite(opcred)                                                                 # paste operator entry string from main GUI
time.sleep(1)
print("Entered operator: ", opcred)

pyautogui.moveRel(xOffset=0, yOffset=30)                                                    # move to "Sample" entry box
pyautogui.click()                                                                           # click in the entry box to become the focus
time.sleep(1)           
pyautogui.hotkey('ctrl', 'a')                                                               # select all hotkey 
pyautogui.typewrite("Alignment")                                                            # paste 'Alignment'

pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_cnfg}'))                   # click on configuration tab
time.sleep(3)                                                                               # pause for 2-3 seconds
pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_cnf_100}'))                    # click "Set 1.00 Width" button
time.sleep(2)  
ascntyp, bscntyp = pyautogui.locateCenterOnScreen(l_path + f'{l_scn_type}')                 # locate Alignment Scan Type image
pyautogui.moveTo(x=ascntyp, y=bscntyp)                                                      # move to x,y coordinates image
pyautogui.moveRel(xOffset=-20, yOffset=100)                                                 # move to circle radiobutton
pyautogui.click()                                                                           # click circle radio button
time.sleep(2)

## Do Alignment stuff... Do we need to save an image?
pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))                   # click on main tab
time.sleep(2)    
pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))                      # click on "Start" button
time.sleep(1)    
pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))                       # click on "Stop" button
time.sleep(1)    
pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))                      # click on "Save B" button
time.sleep(1)  

## After alignment is complete, set back to circle.
pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_cnfg}'))                   # click on configuration tab
time.sleep(2)                                                                               # pause for 2-3 seconds 
pyautogui.moveTo(x=ascntyp, y=bscntyp)                                                      # move to x,y coordinates image
pyautogui.moveRel(xOffset=-20, yOffset=100)                                                 # move to circle radiobutton
pyautogui.click()                                                                           # click radio button
time.sleep(1)

# leave off at configuration tab
lum_mini()                                                                                  # minimize Lumedica to move to the next sample
time.sleep(1)

#########################################################################################################################################################
################################################################    KINESIS AUTOTEST SETUP     ##########################################################
#########################################################################################################################################################
#######################################################       SETUP  KINESIS; CONNECT, LOAD, ETC..        ###############################################
#########################################################################################################################################################
#kin_main()
#time.sleep(1)

### Drag log screen down (to be able to enable X when log is full, otherwise X-axis is half covered)
#pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_thorlabs}'))
#print('Found Thorlabs photo.')
#pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_drag}'))
#print('Found Drag photo')
#pyautogui.moveRel(xOffset=0, yOffset=17)
#print('Move down 10')
#pyautogui.dragRel(xOffset=0, yOffset=200, button='left')
#print('Drag it down 150')

### Check and Connect X&Y. 
#while(True):                                                                                # Loop as long as this is false, can't find the no devices image
#    try:                                                                                    # try and locate "Move devices here to access full functionality" on the screen. Neither X nor Y are connected.
#        anodev, bnodev = pyautogui.locateCenterOnScreen(path + f'{k_nodevices}')
#    except TypeError:                                                                       
#        print("Except: 'Move devices here to access full functionality' IS NOT the screen.")
#    else:                                                                                   # else gets executed if it found the try statement.
#        print("Else: 'Move devices here to access full functionality' IS the screen.")
#        pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_conn}'))                 # press connect button

#        while(True):                                                                        # loop until condition in false.
#            try:                                                                            # Try and find image of the check boxes.
#                anoxnoy, bnoxnoy = pyautogui.locateCenterOnScreen(path + f'{k_noxnoyconn}') # Image of X&Y axis unchecked.
#            except TypeError:                                                               # execute until the check boxes popup.
#                print("Except: No image to select X & Y check boxes yet. Press connect again.")
#                pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_conn}'))         # connect button
#                time.sleep(2)

#                while(True):                                                                # loop until condition is false.
#                    try:                                                                    # try and find image of all the boxes checked.
#                        aallcheck, ballcheck=pyautogui.locateCenterOnScreen(path + f'{k_allchecked}') # Image of All checked
#                        print("Try and check to connect to X and Y.")
#                    except TypeError:                                                       # Execute until boxes are checked.
#                        print("Except: Could not check the boxes. Lets click the checkbox again.")
#                        pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_check}'))# check top box
#                        time.sleep(2) 

#                    while(True):                                                            # loop until condition in false, until it can't find the image of YSN
#                        try:                                                                # Try and find image of the serial number.
#                            aysn, bysn=pyautogui.locateCenterOnScreen(path + f'{k_ysn}')    # Loop until the connected button has been clicked.
#                        except:                                                             # Exception executed, click connect until the serial number pops up.
#                            print("Except: Connect popup has not closed. Press 'connect' to close it.")
#                            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_connn}'))# connect
#                            time.sleep(3) 
#                        else:
#                            print("Else: Connect popup closed.")
#                        break
#                    print("X&Y should be connected")
#                    break
#            break
#    break
#time.sleep(2)

#def conn_x_or_y():
#    aXconn, bXconn = pyautogui.locateCenterOnScreen(path + f'{k_xsn}')                      # write XSN X,Y coordinates of image to the variables (if it exists)
#    aYconn, bYconn = pyautogui.locateCenterOnScreen(path + f'{k_ysn}')                      # write YSN X,Y coordinates of image to the variables (if it exists)
#    if aXconn is True and bXconn is True:                                                   # if locating on screen returns a value, then the image is on the screen
### if XSN is true, then that means X was not connected, and from previous checks, we know Y must be connected (or USB issue)
### Check and Connect Y, we already know that 1 is connected, but both are not connected, from previous while loops.
#        try:                                                                                # try and locate the image if x is connected, that would mean we need to connect Y.
#            aXconn, bXconn = pyautogui.locateCenterOnScreen(path + f'{k_xsn}')              # locate SN of X.
#        except TypeError:
#            print("Could not locate the image Kin-XSN.png")
#        else:
#            print("X is connected, so lets connect Y.")
#            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_conn}'))             # click connect button
#            time.sleep(2) 
#            try:                                                                            # if the image of X and Y not connected is true, this will connect them.
#                aNoYconn,bNoYconn = pyautogui.locateCenterOnScreen(path + f'{k_noyconn}')   # Only Y available to connect
#                time.sleep(3)
#            except TypeError:
#                print("Could not locate the image Kin-NoYConn.png. Something else must the issue, Y appears to be connected")
#            else:
#                time.sleep(3)
#                pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_check}'))        # click check top box
#                time.sleep(3) 
#                pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_connn}'))        # click connect button
#                time.sleep(3) 
#                print("Y is connected")
#    elif aYconn is True and bYconn is True:                                                 # means YSN is true, so we connect YSN now  
# ## Check and Connect X
#        try:                                                                                # try and locate this image on the screen of Y is connected.
#            aYconn, bYconn = pyautogui.locateCenterOnScreen(path + f'{k_ysn}')
#        except TypeError:
#            print("Could not locate the image Kin-YSN.png")
#        else:
#            print("Y is connected, let's connext X'")
#            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_conn}'))             # click connect button
#            time.sleep(2) 
#            try:                                                                            # if the image of X and Y not connected is true, this will connect them.
#                aNoXconn,bNoXconn = pyautogui.locateCenterOnScreen(path + f'{k_noxconn}')   # Only X not conn
#                time.sleep(3)
#            except TypeError:
#                print("Could not locate the image Kin-NoXConn.png. Something else must the issue, X appears to be connected")
#            else:
#                time.sleep(3)
#                pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_check}'))        # click the top check box
#                time.sleep(3) 
#                pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_connn}'))        # click connect button
#                print("X is now connected")
#                time.sleep(3) 
#    else:
#        print("Could not locate XSN or YSN on the screen.... Check USB and power")

### If X and Y are connected, the coordinates of the matching screenshot will be written to these assigned variables.
### Double check that X and Y are connected. No while loop b/c we don't want this to loop if its true or false.
#try:                                                                                        # try and locate this image on the screen. X and Y are connected.
#    aXYconn1, bXYconn1 = pyautogui.locateCenterOnScreen(path + f'{k_connxy}')
#except TypeError:
#    print("Could not locate the image Kin-XYConn.png, therefore X or Y is NOT connected, Let's try to connect to one.")
#    conn_x_or_y()
#else:
#    print("XY are connected, check #1.")

#try:                                                                                         # try and locate this image on the screen of Y and X are connected.
#    aYXconn1, bYXconn1 = pyautogui.locateCenterOnScreen(path + f'{k_connyx}')
#except TypeError:
#    print("Could not locate the image Kin-YXConn.png, therefore Y or X is NOT connected. Let's try to connect to one.")
#    conn_x_or_y()
#else:
#    print("YX are connected, check #1.")

### Double check that X and Y are connected. No while loop b/c we don't want this to loop if its true or false.
#try:                                                                                        # try and locate this image on the screen. X and Y are connected.
#    aXYconn2, bXYconn2 = pyautogui.locateCenterOnScreen(path + f'{k_connxy}')
#except TypeError:
#    print("Could not locate the image Kin-XYConn.png, therefore X & Y are NOT connected")
#else:
#    print("XY are connected, check #2.")
#                                                                                            # Double check that Y and X are connected. No while loop b/c we don't want this to loop if its true or false.
#try:                                                                                        # try and locate this image on the screen of Y and X are connected.
#    aYXconn2, bYXconn2 = pyautogui.locateCenterOnScreen(path + f'{k_connyx}')
#except TypeError:
#    print("Could not locate the image Kin-YXConn.png, therefore Y & X are NOT connected")
#else:
#    print("YX are connected, check #2.")

#while(True):                                                                                # loop until condition in false.
#    try:                                                                                    # Try and find image of the serial number.
#        aysn0,bysn0=pyautogui.locateCenterOnScreen(path + f'{k_ysn}')                       # Loop until the connected button has been clicked.
#    except:                                                                                 # Execute clicking connect until the serial number popsup.
#        print("Except: Could not locate the image of Kin-YSN, so let's click connect.")
#        pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_connn}'))                # connect
#        time.sleep(3) 
#    break
#print("X&Y should be connected, check #3")

#fn=''                                                                                       # needed to say " while false"
### Enable Y-axis
#try:                                                                                        # Try: check if enable is on the screen, if it is then execute else
#    aYenh, bYenh = pyautogui.locateCenterOnScreen(path + f'{k_yen_h}')                      # locate and write coordinates to the variables
#except:                                                                                     # Except, if no enable is on the screen, then it is already enabled
#    print("Except: Couldn't find Kin-YEn Home image.") 
#    try:                                                                                    # Try: check if enable is on the screen, if it is then execute else
#        aYennh, bYennh = pyautogui.locateCenterOnScreen(path + f'{k_yen_nh}')               # locate and write coordinates to the variables
#    except:                                                                                 # except executed if no image was found
#        print("Except: Couldn't find Kin-YEn NotHome image. Therefore Y must already be enabled") 
#    else:                                                                                   # else executed if image was found
#        pyautogui.moveTo(x=aYennh, y=bYennh)                                                # move to center of screenshot, near enable
#        pyautogui.moveRel(xOffset=50, yOffset=45)                                           # move down and to the right, to the enable button
#        pyautogui.click()                                                                   # click the enable button
#        print("Else: Y is now enabled")                                                     # if it finds and clicks the Enable button on try, it will print this.
#else:                                                                                       # else executed if image was found
#    pyautogui.moveTo(x=aYenh, y=bYenh)                                                      # move to center of screenshot, near enable
#    pyautogui.moveRel(xOffset=50, yOffset=45)                                               # move down and to the right, to the enable button
#    pyautogui.click()                                                                       # click enable button
#    print("Else: Y is now enabled")                                                         # if it finds and clicks the Enable button on try, it will print this.

### Enable X-axis
#try:                                                                                        # Try: check if enable is on the screen, if it is then execute else
#    aXenh, bXenh = pyautogui.locateCenterOnScreen(path + f'{k_xen_h}')                      # locate and write coordinates to the variables
#except:                                                                                     # Except, if no enable is on the screen, then it is already enabled
#    print("Except: Couldn't find Kin-XEn Home image.") 
#    try:                                                                                    # Try: check if enable is on the screen, if it is then execute else
#        aXennh, bXennh = pyautogui.locateCenterOnScreen(path + f'{k_xen_nh}')               # locate and write coordinates to the variables
#    except:                                                                                 # except executed if no image was found
#        print("Except: Couldn't find Kin-XEn NotHome image. Therefore X must already be enabled") 
#    else:                                                                                   # else executed if image was found
#        pyautogui.moveTo(x=aXennh, y=bXennh)                                                # move to center of screenshot, near enable
#        pyautogui.moveRel(xOffset=50, yOffset=45)                                           # move down and to the right, to the enable button
#        pyautogui.click()                                                                   # click the enable button
#        print("Else: X is now enabled")                                                           # if it finds and clicks the Enable button on try, it will print this.
#else:                                                                                       # else executed if image was found
#    pyautogui.moveTo(x=aXenh, y=bXenh)                                                      # move to center of screenshot, near enable
#    pyautogui.moveRel(xOffset=50, yOffset=45)                                               # move down and to the right, to the enable button
#    pyautogui.click()                                                                       # click the enable button                      # locate and click enable button
#    print("Else: X is now enabled")                                                               # if it finds and clicks the Enable button on try, it will print this.

### Double check if disable button is now visible Y-axis
#try:                                                                                        # Try: check if Disable is on the screen, if it is then execute else
#    aYdish,bYdish = pyautogui.locateCenterOnScreen(path + f'{k_ydish}')                        
#except:                                                                                     # except executed if no image was found
#    pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_yen_h}'))                    # locate and click enable button home
#    pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_yen_nh}'))                   # locate and click enable button not home
#    pyautogui.moveRel(xOffset=50, yOffset=45)                                               # move down and to the right, to the enable button
#    pyautogui.click()                                                                       # click the enable button
#    print("Except: Couldn't find Kin-YDis Home button, need to click enable.") 
#    try:                                                                                    # Try: check if Disable is on the screen, if it is then execute else
#        aYdish,bYdish = pyautogui.locateCenterOnScreen(path + f'{k_ydis_h}')                        
#    except:                                                                                 # except executed if no image was found
#        pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_yen_h}'))                # locate and click enable button home
#        pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_yen_nh}'))               # locate and click enable button not home
#        pyautogui.moveRel(xOffset=50, yOffset=45)                                           # move down and to the right, to the enable button
#        pyautogui.click()                                                                   # click the enable button
#        print("Except: Couldn't find Kin-YDis NotHome button, need to click enable.") 
#    else:
#        print("Else: Found Y-Disable Not Home button. Therefore, Y is enabled")             # if it finds the Disable button on try, it will print this.
#else:
#    print("Else: Found Y-Disable Home button. Therefore, Y is enabled")                     # if it finds the Disable button on try, it will print this.

### Double check if disable button is now visible X-axis
#try:                                                                                        # Try: check if Disable is on the screen, if it is then execute else
#    aXdish,bXdish = pyautogui.locateCenterOnScreen(path + f'{k_xdis_h}')                        
#except:                                                                                     # except executed if no image was found
#    pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_xen_h}'))                    # locate and click enable button home
#    pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_xen_nh}'))                   # locate and click enable button not home
#    print("Except: Couldn't find Kin-XDis Home button, need to click enable.") 
#    try:                                                                                    # Try: check if Disable is on the screen, if it is then execute else
#        aXdish,bXdish = pyautogui.locateCenterOnScreen(path + f'{k_xdis_h}')                        
#    except:                                                                                 # except executed if no image was found
#        pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_xen_h}'))                # locate and click enable button home
#        pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_xen_nh}'))               # locate and click enable button not home
#        print("Except: Couldn't find Kin-XDis NotHome button, need to click enable.") 
#    else:
#        print("Else: Found X-Disable Not Home button. Therefore, X is enabled")             # if it finds the Disable button on try, it will print this.
#else:
#    print("Else: Found X-Disable Home button. Therefore, X is enabled")                     # if it finds the Disable button on try, it will print this.

### After connected close any home, start or test sequences. The image finder gets confused if any are open initially.
#def seq_close_all():
#    try:                                                                                    # try to find test sequence
#        atseqcls0, btseqcls0 = pyautogui.locateCenterOnScreen(path + f'{k_tseq_cls}')         # assign the image of home sequence already loaded with red x
#    except:                                                                                 # except executed if try statement is false, can't find the image
#        print("Exept: Test Sequence was not open.")
#    else:                                                                                   # else executed if try statement is true, found the image.
#        print("Else: Test Sequence was open. Now it is closed.")
#        pyautogui.moveTo(x=atseqcls0, y=btseqcls0)                                            # move to image of home sequence with red x
#        pyautogui.moveRel(xOffset=90, yOffset=0)                                            # move X,Y relative to current position
#        pyautogui.click()                                                                   # click "close" button

#    try:                                                                                    # try to find test sequence
#        ahomcls0, bhomcls0 = pyautogui.locateCenterOnScreen(path + f'{k_home_cls}')         # assign the image of home sequence already loaded with red x
#    except:                                                                                 # except executed if try statement is false, can't find the image
#        print("Exept: Home Sequence was not open.")
#    else:                                                                                   # else executed if try statement is true, found the image.
#        print("Else: Home Sequence was open. Now it is closed.")
#        pyautogui.moveTo(x=ahomcls0, y=bhomcls0)                                            # move to image of home sequence with red x
#        pyautogui.moveRel(xOffset=90, yOffset=0)                                            # move X,Y relative to current position
#        pyautogui.click()                                                                   # click "close" button

#    try:                                                                                    # try to find test sequence
#        astarcls0, bstarcls0 = pyautogui.locateCenterOnScreen(path + f'{k_start_cls}')         # assign the image of home sequence already loaded with red x
#    except:                                                                                 # except executed if try statement is false, can't find the image
#        print("Exept: Start Sequence was not open.")
#    else:                                                                                   # else executed if try statement is true, found the image.
#        print("Else: Start Sequence was open. Now it is closed.")
#        pyautogui.moveTo(x=starcls0, y=bstarcls0)                                           # move to image of home sequence with red x
#        pyautogui.moveRel(xOffset=90, yOffset=0)                                            # move X,Y relative to current position
#        pyautogui.click()                                                                   # click "close" button

#seq_close_all()                                                                             # make sure all sequences are closed

#def seq_home():                                                                             # home function
#    try:                                                                                    # try and assign the image of X is in home pos 0.000000 mm
#        aXzero, bXzero = pyautogui.locateCenterOnScreen(path + f'{k_xzero}')                # assign X,Y coordinates to the image of x at 0.00000 mm
#    except:                                                                                 # exception executed if image does not exist
#        print("Except: X at 0.0000 not found.")
#        try:
#            ahom, bhom = pyautogui.locateCenterOnScreen(path + f'{k_home}')                 # try and assign the image of home sequence already loaded
#        except TypeError:                                                                   # exception executed if image does not exist 
#            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_arrow}'))            # click on "Open" drop down arrow
#            time.sleep(2)                                                                   # pause
#            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_home_dpdn}'))        # click on home sequence from drop down
#            print("Except: Loading Home Sequence.") 
#            time.sleep(2)                                                                   # pause
#            pyautogui.moveRel(xOffset=-90, yOffset=100)                                     # move X,Y relative to current position
#            pyautogui.click()                                                               # click "Run" button
#            print("Except: Pausing to allow to home...")          
#            time.sleep(9)                                                                   # pause 8 seconds to allow to home.
#            print("Except: Closing home sequence")
#            ahomcls, bhomcls = pyautogui.locateCenterOnScreen(path + f'{k_home_cls}')       # assign the image of home sequence already loaded with red x
#            pyautogui.moveTo(x=ahomcls, y=bhomcls)                                          # move to image of home sequence with red x
#            pyautogui.moveRel(xOffset=90, yOffset=0)                                        # move X,Y relative to current position
#            pyautogui.click()                                                               # click "close" button
#        else:                                                                               # else means try image was found (home sequence already loaded)
#            print("Else: Home sequence is already open, lets press Run.")
#            pyautogui.moveTo(x=ahom, y=bhom)                                                # move to image of home sequence
#            pyautogui.moveRel(xOffset=-30, yOffset=100)                                     # move X,Y relative to current position
#            pyautogui.click()                                                               # click "Run" button
#            print("Else: Pausing to allow to home...")          
#            time.sleep(9)                                                                   # pause 8 seconds to allow to home.
#            print("Else: Closing home sequence")
#            ahomcls, bhomcls = pyautogui.locateCenterOnScreen(path + f'{k_home_cls}')       # assign the image of home sequence already loaded with red x
#            pyautogui.moveTo(x=ahomcls, y=bhomcls)                                          # move to image of home sequence with red x
#            pyautogui.moveRel(xOffset=90, yOffset=0)                                        # move X,Y relative to current position
#            pyautogui.click()                                                               # click "close" button
#    else:                                                                                   # else means try image was found (X is already at starting pos 0.000000 mm)
#        print("Else: X is already at 0.000000 mm.")

#    ## if X is already at 0.000000 mm , but Y is not, we will find out here..
#    try:                                                                                    # try and assign the image of Y is in starting pos 0.000000 mm
#        aYzero, bYzero = pyautogui.locateCenterOnScreen(path + f'{k_yzero}')                # if image exists, assign X,Y coordinates to the image of Y at 0.00000 mm
#    except:                                                                                 # exception executed if image does not exist                                               
#        try:
#            ahom, bhom = pyautogui.locateCenterOnScreen(path + f'{k_home}')                 # try and assign the image of home sequence already loaded
#        except TypeError:                                                                   # if no exception, means no home sequence is loaded. This gets executed if image does not exist
#            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_arrow}'))            # click on "Open" drop down arrow
#            time.sleep(2)                                                                   # pause
#            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_home_dpdn}'))        # click on home sequence from drop down
#            print("Except: Loading Home Sequence.") 
#            time.sleep(2)                                                                   # pause
#            pyautogui.moveRel(xOffset=-90, yOffset=100)                                     # move X,Y relative to current position
#            pyautogui.click()                                                               # click "Run" button
#            print("Except: Pausing to allow to home...")          
#            time.sleep(9)                                                                   # pause 8 seconds to allow to home.
#            print("Except: Closing home sequence")
#            ahomcls, bhomcls = pyautogui.locateCenterOnScreen(path + f'{k_home_cls}')       # assign the image of home sequence already loaded with red x
#            pyautogui.moveTo(x=ahomcls, y=bhomcls)                                          # move to image of home sequence with red x
#            pyautogui.moveRel(xOffset=90, yOffset=0)                                        # move X,Y relative to current position
#            pyautogui.click()                                                               # click "close" button
#        else:                                                                               # else means try image was found (home sequence already loaded)
#            print("Else: Home sequence is already open, lets press Run.")
#            pyautogui.moveTo(x=ahom, y=bhom)                                                # move to image of home sequence
#            pyautogui.moveRel(xOffset=-30, yOffset=100)                                     # move X,Y relative to current position
#            pyautogui.click()                                                               # click "Run" button
#            print("Else: Pausing to allow to home...")          
#            time.sleep(9)                                                                   # pause 8 seconds to allow to home.
#            print("Else: Closing home sequence")
#            ahomcls, bhomcls = pyautogui.locateCenterOnScreen(path + f'{k_home_cls}')       # assign the image of home sequence already loaded with red x
#            pyautogui.moveTo(x=ahomcls, y=bhomcls)                                          # move to image of home sequence with red x
#            pyautogui.moveRel(xOffset=90, yOffset=0)                                        # move X,Y relative to current position
#            pyautogui.click()                                                               # click "close" button
#    else:                                                                                   # else means try image was found (Y is already at starting pos 0.000000 mm)
#        print("Else: Y is already at 0.000000 mm")
#    ## upon startup, X and Y can say 0.00000 mm on the screen, but still be somewhere in space. In that case. Check for "Not Homed" image
#    try:                                                                                    # try and assign the image of "Not Homed"
#        anhome, bnhome = pyautogui.locateCenterOnScreen(path + f'{k_not_homed}')            # assign X,Y coordinates to the image of "Not Homed"
#    except TypeError:                                                                       # exception executed if image does not exist
#        print("Except: No image of Not Homed exists")                                       # click "close" button
#    else:                                                                                   # else means not homed image was found
#        print("Else: Device is not homed, lets home it.")
#        axsn, bxsn = pyautogui.locateCenterOnScreen(path + f'{k_xsn}')                      # assign the coordinates of XSN image
#        aysn, bysn = pyautogui.locateCenterOnScreen(path + f'{k_ysn}')                      # assign the coordinates of YSN image
#        pyautogui.moveTo(x=axsn, y=bxsn)                                                    # move to image of xsn
#        pyautogui.moveRel(xOffset=-160, yOffset=105)                                        # move X,Y relative to current position
#        pyautogui.click()                                                                   # click "start" button
#        time.sleep(2)                                                                       # pause
#        pyautogui.moveTo(x=aysn, y=bysn)                                                    # move to image of ysn
#        pyautogui.moveRel(xOffset=-160, yOffset=105)                                        # move X,Y relative to current position
#        pyautogui.click()                                                                   # click "start" button
#        time.sleep(75)                                                                      # pause for home time 1 minute 12 seconds
#        print("Else: Should be homed now.")

#seq_home()

# shouldn't ever need to do this. Using test sequence it should go to start, beginning position everytime.
#def seq_start():                                                                            # start function for Lumedica loops to not have to return to home position
#    try:                                                                                    # try and assign the image of X is in starting pos 132.700000 mm
#        asXstart, bsXstart = pyautogui.locateCenterOnScreen(path + f'{k_xstart}')           # assign X,Y coordinates to the image of x at 132.70000 mm
#    except:                                                                                 # exception executed if image does not exist
#        try:                                                                                # try and assign the image of start sequence already loaded
#            aseqstart, bseqstart = pyautogui.locateCenterOnScreen(path + f'{k_start}')              
#        except TypeError:                                                                   # exception executed if image does not exist 
#            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_arrow}'))            # click on "Open" drop down arrow
#            time.sleep(2)                                                                   # pause
#            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_start_dpdn}'))       # click on start sequence from drop down
#            print("Loading Start Sequence.") 
#            time.sleep(2)                                                                   # pause
#            pyautogui.moveRel(xOffset=-100, yOffset=140)                                    # move X,Y relative to current position
#            pyautogui.click()                                                               # click "Run" button
#            print("Pausing to allow to start...")
#            time.sleep(9)                                                                   # pause 8 seconds to allow to move to start.
#            print("Closing start sequence")
#            aseqstarcls, bseqstarcls = pyautogui.locateCenterOnScreen(path + f'{k_start_cls}')# assign the image of start sequence already loaded with red x
#            pyautogui.moveTo(x=aseqstarcls, y=bseqstarcls)                                  # move to image of start sequence with red x
#            pyautogui.moveRel(xOffset=90, yOffset=0)                                        # move X,Y relative to current position
#            pyautogui.click()                                                               # click "close" button
#        else:                                                                               # else means try image was found start sequence already loaded)
#            pyautogui.moveTo(x=astart, y=bstart)                                            # move to image of start sequence
#            pyautogui.moveRel(xOffset=-100, yOffset=140)                                    # move X,Y relative to current position
#            pyautogui.click()                                                               # click "Run" button
#            print("Else: Pausing to allow to start...")
#            time.sleep(9)                                                                   # pause 8 seconds to allow to move to start.
#            print("Else: Closing start sequence")
#            astarcls, bstarcls = pyautogui.locateCenterOnScreen(path + f'{k_start_cls}')    # assign the image of start sequence already loaded with red x
#            pyautogui.moveTo(x=astarcls, y=starcls)                                         # move to image of start sequence with red x
#            pyautogui.moveRel(xOffset=90, yOffset=0)                                        # move X,Y relative to current position
#            pyautogui.click()   
#    else:                                                                                   # else means try image was found (X is already at starting pos 0.000000 mm)
#        print("Else: X is already at 132.700000 mm")

#    ## if X is already at 132.700000 mm , but Y is not at 25.7, we will find out here..
#    try:                                                                                    # try and assign the image of Y is in starting pos 25.700000 mm
#        asYstart, bsYstart = pyautogui.locateCenterOnScreen(path + f'{k_ystart}')             # assign X,Y coordinates to the image of x at 25.70000 mm
#    except:                                                                                 # exception executed if image does not exist
#        try:                                                                                # try and assign the image of start sequence already loaded
#            astart, bstart = pyautogui.locateCenterOnScreen(path + f'{k_start}')              
#        except TypeError:                                                                   # exception executed if image does not exist 
#            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_arrow}'))            # click on "Open" drop down arrow
#            time.sleep(2)                                                                   # pause
#            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_start_dpdn}'))       # click on start sequence from drop down
#            print("Loading Start Sequence.") 
#            time.sleep(2)                                                                   # pause
#            pyautogui.moveRel(xOffset=-100, yOffset=140)                                    # move X,Y relative to current position
#            pyautogui.click()                                                               # click "Run" button
#            print("Pausing to allow to start...")
#            time.sleep(9)                                                                   # pause 8 seconds to allow to move to start.
#            print("Closing start sequence")
#            astarcls, bstarcls = pyautogui.locateCenterOnScreen(path + f'{k_start_cls}')    # assign the image of start sequence already loaded with red x
#            pyautogui.moveTo(x=astarcls, y=starcls)                                         # move to image of start sequence with red x
#            pyautogui.moveRel(xOffset=90, yOffset=0)                                        # move X,Y relative to current position
#            pyautogui.click()                                                               # click "close" button
#        else:                                                                               # else means try image was found start sequence already loaded)
#            pyautogui.moveTo(x=astart, y=bstart)                                            # move to image of start sequence
#            pyautogui.moveRel(xOffset=-100, yOffset=140)                                    # move X,Y relative to current position
#            pyautogui.click()                                                               # click "Run" button
#            print("Else: Pausing to allow to start...")
#            time.sleep(9)                                                                   # pause 8 seconds to allow to move to start.
#            print("Else: Closing start sequence")
#            astarcls, bstarcls = pyautogui.locateCenterOnScreen(path + f'{k_start_cls}')    # assign the image of start sequence already loaded with red x
#            pyautogui.moveTo(x=astarcls, y=starcls)                                         # move to image of start sequence with red x
#            pyautogui.moveRel(xOffset=90, yOffset=0)                                        # move X,Y relative to current position
#            pyautogui.click()   
#    else:                                                                                   # else means try image was found (X is already at starting pos 0.000000 mm)
#        print("Else: Y is already at 25.700000 mm")

#def seq_test():                                                                                 # check X first because it takes the longest to get to the start position
#    try:                                                                                        # try and assign the image of X is in starting pos 132.700000 mm
#        atXstart, btXstart = pyautogui.locateCenterOnScreen(path + f'{k_xstart}')               # if image exists, assign X,Y coordinates to the image of X at 132.70000 mm
#    except:                                                                                     # exception executed if image does not exist
#        print("Except: image of X at 132.7000 not found.")
#        try: 
#            atxseq, btxseq = pyautogui.locateCenterOnScreen(path + f'{k_testseq}')              # try and assign the image of test sequence already loaded
#        except TypeError:                                                                       # if no exception, means no test sequence is loaded. This gets executed if image does not exist
#            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_arrow}'))                # click on "Open" drop down arrow
#            time.sleep(2)                                                                       # pause
#            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_tseq_dpdn}'))            # click on test sequence from drop down
#            time.sleep(2)                                                                       # pause
#            pyautogui.moveRel(xOffset=-100, yOffset=120)                                        # move X,Y relative to current position
#            pyautogui.click()                                                                   # click "Run" button
#            print("Except: X check, Loading Test Sequence.")  
#            time.sleep(9)                                                                       # pause at least 5-7 seconds to  move to start
#        else:                                                                                   # else means try image was found (test sequence already loaded)
#            pyautogui.moveTo(x=atxseq, y=btxseq)                                                # move to test sequence image
#            pyautogui.moveRel(xOffset=-72, yOffset=120)                                         # move X,Y relative to current position
#            pyautogui.click()                                                                   # click "Run" button
#            print("Else: X check, Test sequence is already open, lets press Run.")
#            time.sleep(9)                                                                       # pause at least 5-7 seconds to move to start
#    else:                                                                                       # else means try image was found (X is already at starting pos 132.700000 mm)
#        print("Else: X-axis already in starting position.")
#        ## Check Y starting position.
#        try:                                                                                        # try and assign the image of Y in starting pos 25.700000 mm
#            atYstart, btYstart = pyautogui.locateCenterOnScreen(path + f'{k_ystart}')               # if image exists, assign X,Y coordinates to the image of Y at 25.70000 mm
#        except:                                                                                     # exception executed if image does not exist
#            print("Except: image of Y at 25.7000 not found")
#            try: 
#                atyseq, btyseq = pyautogui.locateCenterOnScreen(path + f'{k_testseq}')              # try and assign the image of test sequence already loaded
#            except TypeError:                                                                       # if no exception, means no test sequence is loaded. This gets executed if image does not exist
#                pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_arrow}'))                # click on "Open" drop down arrow
#                time.sleep(2)                                                                       # pause
#                pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_tseq_dpdn}'))            # click on test sequence from drop down
#                time.sleep(2)                                                                       # pause
#                pyautogui.moveRel(xOffset=-100, yOffset=120)                                        # move X,Y relative to current position
#                pyautogui.click()                                                                   # click "Run" button
#                print("Except: Y check, starting Test Sequence.") 
#                time.sleep(9)                                                                       # pause at least 5-7 seconds to move to start 
#            else:                                                                                   # else means try image was found (test sequence already loaded)
#                pyautogui.moveTo(x=atyseq, y=btyseq)                                                  # move to test sequence image
#                pyautogui.moveRel(xOffset=-72, yOffset=120)                                         # move X,Y relative to current position
#                pyautogui.click()                                                                   # click "Start" button
#                print("Else: Y check, Test sequence is already open, lets press Run.")
#                time.sleep(9)                                                                       # pause at least 5-7 seconds to move to start
#        else:                                                                                       # else means try image was found (X is already at starting pos 132.700000 mm)                                                                     # if no exception, means no test sequence is loaded. This gets executed if image does not exist
#            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_arrow}'))                # click on "Open" drop down arrow
#            time.sleep(2)                                                                       # pause
#            pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_tseq_dpdn}'))            # click on test sequence from drop down
#            time.sleep(2)                                                                       # pause
#            pyautogui.moveRel(xOffset=-100, yOffset=120)                                        # move X,Y relative to current position
#            pyautogui.click()                                                                   # click "Run" button
#            print("Else - Except: Y check, starting Test Sequence.")  
#            time.sleep(9)                                                                       # pause at least 5-7 seconds to move to start

## If there are less than 25 samples in a set, we need a way to cancel the test sequence and restart the test for the next .
#def cancel_test():
#    try:
#        kin_pop()                                                               # bring popup to foreground
#    except:
#        print("Except: Can't bring popup to the foreground because there is not Kinesis popup.")

#    try: 
#        acancel, bcancel = pyautogui.locateCenterOnScreen(path + f'{k_cancel}') # try and find the resume button
#    except:                                                                     # except executed if no image was found
#        print("Except: No resume button found")
#    else:                                                                       # else executed if image was found
#        pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_cancel}'))   # Press close on the resume popup
#        time.sleep(1)
#        pyautogui.click(pyautogui.locateCenterOnScreen(path + f'{k_stop}'))     # Press stop on the resume popup
#        print("Else: Should be canceling test sequence.")

############################################     DETERMINING # OF LOOPS        ##################################################  
samp_len_25 = 0                                                 # if this is 0 & loop does not get updated by if statement, loop will not execute.
samp_len_50 = 0                                                 # if this is 0 & loop does not get updated by if statement, loop will not execute.
samp_len_75 = 0                                                 # if this is 0 & loop does not get updated by if statement, loop will not execute.
samp_len_100 = 0                                                # if this is 0 & loop does not get updated by if statement, loop will not execute.
samp_len_125 = 0                                                # if this is 0 & loop does not get updated by if statement, loop will not execute.
samp_len = len(samp_arr_raw)
print("Sample Length is: ", samp_len)

if samp_len <= 25:                                                                      # if the array length is less than 25
    print("Sample array length is between 1 and 25 samples.")
    samp_len_25 = samp_len                                                              # Set the numeric sample length to variable samp_len_25 to use for the loop
    print("samp_len_25 is: ", samp_len_25)
elif samp_len > 25 and samp_len <= 50:                                                  # if the array length is between 26 and 50, prob most common
    print("Sample array length is between 26 and 50 samples.")
    samp_len_25 = 25                                                                    # first inner loop
    samp_len_50 = samp_len - 25                                                         # second inner loop
    print("samp_len_25 is: ", samp_len_25, ", samp_len_50 is: ", samp_len_50)
elif samp_len > 50 and samp_len <= 75:                                                  # if the array length is between 51 and 75
    print("Sample array length is between 51 and 75 samples.")
    samp_len_25 = 25                                                                    # first inner loop
    samp_len_50 = 25                                                                    # second inner loop
    samp_len_75 = samp_len - 50                                                         # third inner loop
    print("samp_len_25 is: ", samp_len_25, ", samp_len_50 is: ", samp_len_50)
    print("samp_len_75 is: ", samp_len_75, ". Therefore 2 outer loops.")
elif samp_len > 75 and samp_len <= 100:                                                 # this is for scalability. If the array length is between 76 and 100
    print("Sample array length is between 76 and 100 samples.")
    samp_len_25 = 25                                                                    # first inner loop
    samp_len_50 = 25                                                                    # second inner loop
    samp_len_75 = 25                                                                    # third inner loop
    samp_len_100 = samp_len - 75                                                        # fourth inner loop
    print("samp_len_25 is: ", samp_len_25, ", samp_len_50 is: ", samp_len_50)
    print("samp_len_75 is: ", samp_len_75, ", samp_len_100 is: ", samp_len_100)
elif samp_len > 101 and samp_len <= 125:                                                # this is for scalability. If the array length is between 101 and 125
    print("Sample array length is between 101 and 125 samples.")
    samp_len_25 = 25                                                                    # first inner loop
    samp_len_50 = 25                                                                    # second inner loop
    samp_len_75 = 25                                                                    # third inner loop
    samp_len_100 = 25                                                                   # fourth inner loop
    samp_len_125 = samp_len - 100                                                       # fifth inner loop
    print("samp_len_25 is: ", samp_len_25, ", samp_len_50 is: ", samp_len_50)
    print("samp_len_75 is: ", samp_len_75, ", samp_len_100 is: ", samp_len_100)
    print("samp_len_125 is: ", samp_len_125)
else:
    print("Too many samples, software not configured for this.")

index_015 = 0                                       # count is for the sample index, naming each sample based on the array. Needs to be outside the loop
index_040 = 0                                       # count is for the sample index, naming each sample based on the array. Needs to be outside the loop

###############################################          START  1st   LOOP           ##################################################  
###############################################          START  015   TEST           ##################################################  
###############################################           SAMPLES 1 to 25            ##################################################
#seq_test()                                                                              # start Kinesis test sequence to get Mold 1 in place
full_lum()                                                                              # lumedica full screen
time.sleep(1)                                                                           # pause to full screen
 
pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_cnfg}'))               # click on configuration tab <- need this for the multi test loop
time.sleep(2)  
pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_cnf_015}'))                # click "Set 0.15 Width" button
time.sleep(1)  

for len25_015 in range(samp_len_25):                                                    # will loop from 0 to samp_len_25
    print("Testing the 015 for loop of len25.", len25_015)
    print("Index 015 test: ", samp_arr_raw[index_015])
    time.sleep(1)
    
    ############################################    LUMEDICA Samples 1 through 2nd to last
    if (len25_015 + 1) < samp_len_25:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_015]) + " 015")                # SAMPLE --> "MOLD" + samp[] + " 015"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_015]) + " 015")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1)     
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")
    
    ############################################    KINESIS NEXT SAMPLE 
    #if (len25_015 + 1) < samp_len_25:
    #    kin_pop()                                                                           # Kinesis popup to the foreground
    #    try: 
    #        ares, bres = pyautogui.locateCenterOnScreen(path + f'{k_resume}')               # try and find the resume button
    #    except:                                                                             # except executed if no image was found
    #        print("Except: No resume button found")
    #    else:                                                                               # else executed if image was found
    #        pyautogui.moveTo(x=ares, y=bres)
    #        pyautogui.click()
    #        pyautogui.moveTo(path + f'{k_thorlabs}')                                        # move mouse out of the way
    #        print("Else: Should be resuming kinesis to move to next sample")
    #        if len25_015 == 4 or len25_015 == 9 or len25_015 == 14 or len25_015 == 19:
    #            print("last sample on the line, 5 second pause to move ", len25_015)
    #            time.sleep(5)
    #elif (len25_015 + 1) == samp_len_25:
    #    print("Elif: Done with loop, no need to hit resume on the last sample.")            # can add, lum_save, cancel_test, and seq_test here.
    #else:
    #    print("Else: This shouldnt happen ever.")
    index_015 +=1                                                                           # Needs to be before the last sample tested on Lumedica

    ############################################    LUMEDICA last sample
    if (len25_015 + 1) == samp_len_25:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("IF: Last sample, measure Lumedica sample last, since we end with Kinesis over the last sample.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_015]) + " 015")                # SAMPLE --> "MOLD" + samp[] + " 015"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_015]) + " 015")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1)       
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")

#cancel_test()                                                                              # cancel Kinesis test sequence if there are less than 25 samples.

###############################################          START  040   TEST        ##################################################  
###############################################           SAMPLES 1 to 25         ##################################################
#seq_test()                                                                             # Start Kinesis sequence to get sample in position 1
full_lum()                                                                              # Bring Lumedica to full screen
pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_cnfg}'))               # Lumedica click on configuration tab
time.sleep(2)  
pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_cnf_040}'))                # click "Set 0.40 Width" button
time.sleep(1) 

for len25_040 in range(samp_len_25):                                                    # will loop from 0 to samp_len_25
    print("Testing the 040 for loop of len25.", len25_040)
    print("Index 040 test: ", samp_arr_raw[index_040])
    time.sleep(1)
    
    ############################################    LUMEDICA Samples 1 through 2nd to last
    if (len25_040 + 1) < samp_len_25:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_040]) + " 040")                # SAMPLE --> "MOLD" + samp[] + " 040"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_040]) + " 040")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1)     
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")

    ############################################    KINESIS
    #if (len25_040 + 1) < samp_len_25:
    #    kin_pop()                                                                           # bring popup to foreground
    #    try: 
    #        ares, bres = pyautogui.locateCenterOnScreen(path + f'{k_resume}')               # try and find the resume button
    #    except:                                                                             # except executed if no image was found
    #        print("Except: No resume button found")
    #    else:                                                                               # else executed if image was found
    #        pyautogui.moveTo(x=ares, y=bres)
    #        pyautogui.click()
    #        pyautogui.moveTo(path + f'{k_thorlabs}')                                        # move mouse out of the way
    #        print("Else: Should be resuming kinesis to move to next sample")
    #        if len25_040 == 4 or len25_040 == 9 or len25_040 == 14 or len25_040 == 19:
    #            print("last sample on the line, 5 second pause to move ", len25_040)
    #            time.sleep(5)
    #elif (len25_040 + 1) == samp_len_25:
    #    print("Elif: Done with loop, no need to hit resume on the last sample.")            # can add, lum_save, cancel_test, and seq_test here.
    #else:
    #    print("Else: This shouldnt happen ever.")
    index_040 +=1

    ############################################    LUMEDICA last sample
    if (len25_040 + 1) == samp_len_25:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_040]) + " 040")                # SAMPLE --> "MOLD" + samp[] + " 040"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_040]) + " 040")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1)   
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")

lum_save()                                                                                  # save lumedica data after 015 and 040 finish
#cancel_test()                                                                               # need this incase there are less than 25 samples.
print(" ##################################        END  LOOP # 1      ########################################## ")

if samp_len > 25:
    msg_load_more = tk.messagebox.askquestion('Load Next Set', 'Please load the next set of samples. Press OK when ready to proceed..', icon='info', type='ok')
    if msg_load_more == 'ok':
        print("Loading next sample set...")
        #seq_test()                                                                                  # start Kinesis test sequence to get Mold 1 in place
        full_lum()                                                                                  # lumedica full screen
        time.sleep(1)                                                                               # pause to full screen
 
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_cnfg}'))                   # click on configuration tab <- need this for the multi test loop
        time.sleep(2)  
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_cnf_015}'))                    # click "Set 0.15 Width" button
        time.sleep(1)  
else:
    print("Else, sample set length not greater than 25.")

###############################################          START  2nd   LOOP           ##################################################   
###############################################          START  015   TEST           ##################################################  
###############################################          SAMPLES 26 to 50            ##################################################
for len50_015 in range(samp_len_50):                                                        # will loop from 0 to samp_len_50
    print("Testing the 015 for loop of len50.", len50_015)
    print("Index 015 test: ", samp_arr_raw[index_015])
    time.sleep(1)
    
    ############################################    LUMEDICA Samples 1 through 2nd to last
    if (len50_015 + 1) < samp_len_50:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_015]) + " 015")                # SAMPLE --> "MOLD" + samp[] + " 015"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_015]) + " 015")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button    
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")
    
    #############################################    KINESIS NEXT SAMPLE 
    #if (len50_015 + 1) < samp_len_50:
    #    kin_pop()                                                                           # bring popup to foreground
    #    try: 
    #        ares, bres = pyautogui.locateCenterOnScreen(path + f'{k_resume}')               # try and find the resume button
    #    except:                                                                             # except executed if no image was found
    #        print("Except: No resume button found")
    #    else:                                                                               # else executed if image was found
    #        pyautogui.moveTo(x=ares, y=bres)
    #        pyautogui.click()
    #        pyautogui.moveTo(path + f'{k_thorlabs}')                                        # move mouse out of the way
    #        print("Else: Should be resuming kinesis to move to next sample")
    #        if len50_015 == 4 or len50_015 == 9 or len50_015 == 14 or len50_015 == 19:
    #            print("last sample on the line, 5 second pause to move ", len50_015)
    #            time.sleep(5)
    #elif (len50_015 + 1) == samp_len_50:
    #    print("Elif: Done with loop, no need to hit resume on the last sample.")            # can add, lum_save, cancel_test, and seq_test here.
    #else:
    #    print("Else: This shouldnt happen ever.")
    index_015 +=1                                                                           # Needs to be before the last sample tested on Lumedica

    ############################################    LUMEDICA last sample
    if (len50_015 + 1) == samp_len_50:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("IF: Last sample, measure Lumedica sample last, since we end with Kinesis over the last sample.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_015]) + " 015")                # SAMPLE --> "MOLD" + samp[] + " 015"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_015]) + " 015")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1) 
        lum_mini()                                                                          # minimize lumedica
        time.sleep(1)      
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")
 
if samp_len > 25:
    #cancel_test()                                                                           # cancel Kinesis test sequence if there are less than 25 samples.
    #seq_test()                                                                              # Start Kinesis sequence to get sample in position 1
    full_lum()                                                                              # Bring Lumedica to full screen
    pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_cnfg}'))               # Lumedica click on configuration tab
    time.sleep(2)  
    pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_cnf_040}'))                # click "Set 0.40 Width" button
    time.sleep(1) 
else:
    print("Else, less than or equal to 25 samples.")

###############################################          START  040   TEST           ##################################################  
###############################################          SAMPLES 26 to 50            ##################################################
for len50_040 in range(samp_len_50):                                                        # will loop from 0 to samp_len_25
    print("Testing the 040 for loop of len25.", len50_040)
    print("Index 040 test: ", samp_arr_raw[index_040])
    time.sleep(1)
    
    ############################################    LUMEDICA Samples 1 through 2nd to last
    if (len50_040 + 1) < samp_len_50:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_040]) + " 040")                # SAMPLE --> "MOLD" + samp[] + " 040"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_040]) + " 040")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1) 
        lum_mini()                                                                          # minimize lumedica
        time.sleep(1)      
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")
 
    ############################################    KINESIS NEXT SAMPLE    
    #if (len50_040 + 1) < samp_len_50:
    #    kin_pop()                                                                           # bring popup to foreground
    #    try: 
    #        ares, bres = pyautogui.locateCenterOnScreen(path + f'{k_resume}')               # try and find the resume button
    #    except:                                                                             # except executed if no image was found
    #        print("Except: No resume button found")
    #    else:                                                                               # else executed if image was found
    #        pyautogui.moveTo(x=ares, y=bres)
    #        pyautogui.click()
    #        pyautogui.moveTo(path + f'{k_thorlabs}')                                        # move mouse out of the way
    #        print("Else: Should be resuming kinesis to move to next sample")
    #        if len50_040 == 4 or len50_040 == 9 or len50_040 == 14 or len50_040 == 19:
    #            print("last sample on the line, 5 second pause to move ", len50_040)
    #            time.sleep(5)
    #elif (len50_040 + 1) == samp_len_50:
    #    print("Elif: Done with loop, no need to hit resume on the last sample.")            # can add, lum_save, cancel_test, and seq_test here.
    #else:
    #    print("Else: This shouldnt happen ever.")
    index_040 +=1

    ############################################    LUMEDICA last sample
    if (len50_040 + 1) == samp_len_50:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_040]) + " 040")                # SAMPLE --> "MOLD" + samp[] + " 040"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_040]) + " 040")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1) 
        lum_mini()                                                                          # minimize lumedica
        time.sleep(1)      
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")

if samp_len > 25:
    #lum_save()                                                                                  # save lumedica data after 015 and 040 finish
    #cancel_test()                                                                               # need this incase there are less than 25 samples.
    print(" ##################################        END  LOOP # 2      ########################################## ")
else:
    print("Else, skip loop 2. Less than or equal to 25 samples.")

if samp_len > 50:
    msg_load_more = tk.messagebox.askquestion('Load Next Set', 'Please load the next set of samples. Press OK when ready to proceed..', icon='info', type='ok')
    if msg_load_more == 'ok':
        print("Loading next sample set...")
        #seq_test()                                                                                  # start Kinesis test sequence to get Mold 1 in place
        full_lum()                                                                                  # lumedica full screen
        time.sleep(1)                                                                               # pause to full screen
 
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_cnfg}'))                   # click on configuration tab <- need this for the multi test loop
        time.sleep(2)  
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_cnf_015}'))                    # click "Set 0.15 Width" button
        time.sleep(1)  
    else:
        print("No else.")
else:
    print("Else, sample set length not greater than 50.")

###############################################          START  3rd   LOOP           ##################################################   
###############################################          START  015   TEST           ##################################################  
###############################################          SAMPLES 51 to 75            ##################################################
for len75_015 in range(samp_len_75):                                                        # will loop from 0 to samp_len_75
    print("Testing the 015 for loop of len75.", len75_015)
    print("Index 015 test: ", samp_arr_raw[index_015])
    time.sleep(1)
    
    ############################################    LUMEDICA Samples 1 through 2nd to last
    if (len75_015 + 1) < samp_len_75:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_015]) + " 015")                # SAMPLE --> "MOLD" + samp[] + " 015"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_015]) + " 015")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button    
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")
    
    ############################################    KINESIS NEXT SAMPLE 
    #if (len75_015 + 1) < samp_len_75:
    #    kin_pop()                                                                           # bring popup to foreground
    #    try: 
    #        ares, bres = pyautogui.locateCenterOnScreen(path + f'{k_resume}')               # try and find the resume button
    #    except:                                                                             # except executed if no image was found
    #        print("Except: No resume button found")
    #    else:                                                                               # else executed if image was found
    #        pyautogui.moveTo(x=ares, y=bres)
    #        pyautogui.click()
    #        pyautogui.moveTo(path + f'{k_thorlabs}')                                        # move mouse out of the way
    #        print("Else: Should be resuming kinesis to move to next sample")
    #        if len75_015 == 4 or len75_015 == 9 or len75_015 == 14 or len75_015 == 19:
    #            print("last sample on the line, 5 second pause to move ", len75_015)
    #            time.sleep(5)
    #elif (len75_015 + 1) == samp_len_75:
    #    print("Elif: Done with loop, no need to hit resume on the last sample.")                  # can add, lum_save, cancel_test, and seq_test here.
    #else:
    #    print("Else: This shouldnt happen ever.")
    index_015 +=1                                                                       # Needs to be before the last sample tested on Lumedica

    ############################################    LUMEDICA last sample
    if (len75_015 + 1) == samp_len_75:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("IF: Last sample, measure Lumedica sample last, since we end with Kinesis over the last sample.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_015]) + " 015")                # SAMPLE --> "MOLD" + samp[] + " 015"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_015]) + " 015")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1) 
        lum_mini()                                                                          # minimize lumedica
        time.sleep(1)      
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")

if samp_len > 50:
    #cancel_test()                                                                           # cancel Kinesis test sequence if there are less than 25 samples.
    #seq_test()                                                                              # Start Kinesis sequence to get sample in position 1
    full_lum()                                                                              # Bring Lumedica to full screen
    pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_cnfg}'))               # Lumedica click on configuration tab
    time.sleep(2)  
    pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_cnf_040}'))                # click "Set 0.40 Width" button
    time.sleep(1) 
else:
    print("Else, less than or equal to 50 samples.")
    
###############################################          START  040   TEST           ##################################################  
###############################################          SAMPLES 51 to 75            ##################################################
for len75_040 in range(samp_len_75):                                                        # will loop from 0 to samp_len_75
    print("Testing the 040 for loop of len75.", len75_040)
    print("Index 040 test: ", samp_arr_raw[index_040])
    time.sleep(1)
    
    ############################################    LUMEDICA Samples 1 through 2nd to last
    if (len75_040 + 1) < samp_len_75:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_040]) + " 040")                # SAMPLE --> "MOLD" + samp[] + " 040"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_040]) + " 040")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1) 
        lum_mini()                                                                          # minimize lumedica
        time.sleep(1)      
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")
    
    ############################################    KINESIS NEXT SAMPLE
    #if (len75_040 + 1) < samp_len_75:
    #    kin_pop()                                                                           # bring popup to foreground
    #    try: 
    #        ares, bres = pyautogui.locateCenterOnScreen(path + f'{k_resume}')               # try and find the resume button
    #    except:                                                                             # except executed if no image was found
    #        print("Except: No resume button found")
    #    else:                                                                               # else executed if image was found
    #        pyautogui.moveTo(x=ares, y=bres)
    #        pyautogui.click()
    #        pyautogui.moveTo(path + f'{k_thorlabs}')                                        # move mouse out of the way
    #        print("Else: Should be resuming kinesis to move to next sample")
    #        if len75_040 == 4 or len75_040 == 9 or len75_040 == 14 or len75_040 == 19:
    #            print("last sample on the line, 5 second pause to move ", len75_040)
    #            time.sleep(5)
    #elif (len75_040 + 1) == samp_len_75:
    #    print("Elif: Done with loop, no need to hit resume on the last sample.")            # can add, lum_save, cancel_test, and seq_test here.
    #else:
    #    print("Else: This shouldnt happen ever.")
    index_040 +=1

    ############################################    LUMEDICA last sample
    if (len75_040 + 1) == samp_len_75:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_040]) + " 040")                # SAMPLE --> "MOLD" + samp[] + " 040"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_040]) + " 040")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1) 
        lum_mini()                                                                          # minimize lumedica
        time.sleep(1)      
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")

if samp_len > 50:
    lum_save()                                                                              # save lumedica data after 015 and 040 finish
    #cancel_test()                                                                           # need this incase there are less than 25 samples.
    print(" ##################################        END  LOOP # 3      ########################################## ")
else:
    print("Else, skip loop 3. Less than or equal to 50 samples.")

if samp_len > 75:
    msg_load_more = tk.messagebox.askquestion('Load Next Set', 'Please load the next set of samples. Press OK when ready to proceed..', icon='info', type='ok')
    if msg_load_more == 'ok':
        print("Loading next sample set...")
        #seq_test()                                                                                  # start Kinesis test sequence to get Mold 1 in place
        full_lum()                                                                                  # lumedica full screen
        time.sleep(1)                                                                               # pause to full screen
 
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_cnfg}'))                   # click on configuration tab <- need this for the multi test loop
        time.sleep(2)  
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_cnf_015}'))                    # click "Set 0.15 Width" button
        time.sleep(1)  
    else:
        print("No else.")
else:
    print("Else, sample set length not greater than 75.")

###############################################          START  4th   LOOP           ##################################################   
###############################################          START  015   TEST           ##################################################  
###############################################         SAMPLES 76 to 100            ##################################################
for len100_015 in range(samp_len_100):                                                    # will loop from 0 to samp_len_100
    print("Testing the 015 for loop of len100.", len100_015)
    print("Index 015 test: ", samp_arr_raw[index_015])
    time.sleep(1)
    
    ############################################    LUMEDICA Samples 1 through 2nd to last
    if (len100_015 + 1) < samp_len_100:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_015]) + " 015")                # SAMPLE --> "MOLD" + samp[] + " 015"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_015]) + " 015")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button    
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")
    
    ############################################    KINESIS NEXT SAMPLE 
    #if (len100_015 + 1) < samp_len_100:
    #    kin_pop()                                                                           # bring popup to foreground
    #    try: 
    #        ares, bres = pyautogui.locateCenterOnScreen(path + f'{k_resume}')               # try and find the resume button
    #    except:                                                                             # except executed if no image was found
    #        print("Except: No resume button found")
    #    else:                                                                               # else executed if image was found
    #        pyautogui.moveTo(x=ares, y=bres)
    #        pyautogui.click()
    #        pyautogui.moveTo(path + f'{k_thorlabs}')                                        # move mouse out of the way
    #        print("Else: Should be resuming kinesis to move to next sample")
    #        if len100_015 == 4 or len100_015 == 9 or len100_015 == 14 or len100_015 == 19:
    #            print("last sample on the line, 5 second pause to move ", len100_015)
    #            time.sleep(5)
    #elif (len100_015 + 1) == samp_len_100:
    #    print("Elif: Done with loop, no need to hit resume on the last sample.")            # can add, lum_save, cancel_test, and seq_test here.
    #else:
    #    print("Else: This shouldnt happen ever.")
    index_015 +=1                                                                           # Needs to be before the last sample tested on Lumedica

    ############################################    LUMEDICA last sample
    if (len100_015 + 1) == samp_len_100:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("IF: Last sample, measure Lumedica sample last, since we end with Kinesis over the last sample.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_015]) + " 015")                # SAMPLE --> "MOLD" + samp[] + " 015"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_015]) + " 015")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1) 
        lum_mini()                                                                          # minimize lumedica
        time.sleep(1)      
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")
                                                                                            # cancel Kinesis test sequence if there are less than 25 samples.
if samp_len > 75:
    #cancel_test()                                                                          # cancel Kinesis test sequence if there are less than 25 samples.
    #seq_test()                                                                             # Start Kinesis sequence to get sample in position 1
    full_lum()                                                                              # Bring Lumedica to full screen
    pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_cnfg}'))               # Lumedica click on configuration tab
    time.sleep(2)  
    pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_cnf_040}'))                # click "Set 0.40 Width" button
    time.sleep(1) 
else:
    print("Else, less than or equal to 75 samples.")
    
###############################################          START  040   TEST           ##################################################  
###############################################          SAMPLES 76 to 100           ##################################################
for len100_040 in range(samp_len_100):                                                    # will loop from 0 to samp_len_100
    print("Testing the 040 for loop of len100.", len100_040)
    print("Index 040 test: ", samp_arr_raw[index_040])
    time.sleep(1)
    
    ############################################    LUMEDICA Samples 1 through 2nd to last
    if (len100_040 + 1) < samp_len_100:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_040]) + " 040")                # SAMPLE --> "MOLD" + samp[] + " 040"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_040]) + " 040")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1) 
        lum_mini()                                                                          # minimize lumedica
        time.sleep(1)      
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")
    
    ############################################    KINESIS NEXT SAMPLE
    #if (len100_040 + 1) < samp_len_100:
    #    kin_pop()                                                                           # bring popup to foreground
    #    try: 
    #        ares, bres = pyautogui.locateCenterOnScreen(path + f'{k_resume}')               # try and find the resume button
    #    except:                                                                             # except executed if no image was found
    #        print("Except: No resume button found")
    #    else:                                                                               # else executed if image was found
    #        pyautogui.moveTo(x=ares, y=bres)
    #        pyautogui.click()
    #        pyautogui.moveTo(path + f'{k_thorlabs}')                                        # move mouse out of the way
    #        print("Else: Should be resuming kinesis to move to next sample")
    #        if len100_040 == 4 or len100_040 == 9 or len100_040 == 14 or len100_040 == 19:
    #            print("last sample on the line, 5 second pause to move ", len100_040)
    #            time.sleep(5)
    #elif (len100_040 + 1) == samp_len_100:
    #    print("Elif: Done with loop, no need to hit resume on the last sample.")           # can add, lum_save, cancel_test, and seq_test here.
    #else:
    #    print("Else: This shouldnt happen ever.")
    index_040 +=1

    ############################################    LUMEDICA last sample
    if (len100_040 + 1) == samp_len_100:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_040]) + " 040")                # SAMPLE --> "MOLD" + samp[] + " 040"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_040]) + " 040")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1) 
        lum_mini()                                                                          # minimize lumedica
        time.sleep(1)      
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")

if samp_len > 75:
    lum_save()                                                                              # save lumedica data after 015 and 040 finish
    #cancel_test()                                                                           # need this incase there are less than 25 samples.
    print(" ##################################        END  LOOP # 4      ########################################## ")
else:
    print("Else, skip loop 4. Less than or equal to 75 samples.")

if samp_len > 100:
    msg_load_more = tk.messagebox.askquestion('Load Next Set', 'Please load the next set of samples. Press OK when ready to proceed..', icon='info', type='ok')
    if msg_load_more == 'ok':
        print("Loading next sample set...")
        #seq_test()                                                                          # start Kinesis test sequence to get Mold 1 in place
        full_lum()                                                                          # lumedica full screen
        time.sleep(1)                                                                       # pause to full screen
 
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_cnfg}'))           # click on configuration tab <- need this for the multi test loop
        time.sleep(2)  
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_cnf_015}'))            # click "Set 0.15 Width" button
        time.sleep(1)  
    else:
        print("No else.")
else:
    print("Else, sample set length not greater than 100.")

###############################################          START  5th   LOOP           ##################################################   
###############################################          START  015   TEST           ##################################################  
###############################################         SAMPLES 101 to 125           ##################################################
for len125_015 in range(samp_len_125):                                                  # will loop from 0 to samp_len_125
    print("Testing the 015 for loop of len125.", len125_015)
    print("Index 015 test: ", samp_arr_raw[index_015])
    time.sleep(1)
    
    ############################################    LUMEDICA Samples 1 through 2nd to last
    if (len125_015 + 1) < samp_len_125:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_015]) + " 015")                # SAMPLE --> "MOLD" + samp[] + " 015"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_015]) + " 015")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button    
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")
    
    ############################################    KINESIS NEXT SAMPLE 
    #if (len125_015 + 1) < samp_len_125:
    #    kin_pop()                                                                           # bring popup to foreground
    #    try: 
    #        ares, bres = pyautogui.locateCenterOnScreen(path + f'{k_resume}')               # try and find the resume button
    #    except:                                                                             # except executed if no image was found
    #        print("Except: No resume button found")
    #    else:                                                                               # else executed if image was found
    #        pyautogui.moveTo(x=ares, y=bres)
    #        pyautogui.click()
    #        pyautogui.moveTo(path + f'{k_thorlabs}')                                        # move mouse out of the way
    #        print("Else: Should be resuming kinesis to move to next sample")
    #        if len125_015 == 4 or len125_015 == 9 or len125_015 == 14 or len125_015 == 19:
    #            print("last sample on the line, 5 second pause to move ", len125_015)
    #            time.sleep(5)
    #elif (len125_015 + 1) == samp_len_125:
    #    print("Elif: Done with loop, no need to hit resume on the last sample.")            # can add, lum_save, cancel_test, and seq_test here.
    #else:
    #    print("Else: This shouldnt happen ever.")
    index_015 +=1                                                                           # Needs to be before the last sample tested on Lumedica

    ############################################    LUMEDICA last sample
    if (len125_015 + 1) == samp_len_125:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("IF: Last sample, measure Lumedica sample last, since we end with Kinesis over the last sample.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_015]) + " 015")                # SAMPLE --> "MOLD" + samp[] + " 015"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_015]) + " 015")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1) 
        lum_mini()                                                                          # minimize lumedica
        time.sleep(1)      
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")

if samp_len > 100:
    #cancel_test()                                                                           # cancel Kinesis test sequence if there are less than 25 samples.
    #seq_test()                                                                              # Start Kinesis sequence to get sample in position 1
    full_lum()                                                                              # Bring Lumedica to full screen
    pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_cnfg}'))               # Lumedica click on configuration tab
    time.sleep(2)  
    pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_cnf_040}'))                # click "Set 0.40 Width" button
    time.sleep(1) 
else:
    print("Else, less than or equal to 100 samples.")
    
###############################################          START  040   TEST           ##################################################  
###############################################         SAMPLES 101 to 125           ##################################################
for len125_040 in range(samp_len_125):                                                  # will loop from 0 to samp_len_125
    print("Testing the 040 for loop of len125.", len125_040)
    print("Index 040 test: ", samp_arr_raw[index_040])
    time.sleep(1)
    
    ############################################    LUMEDICA Samples 1 through 2nd to last
    if (len125_040 + 1) < samp_len_125:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_040]) + " 040")                # SAMPLE --> "MOLD" + samp[] + " 040"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_040]) + " 040")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1) 
        lum_mini()                                                                          # minimize lumedica
        time.sleep(1)      
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")
    
    ############################################    KINESIS NEXT SAMPLE
    #if (len125_040 + 1) < samp_len_125:
    #    kin_pop()                                                                           # bring popup to foreground
    #    try: 
    #        ares, bres = pyautogui.locateCenterOnScreen(path + f'{k_resume}')               # try and find the resume button
    #    except:                                                                             # except executed if no image was found
    #        print("Except: No resume button found")
    #    else:                                                                               # else executed if image was found
    #        pyautogui.moveTo(x=ares, y=bres)
    #        pyautogui.click()
    #        pyautogui.moveTo(path + f'{k_thorlabs}')                                        # move mouse out of the way
    #        print("Else: Should be resuming kinesis to move to next sample")
    #        if len125_040 == 4 or len125_040 == 9 or len125_040 == 14 or len125_040 == 19:
    #            print("last sample on the line, 5 second pause to move ", len125_040)
    #            time.sleep(5)
    #elif (len125_040 + 1) == samp_len_125:
    #    print("Elif: Done with loop, no need to hit resume on the last sample.")                  # can add, lum_save, cancel_test, and seq_test here.
    #else:
    #    print("Else: This shouldnt happen ever.")
    index_040 +=1

    ############################################    LUMEDICA last sample
    if (len125_040 + 1) == samp_len_125:
        full_lum()                                                                          # maximize Lumedica
        time.sleep(1)
        print("Measure Lumedica sample first, since we initially start with Kinesis in place.")
        pyautogui.moveTo(x=a_att_pop, y=b_att_pop)                                          # move to x,y coordinates of file attributes 
        pyautogui.moveRel(xOffset=150, yOffset=48)                                          # move to "Sample" entry box
        pyautogui.click()                                                                   # click in the entry box to become the focus
        time.sleep(1)           
        pyautogui.hotkey('ctrl', 'a')                                                       # select all hotkey
        pyautogui.typewrite("MOLD " + str(samp_arr_raw[index_040]) + " 040")                # SAMPLE --> "MOLD" + samp[] + " 040"
        time.sleep(1)
        print("Entered sample number: MOLD " + str(samp_arr_raw[index_040]) + " 040")

        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_tab_main}'))           # click on main tab
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_start}'))              # click on "Start" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_stop}'))               # click on "Stop" button
        time.sleep(1)    
        pyautogui.click(pyautogui.locateCenterOnScreen(l_path + f'{l_saveB}'))              # click on "Save B" button
        time.sleep(1) 
        lum_mini()                                                                          # minimize lumedica
        time.sleep(1)      
        lum_mini()                                                                          # minimize lumedica or left justify?
    else:
        print("  ")

if samp_len > 100:
    lum_save()                                                                              # save lumedica data after 015 and 040 finish
    #cancel_test()                                                                           # need this incase there are less than 25 samples.
    print(" ##################################        END  LOOP # 5      ########################################## ")
else:
    print("Else, skip loop 5. Less than or equal to 100 samples.")

if samp_len > 125:
    msg_too_much = tk.messagebox.askquestion('WARNING', 'SOFTWARE NOT CONFIGURED FOR >125 SAMPLES', icon='warning', type='ok')
    if msg_too_much == 'ok':
        print("Too many samples")
    else:
        print("No else.")
else:
    print("Else, sample set length not greater than 125.")

#seq_close_all()                                                                         # make sure all sequences are closed
#seq_home()                                                                              # Return XY stage to home before closing.

msg_box_retest = tk.messagebox.askquestion('Edit Samples', 'Do you need to retest any samples manually?', icon='question', type='yesno')
if msg_box_retest == 'yes':
    print("Create a manual mode that doesn't close the app")
    msg_box_ok = tk.messagebox.askquestion('Manual Mode', 'Click OK when finished testing manually', icon='info', type='okcancel')
    if msg_box_ok == 'ok':
        print("Ok was selected, operator finished manually testing samples.")
    else:
        print("Cancel was selected.")
else:
    print("No was selected, no samples need to be retested manually")

msg_box_newtest = tk.messagebox.askquestion('New Work Order', 'Would you like to run another work order?', icon='question', type='yesno')
if msg_box_newtest == 'yes':
    print("Start New Work order")
    # Have operator enter new info on the main window.
    # is there a way to reinitialize a GUI and clear all info??
    exit()                                                  # Exit out of this class. Go back to Main Window GUI.
else:
    print("The test has ended, closing Lumedica and Kinesis.")
    #os.system("TaskKill /F /IM Thorlabs.MotionControl.Kinesis.exe")                       # close Kinesis
    os.system("TaskKill /F /IM OctEngine.exe")                                            # close Lumedica
    exit()
