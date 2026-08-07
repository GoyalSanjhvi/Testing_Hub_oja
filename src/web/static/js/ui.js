/*
=========================================================
ui.js

UI Helper Functions
=========================================================
*/

let currentMode = "VISUAL";

/* ==========================================
Get Current Mode
========================================== */

export function getMode() {

    return currentMode;

}

/* ==========================================
Set Mode
========================================== */

export function setMode(mode) {

    currentMode = mode;

}

/* ==========================================
Initialize Mode Dropdown
========================================== */

export function initializeReportButton() {

    const button = document.getElementById(
        "mode-button"
    );

    const menu = document.getElementById(
        "mode-menu"
    );

    const text = button.querySelector(
        ".mode-text"
    );

    document.querySelectorAll(
        ".mode-item"
    ).forEach(item => {

        item.addEventListener(
            "click",
            () => {

                currentMode = item.dataset.mode;

                text.textContent =
                    currentMode === "VISUAL"
                        ? "Visual"
                        : "Regression";

                menu.classList.remove(
                    "show"
                );

            }
        );

    });

}