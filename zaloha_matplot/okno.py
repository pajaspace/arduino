import easygui
from easygui import *
import sys
easygui.msgbox('probehlo 10 mereni vytvarime obrazove zalohy.', 'oznameni')

msg = "Mam pokracovat v mereneni ?"
title = "Mam merit dal ?"
if ccbox(msg, title):     # show a Continue/Cancel dialog
    pass  # user chose Continue
else:
    msg = "System odpojen ..."
    pause=1000
    sys.exit(0)           # user chose Cancel
   
