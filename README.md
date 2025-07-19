# Facebook Messenger Bot

This project is a Python-based Facebook Messenger bot that uses the Meta Graph API to send and receive messages. It's built with Flask and uses `python-dotenv` for managing credentials.

## Features

-   **Modular Structure:** Clean and organized codebase.
-   **Secure Configuration:** Uses a `.env` file to keep your credentials safe.
-   **Message Handling:** Basic message handler to process incoming messages.
-   **Easy to Extend:** Add new handlers and features with ease.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/fb-messenger-bot.git
    cd fb-messenger-bot
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure your credentials:**

    -   Create a `.env` file in the root of the project.
    -   Add your `PAGE_ACCESS_TOKEN` and `VERIFY_TOKEN` to the `.env` file:

    ```
    PAGE_ACCESS_TOKEN="YOUR_PAGE_ACCESS_TOKEN"
    VERIFY_TOKEN="YOUR_VERIFY_TOKEN"
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
├── fb_messenger_bot
│   ├── api.py
│   ├── config.py
│   ├── handlers
│   │   └── message_handler.py
│   └── __init__.py
├── main.py
├── README.md
└── requirements.txt
```
