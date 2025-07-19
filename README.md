# AI Social Media Manager

This project is a Python-based AI social media manager that connects to Meta's Graph API to send and receive messages. It's built with FastAPI and uses `python-dotenv` for managing credentials.

## Features

-   **Modular Structure:** Clean and organized codebase.
-   **Secure Configuration:** Uses a `.env` file to keep your credentials safe.
-   **AI-Powered Responses:** Integrates with OpenAI to generate human-like responses.
-   **Easy to Extend:** Add new handlers and features with ease.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/ai-social-media-manager.git
    cd ai-social-media-manager
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure your credentials:**

    -   Create a `.env` file in the root of the project.
    -   Add your `META_PAGE_ACCESS_TOKEN`, `META_VERIFY_TOKEN`, and `OPENAI_API_KEY` to the `.env` file:

    ```
    META_PAGE_ACCESS_TOKEN="YOUR_META_PAGE_ACCESS_TOKEN"
    META_VERIFY_TOKEN="YOUR_META_VERIFY_TOKEN"
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

4.  **Run the application:**

    ```bash
    uvicorn main:app --reload
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
├── handlers
│   └── message_handler.py
├── main.py
├── models
├── README.md
├── requirements.txt
└── utils
    └── meta_api_client.py
```
