# arduino

 Installing 
- 
- Download project actual version is Anemometr v_2.0
 
 - best think is import to eclipse python code
 - *.ino code start in the Arduino.IDE 
  
 -  on the line in python code   arduinoData = serial.Serial('/dev/ttyACM0', 9600)    - fill the correct port - same like you have setted in arduino IDE
                                                        
 
  Running

  - starting mat.py
  
  ---------------------------------------
   Note> Its not started on first time , because of not_cleaned_cash problem.
   
typ of failure >> 

  hod = int(dataArray[0])  # Convert first element to floating number and put in temp
   ValueError: invalid literal for int() with base 10: '9\r-5\r\n'
  
work arround >> just starting application couple of times , abd its started ok . ... - one of bug currently 
   But it is working fine :-)
   
   ----------------------------------------
   
   TO DO - make this readme more complex

    Regarding this project is to on wiki pages github.
    
    
