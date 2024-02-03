from pymongo import MongoClient
from . import zed
import threading
import string
import random
#connect to the db
client = MongoClient('localhost', 27017)
db = client['Nova']

def generate_random_string(length=10):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(length))



    


def threadchaos(prompt, subject):
    #ignore prompt for now, just use subjects
    #subjects is a list of strings
    #prompt is to build dynamic pages in the future

    #get the subfields for each subject
    subjectpage = generate_random_string()
    subfields = zed.getsubfields(subject, prompt) #returns a list of strings
    subcol = db[subject]
    subcol.insert_one({"subject":subject, "subjectpage": subjectpage, "subfields": subfields})
    for subfield in subfields:
        #implement the following
        #if subfield in db:
        #   listoflinks_tosubfieldpages.append({subfield: db[subfield]})
        #else:
        subfieldpage = generate_random_string() #have to generate a html page for this
        subficol = db[subfield]
        subtopics = zed.getsubtopics(subfield, subject, prompt)
        subtopiclinks={subtopic: generate_random_string() for subtopic in subtopics}

        #lets gen navbar content

        navbarcontent = [{'title': subtopicname, 'link': subtopiclinks[subtopicname]} for subtopicname in subtopics]
        
        #for each subtopic, call omen.createpage(subtopic)
        #return the link to the page
        #add the following to the subfield collection
        #subfield:[{subtopic1, link1}, {subtopic2, link2}, {subtopic3, link3}]
        linkstosubtopic=zed.generatepages(subject, subfield, subtopics, subtopiclinks, navbarcontent) #should return a list of dicts of name of subtopic as key and link as value
        #holds the form [{subtopic1: link1}, {subtopic2: link2}, {subtopic3: link3}]

    
        subficol.insert_one({"subfield":subfield, "subfieldpage": subfieldpage, "subtopics":linkstosubtopic})
        #add the following to the subject collection
        #linkstosubtopic holds list of dicts of title key holding subtopic, link key holding entire path to subtopic
    return None


    



    


