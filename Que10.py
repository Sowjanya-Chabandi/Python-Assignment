'''10)Write a Python program to display the date and time in a human-friendly string(vice versa human-friendly to date time)'''

import time
hf=time.asctime()
print("Human friendly time ",hf)

import datetime
dt=datetime.datetime.now()
print("date time ",dt)
