/*
=========================================================
Modal Controller
=========================================================
*/

export class Modal {

    static open(id) {

        const modal = document.getElementById(id);

        if (!modal) return;

        modal.classList.add("show");

        document.body.style.overflow = "hidden";

    }

    static close(id) {

        const modal = document.getElementById(id);

        if (!modal) return;

        modal.classList.remove("show");

        document.body.style.overflow = "auto";

    }

    static initialize() {

        document.querySelectorAll(".close-btn").forEach(button => {

            button.addEventListener(

                "click",

                () => {

                    const modal = button.closest(".modal");

                    modal.classList.remove("show");

                    document.body.style.overflow = "auto";

                }

            );

        });

        document.querySelectorAll(".modal").forEach(modal => {

            modal.addEventListener(

                "click",

                e => {

                    if (e.target === modal) {

                        modal.classList.remove("show");

                        document.body.style.overflow = "auto";

                    }

                }

            );

        });

    }

}