/*
chatbot_logs.js

Chatbot Logs UI.
*/

let logs = [];


async function loadLogs() {

    const response = await fetch(
        "/api/chatbot-logs"
    );

    logs = await response.json();

    renderLogs(logs);

}


function renderLogs(data) {

    const tbody = document.querySelector(
        "#logsTable tbody"
    );

    tbody.innerHTML = "";

    data.forEach(log => {

        const row = document.createElement("tr");

        row.innerHTML = `

            <td>

                <input
                    type="checkbox"
                    class="log-checkbox"
                    value="${log.filename}"
                >

            </td>

            <td>${log.execution_time}</td>

            <td>${log.module}</td>

            <td>

                <span class="${log.status.toLowerCase()}">

                    ${log.status}

                </span>

            </td>

            <td>${log.questions.length}</td>

            <td>

                <button
                    class="view-btn"
                    data-file="${log.filename}"
                >
                    👁 View
                </button>

                <button
                    class="delete-btn"
                    data-file="${log.filename}"
                >
                    🗑 Delete
                </button>

            </td>

        `;

        tbody.appendChild(row);

    });

}


function showLog(log) {

    let html = `

        <h2>${log.module}</h2>

        <p><b>Status:</b> ${log.status}</p>

        <p><b>Execution Time:</b> ${log.execution_time}</p>

        <p><b>Duration:</b> ${log.duration} sec</p>

        <hr>

    `;

    log.questions.forEach((q, index) => {

        html += `

            <h3>Question ${index + 1}</h3>

            <p><b>Question</b></p>

            <div class="log-box">

                ${q.question}

            </div>

            <br>

            <p><b>AI Response</b></p>

            <div class="log-box">

                ${q.response}

            </div>

            <br>

            <b>Status :</b> ${q.status}

            <hr>

        `;

    });

    html += `

        <button

            onclick="location.reload()"

            class="primary"

        >

            ← Back

        </button>

    `;

    document.querySelector(".container").innerHTML = html;

}


// --------------------------------------------------
// SEARCH
// --------------------------------------------------

function initializeSearch() {

    const search = document.getElementById(
        "search"
    );

    if (!search) return;

    search.addEventListener(

        "input",

        () => {

            const text = search.value
                .toLowerCase()
                .trim();

            if (text === "") {

                renderLogs(logs);

                return;

            }

            const filtered = logs.filter(log => {

                return (

                    log.module
                        .toLowerCase()
                        .includes(text)

                    ||

                    log.status
                        .toLowerCase()
                        .includes(text)

                    ||

                    log.execution_time
                        .toLowerCase()
                        .includes(text)

                    ||

                    log.questions.some(q =>

                        q.question
                            .toLowerCase()
                            .includes(text)

                        ||

                        q.response
                            .toLowerCase()
                            .includes(text)

                    )

                );

            });

            renderLogs(filtered);

        }

    );

}


// --------------------------------------------------
// SELECT ALL
// --------------------------------------------------

function initializeSelectAll() {

    const selectAll = document.getElementById(
        "select-all"
    );

    if (!selectAll) return;

    selectAll.addEventListener(

        "change",

        () => {

            document

                .querySelectorAll(

                    ".log-checkbox"

                )

                .forEach(box => {

                    box.checked =
                        selectAll.checked;

                });

        }

    );

}


// --------------------------------------------------
// DASHBOARD
// --------------------------------------------------

function initializeDashboard() {

    const button = document.getElementById(
        "back"
    );

    if (!button) return;

    button.onclick = () => {

        window.location.href = "/";

    };

}


// --------------------------------------------------
// DELETE SELECTED
// --------------------------------------------------

function initializeDeleteSelected() {

    const button = document.getElementById(
        "delete-selected"
    );

    if (!button) return;

    button.onclick = async () => {

        const filenames = [];

        document

            .querySelectorAll(

                ".log-checkbox:checked"

            )

            .forEach(box => {

                filenames.push(box.value);

            });

        if (filenames.length === 0) {

            alert(

                "No logs selected."

            );

            return;

        }

        if (

            !confirm(

                `Delete ${filenames.length} log(s)?`

            )

        ) {

            return;

        }

        await fetch(

            "/api/chatbot-logs/delete-selected",

            {

                method: "POST",

                headers: {

                    "Content-Type":

                        "application/json"

                },

                body: JSON.stringify({

                    filenames

                })

            }

        );

        loadLogs();

    };

}


// --------------------------------------------------
// DELETE ALL
// --------------------------------------------------

function initializeDeleteAll() {

    const button = document.getElementById(
        "delete-all"
    );

    if (!button) return;

    button.onclick = async () => {

        if (

            !confirm(

                "Delete ALL chatbot logs?"

            )

        ) {

            return;

        }

        await fetch(

            "/api/chatbot-logs/delete-all",

            {

                method: "DELETE"

            }

        );

        loadLogs();

    };

}


// --------------------------------------------------
// EVENTS
// --------------------------------------------------

document.addEventListener(

    "click",

    async event => {

        if (

            event.target.classList.contains(

                "view-btn"

            )

        ) {

            const response = await fetch(

                "/api/chatbot-logs/" +

                event.target.dataset.file

            );

            const log = await response.json();

            showLog(log);

        }

        if (

            event.target.classList.contains(

                "delete-btn"

            )

        ) {

            if (

                !confirm(

                    "Delete this log?"

                )

            ) {

                return;

            }

            await fetch(

                "/api/chatbot-logs/" +

                event.target.dataset.file,

                {

                    method: "DELETE"

                }

            );

            loadLogs();

        }

    }

);


// --------------------------------------------------
// START
// --------------------------------------------------

window.addEventListener(

    "DOMContentLoaded",

    () => {

        loadLogs();

        initializeSearch();

        initializeDashboard();

        initializeDeleteSelected();

        initializeDeleteAll();

        initializeSelectAll();

    }

);