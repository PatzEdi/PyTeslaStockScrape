#!/usr/bin/env python3
import requests
import urllib
import urllib.request
import re
import time
import random

#plyer used if you want to send the notifications locally:
#from plyer import notification

#OPTIMIZED with NTFY: Service to send notifications easily from place to place.
#Huge credits to the NTFY team. They make the notification sending as easy as can be!

#Initial variable:
notifiedornot = 0
#Introduction:
print("Welcome to PyTSLA!\n")
time.sleep(1)
print("Please make sure you have assigned your ntfy.sh channel in the code.\n")
time.sleep(1)
#MainMenu:
MainMenu = int(input("(1) Get notified once TSLA stock goes above a custom value (Sell):\n(2) Get Notified once TSLA stock goes below a custom value (Buy):\n(3) Both!\n(4) Info:\n(99) Exit:\nChoice: "))

#Above
if MainMenu == 1:
	#Input amount of hours to run:
	hours = float(input("\n*Note* The higher the hours, the higher the risk of getting banned from the website. Use a VPN with a rotating IP in order to prevent this.\n\nHow many hours you would like for the program to run: "))
	#Convert into total rounds by dividing hours by 3600 seconds to average of delay:
	sequencenumbers = str((hours*3600)/12.5)
	#Remove everything after decimal point in order for the for loop to function:
	separator = '.'
	sequencenofloat = sequencenumbers.split(separator, 1)[0]
	sequencenofloat = int(sequencenofloat)
	line1 = float(input("\nEnter any number to get notified when TSLA stock will go above it: "))
	time.sleep(1)
	print("\nRetrieving data...")
	
	for i in range(sequencenofloat):
		randomint = float(random.randint(1000, 1500))
		randomdivide = randomint/100
		request_url = urllib.request.urlopen("https://www.cnbc.com/quotes/TSLA")
		readelements = request_url.read()
		readelements = str(readelements)
		#time.sleep(randomdivide)
		#regex pattern to select the value of price (in between price and priceChange, varies with each website)
		pattern = re.findall('(?<="price":")(.*)(?=","priceChange":")', readelements)
		#convert pattern from list to string, to float
		shortenedpattern = ''.join(pattern)
		shortenedpattern = float(shortenedpattern)
		#If stock goes under the line value, send notification.	
		if shortenedpattern > line1:
			print("\nTime to sell! The Tesla Stock is Above %f." % line1)
			#Send to all linked devices in that ntfy channel:
			requests.post("https://ntfy.sh/TSLAScrape",
				data="Time to sell! The Tesla Stock has gone above your line of %f USD." % line1,)
			#Send locally
			#plyer settings(optional):
			#notification.notify(
				#title = 'TSLA Stock',
				#message = 'Time to sell! The Tesla Stock has gone above your line of %f USD.' % line1,
				#app_icon = '/Users/edwardferrari/TSLA.png',
				#timeout = 10,
			#)
			break
		else:
			if notifiedornot != 1:
				print("\nYou'll get notified as soon as the TSLA stock goes above your given value of %f." % line1)
				time.sleep(1.5)
				print("\nSet to run for %f hour(s), %d refresh rounds." % (hours, sequencenofloat))
				print("\nCurrent value of TSLA stock is: %f USD" % shortenedpattern)
				notifiedornot = 1
				time.sleep(randomdivide)
			else:
				print("\nCurrent value of TSLA stock is: %f USD" % shortenedpattern)
				time.sleep(randomdivide)
				
#Below
if MainMenu == 2:
	#Input amount of hours to run:
	hours = float(input("\n*Note* The higher the hours, the higher the risk of getting banned from the website. In order to prevent this, use a VPN with a rotating IP.\n\nHow many hours you would like for the program to run: "))
	#Convert into total rounds by dividing hours by 3600 seconds to average of delay:
	sequencenumbers = str((hours*3600)/12.5)
	#Remove everything after decimal point in order for the for loop to function:
	separator = '.'
	sequencenofloat = sequencenumbers.split(separator, 1)[0]
	sequencenofloat = int(sequencenofloat)
	line2 = float(input("\nEnter any number to get notified when TSLA stock will go below it: "))
	time.sleep(1)
	print("\nRetrieving data...")
	
	for i in range(sequencenofloat):
		randomint = float(random.randint(1000, 1500))
		randomdivide = randomint/100
		request_url = urllib.request.urlopen("https://www.cnbc.com/quotes/TSLA")
		readelements = request_url.read()
		readelements = str(readelements)
		#time.sleep(randomdivide)
		#regex pattern to select the value of price (in between price and priceChange, varies with each website)
		pattern = re.findall('(?<="price":")(.*)(?=","priceChange":")', readelements)
		#convert pattern from list to string, to float
		shortenedpattern = ''.join(pattern)
		shortenedpattern = float(shortenedpattern)
		#If stock goes under the line value, send notification.	
		if shortenedpattern < line2:
			print("\nTime to Buy! The Tesla Stock is Under %f." % line2)
			#Send notification to mobile device:
			requests.post("https://ntfy.sh/TSLAScrape",
				data="Time to buy! The Tesla Stock has gone lower than your line of %f USD." % line2,)
			#plyer settings
			#notification.notify(
				#title = 'TSLA Stock',
				#message = 'Time to buy! The Tesla Stock has gone lower than your line of %f USD.' % line2,
				#timeout = 10,
			#)
			break
		else:
			if notifiedornot != 1:
				print("\nYou'll get notified as soon as the TSLA stock goes down to your given value of %f." % line2)
				time.sleep(1.5)
				print("\nSet to run for %f hour(s), %d refresh rounds." % (hours, sequencenofloat))
				print("\nCurrent value of TSLA stock is: %f USD" % shortenedpattern)
				notifiedornot = 1
				time.sleep(randomdivide)
			else:
				print("\nCurrent value of TSLA stock is: %f USD" % shortenedpattern)
				time.sleep(randomdivide)
				
elif MainMenu == 4:
	print("\nCreated by Patzedi! This script will scrape cnbc and their TSLA stock in real time, and you will get notified when its time to sell or buy based on your inputted values!\nHuge credits to NTFY.sh and binwiederhier! https://github.com/binwiederhier/ntfy.")
elif MainMenu == 3:
	print("\nThat feature will be available soon!")
elif MainMenu == 99:
	exit()
	