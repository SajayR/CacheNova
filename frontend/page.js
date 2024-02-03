document.querySelector('.searchtext').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
      handleSearch();
    }
  });
  
  function handleSearch() {
    const searchQuery = document.querySelector('.searchtext').value;
    const subtopics = ['Subtopic 1', 'Subtopic 2', 'Subtopic 3'];
  
    subtopics.forEach((subtopic) => {
      displayPopupCard(subtopic);
    });
  }
  
  function displayPopupCard(subtopic) {
    const card = document.createElement('div');
    card.classList.add('popup-card');
    card.textContent = subtopic;
    document.body.appendChild(card);
  
    setTimeout(() => {
      card.classList.add('show');
    }, 100);
  }
  