gis_file = open('C:/Users/sergioh/Downloads/501Lab3/Gis_is_the_best.txt')
file_list = gis_file.read()

new_file = gis_file.replace('Science', 'Systems').replace('Systems', 'Science')
#>>> create_new = (

gis_file = open('c:/users/sergioh/Downloads/501Lab3/GIS_is_the_best.txt', 'w')
gis_file.write(new_file)

gis_file.close()