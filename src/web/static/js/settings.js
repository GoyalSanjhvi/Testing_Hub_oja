/*
=========================================================
Settings
=========================================================
*/

import { Modal } from "./modal.js";

export function initializeSettings() {

    const button = document.getElementById(

        "settings-button"

    );

    if (!button) return;

    button.addEventListener(

        "click",

        () => {

            alert(

                "⚙ Settings\n\nComing Soon."

            );

        }

    );

}