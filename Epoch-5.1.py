#Importing necessary libraries
import datetime #This module provides classes for manipulating dates and times.
import time #This module provides various time-related functions.

#Get the current local datetime
#datetime.datetime.now() returns the current local date and time as a datetime object.
now = datetime.datetime.now()

#Extracting hours, minutes, and seconds from the datetime object.
#now.hour, now.minute, and now.second are attributes of the datetime object that return the hour, minute, and second of the current time, respectively.
hours = now.hour
minutes = now.minute
seconds = now.second

#Getting the total seconds since the epoch (1 January 1970) 
#time.time() returns the current time in seconds since the epoch as a floating-point number.
total_seconds_since_epoch = time.time()

#Calculating the total days since the epoch by dividing the total seconds by the number of seconds in a day  (86400 seconds/day), we get the total number of full days since the epoch.
days_since_epoch = total_seconds_since_epoch // 86400 #Using floor division to get whole days


#Print the results 
#These print statements display the calculated values:
#-Current time in the format hours:minutes:seconds
#-Total number of days sincethe Unix epoch (January 1, 1970)
print(f"Current time: {hours}:{minutes}:{seconds}")
print(f"Days since the epoch: {days_since_epoch}")
