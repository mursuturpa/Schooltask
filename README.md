<!DOCTYPE html>
<html>

<body>

<h1>Groq API Integration</h1>
<p class="subtitle">An example project demonstrating how to integrate an API (mocked as Groq API) with FastAPI, including translation capabilities via a Hugging Face model.</p>

<hr />

<div class="section">
    <h2>Overview</h2>
    <p>
        This repository shows a simple proof-of-concept for integrating a <strong>Groq API token</strong> with a <strong>FastAPI</strong> backend. 
        The API presented here:
    </p>
    <ul>
        <li>Expects a JSON payload with text in English.</li>
        <li>Authenticates using a <code>GROQ_API_TOKEN</code> (mocked). </li>
        <li>Translates the text into another language (e.g., Spanish) using a <a href="https://huggingface.co/Helsinki-NLP/">Hugging Face MarianMT model</a>.</li>
        <li>Returns the translated text in JSON form.</li>
    </ul>
</div>

<div class="section">
    <h2>Project Structure</h2>
    <p>The main file is:</p>
    <ul>
        <li><code>app.py</code>: FastAPI application containing one endpoint (<code>/translate</code>) which demonstrates the API call and translation.</li>
    </ul>
</div>

<div class="section">
    <h2>Installation & Requirements</h2>
    <p>Recommended steps:</p>
    <ol>
        <li>Clone this repository or download the files.</li>
        <li>Install Python 3.7+ and create a virtual environment (optional):</li>
    </ol>
    <pre><code>python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
</code></pre>
    <ol start="3">
        <li>Install required dependencies:</li>
    </ol>
    <pre><code>pip install fastapi uvicorn transformers
</code></pre>
    <p>Note: If you need GPU acceleration for large translations, you can also install 
    <code>torch</code> <em>with CUDA</em> from the official PyTorch website.</p>
</div>

<div class="section">
    <h2>Usage</h2>
    <p>To run the FastAPI server:</p>
    <pre><code># If you have an environment variable for the Groq token, set it:
export GROQ_API_TOKEN="my_mock_groq_api_token_12345"

# Then run the server:
uvicorn app:app --host 0.0.0.0 --port 8000
</code></pre>
    <p>Once the server is running, you can visit <code>http://0.0.0.0:8000/docs</code> or 
    <code>http://127.0.0.1:8000/docs</code> (depending on your environment) to see an 
    auto-generated Swagger UI, test the endpoint, and visualize the request and response schema.</p>
</div>

<div class="section">
    <h2>API Endpoint</h2>
    <p>
        <strong>POST /translate</strong><br>
        Expects a JSON payload in the format:
    </p>
    <pre><code>{
    "text": "Hello, how are you?"
}
</code></pre>
    <p>
        If the <code>GROQ_API_TOKEN</code> environment variable is set, the endpoint will 
        invoke a Hugging Face MarianMT model to translate the text into Spanish. 
        The response is a JSON object:
    </p>
    <pre><code>{
    "translated_text": "Hola, ¿cómo estás?"
}
</code></pre>
</div>

<div class="section">
    <h2>Files</h2>
    <ul>
        <li><code>app.py</code> — The main FastAPI application.</li>
        <li><code>requirements.txt</code> (optional) — Can be used to pin down exact library versions.</li>
        <li><em>Other configuration files</em> or scripts as needed.</li>
    </ul>
</div>

<div class="section">
    <h2>Extending This Project</h2>
    <p>You can extend the sample to any other translations, or even add additional endpoints for tasks like summarization, sentiment analysis, or custom NLP pipelines. Simply modify:</p>
    <ul>
        <li>The <code>model_name</code> in <code>app.py</code> to any supported Hugging Face model.</li>
        <li>The logic to handle multiple languages or tasks (question answering, text generation, etc.).</li>
    </ul>
</div>

<div class="section">
    <h2>License</h2>
    <p>
        This project is provided as-is for demonstration purposes. You can integrate the code into your own 
        solutions as needed.
    </p>
</div>


</body>
</html>
