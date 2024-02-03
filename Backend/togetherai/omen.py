from pymongo import MongoClient
from . import zed
import threading
#connect to the db
client = MongoClient('localhost', 27017)
db = client['Nova']






def threadchaos(prompt, subject):
    #ignore prompt for now, just use subjects
    #subjects is a list of strings
    #prompt is to build dynamic pages in the future

    #get the subfields for each subject
    subfields = zed.getsubfields(subject, prompt) #returns a list of strings
    subcol = db[subject]
    subcol.insert_one({"subject":subject, "subfields": subfields})
    for subfield in subfields:
        subficol = db[subfield]
        subtopics = zed.getsubtopics(subfield, prompt)
        #for each subtopic, call omen.createpage(subtopic)
        #return the link to the page
        #add the following to the subfield collection
        #subfield:[{subtopic1, link1}, {subtopic2, link2}, {subtopic3, link3}]
        zed.generatepages(subject, subfield, subtopics) #should return a list of dicts of name of subtopic as key and link as value
        subficol.insert_one({"subfield":subfield, "subtopics":subtopics})
    
    return None


    



    


