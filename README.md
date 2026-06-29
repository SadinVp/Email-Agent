# Email Agent

A Python-based project to learn how AI agents work by building one from scratch.

## Project Goal

The objective of this project is to understand the fundamentals of AI agents instead of relying on high-level frameworks.

Rather than starting with LangChain or LangGraph, this project builds each component manually to understand how an AI agent interacts with tools.

The first tool implemented is an **Email Sending Tool**, which will later be used by an AI agent to send emails automatically.

---

## Current Progress

### ✅ Step 1: Email Sending Tool

The following features have been implemented:

* Send emails using Gmail SMTP.
* Secure authentication using a Gmail App Password.
* Store sensitive credentials in a `.env` file.
* Load environment variables using `python-dotenv`.
* Create email messages using Python's `EmailMessage` class.
* Handle errors using `try` and `except`.
* Return structured responses indicating success or failure.

Example response:

```python
{
    "success": True,
    "message": "Email sent successfully."
}
```

---

## Project Structure

```
email-agent/
│
├── main.py
├── config.py
├── .env
├── requirements.txt
│
└── tools/
    └── email_tool.py
```

---

## Technologies Used

* Python 3
* SMTP (Simple Mail Transfer Protocol)
* Gmail SMTP Server
* python-dotenv

---

## Installation

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Create a virtual environment.

```bash
python -m venv .venv
```

3. Activate the virtual environment.

**Windows**

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

4. Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

> **Note:** Use a Gmail App Password instead of your normal Gmail password.

---

## How to Run

```bash
python main.py
```

If the email is sent successfully, the program returns:

```python
{
    "success": True,
    "message": "Email sent successfully."
}
```

---

## What I Learned

Through this step, I learned:

* How SMTP works for sending emails.
* Why environment variables should be used for sensitive credentials.
* How to build reusable Python functions.
* How to structure a Python project.
* Basic error handling with `try`/`except`.
* How tools form the foundation of an AI agent.

---

## Next Steps

* Build a simple rule-based email agent.
* Allow users to provide email details interactively.
* Integrate an LLM to understand natural language.
* Enable the AI agent to decide when to use the email tool.
* Add support for contacts, attachments, and memory.
