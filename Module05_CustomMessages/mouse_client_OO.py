#!/usr/bin/env python3

#Col Brian Neff
#ROS Enabled mouse client 
#Activates when mouse wheel is scrolled down and 
#Deactivates when mouse wheel is scrolled up 
#last modified 2 Jan 2023
#mouse_client_OO.py

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

class Mouse:
    def __init__(self):
        listener = Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        listener.start()
        self.ctrl_c = False
        rospy.on_shutdown(self.shutdownhook)

    # Handle the event of the user moving the mouse    
    def on_move(self,x,y):
        #We need to establish the use of the global variable for button activation
        global activate
        

        if(activate == False):
            messageString = "No movement sent, activate cursor first by scrolling down on the mouse wheel"
            print(messageString, end='')
            # overwrite same line
            print('\b' *len(messageString), end='', flush=True)
        else:
            # Use the dimensions of the monitor to convert output into x & y between -1 and 1
            xScale = ((x/(xDim/2))-1)
            yScale = -((y/(yDim/2))-1)
            xFormat = "{:+.3f}".format(xScale)
            yFormat = "{:+.3f}".format(yScale)
            # create 19 byte message with x,y coordinates embedded and print to screen
            positionStr = 'X: ' + str(xFormat) + ' Y: ' + str(yFormat) + "                                                           "
            print(positionStr, end='')
            # overwrite same line
            print('\b' *len(positionStr), end='', flush=True)
    
    #Currently I'm not doing anything with the button click.
    #Eventually we could add additional modes if we wanted to.
    def on_click(self,x,y,button,pressed):
        pass

    # Handle the event of the user using the scroll wheel on the mouse    
    def on_scroll(self,x,y,dx,dy):
        global activate
        if dy == 1:
            os.system("clear")
            print("Welcome to the mouse controller!\n\n")
            print("In order to ACTIVATE the controller scroll down on the mouse wheel.\n\n")
            print("In order to DEACTIVATE the controller scroll up on the mouse wheel.\n\n") 
            print("To close the program, left-click on the terminal window and type ctrl-c.\n\n")
            activate = False
        if dy == -1:
            activate = True

    # Handle the event of the user pressing ctrl_c        
    def shutdownhook(self):
        print("Shutting down the client                                                      ")
        self.ctrl_c = True



if __name__ == "__main__":
    os.system("clear")
    print("Welcome to the mouse controller!\n\n")
    print("In order to ACTIVATE the controller scroll down on the mouse wheel.\n\n")
    print("In order to DEACTIVATE the controller scroll up on the mouse wheel.\n\n") 
    print("To close the program, left-click on the terminal window and type ctrl-c.\n\n")
    rospy.init_node('Mouse')
    mouseInst = Mouse()
    rospy.spin()


