
# ChatOnlyBot

ChatOnlyBot is a minimalist, ChatGPT-inspired chatbot application. Its purpose is to provide an interactive chat interface through a web browser, facilitating user-bot conversations. It adopts a dark-themed UI, with message bubbles and a layout reminiscent of ChatGPT. This project is intended as a simple, customizable boilerplate that can be adapted to various language model backends or APIs.

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Architecture](#architecture)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [License](#license)

## Features
- **Dark Theme:** A sleek, modern dark-themed UI that is easy on the eyes.
- **Responsive Design:** Works well on desktop and mobile displays.
- **ChatGPT-like Interface:** Clean and simple chat layout with user and bot bubbles aligned opposite each other.
- **Markdown Formatting:** Messages from the bot are processed as HTML, enabling support for **bold**, *italic*, and `code` formatting, as well as line breaks and lists.
- **Simple Backend API:** A Flask-based server exposes a `/chat` endpoint for handling user requests and returning responses from the model.
- **Easy Integration:** The front-end is designed to integrate seamlessly with any backend model endpoint, making it easy to switch between different APIs or language models.

## Demo
To see ChatOnlyBot in action:
1. Run the Flask server (instructions below).
2. Open your browser and navigate to `http://localhost:5000`.
3. Type a message and click "Send."

You should see the bot’s response rendered on the screen.

## Prerequisites
- **Python 3.7+**
- **Flask:** Used to serve the backend API.
- **Requests:** Used by the backend to query the model endpoint.
- **Markdown Library:** For converting bot responses from Markdown to HTML.
  
You can install these prerequisites using:
```bash
pip install flask requests markdown
```

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/ChatOnlyBot.git
   cd ChatOnlyBot
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   *(If you don’t have a `requirements.txt` file, just run the `pip install` commands mentioned in [Prerequisites](#prerequisites).)*

3. **Set up Backend:**
   By default, ChatOnlyBot communicates with a language model running on a local endpoint (e.g., `localhost:11434`). If you have a different endpoint, update the Flask API code as needed in `app.py`.

## Usage
1. **Start the Flask Server:**
   ```bash
   python app.py
   ```
   This starts the web server on `http://localhost:5000`.

2. **Open the Web Interface:**
   Open your browser and navigate to `http://localhost:5000`.  
   You’ll see the ChatOnlyBot interface. Type your message and press "Send" or hit Enter to communicate with the bot.

3. **Interact With Your Bot:**
   All messages from the user and the bot will appear in the chat box. The bot’s responses will be formatted according to the HTML and Markdown rules set in the backend. Scroll to read older messages as desired.

## Configuration
- **Backend Model URL:** If you are using Ollama or another LLM running locally, modify `OLLAMA_API_URL` in `app.py` to match your LLM’s endpoint.
- **Model Name and Parameters:** Update the `data` dictionary in `app.py` if you want to use a different model or prompt settings.
- **Markdown to HTML Conversion:** The backend uses `markdown` library to convert bot responses to HTML. If the responses are not in Markdown, you can remove or modify this step.

## Architecture
- **Frontend (index.html):** 
  - A dark-themed HTML/CSS/JS interface for sending messages and displaying responses.
  - Uses `fetch()` to send POST requests to the `/chat` endpoint.
  - Renders bot responses as HTML, allowing for rich text formatting.

- **Backend (app.py):**
  - A Flask server exposing:
    - `GET /`: Serves the HTML file.
    - `POST /chat`: Accepts a JSON body with `message`, sends it to the language model endpoint, and returns a formatted response.
  - Integrates Markdown conversion before returning the response.
  
- **Language Model API:**
  - By default, targets `http://localhost:11434/api/generate` (Ollama API).
  - Easily replaceable with any other LLM or conversation endpoint.

## Customization
- **Styling:** 
  Modify `index.html`’s `<style>` section to change colors, fonts, margins, or layout.
- **Message Formatting:**
  Update the `appendMessage()` function in `index.html` to change how messages are displayed (e.g., add timestamps, user avatars, etc.).
- **Key Bindings:**
  By default, pressing Enter sends a message. You can modify this behavior in the JavaScript code.

## Troubleshooting
- **No Response from Server:**
  - Check that the Flask server is running correctly.
  - Verify that the LLM API endpoint is reachable and returns a valid response.
- **Markdown Not Rendering:**
  - Ensure `markdown` library is installed and imported in `app.py`.
  - Confirm that the backend sets `response_html = markdown(response_text)` before returning.
  - On the frontend, ensure `msg.innerHTML = text` is used instead of `textContent`.
  
- **CORS Issues:**
  - If you’re hosting the front-end and back-end on different domains, enable CORS in `app.py`.

## FAQ
**Q:** Can I use another LLM or API endpoint instead of Ollama?  
**A:** Yes. Simply update the `OLLAMA_API_URL` and the JSON payload in `app.py` to point to your desired API.

**Q:** How can I deploy this to production?  
**A:** For production, consider using a production-ready server (e.g., Gunicorn or uWSGI) in front of Flask. Ensure HTTPS is configured, and secure your endpoints as needed.

**Q:** Can I customize the model parameters sent to the API?  
**A:** Absolutely. Edit the `data` object in `app.py` and include any parameters your target LLM endpoint supports.

## License
This project is released under the [MIT License](LICENSE). Feel free to use, modify, and distribute as you see fit.
```