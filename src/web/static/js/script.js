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


window.addEventListener(

    "DOMContentLoaded",

    () => {

        initializeReportButton();

        initializeExecution();

        //
        // Chatbot Logs Button
        //

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

    }

);