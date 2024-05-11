import numpy as np
import collections
npArray= np.array([60, 70, 70, 70, 80,90,60])
c=collections.Counter(npArray) # Generate a dictionary {"value":"nbOfOccurrences"}
arraySize=npArray.size
nbOfOccurrences=c[60] #assuming you want the proba to get 10
proba=(nbOfOccurrences/arraySize)*100
print(proba) #print 60.0
30 | PageProblem2:- If In class 80 students and 60 students got 60 % marks then Calculate the
Probability of finding how many students got the 60 marks for given data set .
#!/usr/bin/env python3
"""reducer.py"""
import sys
# Create a dictionary to map marks
Marksprob = {}
# Get input from stdin
for line in sys.stdin:
 #Remove spaces from beginning and end of the line
 line = line.strip()
 # parse the input from mapper.py
 ClassA, Marks = line.split('\t', 1)
# Create function that returns probability percent rounded to one decimal place
def event_probability(event_outcomes, sample_space):
 probability = (event_outcomes / sample_space) * 100
 return round(probability, 1)
31 | Page# Sample Space
ClassA = 30
# Determine the probability of drawing a heart
Marks = 15
grade_probability = event_probability(Marks, ClassA)
# Print each probability
print(str(grade_probability) + '%')
Output:- 28.57