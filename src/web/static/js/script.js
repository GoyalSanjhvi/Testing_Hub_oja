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

import {
    initializeEvidence
} from "./evidence.js";


window.addEventListener(

    "DOMContentLoaded",

    () => {

        // ------------------------------------------
        // Report Button
        // ------------------------------------------

        initializeReportButton();

        // ------------------------------------------
        // Execution
        // ------------------------------------------

        initializeExecution();

        // ------------------------------------------
        // Logs & Evidence
        // ------------------------------------------

        initializeEvidence();

    }

);