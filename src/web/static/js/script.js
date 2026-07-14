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


window.addEventListener("DOMContentLoaded", () => {

    initializeReportButton();

    initializeExecution();

});