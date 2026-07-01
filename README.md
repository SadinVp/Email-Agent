# Email Agent

A Python project that builds an AI agent from scratch to understand how modern AI agents work internally before using frameworks like LangChain or LangGraph.

Instead of relying on existing libraries, this project focuses on implementing every component manually, including tools, an agent, a tool registry, and a reasoning layer.

---

# Project Goal

The objective of this project is to understand the architecture of AI agents by building one step by step.

The project demonstrates:

* Tool creation
* Agent design
* Tool registration
* Intent recognition
* Dynamic tool execution
* Gmail automation

The long-term goal is to replace the rule-based reasoning with a Large Language Model (LLM) while keeping the overall architecture unchanged.

---

# Current Features

## ✅ Gmail Email Tool

Implemented a reusable email sending tool using Gmail SMTP.

Features:

* Send emails using Gmail SMTP.
* Secure authentication using Gmail App Password.
* Credentials stored in `.env`.
* Structured success/error responses.
* Exception handling.

---

## ✅ Gmail Inbox Reader

Implemented an email reading tool using Gmail IMAP.

Features:

* Connect to Gmail Inbox.
* Read the latest emails.
* Extract sender information.
* Extract subject lines.
* Return structured email data.

---

## ✅ Email Agent

Implemented a rule-based Email Agent.

Responsibilities:

* Receive user requests.
* Detect user intent.
* Select the appropriate tool.
* Execute the selected tool.
* Display the result.

The agent does **not** directly interact with Gmail protocols.

Instead, it delegates all work to specialized tools.

---

## ✅ Tool Registry

Implemented a centralized Tool Registry.

Instead of importing every tool inside the agent, all available tools are registered in one place.

Current tools:

* Send Email
* Read Latest Emails

This makes the project scalable as new Gmail capabilities are added.

---

## ✅ Tool Abstraction

Implemented a reusable `Tool` class.

Each tool now contains:

* Name
* Description
* Parameters
* Function

Example:

```python
Tool(
    name="send_email",
    description="Send an email to a recipient",
    parameters=[
        "receiver",
        "subject",
        "body"
    ],
    function=send_email
)
```

The agent now interacts with `Tool` objects instead of raw Python functions.

---

## ✅ Intent Recognition

Implemented a rule-based reasoning layer.

Current implementation uses keyword matching.

Examples:

Input:

```text
send email
```

↓

Intent:

```text
send_email
```

Input:

```text
show inbox
```

↓

Intent:

```text
read_email
```

This module has been intentionally isolated so it can later be replaced by an LLM without changing the rest of the application.

---

# Current Architecture

```text
                    User
                      │
                      ▼
              Intent Recognizer
                      │
                      ▼
                 EmailAgent
                      │
                      ▼
                Tool Registry
          ┌───────────┴───────────┐
          ▼                       ▼
     Send Email Tool        Read Email Tool
          │                       │
          ▼                       ▼
      Gmail SMTP             Gmail IMAP
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
├── reasoning/
│   ├── __init__.py
│   └── intent.py
│
└── tools/
    ├── __init__.py
    ├── base_tool.py
    ├── registry.py
    ├── email_tool.py
    └── read_email_tool.py
```

---

# Technologies Used

* Python 3
* SMTP
* IMAP
* Gmail App Password
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

Activate the virtual environment.

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```text
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

---

# Running the Project

Start the application:

```bash
python main.py
```

Example interactions:

```text
What would you like me to do?

> send email
```

or

```text
What would you like me to do?

> read latest emails
```

The agent detects the intent, selects the appropriate tool from the registry, executes it, and displays the result.

---

# AI Agent Concepts Implemented

* Tool-based architecture
* Agent abstraction
* Tool registry
* Intent recognition
* Dynamic tool execution
* Separation of responsibilities
* Gmail integration
* Modular project structure

---

# What I Learned

Through this project, I learned:

* The difference between an AI agent and a tool.
* How SMTP and IMAP work.
* How to build reusable Python modules.
* How to design scalable software architecture.
* How a tool registry works.
* Why agent frameworks organize tools using metadata.
* How reasoning can be separated from execution.
* How to prepare an application for future LLM integration.

---

# Next Steps

* Dynamic argument collection using tool metadata.
* Search emails.
* Reply to emails.
* Delete emails.
* Draft emails using AI.
* Attach files automatically.
* Replace rule-based intent detection with an LLM.
* Introduce memory.
* Build a fully autonomous Gmail AI Agent.
