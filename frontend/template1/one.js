function fetchAndInsertMarkdown(url) {
    fetch(url)
        .then(response => response.text())
        .then(markdownData => {
            var converter = new showdown.Converter();
            var htmlContent = converter.makeHtml(markdownData);


            document.getElementById('main-doc').innerHTML += htmlContent;
        })
        .catch(error => console.error('Error fetching markdown file:', error));
}

// Fetch markdown file automatically
fetchAndInsertMarkdown('output2.md');

fetchAndInsertMarkdown('output2.md');




// responsive

