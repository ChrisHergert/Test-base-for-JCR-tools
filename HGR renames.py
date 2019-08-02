import os
import csv
import pandas as pd
from pprint import pprint

path = r"C:\Users\cjh0372\Desktop\New folder"
#path2 = 
catch1 = 'Categories: \''
catch2 = '\' Selected Category'
edition = 'SCIE - '

files = os.listdir(path)

for file in files:
	if "JournalHome" in file:
		with open(os.path.join(path, file)) as f:
			reader = csv.reader(f)
			row1 = next(reader) #get the first line
		#category_name = row1[0].split(catch1)[1].split(catch2)[0]
		category_name = row1[0].split(catch1)[1].split(catch2)[0]
		categ = edition + category_name + '.csv'	
		os.rename(os.path.join(path, file), os.path.join(path, categ))
# ######################################################### os.rename(os.path.join(path, file), os.path.join(path, str(index)+'.jpg'))
'''
ogdf = pd.DataFrame(columns = [	'Rank',
								'Full Journal Title',
								'JCR Abbreviated Title',
								'ISSN',
								'Total Cites',
								'Journal Impact Factor',
								'Impact Factor without Journal Self Cites',
								'5-Year Impact Factor,'
								'Immediacy Index',
								'Citable Items',
								'Cited Half-Life',
								'Citing Half-life',
								'Eigenfactor Score',
								'Article Influence Score',
								'% Articles in Citable Items',
								'Average Journal Impact Factor Percentile',
								'Normalized Eigenfactor',
								'Category'])
#
for file in files: 		# look at each file in the directory
	with open(os.path.join(path, file),'r') as f:	# open the current file in read-only mode as 'f'
		newname = file.split(' - ')[1]		# extract the subject name from the file
		with open(newname,'w') as f1:
			row0 = next(f) # skip trash line
			category_name = (row0.split(catch1)[1]).split(catch2)[0] # This will get you the category name if the top row hasn't been eliminated.
			for line in f:
				f1.write(line)
			df = pd.read_csv(newname)
			df['Category'] = category_name
			ogdf = pd.concat([ogdf, df], ignore_index = True)
		os.remove(newname)
print('done!')
ogdf.to_csv('ogdf.csv')
#'''
