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
    -   Add your `META_PAGE_ACCESS_TOKEN` and `OPENAI_API_KEY` to the `.env` file:

    ```
    META_PAGE_ACCESS_TOKEN="YOUR_META_PAGE_ACCESS_TOKEN"
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

4.  **Run the application:**

    ```bash
    python main.py
    ```

## How to Use

1.  **Set up a Facebook Page and a Meta Developer App.**
2.  **Get your Page Access Token and set up the webhook in the Meta Developer Dashboard.**
3.  **Use a tool like ngrok to expose your local server to the internet.**
4.  **Configure the webhook URL in the Meta Developer Dashboard to point to your ngrok URL.**

## Project Structure

```
.
├── .env
├── app.py
├── config.py
├── handlers
│   ├── behavior_analyzer.py
│   ├── growth_automator.py
│   └── message_handler.py
├── main.py
├── models
├── README.md
├── requirements.txt
├── static
│   └── style.css
├── templates
│   └── dashboard.html
└── utils
    └── meta_api_client.py
```
