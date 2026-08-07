/*
=========================================================
script.js

Application Entry Point
=========================================================
*/

import {

    initializeExecution

} from "./execution.js";

import {

    initializeEvidence

} from "./evidence.js";

import {

    initializeMode

} from "./mode.js";

import {

    initializeSettings

} from "./settings.js";

import {

    updateSummary

} from "./summary.js";

import {

    Modal

} from "./modal.js";


window.addEventListener(

    "DOMContentLoaded",

    () => {

        console.clear();

        console.log(

            "🧪 OJA Automation Framework"

        );

        console.log(

            "Initializing Dashboard..."

        );

        // ----------------------------------
        // Initialize UI
        // ----------------------------------

        Modal.initialize();

        initializeMode();

        initializeSettings();

        initializeEvidence();

        initializeExecution();

        // ----------------------------------
        // Summary
        // ----------------------------------

        updateSummary();

        console.log(

            "Dashboard Ready."

        );

    }

);