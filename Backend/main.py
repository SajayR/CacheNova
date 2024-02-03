import threading
from togetherai import omen, zed
from pymongo import MongoClient
import random
import string

client = MongoClient('localhost', 27017)
db = client['Nova']
collection = db=['links']

def generate_random_string(length=10):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(length))

def chaos(prompt):
    if prompt =="" or prompt == None:
        return "Please provide a prompt"
    cleanprompt = zed.cleanprompt(prompt) #returns strin
    subjects = zed.getsubjects(cleanprompt) #will return a list of all subjects related to prompt, might need to be semantic searched       
    print(cleanprompt)
    print(subjects)

    def run_threadchaos(cleanprompt, subject):   #sends only one of the subjects to the threadchaos function
        omen.threadchaos(cleanprompt, subject)

    for subject in subjects:
        #subjectpage = generate_random_string()
        #implement the following
        #if subject already exists in the db, return the link to the subject page
        #else, create a new subject page and return the link to the subject page
        print(subject)
        thread = threading.Thread(target=run_threadchaos, args=(cleanprompt, subject))
        thread.start()
        
            
    #link = omen.getsubjectlink(subjects)
    #return(link)
    #return(a link to the dynamic page where the user can only see the subjects thats needed for his prompt)



if __name__=="__main__":
    #prompt=frontendselamadarchod
    print("Hey")
    chaos("Deep learning")
    #chaos(prompt)
    