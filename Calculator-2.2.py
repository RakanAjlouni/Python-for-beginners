#How many seconds are there in 42 minutes 42 seconds?
minutes = 42
seconds = 42

total_seconds = (minutes * 60) + seconds
print(total_seconds)

#How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
kilometers = 10 
miles = kilometers / 1.61
print(miles)

#If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)?
total_distance_km = 10 
total_time_minutes = 42 + 42/60

#Convert kilometers to miles (1 mile = 1.61 kilometers)
total_distance_miles = total_distance_km / 1.61 # converting kilometers to miles

#Caculate the average pace per mile
average_pace_per_mile = total_time_minutes / total_distance_miles

#Convert the average pace to minutes and seconds

pace_minutes = int(average_pace_per_mile) # integer part is the minutes
pace_seconds = int((average_pace_per_mile - pace_minutes) * 60) # converting remaining fraction to seconds

total_time_hours = total_time_minutes / 60 # converting total time from minutes to hours
average_speed_mph = total_distance_miles / total_time_hours

print("Average pace per mile: {} minutes {} seconds".format(pace_minutes, pace_seconds))
print("Average speed: {:.2f} miles per hour".format(average_speed_mph))