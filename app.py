from flask import Flask, request, render_template
import os
from openai import AzureOpenAI

app = Flask(__name__)

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        try:
            response = client.chat.completions.create(
                model="gpt-35-turbo",  # Replace with your deployment name
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message.content
        except Exception as e:
            answer = f"Error: {str(e)}"
        return render_template('index.html', answer=answer)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)