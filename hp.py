# Current Date and Time

from datetime import datetime

def current_datetime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

print(current_datetime()) 

'''
Here's an explanation of the code:

from datetime import datetime imports the datetime class from the datetime module, which provides functions for working with dates and times.

def current_datetime(): defines a function named current_datetime that does not take any parameters.

now = datetime.now() gets the current date and time using datetime.now(), 
which returns a datetime object representing the current local date and time.

return now.strftime("%Y-%m-%d %H:%M:%S") formats the datetime object now as a string in the format "YYYY-MM-DD HH:MM:SS" using the strftime method. This method converts the datetime object into a string according to the specified format.

print(current_datetime()) calls the current_datetime function and prints the formatted current date and time.
'''