/*
=========================================================
execution.js

Handles Test Execution
=========================================================
*/

import { getMode } from "./ui.js";
import { updateSummary } from "./summary.js";

function getApplication() {

    return document
        .getElementById("application")
        .value;

}

async function executeModule(row) {

    const button = row.querySelector(".run-btn");
    const status = row.querySelector(".status");
    const duration = row.querySelector(".duration");

    button.disabled = true;
    button.textContent = "⏳ Running";

    status.textContent = "RUNNING";
    status.className = "status running";

    duration.textContent = "--";

    try {

        const response = await fetch("/run", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                application: getApplication(),

                module: button.dataset.module,

                mode: getMode()

            })

        });

        const result = await response.json();

        console.log(result);

        duration.textContent =
            `${result.duration} s`;

        if (result.status === "PASS") {

            status.textContent = "PASS";
            status.className = "status pass";

        }

        else {

            status.textContent = "FAIL";
            status.className = "status fail";

        }

    }

    catch (error) {

        console.error(error);

        status.textContent = "FAIL";
        status.className = "status fail";

    }

    finally {

        button.disabled = false;
        button.textContent = "▶ Execute";

        updateSummary();

    }

}

export function initializeExecution() {

    document.addEventListener(

        "click",

        async (event) => {

            const button = event.target.closest(".run-btn");

            if (!button)
                return;

            const row = button.closest(".module-row");

            await executeModule(row);

        }

    );

    const runAll = document.getElementById("run-all");

    if (!runAll)
        return;

    runAll.addEventListener(

        "click",

        async () => {

            const rows = document.querySelectorAll(".module-row");

            runAll.disabled = true;

            for (const row of rows) {

                await executeModule(row);

            }

            runAll.disabled = false;

            runAll.textContent = "🚀 Run All Tests";

        }

    );

}