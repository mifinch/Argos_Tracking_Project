#-------------------------------------------------------------
# ArgosSelectionTool.py
#
# Description: Reads in an Argos tracking data file and allows
#   the user to identify the tracked sitings found within a 
#   specified bounding box.
#
# Author: Morgan Finch (mif15@duke.edu)
# Date:   Fall 2026
#--------------------------------------------------------------

# Create the geographic selection box
the_box = {
    'x_min' : 34.00,
    'y_min' : -76.00,
    'x_max' : 34.50,
    'y_max' : -75.00
}

#Create a variable pointing to the data file
file_name = 'data/raw/Satellite tracking of black-capped petrels 2019-argos.csv'

#Read the contents of the file into a list of lines
f= open(file_name,'r')
#read the header line
headerline = f.readline()
#Read contents of one line at a time
lineString = f.readlines()

#Pretend we read one line of data from the file
while lineString != "": #loop through line list, skip header line

    # Use the split command to parse the items in lineString into a list object
    line_data = lineString.split(',')
    
    # Assign variables to specfic items in the list
    event_id = line_data[0]   # Argos tracking event ID ("event-id")
    timestamp = line_data[2]  # Observation date ("timestamp")
    lc  = line_data[14]        # Observation location class ("argos:lc")
    if lc not in ['"1"', '"2"', '"3"']:
        continue #skip records that don't have coordinate info
    lat = float(line_data[4])        # Observation latitude  ("location-lat")
    lon = float(line_data[3])        # Observation longitude ("location-lon")
    tag_id = line_data[-3]     # Tag identifier ("tag-local-identifier")
    
    #Evaluate latitude and longitude conditions (boolean values)
    lat_condition = the_box['y_min'] < lat < the_box['y_max']
    lon_condition = the_box['x_min'] < lon < the_box['x_max']

    #Report whether the point falls within the box
    if lat_condition & lon_condition:
        print(f'Record {event_id}: {tag_id} was IN the box at {timestamp}')
    else:
        print(f'Record {event_id}: {tag_id} was NOT IN the box at {timestamp}')

    #move to the next line 
    lineString = f.readline()

#Close the file
f.close()