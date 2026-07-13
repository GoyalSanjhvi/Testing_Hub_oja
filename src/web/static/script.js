// =============================================
// OJA Regression Framework
// script.js
// =============================================

// -------------------------------------
// Execution Mode
// -------------------------------------

function getMode() {

    return document.querySelector(
        'input[name="mode"]:checked'
    ).value;

}


// -------------------------------------
// Report Button
// -------------------------------------

const reportButton = document.getElementById("report");

document
.querySelectorAll('input[name="mode"]')
.forEach(radio => {

    radio.addEventListener("change", () => {

        if (getMode() === "regression") {

            reportButton.style.display = "inline-block";

        }

        else {

            reportButton.style.display = "none";

        }

    });

});


// -------------------------------------
// Summary
// -------------------------------------

function updateSummary() {

    let pass = 0;

    let fail = 0;

    let totalTime = 0;

    document
    .querySelectorAll(".module-row")
    .forEach(row => {

        const status = row
            .querySelector(".status")
            .innerText;

        const duration = row
            .querySelector(".duration")
            .innerText;

        if (status === "PASS") {

            pass++;

        }

        else if (status === "FAIL") {

            fail++;

        }

        if (duration !== "--") {

            totalTime += parseFloat(duration);

        }

    });

    document.getElementById("passed").innerText = pass;

    document.getElementById("failed").innerText = fail;

    document.getElementById("time").innerText =
        totalTime.toFixed(2) + " s";

}


// -------------------------------------
// Run One Module
// -------------------------------------

document
.querySelectorAll(".run-btn")
.forEach(button => {

    button.addEventListener("click", () => {

        const row = button.closest("tr");

        const status = row.querySelector(".status");

        const duration = row.querySelector(".duration");

        status.innerText = "RUNNING";

        status.className = "status running";

        duration.innerText = "--";

        button.disabled = true;

        button.innerText = "Running...";

        fetch("/run", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                module: button.dataset.module,

                mode: getMode()

            })

        })

        .then(response => response.json())

        .then(result => {

            duration.innerText = result.duration + " s";

            if (result.status === "PASS") {

                status.innerText = "PASS";

                status.className = "status pass";

            }

            else {

                status.innerText = "FAIL";

                status.className = "status fail";

            }

            updateSummary();

        })

        .catch(error => {

            console.error(error);

            status.innerText = "FAIL";

            status.className = "status fail";

        })

        .finally(() => {

            button.disabled = false;

            button.innerText = "▶ Run";

        });

    });

});


// -------------------------------------
// Run All Modules
// -------------------------------------

document
.getElementById("run-all")
.addEventListener("click", () => {

    const button = document.getElementById("run-all");

    button.disabled = true;

    button.innerText = "Running...";

    const rows = document.querySelectorAll(".module-row");

    rows.forEach(row => {

        row.querySelector(".status").innerText = "RUNNING";

        row.querySelector(".status").className = "status running";

        row.querySelector(".duration").innerText = "--";

    });

    fetch("/run_all", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify({

            mode: getMode()

        })

    })

    .then(response => response.json())

    .then(results => {

        rows.forEach((row, index) => {

            const result = results[index];

            if (!result) return;

            const status = row.querySelector(".status");

            const duration = row.querySelector(".duration");

            duration.innerText = result.duration + " s";

            if (result.status === "PASS") {

                status.innerText = "PASS";

                status.className = "status pass";

            }

            else {

                status.innerText = "FAIL";

                status.className = "status fail";

            }

        });

        updateSummary();

    })

    .catch(error => {

        console.error(error);

    })

    .finally(() => {

        button.disabled = false;

        button.innerText = "🚀 Run All Tests";

    });

});