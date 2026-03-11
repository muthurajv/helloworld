from flask import Flask, request, render_template
import os
from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

app = Flask(__name__)

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Initialize Azure Search client
search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name=os.getenv("AZURE_SEARCH_INDEX"),
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
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

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        try:
            results = search_client.search(search_text=query)
            search_results = [doc for doc in results]
        except Exception as e:
            search_results = f"Error: {str(e)}"
        return render_template('search.html', results=search_results)
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)