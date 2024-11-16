# FastAPI Langchain QA Bot

This application is a Question-Answering API using FastAPI and Langchain. It answers questions based on the contents of uploaded documents (PDF or JSON).

## Setup

### Prerequisites

* **Python 3.6 or later**

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/fastapi-langchain-qa-bot.git](https://github.com/your-username/fastapi-langchain-qa-bot.git)
   cd fastapi-langchain-qa-bot
   ```

2. **Create a virtual environment**:
    ```bash
   python -m venv venv
   source venv/bin/activate
    ```
3. **Install dependencies**:
   ```bash 
   pip install -r requirements.txt
   ```
4. **Configuration**:
   
   ***OpenAI API Key***
   1. Create a .env file:
      - Create a .env file in the project's root directory.
   2. Add your OpenAI API key:
      * Add the following line to your .env file, replacing <YOUR_OPENAI_API_KEY> with your actual API key:
   
       ```bash
       OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
       ```
      To get an OpenAI API key:
      * Create an OpenAI account on the OpenAI platform.
      * Obtain your API key from your account settings.

5. **Run application**:
   * Run tests (optional):
     ```bash
     pytest tests
     ```
   * Run application: 
     ```bash
     uvicorn app.main:app --reload
     ```
     This will start the FastAPI application, and you can access the API documentation at http://127.0.0.1:8000/docs.
   
   
   ***Streamlit Instructions***:
   Run locally, or use Docker.
   ```bash
      streamlit run app/ui/app.py
   ```
   Access the UI at http://localhost:8501.

6. **Docker**(Optional):
   ```bash
    docker build -t fastapi-langchain-app .
    docker run -p 8000:8000 fastapi-langchain-app
   ```

7. **API Documentation: Visit** http://localhost:8000/docs to explore the API.
    ```bash
   This should provide a comprehensive guide to setting up, running, and testing the FastAPI app with Langchain.
   ```

**Security Details**:
* Use .env for secret management.

**Important Note**:
*Do not commit your .env file to version control.* This file contains sensitive information like your OpenAI API key.
