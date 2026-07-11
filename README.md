# Py - AI Learning Buddy

Py - AI Learning Buddy is an AI-powered educational web application built with Streamlit and Google's Gemini API. It helps beginners understand programming concepts through simple explanations, real-life examples, interactive quizzes, and question-answering.

## Features

* Explain programming concepts in simple language
* Generate real-life examples for better understanding
* Create interactive multiple-choice quizzes
* Answer programming-related questions
* Download generated responses
* View previous conversation history
* Clean and user-friendly interface

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* JSON
* Regular Expressions

## Project Structure

```text
Py-AI-Learning-Buddy/
│
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml (Local Development Only)
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Py-AI-Learning-Buddy.git
```

```bash
cd Py-AI-Learning-Buddy
```

### 2. Create a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Get a Gemini API Key

1. Visit Google AI Studio.
2. Create a Gemini API key.
3. Copy the generated API key.

Do not hardcode the API key in your source code.

## Configure Secrets

### Local Development

Create the following file:

```text
.streamlit/secrets.toml
```

Add:

```toml
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
```

### Streamlit Community Cloud

Open your application.

Go to:

```
Manage App
Settings
Secrets
```

Add:

```toml
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
```

Save the changes and Streamlit will automatically restart the application.

## Running the Application

```bash
streamlit run app.py
```

If the `streamlit` command is not recognized:

```bash
python -m streamlit run app.py
```

## Requirements

Example `requirements.txt`

```text
streamlit
google-generativeai
```

Or install manually:

```bash
pip install streamlit google-generativeai
```

## Application Workflow

1. Enter a programming topic.
2. Select one of the available learning activities.
3. Click Generate.
4. Read the AI-generated explanation or example.
5. Take quizzes and view instant feedback.
6. Download responses if needed.
7. Review previous conversations.

## Activities

* Explain Concept
* Real-Life Example
* Generate Quiz
* Ask Anything

## Security

* Never store API keys directly in the source code.
* Use Streamlit Secrets for deployment.
* Add the following to `.gitignore`:

```text
.streamlit/secrets.toml
.env
```

If an API key has been accidentally committed to GitHub:

1. Remove it from the code.
2. Generate a new API key.
3. Revoke the exposed key.
4. Push the updated code.

## Deployment

### Streamlit Community Cloud

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Create a new application.
4. Select your repository.
5. Set the main file as:

```text
app.py
```

6. Add your API key under **Settings → Secrets**.
7. Deploy the application.

## Future Improvements

* Support for multiple programming languages
* Voice-based interaction
* Learning progress tracking
* User authentication
* Dark mode
* Code execution environment
* Personalized learning recommendations

## License

This project is intended for educational purposes.
