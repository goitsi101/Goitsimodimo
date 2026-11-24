document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('mobile-toggle');
  const mobileMenu = document.getElementById('mobile-menu');

  if (toggleBtn && mobileMenu) {
    toggleBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
      toggleBtn.textContent = mobileMenu.classList.contains('open') ? '✕' : '☰';
    });

    const menuLinks = mobileMenu.querySelectorAll('a');
    menuLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        toggleBtn.textContent = '☰';
      });
    });
  }

  const copyButtons = document.querySelectorAll('[data-copy]');
  copyButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const textToCopy = btn.getAttribute('data-copy');
      if (!textToCopy) return;

      navigator.clipboard.writeText(textToCopy).then(() => {
        const originalText = btn.textContent;
        btn.textContent = 'Copied';
        btn.style.color = '#047857';
        btn.style.borderColor = '#10b981';

        setTimeout(() => {
          btn.textContent = originalText;
          btn.style.color = '';
          btn.style.borderColor = '';
        }, 2000);
      });
    });
  });

  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const honeypot = document.getElementById('form-honeypot');
      if (honeypot && honeypot.value) {
        return;
      }

      const nameInput = document.getElementById('form-name');
      const emailInput = document.getElementById('form-email');
      const msgInput = document.getElementById('form-message');
      const submitBtn = document.getElementById('form-submit');

      const name = nameInput ? nameInput.value.replace(/[<>]/g, '').trim() : '';
      const email = emailInput ? emailInput.value.replace(/[<>]/g, '').trim() : '';
      const message = msgInput ? msgInput.value.replace(/[<>]/g, '').trim() : '';

      const subject = encodeURIComponent(`Message from ${name}`);
      const body = encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\n${message}`);

      window.location.href = `mailto:goitsimarobela@gmail.com?subject=${subject}&body=${body}`;

      if (submitBtn) {
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Sent';
        setTimeout(() => {
          submitBtn.textContent = originalText;
        }, 3000);
      }
    });
  }
});
