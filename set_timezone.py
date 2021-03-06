#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from pytz import all_timezones
from Tkinter import *
import tkMessageBox

def get_list(event):
	"""
	function to read the listbox selection
	and put the result in an entry widget
	"""
	# get selected line index
	index = listbox1.curselection()[0]
	# get the line's text
	seltext = listbox1.get(index)
	# delete previous text in enter1
	enter1.delete(0, END)
	# now display the selected text
	enter1.insert(0, seltext)

root = Tk()
root.wm_title("RaceDB: Set Time Zone")
root.geometry( '300x500' )

root.columnconfigure( 0, weight=1 )
root.rowconfigure( 1, weight=1 )

rowCur = 0
label = Label(root, text="Choose a Time Zone and press OK:")
label.grid( row=rowCur, column=0, sticky=W, padx=4, pady=4 )
rowCur += 1

# create the listbox (note that size is in characters)
listbox1 = Listbox(root, width=50, height=6)
listbox1.grid(row=rowCur, column=0, sticky=N+E+W+S, padx=4, pady=4)
# create a vertical scrollbar to the right of the listbox
yscroll = Scrollbar(command=listbox1.yview, orient=VERTICAL)
yscroll.grid(row=rowCur, column=1, sticky=N+S, pady=8)
listbox1.configure(yscrollcommand=yscroll.set)
rowCur += 1

# load the listbox with data
for item in all_timezones:
	listbox1.insert(END, item)
	
# get the current time zone from the time_zone.py
try:
	from RaceDB.time_zone import TIME_ZONE as currentTZ
except Exception as e:
	currentTZ = None

# Initialize the list box with the current time zone.
if currentTZ:
	for row, item in enumerate(all_timezones):
		if item == currentTZ:
			listbox1.see( row )
			listbox1.selection_set( row )
			break

# create data entry
enter1 = Entry(root, width=50, bg='yellow')
enter1.insert(0, currentTZ if currentTZ else 'Choose a Time Zone and press OK')
enter1.grid(row=rowCur, column=0, sticky=E+W, padx=8, pady=8)
rowCur += 1

def ok_callback():
	timezone = enter1.get()
	if 'Time Zone' in timezone:
		enter1.delete(0, END)
		enter1.insert(0, 'Select your Time Zone and press OK')
		tkMessageBox.showerror("Time Zone Select Error", "Select your Time Zone from the list and press OK.")
		return
	
	try:
		os.remove('RaceDB/time_zone.pyc')
	except Exception as e:
		pass

	with open('RaceDB/time_zone.py','w') as f:
		f.write( 'TIME_ZONE="{}"\n'.format(timezone) )
	sys.exit()

def cancel_callback():
	sys.exit()

button_frame = Frame( root )
button_frame.grid( row=rowCur, column=0, padx=8, pady=8 )
rowCur += 1

button_ok = Button( button_frame, text='OK', command=ok_callback )
button_cancel = Button( button_frame, text='Cancel', command=cancel_callback )

button_ok.grid(row=0, column=0, padx=8, pady=4)
button_cancel.grid(row=0, column=1, padx=8, pady=4)

# left mouse click on a list item to display selection
listbox1.bind('<ButtonRelease-1>', get_list)
root.mainloop()
