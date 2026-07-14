/*
ui.js

UI helper functions.
*/

export function getMode() {

    return document.querySelector(
        'input[name="mode"]:checked'
    ).value;

}


export function initializeReportButton() {

    const reportButton = document.getElementById("report");

    document
        .querySelectorAll('input[name="mode"]')
        .forEach(radio => {

            radio.addEventListener("change", () => {

                reportButton.style.display =
                    getMode() === "regression"
                        ? "inline-block"
                        : "none";

            });

        });

}