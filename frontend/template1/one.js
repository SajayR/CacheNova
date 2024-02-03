function fetchAndInsertMarkdown() {
    fetch('/markdown')
        .then(response => response.text())
        .then(markdownData => {
            var converter = new showdown.Converter();
            var htmlContent = converter.makeHtml(markdownData);
            document.getElementById('main-doc').innerHTML = htmlContent;
        })
        .catch(error => console.error('Error fetching markdown file:', error));
}

fetchAndInsertMarkdown();

const exampleNavbarContent = [
    { id: "introduction", title: "Introduction" },
    { id: "what_you_should_already_know", title: "What you should already know" },
    { id: "javascript_and_java", title: "JavaScript and Java" },
    { id: "hello_world", title: "Hello World" },
    { id: "variables", title: "Variables" },
];

function populateNavbar(content) {
    const navbarList = document.querySelector('#navbar .navlist');
    navbarList.innerHTML = ''; // Clear existing content

    content.forEach(item => {
        const listItem = document.createElement('li');
        const link = document.createElement('a');
        link.classList.add('nav-link');
        link.href = `#${item.id}`;
        link.textContent = item.title;
        listItem.appendChild(link);
        navbarList.appendChild(listItem);
    });
}

populateNavbar(exampleNavbarContent);

document.getElementById('toggleNav').addEventListener('click', function() {
    document.getElementById('navbar').classList.toggle('active');
});


