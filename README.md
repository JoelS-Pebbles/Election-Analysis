# Election-Analysis

## Project Overview
A Colorado board of elections employee has given me the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received. 
4. Calculate the percent of votes each candidate got. 
5. Determine the winner of the election based on popular vote. 

## Resources
-Data source: election_results.csv
- Software: Python 3.7.6, Google Colab

## Summary 
The analysis of the election show that: 
- There were 369,711 votes cast in the election. 
-The candidates were: 
  -Raymon Anthony Doane 
  -Diana DeGette 
  -Charles Casper Stockham 
 -The results were: 
  -Charles Casper Stockham:23.0%(85,213) 
  -Diana DeGette:73.8%(272,892) 
  -Raymon Anthony Doane:3.1%(11,606) 
The winner of the election was: 
  Diana who received 73.8% of the votes with 272,892 total votes. 
  
  ## Challenge Overview
  The purpose of the election audit was to see who won the election. The analsyis also revealed how many votes and what percentage of votes that the candidates received. The results also showed the voter turnout of the each of the three counties. 
  
  ## Election-Audit Results
  * There were 369,711 total votes cast in the election.
  * Jefferson had 10.5% of the votes with 38,855 total votes
  * Denver had 82.8% of the votes with 306,055 total votes
  * Arapahoe had 6.7% of the votes with 24,801 total votes
  * Denver had the largest number of votes compared to the other counties
  * Charles Casper Stockham received 23% of the votes with 85,213 total votes. 
  * Diana DeGette received 73.8% of the votes with 272,892 total votes. 
  * Raymon Anthony Doane received 3.1% of the votes with 11,606 total votes.
  * Diana DeGette won the election with 73.8% of the votes and 272,892 total votes. 
  
![challege_three_pic.png]https://github.com/JoelS-Pebbles/Election-Analysis/blob/master/challege%20three%20pic.PNG
  
  ## Challenge Summary
  There was a list of votes, each one coming from one of the three counties and each vote was for one of the three candidates. My job was to analyze the data and figure out which candidate won, what were the candidate's voting percentage and how many votes they got. The results also showed the the county vote percentage and the number of votes per county.
  This script of code can be used for any election. Two things that could be added to the script to make the results more meaningful is to add the gender and age demographic of the voters. We would need the raw data for each of the voters in the csv file to start with. Then for the script I would add whether they were male or not, if not then they were female. I would also make age ranges with each block in the range containing 5 years. Both of these demographics would be shown in the conuty votes and candidate votes. 
