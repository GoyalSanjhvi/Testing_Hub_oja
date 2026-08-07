/*
=========================================================
evidence.js

Handles Logs & Evidence
=========================================================
*/

import { Modal } from "./modal.js";

/* ==========================================
Current Application
========================================== */

function currentApplication() {

    return document
        .getElementById(
            "application"
        )
        .value;

}

/* ==========================================
Logs
========================================== */

async function openLogs(module) {

    try {

        const application = currentApplication();

        const response = await fetch(

            `/logs/${application}/${encodeURIComponent(module)}`

        );

        if (!response.ok) {

            throw new Error(

                "Unable to load logs."

            );

        }

        const data = await response.json();

        const container = document.getElementById(

            "logs-content"

        );

        container.innerHTML = "";

        if (

            !data.logs ||

            data.logs.trim() === ""

        ) {

            container.innerHTML =

                "<p>No execution logs found.</p>";

        }

        else {

            container.innerHTML = `

<pre class="log-text">${data.logs}</pre>

            `;

        }

        Modal.open(

            "logs-modal"

        );

    }

    catch (error) {

        console.error(error);

        document.getElementById(

            "logs-content"

        ).innerHTML =

            "<p>Unable to load execution logs.</p>";

        Modal.open(

            "logs-modal"

        );

    }

}

/* ==========================================
Evidence
========================================== */

async function openEvidence(module) {

    try {

        const application = currentApplication();

        const response = await fetch(

            `/evidence/${application}/${encodeURIComponent(module)}`

        );

        if (!response.ok) {

            throw new Error(

                "Unable to load evidence."

            );

        }

        const data = await response.json();

        const container = document.getElementById(

            "evidence-content"

        );

        container.innerHTML = "";

        if (

            !data.steps ||

            data.steps.length === 0

        ) {

            container.innerHTML =

                "<h3>No evidence available.</h3>";

            Modal.open(

                "evidence-modal"

            );

            return;

        }

        container.innerHTML =

            `<div class="evidence-grid"></div>`;

        const grid = container.querySelector(

            ".evidence-grid"

        );

        data.steps.forEach(step => {

            grid.innerHTML += `

<div class="evidence-card">

    <img

        src="/file/screenshot/${application}/${module}/${step.screenshot}"

        class="evidence-image"

        loading="lazy"

    >

    <div class="evidence-content">

        <div class="evidence-title">

            Step ${step.step}

        </div>

        <div class="evidence-time">

            ${step.title}

        </div>

        

</div>

            `;

        });

        document.querySelectorAll(

            ".evidence-image"

        ).forEach(image => {

            image.addEventListener(

                "click",

                () => showImage(

                    image.src

                )

            );

        });

        Modal.open(

            "evidence-modal"

        );

    }

    catch (error) {

        console.error(error);

        document.getElementById(

            "evidence-content"

        ).innerHTML =

            "<h3>Unable to load evidence.</h3>";

        Modal.open(

            "evidence-modal"

        );

    }

}

/* ==========================================
Image Viewer
========================================== */

function showImage(src) {

    let viewer = document.getElementById(

        "image-viewer"

    );

    if (!viewer) {

        viewer = document.createElement(

            "div"

        );

        viewer.id = "image-viewer";

        viewer.className = "image-viewer";

        viewer.innerHTML =

            `<img src="">`;

        document.body.appendChild(

            viewer

        );

        viewer.addEventListener(

            "click",

            () => {

                viewer.classList.remove(

                    "show"

                );

            }

        );

    }

    viewer.querySelector(

        "img"

    ).src = src;

    viewer.classList.add(

        "show"

    );

}

/* ==========================================
Initialize
========================================== */

export function initializeEvidence() {

    document.querySelectorAll(

        ".logs-btn"

    ).forEach(button => {

        button.addEventListener(

            "click",

            () =>

                openLogs(

                    button.dataset.module

                )

        );

    });

    document.querySelectorAll(

        ".evidence-btn"

    ).forEach(button => {

        button.addEventListener(

            "click",

            () =>

                openEvidence(

                    button.dataset.module

                )

        );

    });

}