// AI-ASSISTED START | ID: AI-2026-001
const formSteps = document.querySelectorAll(".form-step");
const progressSteps = document.querySelectorAll(".step");

const nextButton = document.getElementById("next-button");
const nextButton2 = document.getElementById("next-button-2");

const backButton = document.getElementById("back-button");
const backButton2 = document.getElementById("back-button-2");

const dateInput = document.getElementById("wanted-date");

const today = new Date().toISOString().split("T")[0];

dateInput.min = today;

let currentStep = 0;

function showStep(stepNumber) {

// Hide every form step
formSteps.forEach((step) => {
    step.classList.remove("active");
});

// Show the current form step
formSteps[stepNumber].classList.add("active");

// Update the progress indicator
progressSteps.forEach((step, index) => {
    step.classList.remove("active");

    if (index === stepNumber) {
        step.classList.add("active");
    }
});

currentStep = stepNumber;


}

// STEP 1 → STEP 2
nextButton.addEventListener("click", () => {

    const services = document.querySelectorAll('input[name="box-name"]');

    const serviceSelected = [...services].some(service => service.checked);

    if (!serviceSelected) {
        alert("Please select at least one service.");
        return;
    }

    showStep(1);
});

// STEP 2 → STEP 1
backButton.addEventListener("click", () => {
showStep(0);
});

// STEP 2 → STEP 3
nextButton2.addEventListener("click", () => {

    const name = formSteps[1].querySelector('[name="your-name"]');
    const email = formSteps[1].querySelector('[name="your-email"]');
    const phone = formSteps[1].querySelector('[name="your-number"]');
    const vehicle = formSteps[1].querySelector('[name="vehicle"]');
    const registration = formSteps[1].querySelector('[name="registration"]');

    // Name
    if (name.value.trim() === "") {
        alert("Please enter your full name.");
        return;
    }

    // Email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailPattern.test(email.value.trim())) {
        alert("Please enter a valid email address.");
        return;
    }

    // Phone number
    const phonePattern = /^04\d{2}[\s-]?\d{3}[\s-]?\d{3}$/;

    if (!phonePattern.test(phone.value.trim())) {
        alert("Please enter a valid Australian mobile number.");
        return;
    }


    // Vehicle
    if (vehicle.value.trim() === "") {
        alert("Please enter your vehicle.");
        return;
    }

    // Registration
    const registrationValue = registration.value.trim().toUpperCase();

    if (!/^[A-Z0-9]{6}$/.test(registrationValue)) {
        alert("Please enter a valid 6-character registration number.");
        return;
    }

    // Everything is valid
    showStep(2);
});

// STEP 3 back to STEP 2
backButton2.addEventListener("click", () => {
showStep(1);
});

// Start on Step 1
showStep(0);

const bookingForm = document.getElementById("booking-form");

// Checking if user clicks the "submit" button
bookingForm.addEventListener("submit", (event) => {

    const date = document.getElementById("wanted-date");
    const time = document.getElementById("preferred-time");

    // Form validation to prevent user submitting incomplete form
    if (date.value === "") {
        event.preventDefault();
        alert("Please select a preferred date.");
        return;
    }

    if (time.value === "") {
    event.preventDefault();
    alert("Please select a preferred time.");
    return;
    }

    // Ensures user only selects a time in the operating hours of the company
    if (time.value < "09:00" || time.value > "17:30") {
        event.preventDefault();
        alert("Please select a time between 9:00 AM and 5:30 PM.");
        return;
    }
});

// AI-ASSISTED END | ID: AI-2026-001