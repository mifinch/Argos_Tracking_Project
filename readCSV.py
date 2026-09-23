#Set a variable to the CSV filename
the_filename = 'data/raw/Satellite tracking of black-capped petrels 2019-argos.csv'
#Create a file object pointing to file name
f = open(the_filename,'r') #r for READ ONLY

#Create a list of all the lines in the file via the file object
line_list = f.readlines()
#Close the file
f.close()
#Print the 11th item in the line list
print(line_list[10])