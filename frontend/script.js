function fadeOutAndNavigate() {
  var button = document.getElementById('siri-button');
  var particlesContainer = document.getElementById('particles-js');


  button.style.animation = 'explode 3s ease forwards';


  particlesContainer.style.transition = 'opacity 2s ease-out';
  particlesContainer.style.opacity = '0';


  setTimeout(function() {

    button.style.display = 'none';
    window.location.href = "page.html";
  }, 3000); 
}





