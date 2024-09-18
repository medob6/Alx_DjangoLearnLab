// static/js/scripts.js

// Add animations for buttons and forms (if required)
const buttons = document.querySelectorAll('.login-btn');

buttons.forEach(button => {
  button.addEventListener('mouseenter', function() {
    const spanElements = this.querySelectorAll('span');
    spanElements.forEach(span => span.style.animationPlayState = 'running');
  });
  
  button.addEventListener('mouseleave', function() {
    const spanElements = this.querySelectorAll('span');
    spanElements.forEach(span => span.style.animationPlayState = 'paused');
  });
});
