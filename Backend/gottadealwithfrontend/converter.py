import execjs
import asyncio
from pyppeteer import launch
import nest_asyncio
nest_asyncio.apply()
import json

scriptcontentpart = """function populateNavbar(content) {
            const navbarList = document.querySelector('#navbar .navlist');
            navbarList.innerHTML = '';

            content.forEach(item => {
                const listItem = document.createElement('li');
                const link = document.createElement('a');
                link.classList.add('nav-link');
                link.href = `#${item.link}`;
                link.textContent = item.title;
                listItem.appendChild(link);
                navbarList.appendChild(listItem);
            });
        }

        populateNavbar(navbarContent);

        document.getElementById('toggleNav').addEventListener('click', function() {
            document.getElementById('navbar').classList.toggle('active');
        });"""

async def convert_markdown_to_html(markdown_path, navbar_content):
    # Read the Markdown file
    with open(markdown_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Serialize navbar_content to JSON
    navbar_content_json = json.dumps(navbar_content)

    # Use pyppeteer to load showdown.js
    browser = await launch()
    page = await browser.newPage()
    await page.addScriptTag({'url': 'https://cdnjs.cloudflare.com/ajax/libs/showdown/1.9.1/showdown.min.js'})

    # Convert Markdown to HTML using showdown.js
    html_content = await page.evaluate('''(markdown) => {
        const converter = new showdown.Converter();
        return converter.makeHtml(markdown);
    }''', markdown_content)

    await browser.close()

    # HTML template with JavaScript for navbar
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.freecodecamp.org/testable-projects-fcc/v1/bundle.js"></script>
        <link href='https://fonts.googleapis.com/css?family=Aldrich' rel='stylesheet'>
        <link href='https://fonts.googleapis.com/css?family=Asap' rel='stylesheet'>
        <link rel="stylesheet" href="one.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title></title>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_HTML"></script>
    </head>
    <body>
        <button id="toggleNav" class="hamburger">
            <i class="fas fa-bars"></i>
        </button>
        
        <main id="main-doc">
            {html_content}
        </main>

        <nav id="navbar">
            <ul class="navlist">
                <!-- Dynamic navbar content here -->
            </ul><br>
        </nav><br>

        <script>
        const navbarContent = {navbar_content_json};
        {scriptcontentpart}
        </script>
        <script src="one.js"></script>
        
    </body>
    </html>
    """

    # Determine the new HTML file path
    md_name = markdown_path.split('/')
    md_name[-1] = md_name[-1].replace('.md', '.html')  # Change the extension to .html
    md_name[-2] = 'htmldatacluster'  # Change the directory to htmldatacluster
    html_file_path = '/'.join(md_name)

    # Write the final HTML content to the new file
    with open(html_file_path, "w", encoding='utf-8') as file:
        file.write(html_template)

    return html_file_path




def convplease(path, navbarcontent):
    lol = asyncio.run(convert_markdown_to_html(path, navbarcontent))
    return lol
''''
if __name__ == "__main__":

    path = "/Users/ciscorrr/Documents/CisStuff/curr/CacheNova/Backend/mddatacluster/0JEtbFtfLD.md"
    sample= [
    {'title': "Introduction", 'link': "some-link" },
    {'title': "What you should already know", 'link': "some-link" },
    {'title': "JavaScript and Java", 'link': "some-link" },
    {'title': "Hello World", 'link': "some-link" },
    {'title': "Variables", 'link': "some-link" },
]
    sex=convplease(path, sample)
    print(sex)'''