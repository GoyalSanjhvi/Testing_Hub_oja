"""
config.py

Chatbot configuration.
"""


class ChatbotConfig:

    # -----------------------------
    # Execution
    # -----------------------------

    QUESTIONS_PER_RUN = 2

    RANDOMIZE = True

    RESPONSE_TIMEOUT = 60

    RETRY_COUNT = 2

    # -----------------------------
    # Validation
    # -----------------------------

    MIN_RESPONSE_LENGTH = 20

    REQUIRE_KEYWORDS = False

    # -----------------------------
    # Waiting
    # -----------------------------

    CHAT_OPEN_TIMEOUT = 15000

    RESPONSE_POLL_INTERVAL = 500

    # -----------------------------
    # Reporting
    # -----------------------------

    SAVE_RESPONSES = True

    SAVE_RESPONSE_TIME = True

    PRINT_RESPONSE = True