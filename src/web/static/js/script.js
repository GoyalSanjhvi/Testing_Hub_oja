/*
script.js

Entry Point.
*/

import {
    initializeReportButton
} from "./ui.js";

import {
    initializeExecution
} from "./execution.js";


function updateApplicationUI() {

    const application = document.getElementById("application").value;

    const logsButton = document.getElementById("chatbot-logs");

    if (!logsButton) {

        return;

    }

    if (application === "oja") {

        logsButton.style.display = "inline-block";

    }

    else {

        logsButton.style.display = "none";

    }

}


window.addEventListener(

    "DOMContentLoaded",

    () => {

        initializeReportButton();

        initializeExecution();

        // -----------------------------
        // Chatbot Logs Button
        // -----------------------------

        const logsButton = document.getElementById(

            "chatbot-logs"

        );

        if (logsButton) {

            logsButton.addEventListener(

                "click",

                () => {

                    window.location.href =

                        "/chatbot-logs";

                }

            );

        }

        // -----------------------------
        // Application Change
        // -----------------------------

        const application = document.getElementById(

            "application"

        );

        if (application) {

            application.addEventListener(

                "change",

                updateApplicationUI

            );

        }

        updateApplicationUI();

    }

);