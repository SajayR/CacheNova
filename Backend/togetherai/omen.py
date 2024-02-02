from pymongo import MongoClient
import zed
import threading
#connect to the db
client = MongoClient('localhost', 27017)
db = client['Nova']







def threadchaos(prompt, subject):
    #ignore prompt for now, just use subjects
    #subjects is a list of strings
    #prompt is to build dynamic pages in the future

    #get the subfields for each subject
    subfields = zed.getsubfields(subject) #returns a list of strings

    



    


