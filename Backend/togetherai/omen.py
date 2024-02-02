from pymongo import MongoClient
import zed
import threading
#connect to the db
client = MongoClient('localhost', 27017)
db = client['Nova']


def generate_subtopic_name(subject: str, prompt: str) -> list:
    #this function will generate a subtopic name for the subject
    #this will be used to create a collection in the db
    pass




def threadchaos(prompt, subject):
    #ignore prompt for now, just use subjects
    #subjects is a list of strings
    #prompt is to build dynamic pages in the future

    #get the subfields for each subject
    subfields = zed.getsubfields(subject) #returns a list of strings
    subcol = db[subject]
    subcol.insert_one({"subject":subject, "subfields":subfields})
    for subfield in subfields:
        subficol = db[subfield]
        subtopics = zed.getsubtopics(subfield, prompt)
        #for each subtopic, call omen.createpage(subtopic)
        #return the link to the page
        #add the following to the subfield collection
        #subfield:[{subtopic1, link1}, {subtopic2, link2}, {subtopic3, link3}]




    



    


