document.addEventListener('DOMContentLoaded', function () {
    var searchInput = document.querySelector('.searchtext');
    var searchContainer = document.querySelector('.search');
  
    searchInput.addEventListener('keypress', function (e) {
      if (e.key === 'Enter') {
        searchContainer.classList.toggle('vertical');
        searchInput.classList.toggle('vertical');
      }
    });
  });
  