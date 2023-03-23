from process import Process

file_1 = Process('./files/april_12')
file_2 = Process('./files/april_13')
file_3 = Process('./files/april_14')
file_4 = Process('./files/april_15')
file_5 = Process('./files/april_16')
file_6 = Process('./files/april_17')
file_7 = Process('./files/april_18')

#Task 2) Can perform all three of the basic task on all seven files
"""
file_1.run(); 
file_2.run(); 
file_3.run(); 
file_4.run(); 
file_5.run(); 
file_6.run(); 
file_7.run(); 
"""

#Task 3) a
if len(file_7.findUsers()) < len(file_1.findUsers()): 
  print("There was not an increase in users who published posts.")
else: 
  print("There was an increase in users who published posts.")

#Task 3)b 
if len(file_7.taskC()) < len(file_1.taskC()): 
  print("There was not an increase in users who published posts that mentioned symptoms of sickness.")
else: 
  print("There was an increase in users who published posts that mentioned symptoms of sickness.")
