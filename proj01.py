###########################################################
#  Project 1
#
#  Algorithm
#    prompt for a rod number
#    input a rod string
#    convert the string to a float
#    conversions:
#        convert rods to meters
#        convert rods to feet
#        convert rods to miles
#        convert rods to furlongs
#        convert rods to time based on 3.1 miles per hour
#    print conversions
###########################################################

rods_string = input("Input rods: ") # Prompt for input of rod number
rods_float = float(rods_string) # Convert rods string to float

RODS_PER_METER = 5.0292    # Amount of rods per meter
METERS_PER_FOOT = .3048    # Amount of meters per foot
METERS_PER_MILE = 1609.34    # Amount of meters per mile
RODS_PER_FURLONG = 40    # Amount of rods per furlong
MINUTES_PER_SECOND = 60    # Amount of minutes per second
MILE_PER_HOUR = 3.1    # Miles per hour of average walking speed

meters_float = rods_float * RODS_PER_METER  # Conversion of rods to meters
feet_float = meters_float / METERS_PER_FOOT    # Conversion of rods to feet
miles_float = meters_float / METERS_PER_MILE    # Conversion of rods to miles
furlongs_float = rods_float / RODS_PER_FURLONG  
    # Conversion of rods to furlongs  
time_float = (miles_float / MILE_PER_HOUR) * MINUTES_PER_SECOND 
    # Conversion of rods to minutes to walk   

print( "You input", rods_float , "rods." )
print( "\nConversions")
print( "Meters:", round( meters_float, 3 ))
print( "Feet:", round( feet_float, 3))
print( "Miles:", round( miles_float, 3))
print( "Furlongs:", round( furlongs_float, 3))
print( "Minutes to walk", rods_float,"rods:", round( time_float, 3))
    # Print final conversions with strings