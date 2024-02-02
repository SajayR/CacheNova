import threading
import togetherai


def chaos(prompt):
    if prompt =="" or prompt == None:
        return "Please provide a prompt"
    


    cleanprompt = togetherai.cleanprompt(prompt)


    subjects = togetherai.getsubjects(cleanprompt) #will return a list of all subjects related to prompt, might need to be semantic searched
    if len(subject) < 3:
        subjects = subject[:3]          

    

    def run_threadchaos(cleanprompt, subjects):
        togetherai.threadchaos(cleanprompt, subjects)

    for subject in subjects:
        thread = threading.Thread(target=run_threadchaos, args=(cleanprompt, subject))
        thread.start()
        return "Chaos has been initiated with the subjecewacf4gtvvCD "
