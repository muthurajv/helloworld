# Azure OpenAI Web App

A simple Flask web application that interacts with Microsoft Azure OpenAI.

## Setup

1. Create a virtual environment and activate it:
   ```
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set environment variables:
   - `AZURE_OPENAI_API_KEY`: Your Azure OpenAI API key
   - `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint URL

   You can set them in your terminal:
   ```
   $env:AZURE_OPENAI_API_KEY = "your-api-key"
   $env:AZURE_OPENAI_ENDPOINT = "https://your-resource.openai.azure.com/"
   ```

4. Run the app:
   ```
   python app.py
   ```

5. Open your browser to `http://127.0.0.1:5000/`

## Notes

- Replace `"gpt-35-turbo"` in `app.py` with your actual deployment name in Azure OpenAI.
- This is a basic "Hello World" example. Enhance as needed.