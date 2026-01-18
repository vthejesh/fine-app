"use strict";

/**
 * Application entry point
 */
(function main() {
    console.log("Application started");

    initializeApp();
})();

/**
 * Initialize the application
 */
function initializeApp() {
    registerEventListeners();
    loadInitialData();
}

/**
 * Register all DOM event listeners
 */
function registerEventListeners() {
    const submitBtn = document.getElementById("submitBtn");

    if (submitBtn) {
        submitBtn.addEventListener("click", handleSubmit);
    }
}

/**
 * Load initial data if required
 */
function loadInitialData() {
    // Example: fetch data from API
    // fetchDataFromServer();
}

/**
 * Handle submit button click
 */
function handleSubmit(event) {
    event.preventDefault();

    try {
        const inputValue = getInputValue("username");
        validateInput(inputValue);

        console.log("Submitted value:", inputValue);

        // TODO: Call API or process data here
    } catch (error) {
        console.error("Error:", error.message);
        showError(error.message);
    }
}

/**
 * Get input value safely
 */
function getInputValue(elementId) {
    const element = document.getElementById(elementId);

    if (!element) {
        throw new Error("Input element not found");
    }

    return element.value.trim();
}

/**
 * Validate user input
 */
function validateInput(value) {
    if (!value) {
        throw new Error("Input cannot be empty");
    }
}

/**
 * Display error message to user
 */
function showError(message) {
    alert(message);
}
