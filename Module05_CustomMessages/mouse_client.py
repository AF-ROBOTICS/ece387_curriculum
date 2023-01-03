#!/usr/bin/env python3

#Col Brian Neff
#ROS Enabled mouse client 
#Activates when mouse wheel is scrolled up and 
#Deactivates when mouse wheel is scrolled down 
#last modified 2 Jan 2023
#mouse_client.py

import rospy
import pyautogui
import sys
import time
import os
from pynput.mouse import Listener

#Initialize global variable that will keep track of mouse button status
global activate
activate = False


#get dimensions of screen so that we can scale for (-1,1) in both x and y
xDim,yDim = pyautogui.size()


def on_move(x, y):
    #We need to establish the use of the global variable for button activation
    global activate
    

    if(activate == False):
        messageString = "No movement sent, activate cursor first by scrolling down on the mouse wheel"
        print(messageString, end='')
        # overwrite same line
        print('\b' *len(messageString), end='', flush=True)
    else:
        xScale = ((x/(xDim/2))-1)
        yScale = -((y/(yDim/2))-1)
        xFormat = "{:+.3f}".format(xScale)
        yFormat = "{:+.3f}".format(yScale)
        # create 19 byte message with x,y coordinates embedded
        positionStr = 'X: ' + str(xFormat) + ' Y: ' + str(yFormat) + "                                                           "
        print(positionStr, end='')
        # overwrite same line
        print('\b' *len(positionStr), end='', flush=True)


#Currently I'm not doing anything with the button click.
#Eventually we could add additional modes if we wanted to.
def on_click(x, y, button, pressed):
    pass


def on_scroll(x, y, dx, dy):
    global activate
    if dy == 1:
    #     print("Activating")
        os.system("clear")
        print("Welcome to the mouse controller!\n\n")
        print("In order to ACTIVATE the controller scroll down on the mouse wheel.\n\n")
        print("In order to DEACTIVATE the controller scroll up on the mouse wheel.\n\n") 
        print("To close the program, left-click on the terminal window and type ctrl-c.\n\n")
        activate = False
    if dy == -1:
        # print("Deactivating")
        activate = True

def myhook():
    print("Shutdown time")

if __name__ == "__main__":
    try:
        os.system("clear")
        print("Welcome to the mouse controller!\n\n")
        print("In order to ACTIVATE the controller scroll down on the mouse wheel.\n\n")
        print("In order to DEACTIVATE the controller scroll up on the mouse wheel.\n\n") 
        print("To close the program, left-click on the terminal window and type ctrl-c.\n\n")
        with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
            listener.join()
        # listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
        # listener.start()

    except KeyboardInterrupt:
        print('\n')
        print('Closing the Mouse Controller')


