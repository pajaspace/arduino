import serial  # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt  # import matplotlib library
from drawnow import *
import pickle
import datetime
from matplotlib.pyplot import savefig
import Tkinter  as tk
import pygame
import os, sys
import pygame
from pygame.locals import *
from sys import exit
import vitacka2





 
tempF = []
pressure = []
hodnota = []
hod = 0
arduinoData = serial.Serial('/dev/ttyACM0', 9600)  # Creating our serial object named arduinoData
plt.ion()  # Tell matplotlib you want interactive mode to plot live data
cnt = 0
hod = 0


# datum
dnes = datetime.datetime.now()
soubor = open('zaloha.txt', 'at')
soubor.write('dnesni mereni')
soubor.close()

# Pickle dictionary using protocol 0.
output1 = open('zaloha2.txt', 'wb')  # vytisteni hodnoty
pickle.dump((dnes , " ", " \n"), output1)  # zapisovani posledni hodnoty  
output1.close()  # https://docs.python.org/2/library/pickle.html

 
def makeFig():  # Create a function that makes our desired plot

    plt.ylim(0, 130)  # Set y min and max values
    plt.title('Anemometr - sila rychlosti vetru')  # Plot the title
    plt.grid(True)  # Turn the grid on
    plt.ylabel('Hodnota')  # Set ylabels
    plt.plot(hodnota, 'ro-', color='blue' , label='Sila vetru')  # plot the temperature
    plt.legend(loc='upper right')  # plot the legend
    plt.xlabel('Casova jednotka ,mereni zhruba po sekunde')  # Set xlabels  
    
    
 
 
while True:  # While loop that loops forever
    while (arduinoData.inWaiting() == 0):  # Wait here until there is data
        pass  # do nothing
    arduinoString = arduinoData.readline()  # read the line of text from the serial port
    dataArray = arduinoString.split(',')  # Split it into an array called dataArray
    
    # Pickle dictionary using protocol 0.
    output = open('zaloha.txt', 'wb')  # vytisteni hodnoty
    pickle.dump((hodnota , " ", " \n"), output)  # zapisovani posledni hodnoty  
    output.close()  # https://docs.python.org/2/library/pickle.html
    
    
    
    
    
    
    hod = int(dataArray[0])  # Convert first element to floating number and put in temp

    hodnota.append(hod)  # Build our tempF array by appending temp readings
    drawnow(makeFig)  # Call drawnow to update our live graph
    plt.pause(.000001)  # Pause Briefly. Important to keep drawnow from crashing
    print hod
          
    # Testovani kolikrat se muze merit
cnt = cnt + 1
if(cnt > 10):  # If you have 50 or more points, delete the first one from the array
                               # This allows us to just see the last 50 data points
 #       pressure.pop(0) 
 
 # oznamovaci okno
  
        
        
 # vytvoreni zalohy v podobe png 
        p = makeFig()             
        p = savefig('test.png')
        
import okno
 #       import sys
 #       sys.exit(0) 

    
