# 🐶 Dog Chatbot App (Streamlit + Anthropic + Docker)

This is a fun AI chatbot demo app built with **Streamlit** and **Anthropic Claude** (Vision + LLM). The chatbot pretends to be your dog and chats in Japanese based on a generated persona from an uploaded image 🐾

---

## ✨ Features

- 📸 **Upload a dog image + name** to generate a personalized dog persona (in Japanese)
- 🤖 **LLM-powered chat** using Claude 3 (via Anthropic API)
- 🧠 **Vision AI integration** for image-based persona generation
- 🐾 **Persona saved to file** for reproducibility and easy testing
- ✍️ **Persona editor page** available at a hidden path for developer access
- 🐳 **Docker Compose** setup for easy deployment
- 🌐 **No .env needed** — secrets managed via Streamlit’s `secrets.toml`

---

## 🧪 Tech Stack

- [Streamlit](https://streamlit.io/) – front-end app framework
- [Anthropic Claude 3](https://www.anthropic.com/index/claude) – Vision + LLM API
- [LiteLLM](https://github.com/BerriAI/litellm) – abstraction layer for LLMs
- [Docker](https://www.docker.com/) – containerized deployment
- [Python 3.12](https://www.python.org/)

---

 ## File Structure
 ```
 dog-chatbot-app/
├── app/
│   ├── main.py               # Main chat UI
│   ├── utils.py              # Image processing + API calls
│   ├── persona_editor.py     # Hidden persona editing page
│   ├── persona.txt           # Generated persona (editable)
│   └── requirements.txt
├── .streamlit/
│   └── secrets.toml          # 🔐 Your API key (DO NOT COMMIT)
├── Dockerfile
├── docker-compose.yml
└── README.md
```


## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/dog-chatbot-app.git
cd dog-chatbot-app
```

### 2. Add API Key
Instead of using .env, this project uses Streamlit's built-in secret management.
Create a file:

```bash
.streamlit/secrets.toml
```
Add your Anthropic API key:
```toml
ANTHROPIC_API_KEY='your_anthropic_api_key_here'
```
Make sure you use a Claude 3 model that supports vision, e.g. claude-3-opus-20240229

### 3. Run with Docker Compose
```bash
docker-compose up --build
```
Access the app at:

🗨️ Chatbot: http://localhost:8503


