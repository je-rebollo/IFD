const accordionHeaders = document.querySelectorAll('.accordion-header');

accordionHeaders.forEach(function(header) {
  header.addEventListener('click', function() {
    const content = header.nextElementSibling;
    content.classList.toggle('active');
    if (header.classList.contains('active')) {
      header.classList.remove('active');
    } else {
      header.classList.add('active');
    }
  });
});
