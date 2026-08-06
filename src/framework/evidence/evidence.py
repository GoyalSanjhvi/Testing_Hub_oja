"""
evidence.py

Evidence manager.
"""

import json

from datetime import datetime

from src.framework.logger import Logger

from .models import EvidenceStep
from .storage import EvidenceStorage


class Evidence:

    _steps = {}

    # --------------------------------------------------
    # Record Step
    # --------------------------------------------------

    @classmethod
    def step(

        cls,

        page,

        application,

        module,

        title,

        status="PASS"

    ):

        folder = EvidenceStorage.module_folder(

            application,

            module

        )

        key = f"{application}/{module}"

        if key not in cls._steps:

            cls._steps[key] = []

        number = len(

            cls._steps[key]

        ) + 1

        safe_name = (

            title

            .replace(" ", "_")

            .replace("/", "_")

            .replace("\\", "_")

        )

        screenshot = (

            folder

            / f"{number:02d}_{safe_name}.png"

        )

        html = (

            folder

            / f"{number:02d}_{safe_name}.html"

        )

        # ------------------------------------------
        # Screenshot
        # ------------------------------------------

        page.screenshot(

            path=str(screenshot),

            full_page=True

        )

        # ------------------------------------------
        # HTML
        # ------------------------------------------

        html.write_text(

            page.content(),

            encoding="utf-8"

        )

        # ------------------------------------------
        # Step Model
        # ------------------------------------------

        step = EvidenceStep(

            application=application,

            module=module,

            step=number,

            title=title,

            status=status,

            timestamp=datetime.now().strftime(

                "%H:%M:%S"

            ),

            screenshot=screenshot.name,

            html=html.name

        )

        cls._steps[key].append(

            step

        )

        # ------------------------------------------
        # Save JSON
        # ------------------------------------------

        with open(

            folder / "steps.json",

            "w",

            encoding="utf-8"

        ) as fp:

            json.dump(

                [

                    vars(s)

                    for s in cls._steps[key]

                ],

                fp,

                indent=4

            )

        # ------------------------------------------
        # Execution Log
        # ------------------------------------------

        with open(

            folder / "execution.log",

            "a",

            encoding="utf-8"

        ) as fp:

            fp.write(

                f"[{step.timestamp}] "

                f"{title} "

                f"[{status}]\n"

            )

        # ------------------------------------------
        # Console
        # ------------------------------------------

        Logger.step(

            module,

            number,

            title

        )

        Logger.screenshot(

            screenshot

        )

        Logger.html(

            html

        )

        return step

    # --------------------------------------------------
    # Clear Module
    # --------------------------------------------------

    @classmethod
    def clear(

        cls,

        application,

        module

    ):

        EvidenceStorage.clear_module(

            application,

            module

        )

        key = f"{application}/{module}"

        cls._steps[key] = []