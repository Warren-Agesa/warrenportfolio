// Initialize plugins and global functionality
document.addEventListener('DOMContentLoaded', () => {
  // Initialize AOS (Animate On Scroll)
  AOS.init({ duration: 1000, once: true });

  // Mobile Navigation Toggle
  const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
  const navMenu = document.querySelector('#navmenu');

  if (mobileNavToggle) {
    mobileNavToggle.addEventListener('click', () => {
      navMenu.classList.toggle('active');
      mobileNavToggle.classList.toggle('bi-list');
      mobileNavToggle.classList.toggle('bi-x');
    });
  }

  // Header scroll effect
  window.addEventListener('scroll', () => {
    const header = document.querySelector(".header");
    if (header) {
      header.classList.toggle("scrolled", window.scrollY > 50);
    }
  });

  // Contact Form Submission
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', handleContactFormSubmit);
  }

  // Portfolio Filter
  initPortfolioFilter();
});

// Handle Contact Form Submission
function handleContactFormSubmit(e) {
  e.preventDefault();

  const form = this;
  const formData = new FormData(form);
  const submitBtn = document.getElementById('submitBtn');
  const submitText = document.getElementById('submitText');
  const successMessage = document.getElementById('successMessage');
  const errorMessage = document.getElementById('errorMessage');
  const successText = document.getElementById('successText');
  const errorText = document.getElementById('errorText');

  // Hide previous messages
  if (successMessage) successMessage.style.display = 'none';
  if (errorMessage) errorMessage.style.display = 'none';

  // Disable button and show loading state
  submitBtn.disabled = true;
  const originalText = submitText.textContent;
  submitText.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Sending...';

  // Send form via AJAX
  fetch(form.action || window.location.pathname, {
    method: 'POST',
    body: formData,
    headers: {
      'X-Requested-With': 'XMLHttpRequest'
    }
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      successText.textContent = data.message;
      successMessage.style.display = 'flex';
      successMessage.classList.add('show');
      
      // Reset form
      form.reset();
      
      // Clear messages after 5 seconds
      setTimeout(() => {
        successMessage.style.display = 'none';
        successMessage.classList.remove('show');
      }, 5000);
    } else {
      errorText.textContent = data.message;
      errorMessage.style.display = 'flex';
      errorMessage.classList.add('show');
      
      // Clear error after 5 seconds
      setTimeout(() => {
        errorMessage.style.display = 'none';
        errorMessage.classList.remove('show');
      }, 5000);
    }
  })
  .catch(error => {
    console.error('Error:', error);
    errorText.textContent = 'An error occurred. Please try again.';
    errorMessage.style.display = 'flex';
    errorMessage.classList.add('show');
    
    setTimeout(() => {
      errorMessage.style.display = 'none';
      errorMessage.classList.remove('show');
    }, 5000);
  })
  .finally(() => {
    // Re-enable button
    submitBtn.disabled = false;
    submitText.textContent = originalText;
  });
}

// Portfolio Filter Functionality
function initPortfolioFilter() {
  const filterButtons = document.querySelectorAll('.filter-btn');
  if (filterButtons.length === 0) return;

  filterButtons.forEach(button => {
    button.addEventListener('click', function() {
      const filter = this.dataset.filter;
      
      // Update active button
      filterButtons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');

      // Filter projects
      const projectItems = document.querySelectorAll('.project-item');
      projectItems.forEach(item => {
        if (filter === 'all') {
          item.style.display = 'block';
          setTimeout(() => item.classList.add('show'), 10);
        } else if (item.dataset.category === filter) {
          item.style.display = 'block';
          setTimeout(() => item.classList.add('show'), 10);
        } else {
          item.classList.remove('show');
          setTimeout(() => item.style.display = 'none', 300);
        }
      });
    });
  });

  // Initialize - show all projects
  document.querySelectorAll('.project-item').forEach(item => {
    item.classList.add('show');
  });
}
