// Served at /static/js/main.js and linked from templates/base.html.
console.log("KlinikaQ starter app loaded");

document.addEventListener("DOMContentLoaded", () => {
    const alerts = document.querySelectorAll(".alert");
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.remove("show");
            alert.classList.add("fade");
            setTimeout(() => alert.remove(), 500); // Wait for transition
        }, 5000); // 5 seconds
    });
});

document.querySelectorAll("form[data-confirm]").forEach((form) => {
    form.addEventListener("submit", (event) => {
        if (!form.dataset.confirmed) {
            event.preventDefault();
            const message = form.dataset.confirm;
            const modalBody = document.getElementById("confirmModalBody");
            const modalBtn = document.getElementById("confirmModalBtn");
            const modal = new bootstrap.Modal(document.getElementById('confirmModal'));
            
            modalBody.textContent = message;
            modal.show();
            
            // Remove previous event listeners to prevent multiple triggers
            const newBtn = modalBtn.cloneNode(true);
            modalBtn.parentNode.replaceChild(newBtn, modalBtn);
            
            newBtn.addEventListener("click", () => {
                form.dataset.confirmed = "true";
                modal.hide();
                form.submit();
            });
        }
    });
});