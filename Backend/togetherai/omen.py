from pymongo import MongoClient
from . import zed
import threading
import string
import markdown2
import time
from urllib.parse import quote
import random
#connect to the db
client = MongoClient('localhost', 27017)
db = client['Nova']

def generate_random_string(length=10):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(length))



def generatemarkdown_for_subject(subject, subfields):
    #generates markdown for the subject page
    #subfields is a list of strings
    #subject is a string
    #return a string
    markdown = f"# {subject}\n\n"
    for subfield in subfields:
        markdown += f"## {subfield}\n\n"
    return markdown

def generatemarkdown_for_subfields(subfields):
    # Generates markdown for subfields under the main subject
    markdown = ""
    for subfield in subfields:
        markdown += f"## {subfield}\n\n"
    return markdown

def convert_subject_markdown_to_html(markdown_content, subject):
    # Convert Markdown to HTML
    html_content = markdown2.markdown(markdown_content, extras=["mathjax"])

    # Fetch subfields and their corresponding links from the database
    subcol = db[subject]
    subject_data = subcol.find_one({"type": "subject", "subject": subject})
    subfields = subject_data.get("subfields", [])

    subfield_links = {}
    for subfield in subfields:
        subficol = db[subfield]
        subfield_data = subficol.find_one({"type": "subfield", "subfield": subfield})
        if subfield_data:
            subfield_links[subfield] = subfield_data.get("subfieldpage", "")

    # Replace subfield names in HTML content with links
    for subfield, link in subfield_links.items():
        html_content = html_content.replace(f"<h2>{subfield}</h2>", f"<h2><a href='{link}.html'>{subfield}</a></h2>")

    # HTML template without navbar and with glossary styling
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link href='https://fonts.googleapis.com/css?family=Aldrich' rel='stylesheet'>
        <link href='https://fonts.googleapis.com/css?family=Asap' rel='stylesheet'>
        <link rel="stylesheet" href="glossary.css">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>{subject} Glossary</title>
    </head>
    <body>
        
        <main id="main-doc">
            {html_content}
        </main>
        
    </body>
    </html>
    """

    encoded_subject = quote(subject)
    html_file_path = f"/Users/ciscorrr/Documents/CisStuff/curr/CacheNova/Backend/subjecthtmldatacluster/{encoded_subject}.html"

    # Write the final HTML content to the new file
    with open(html_file_path, "w", encoding='utf-8') as file:
        file.write(html_template)
    return html_file_path
'''

def threadchaos(prompt, subject):
    subfields = zed.getsubfields(subject, prompt)  # returns a list of strings
    subcol = db[subject]
    subjectfile = f"/Users/ciscorrr/Documents/CisStuff/curr/CacheNova/Backend/subjecthtmldatacluster/{subject}.html"
    subcol.insert_one({"type": "subject", "subject": subject, "subjectpage": subjectfile, "subfields": subfields})

    for subfield in subfields:
        subficol = db[subfield]
        subtopics = zed.getsubtopics(subfield, subject, prompt)
        subtopiclinks = {subtopic: generate_random_string() for subtopic in subtopics}
        subfieldpage = subtopiclinks[subtopics[0]]  # this is the link to the subfield page

        navbarcontent = [{'title': subtopicname, 'link': subtopiclinks[subtopicname]} for subtopicname in subtopics]
        
        subficol.insert_one({"type": "subfield", "subfield": subfield, "subfieldpage": subfieldpage, "subtopics": []})
        linkstosubtopic = zed.generatepages(subject, subfield, subtopics, subtopiclinks, navbarcontent)

        # After processing each subfield, regenerate and update the subject HTML file
        # This ensures the HTML file is updated with the latest subfield information
        markdown_content = generatemarkdown_for_subject(subject, subfields)
        with open(f'/Users/ciscorrr/Documents/CisStuff/curr/CacheNova/Backend/subjectmddatacluster/{subject}.md', "w", encoding='utf-8') as file:
            file.write(markdown_content)
        convert_subject_markdown_to_html(markdown_content, subject)'''


def process_subfield(subject, subfield, prompt):
    subficol = db[subfield]
    subtopics = zed.getsubtopics(subfield, subject, prompt)
    subtopiclinks = {subtopic: generate_random_string() for subtopic in subtopics}
    subfieldpage = subtopiclinks[subtopics[0]]  # this is the link to the subfield page

    navbarcontent = [{'title': subtopicname, 'link': subtopiclinks[subtopicname]} for subtopicname in subtopics]
    
    subficol.insert_one({"type": "subfield", "subfield": subfield, "subfieldpage": subfieldpage, "subtopics": []})
    linkstosubtopic = zed.generatepages(subject, subfield, subtopics, subtopiclinks, navbarcontent)

    # After processing each subfield, regenerate and update the subject HTML file
    # This ensures the HTML file is updated with the latest subfield information
    markdown_content = generatemarkdown_for_subfields([subfield])
    with open(f'/Users/ciscorrr/Documents/CisStuff/curr/CacheNova/Backend/subjectmddatacluster/{subject}.md', "a", encoding='utf-8') as file:
        file.write(markdown_content)
    convert_subject_markdown_to_html(markdown_content, subject)

def threadchaos(prompt, subject):
    subfields = zed.getsubfields(subject, prompt)  # returns a list of strings
    subcol = db[subject]
    encoded_subject = quote(subject)
    subjectfile = f"/Users/ciscorrr/Documents/CisStuff/curr/CacheNova/Backend/subjecthtmldatacluster/{encoded_subject}.html"
    subcol.insert_one({"type": "subject", "subject": subject, "subjectpage": subjectfile, "subfields": subfields})

    threads = []
    for subfield in subfields:
        thread = threading.Thread(target=process_subfield, args=(subject, subfield, prompt))
        threads.append(thread)
        thread.start()
        time.sleep(60)
        thread.join()
    

    # After all threads have completed, update the subject HTML file one final time to ensure it contains all updates
    markdown_content = generatemarkdown_for_subject(subject, subfields)
    with open(f'/Users/ciscorrr/Documents/CisStuff/curr/CacheNova/Backend/subjectmddatacluster/{subject}.md', "w", encoding='utf-8') as file:
        file.write(f"# {subject}\n\n")
    convert_subject_markdown_to_html(markdown_content, subject)