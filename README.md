# Email Agent

A Python project built to understand how AI agents work by implementing one from scratch, without relying on agent frameworks such as LangChain or LangGraph.

The goal is to first understand the architecture of an AI agent, how it interacts with tools, and how decisions are made before introducing Large Language Models (LLMs).

---

# Project Goal

This project focuses on learning the fundamentals of AI agents through incremental development.

Instead of using high-level frameworks, every component is built manually to understand:

* How an AI agent is structured.
* How tools are integrated.
* How an agent delegates tasks.
* How AI can later be introduced into the workflow.

---

# Current Progress

## ✅ Step 1 – Email Sending Tool

Implemented a reusable email sending tool using Gmail SMTP.

### Features

* Send emails using Gmail SMTP.
* Secure authentication using Gmail App Password.
* Store credentials securely using `.env`.
* Load environment variables using `python-dotenv`.
* Create email messages using Python's `EmailMessage`.
* Handle exceptions using `try` and `except`.
* Return structured success or failure responses.

Example response:

```python
{
    "success": True,
    "message": "Email sent successfully."
}
```

---

## ✅ Step 2 – Basic Email Agent

Implemented a simple rule-based Email Agent.

The agent:

* Collects recipient email.
* Collects email subject.
* Collects email body.
* Uses the Email Tool to send the email.
* Displays the result to the user.

At this stage, the agent is **not AI-powered**.

Its purpose is to demonstrate the relationship between an **Agent** and a **Tool**.

---

# Current Architecture

```text
                User
                  │
                  ▼
            EmailAgent
                  │
        Collect User Input
                  │
                  ▼
          send_email()
          (Email Tool)
                  │
                  ▼
            Gmail SMTP
                  │
                  ▼
         Success / Failure
                  │
                  ▼
            EmailAgent
                  │
                  ▼
          Display Result
```

---

# Project Structure

```text
email-agent/
│
├── main.py
├── agent.py
├── config.py
├── requirements.txt
├── .env
│
└── tools/
    └── email_tool.py
```

---

# Technologies Used

* Python 3
* SMTP (Simple Mail Transfer Protocol)
* Gmail SMTP Server
* python-dotenv

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd email-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```text
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

> **Important:** Use a Gmail App Password instead of your regular Gmail password.

---

# Running the Project

Execute:

```bash
python main.py
```

The Email Agent will ask for:

* Recipient Email
* Subject
* Email Body

Once the information is collected, it uses the Email Tool to send the email and displays whether the operation was successful.

---

# What I Learned

Through this project, I learned:

* How SMTP works.
* How Gmail authentication works using App Passwords.
* How to securely manage credentials using environment variables.
* How to build reusable Python modules.
* Error handling using `try` and `except`.
* The difference between an **Agent** and a **Tool**.
* How an agent delegates work to specialized tools.

---

# Current Workflow

```text
User
   │
   ▼
EmailAgent
   │
   ├── Ask for recipient
   ├── Ask for subject
   ├── Ask for body
   │
   ▼
Email Tool
(send_email)
   │
   ▼
Gmail SMTP
   │
   ▼
Response
   │
   ▼
EmailAgent
   │
   ▼
Display Result
```

---

# Next Steps

* Replace manual user input with an LLM.
* Allow users to describe emails using natural language.
* Extract recipient, subject, and body automatically.
* Add conversation memory.
* Integrate a contacts tool.
* Support email attachments.
* Introduce multiple tools.
* Build a complete AI-powered Email Agent.

---

# Future Vision

The final version of this project will evolve from a simple rule-based agent into a fully autonomous AI agent capable of understanding natural language, reasoning about user requests, selecting the appropriate tools, and completing tasks with minimal user interaction.
