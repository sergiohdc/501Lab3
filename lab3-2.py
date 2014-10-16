gis_file = open('C:/Users/sergioh/Downloads/501Lab3/Gis_is_the_best.txt')
file_list = gis_file.read()

system_count, science_count, total_words, = 0, 0, 0


for word in file_list.split(' '):
	if word.lower() == 'systems':
		system_count = system_count + 1
	elif word.lower() == 'science':
		science_count = science_count + 1
 
	else:
		total_words = total_words + 1

total_words = total_words + science_count + system_count

print total_words
print system_count
print science_count
