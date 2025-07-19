# 🚀 AI Social Bot 🚀

This project is a Python-based AI social media bot that connects to Meta's Graph API to send and receive messages. It's built with a modular structure and uses `python-dotenv` for managing credentials.

## Features

-   **Modular Structure:** Clean and organized codebase with a unique futuristic theme.
-   **Secure Configuration:** Uses a `.env` file to keep your credentials safe.
-   **API-Centric:** All interactions with Meta are handled through the Graph API.
-   **AI-Powered:** Integrates with OpenAI to generate human-like responses and perform sentiment analysis.
-   **Growth Automation:** Includes modules for following leads and suggesting content.
-   **Behavior Analysis:** Tracks client engagement and other metrics.
-   **Web UI Dashboard:** A simple Flask-based dashboard to monitor logs, stats, and the message queue.
-   **Scheduled Jobs:** Uses `schedule` to run tasks periodically.
-   **Advanced Features:** Includes a wide range of advanced features, such as a persona handler, emotion responder, security filter, and more.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/ai-social-bot.git
    cd ai-social-bot
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure your credentials:**

    -   Create a `.env` file in the `ai_social_bot` directory.
    -   Add your `PAGE_ACCESS_TOKEN`, `VERIFY_TOKEN`, `GRAPH_API_BASE`, and `OPENAI_API_KEY` to the `.env` file.

4.  **Run the application:**

    ```bash
    python main.py
    ```

## Project Structure

```
.
├── .env
├── config.py
├── growth
│   ├── lead_scanner.py
│   └── spiritual_uplifter.py
├── handlers
│   ├── emotion_responder.py
│   ├── message_handler.py
│   ├── persona_handler.py
│   └── welcome_greeter.py
├── main.py
├── memory
│   └── user_memory.py
├── models
│   └── engagement_forecaster.py
├── README.md
├── requirements.txt
└── utils
    ├── language_router.py
    ├── meta_api_client.py
    ├── post_composer.py
    └── security_filter.py
```
