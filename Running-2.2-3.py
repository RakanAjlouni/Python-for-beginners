#If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
#what time do I get home for breakfast?

#Time you leave your house
start_time_hours = 6 #Starting hour (6:00 am)
start_time_minutes = 52 #Starting minute (52 minutes past 6:00 am)

#Time taken for each mile in seconds
easy_pace_seconds_per_mile = 8 * 60 + 15 #8 minutes and 15 seconds per mile
tempo_pace_seconds_per_mile = 7 * 60 + 12 #7 minutes and 12 seconds per mile

#Total time spent running
total_running_time_seconds = (easy_pace_seconds_per_mile + tempo_pace_seconds_per_mile * 3 + easy_pace_seconds_per_mile)

#Converting total running time to hours, minutes, and seconds
total_running_time_minutes = total_running_time_seconds // 60
total_running_time_seconds = total_running_time_seconds % 60

#Calculating the time you get home for breakfast
arrival_time_hours = start_time_hours + (total_running_time_minutes // 60)
arrival_time_minutes = start_time_minutes + (total_running_time_minutes % 60)

# Adjust the arrival time if it exceeds 60 minutes
arrival_time_hours += arrival_time_minutes // 60
arrival_time_minutes %= 60

# Adjust the arrival time if it exceeds 24 hours
arrival_time_hours %= 24

#Printing the time you get home for breakfast
print("You get home for breakfast at", arrival_time_hours,":",arrival_time_minutes,"AM")

