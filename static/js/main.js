// Served at /static/js/main.js and linked from templates/base.html.
console.log("KlinikaQ starter app loaded");

const joinForm = document.getElementById("join-form");
if (joinForm) {
  joinForm.addEventListener("submit", (event) => {
    if (joinForm.dataset.submitting === "true") {
      event.preventDefault();
      return;
    }

    const button = joinForm.querySelector('button[type="submit"]');
    if (!button) return;

    joinForm.dataset.submitting = "true";
    button.disabled = true;
    button.textContent = "Getting your ticket…";
  });
}
