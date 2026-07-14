/*
execution.js

Handles module execution.
*/

import {
    getMode
} from "./ui.js";

import {
    updateSummary
} from "./summary.js";


async function executeModule(row) {

    const button = row.querySelector(".run-btn");

    const status = row.querySelector(".status");

    const duration = row.querySelector(".duration");

    button.disabled = true;

    status.innerText = "RUNNING";

    status.className = "status running";

    duration.innerText = "--";

    try {

        const response = await fetch("/run", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                module: button.dataset.module,

                mode: getMode()

            })

        });

        const result = await response.json();

        duration.innerText = result.duration + " s";

        if (result.status === "PASS") {

            status.innerText = "PASS";

            status.className = "status pass";

        }

        else {

            status.innerText = "FAIL";

            status.className = "status fail";

        }

    }

    catch (error) {

        console.error(error);

        status.innerText = "FAIL";

        status.className = "status fail";

    }

    finally {

        button.disabled = false;

        button.innerText = "▶ Run";

        updateSummary();

    }

}


export function initializeExecution() {

    // -----------------------------
    // Individual Run
    // -----------------------------

    document
        .querySelectorAll(".run-btn")
        .forEach(button => {

            button.addEventListener("click", async () => {

                const row = button.closest("tr");

                await executeModule(row);

            });

        });


    // -----------------------------
    // Run All
    // -----------------------------

    document
        .getElementById("run-all")
        .addEventListener("click", async () => {

            const runAll = document.getElementById("run-all");

            runAll.disabled = true;

            runAll.innerText = "Running...";

            const rows = document.querySelectorAll(".module-row");

            document
                .querySelectorAll(".run-btn")
                .forEach(btn => btn.disabled = true);

            for (const row of rows) {

                await executeModule(row);

            }

            document
                .querySelectorAll(".run-btn")
                .forEach(btn => btn.disabled = false);

            runAll.disabled = false;

            runAll.innerText = "🚀 Run All Tests";

        });

}