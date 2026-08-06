/*
evidence.js

Handles Logs and Evidence.
*/

function currentApplication() {

    return document

        .getElementById(

            "application"

        )

        .value;

}


// --------------------------------------------------
// Logs
// --------------------------------------------------

async function openLogs(module) {

    const application = currentApplication();

    const response = await fetch(

        `/logs/${application}/${encodeURIComponent(module)}`

    );

    const data = await response.json();

    document.getElementById(

        "logs-content"

    ).textContent =

        data.logs || "No logs available.";

    document.getElementById(

        "logs-modal"

    ).style.display = "block";

}


// --------------------------------------------------
// Evidence
// --------------------------------------------------

async function openEvidence(module) {

    const application = currentApplication();

    const response = await fetch(

        `/evidence/${application}/${encodeURIComponent(module)}`

    );

    const data = await response.json();

    const container = document.getElementById(

        "evidence-content"

    );

    container.innerHTML = "";

    if (

        data.steps.length === 0

    ) {

        container.innerHTML =

            "<p>No evidence found.</p>";

        document.getElementById(

            "evidence-modal"

        ).style.display = "block";

        return;

    }

    data.steps.forEach(step => {

        container.innerHTML += `

            <div class="evidence-step">

                <h3>

                    Step ${step.step}

                </h3>

                <p>

                    <strong>${step.title}</strong>

                </p>

                <p>

                    ${step.timestamp}

                </p>

                <a

                    href="/file/screenshot/${step.application}/${step.module}/${step.screenshot}"

                    target="_blank"

                >

                    📷 Screenshot

                </a>

                <br>

                <a

                    href="/file/html/${step.application}/${step.module}/${step.html}"

                    target="_blank"

                >

                    🌐 HTML

                </a>

            </div>

            <hr>

        `;

    });

    document.getElementById(

        "evidence-modal"

    ).style.display = "block";

}


// --------------------------------------------------
// Initialize
// --------------------------------------------------

export function initializeEvidence() {

    document

        .querySelectorAll(

            ".logs-btn"

        )

        .forEach(button => {

            button.addEventListener(

                "click",

                () =>

                    openLogs(

                        button.dataset.module

                    )

            );

        });


    document

        .querySelectorAll(

            ".evidence-btn"

        )

        .forEach(button => {

            button.addEventListener(

                "click",

                () =>

                    openEvidence(

                        button.dataset.module

                    )

            );

        });


    document

        .getElementById(

            "close-logs"

        )

        .onclick = () =>

        document.getElementById(

            "logs-modal"

        ).style.display = "none";


    document

        .getElementById(

            "close-evidence"

        )

        .onclick = () =>

        document.getElementById(

            "evidence-modal"

        ).style.display = "none";

}