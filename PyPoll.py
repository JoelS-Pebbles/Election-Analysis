#The data we need to retrieve
# The total number of votes cast
# Acomplete list of canddidates who received votes
# The percent of votes each candidate won
# The winner of the election based on popular vote


#Text to the election analysis file from this file
# import os
# import csv

# file_to_save=os.path.join("analysis","election_analysis.txt")

# with open(file_to_save,"w") as txt_file:

#     txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")
    


#3.4.2 reading the csv file in python
import csv
dir(csv)
file_to_load=r'C:\Users\12109\code\Election-Analysis\Resources\election_results.csv'
with open(file_to_load) as election_data:
    print (election_data.readlines())



#Read the election_results.csv file- code

# import csv
# import os
# file_to_load=os.path.join('election_results.csv')
# file_to_save=os.path.join('election_analysis.txt')
# with open(file_to_load) as election_data:
#     file_reader=csv.reader(election_data)
#     headers=next(file_reader)
#     print(headers)