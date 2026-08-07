/*
=========================================================
progress.js

Execution Progress Controller
=========================================================
*/

let startTime = null;

let timer = null;

let totalModules = 0;

let completedModules = 0;


/* =====================================================
Show
===================================================== */

export function showProgress(total) {

    totalModules = total;

    completedModules = 0;

    startTime = Date.now();

    const panel = document.getElementById(

        "progress-panel"

    );

    panel.classList.add(

        "show"

    );

    updateProgress(

        0,

        "",

        0

    );

    timer = setInterval(

        updateElapsed,

        1000

    );

}


/* =====================================================
Hide
===================================================== */

export function hideProgress() {

    clearInterval(

        timer

    );

    setTimeout(

        () => {

            document

                .getElementById(

                    "progress-panel"

                )

                .classList.remove(

                    "show"

                );

        },

        1500

    );

}


/* =====================================================
Update
===================================================== */

export function updateProgress(

    completed,

    currentModule,

    total = totalModules

) {

    completedModules = completed;

    totalModules = total;

    const percent =

        total === 0

        ? 0

        : Math.round(

            (completed / total) * 100

        );

    document.getElementById(

        "progress-fill"

    ).style.width =

        percent + "%";

    document.getElementById(

        "progress-percentage"

    ).textContent =

        percent + "%";

    document.getElementById(

        "completed-count"

    ).textContent =

        `${completed} / ${total}`;

    document.getElementById(

        "current-module"

    ).textContent =

        currentModule || "--";

}


/* =====================================================
Elapsed
===================================================== */

function updateElapsed() {

    if (!startTime)

        return;

    const seconds = Math.floor(

        (Date.now() - startTime)

        / 1000

    );

    let value;

    if (seconds >= 60) {

        const min = Math.floor(

            seconds / 60

        );

        const sec = seconds % 60;

        value = `${min}m ${sec}s`;

    }

    else {

        value = `${seconds}s`;

    }

    document.getElementById(

        "elapsed-time"

    ).textContent = value;

}


/* =====================================================
Complete
===================================================== */

export function completeProgress() {

    updateProgress(

        totalModules,

        "Completed"

    );

    clearInterval(

        timer

    );

}