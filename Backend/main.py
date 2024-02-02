import threading
from togetherai import omen, zed


def chaos(prompt):
    if prompt =="" or prompt == None:
        return "Please provide a prompt"
    cleanprompt = zed.cleanprompt(prompt) #returns strin
    subjects = zed.getsubjects(cleanprompt) #will return a list of all subjects related to prompt, might need to be semantic searched

    if len(subject) < 3:
        subjects = subject[:3]         


    def run_threadchaos(cleanprompt, subject):   #sends only one of the subjects to the threadchaos function
        omen.threadchaos(cleanprompt, subject)

    for subject in subjects:
        thread = threading.Thread(target=run_threadchaos, args=(cleanprompt, subject))
        thread.start()
        
    link = omen.getsubjectlink(subjects)
    return(link)
    #return(a link to the dynamic page where the user can only see the subjects thats needed for his prompt)



if __name__=="__init__":
    #prompt=frontendselamadarchod
    #chaos(prompt)
    pass