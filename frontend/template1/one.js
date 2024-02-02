// this thign is when you make it dynamui

// function createSection(id, heading, content) {
//     const section = document.createElement('section');
//     section.classList.add('main-section');
//     section.id = id;

//     const header = document.createElement('header');
//     const h3 = document.createElement('h3');
//     h3.textContent = heading;
//     header.appendChild(h3);
//     section.appendChild(header);

//     const article = document.createElement('article');
//     article.innerHTML = content;
//     section.appendChild(article);

//     return section;
// }


// const data = {
//     title: "JavaScript Documentation",
//     mainTitle: "JavaScript Documentation",
//     sections: [
//         {
//             id: "Introduction",
//             heading: "Introduction",
//             content: "<p>JavaScript is a cross-platform, object-oriented scripting language...</p>"
//         },

//     ],
//     navbarTitle: "JavaScript Documentation",
//     navLinks: [
//         { id: "intro-link", text: "Introduction", href: "#Introduction" },

//     ]
// };


// document.getElementById('title').textContent = data.title;


// document.getElementById('main-title').textContent = data.mainTitle;


// const sectionsContainer = document.getElementById('sections');
// data.sections.forEach(sectionData => {
//     const section = createSection(sectionData.id, sectionData.heading, sectionData.content);
//     sectionsContainer.appendChild(section);
// });


// document.getElementById('navbar-title').textContent = data.navbarTitle;


// const navLinksContainer = document.getElementById('nav-links');
// data.navLinks.forEach(linkData => {
//     const li = document.createElement('li');
//     const a = document.createElement('a');
//     a.classList.add('nav-link');
//     a.textContent = linkData.text;
//     a.href = linkData.href;
//     li.appendChild(a);
//     navLinksContainer.appendChild(li);
// });
