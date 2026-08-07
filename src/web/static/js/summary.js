/*
=========================================================
Summary
=========================================================
*/

export function updateSummary() {

    const rows = document.querySelectorAll(

        ".module-row"

    );

    let pass = 0;

    let fail = 0;

    let waiting = 0;

    let totalTime = 0;

    rows.forEach(row => {

        const status = row.querySelector(

            ".status"

        ).textContent.trim().toUpperCase();

        const duration = row.querySelector(

            ".duration"

        ).textContent;

        if (status === "PASS")

            pass++;

        else if (status === "FAIL")

            fail++;

        else

            waiting++;

        if (

            duration.includes("s")

        ) {

            totalTime += parseFloat(

                duration

            );

        }

    });

    document.getElementById(

        "pass-count"

    ).textContent = pass;

    document.getElementById(

        "fail-count"

    ).textContent = fail;

    document.getElementById(

        "waiting-count"

    ).textContent = waiting;

    document.getElementById(

        "total-count"

    ).textContent = rows.length;

    if (totalTime > 60) {

        const min = Math.floor(

            totalTime / 60

        );

        const sec = (

            totalTime % 60

        ).toFixed(1);

        document.getElementById(

            "execution-time"

        ).textContent =

            `${min}m ${sec}s`;

    }

    else {

        document.getElementById(

            "execution-time"

        ).textContent =

            `${totalTime.toFixed(2)} s`;

    }

    document.getElementById(

        "last-run"

    ).textContent =

        new Date().toLocaleString();

}