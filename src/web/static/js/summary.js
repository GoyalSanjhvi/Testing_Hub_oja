/*
summary.js

Updates dashboard summary.
*/

export function updateSummary() {

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

            if (status === "FAIL") {

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