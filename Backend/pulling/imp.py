from pymongo import MongoClient
#connect to the database
client = MongoClient('localhost', 27017)
db = client['Nova']


def get_subjectlink(subject):
    col = db[subject]
    need = {"subjectpage":1, "_id":0}   #specifying what to return
    sub_dict = col.find_one({"subject": subject}, need)
    return sub_dict.get("subjectpage", None)

def get_subfields(subject):
    col = db[subject]
    need = {"subfields":1, "_id":0}     #only want subfields list
    sub_list = col.find_one({"subject": subject}, need)
    return sub_list.get("subfields", [])

def get_subfieldslink(subfield):
    col = db[subfield]
    need = {"subfieldpage":1, "_id":0}          #dictionary - subfield 
    sub_dict = col.find_one({"subfield":subfield}, need)
    return sub_dict.get("subfieldpage", None)

def get_subtopics(subfield):
    col = db[subfield]
    need = {"subtopics":1, "_id":0}
    sub_dict = col.find_one({"subfield": subfield}, need)
    key = "link"
    values = [d[key] for d in sub_dict.get("subtopics", [])]
    return values


def generate_subject_page(subject):
    subfields = get_subfields(subject)
    for i in range(len(subfields)):
        with open(f"/Users/ciscorrr/Documents/CisStuff/curr/CacheNova/Backend/mddatacluster/{subfields[i]}.md", "w") as md_file:
            for subfield in subfields:
                md_file.write(f"###{subfield} \n")

def generate_subfield_page(subfield):
    subtopics = get_subtopics(subfield)
    for i in range(len(subtopics)):
        with open(f"/Users/ciscorrr/Documents/CisStuff/curr/CacheNova/Backend/mddatacluster/{subtopics[i]}.md", "w") as md_file:
            for subtopic in subtopics:
                md_file.write(f"###{subtopic} \n")