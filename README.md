
# 🤖 Smart AI Assistant Prototype

A lightweight, voice-enabled AI chatbot powered by **DialoGPT** and built using **Streamlit** and **Hugging Face Transformers**. This assistant supports natural language conversations, voice input/output, and short-term memory — all inside a clean UI.

🔗 **Live Demo**: [Try it on Hugging Face Spaces](https://huggingface.co/spaces/RuthvikReddy45/smart-ai-assistant-prototype)

---

## ✨ Features

- 💬 Chatbot powered by `DialoGPT-small` from Microsoft
- 🗣️ Voice input (speech-to-text) and audio replies (text-to-speech)
- 🧵 Short-term memory (remembers the last 3 exchanges)
- 🖼️ Clean UI using Streamlit's chat layout
- 🔐 `.env` support for Hugging Face tokens

---

## 📸 Demo

<!-- Optional: Add a screenshot -->
![Chat UI Preview](https://your-image-link.png)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Fearless2389/smart-open-ai-assistant.git
cd smart-open-ai-assistant
````

### 2. Install Dependencies

Make sure Python 3.9+ is installed.

```bash
pip install -r requirements.txt
```

### 3. Add Your Hugging Face Token (optional but recommended)

Create a `.env` file in the project root:

```
HF_TOKEN=your_huggingface_token_here
```

> You can generate a token at: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

* Uses `DialoGPT-small` via Hugging Face Transformers
* Manages history using `st.session_state` for multi-turn conversations
* Allows switching between typing or speaking via sidebar radio
* Converts responses to speech using `gTTS` and plays them with `playsound`

---

## 📁 Project Structure

```
├── app.py                 # Main Streamlit app
├── modules/
│   ├── chat.py            # Generates responses using DialoGPT
│   ├── memory.py          # Save/load chat history locally (optional)
│   └── voice.py           # Voice input/output utilities
├── requirements.txt       # All dependencies
├── .env                   # Hugging Face token (ignored in Git)
└── README.md              # Project overview
```

---

## 🧩 Dependencies

* `transformers`
* `torch`
* `streamlit`
* `gTTS`
* `SpeechRecognition`
* `pydub`, `playsound`
* `opencv-python-headless`, `Pillow`
* `python-dotenv`, `tenacity`, `requests`

> See [`requirements.txt`](./requirements.txt) for full versions.

---

## 📌 To Do / Ideas

* [ ] Add long-term memory using a database or vector store
* [ ] Replace DialoGPT with LLaMA 3, Mistral, or OpenAI chat models
* [ ] Add chat avatars and typing animations
* [ ] Enhance voice support (multi-language, whisper model)

---




