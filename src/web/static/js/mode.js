/*
=========================================================
Execution Mode
=========================================================
*/

export function initializeMode() {

    const button = document.getElementById(

        "mode-button"

    );

    const menu = document.getElementById(

        "mode-menu"

    );

    if (!button || !menu)

        return;

    button.addEventListener(

        "click",

        () => {

            menu.classList.toggle(

                "show"

            );

        }

    );

    document.querySelectorAll(

        ".mode-item"

    ).forEach(item => {

        item.addEventListener(

            "click",

            () => {

                const mode = item.dataset.mode;

                button.innerHTML =

                    mode === "VISUAL"

                    ? "🟢 Visual <span>▼</span>"

                    : "⚡ Regression <span>▼</span>";

                localStorage.setItem(

                    "executionMode",

                    mode

                );

                menu.classList.remove(

                    "show"

                );

            }

        );

    });

    const saved = localStorage.getItem(

        "executionMode"

    );

    if (saved) {

        button.innerHTML =

            saved === "VISUAL"

            ? "🟢 Visual <span>▼</span>"

            : "⚡ Regression <span>▼</span>";

    }

    document.addEventListener(

        "click",

        e => {

            if (

                !button.contains(e.target) &&

                !menu.contains(e.target)

            ) {

                menu.classList.remove(

                    "show"

                );

            }

        }

    );

}