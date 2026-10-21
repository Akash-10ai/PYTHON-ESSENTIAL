#compare Two strings Directly using in operator
# add string 

string = "The BodyGaurd is best album"

#Define a function 
def check_string(text):

# use if else statement and 'in' operatore to compare the string

 if text in string:
  return 'String matched'
 else:
  return 'String not matched'

 check_string("The BodyGaurd is the best")