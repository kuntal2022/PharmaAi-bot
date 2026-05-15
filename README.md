# ⚕️ Pharma-AI — Intelligent Pharmacy Chatbot

A conversational AI chatbot built for pharmacy and medicine-related queries, powered by OpenAI GPT models and LangGraph with memory support.

---

## 🖥️ Demo

![Pharma-AI Screenshot](pharma_ai.png)

---

## ✨ Features

- 💊 Answers pharmacy and medicine-related questions only
- 🧠 Conversation memory — remembers chat history within a session
- 🌐 Web search support via DuckDuckGo for latest drug information
- 🤖 Multiple GPT model selection (GPT-4.1, GPT-4o, GPT-4.1-mini, GPT-3.5-turbo)
- ⚠️ Always adds safety disclaimer for medicine advice
- 🎨 Custom dark-themed UI with Streamlit

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Streamlit | Frontend UI |
| LangChain | LLM chaining and prompt management |
| LangGraph | Stateful agent graph with memory |
| OpenAI GPT | Language model |
| DuckDuckGo | Web search tool |
| InMemorySaver | Conversation checkpointing |

---

## 📁 Project Structure

```
PharmaAi-bot/
│
├── front_end.py       # Streamlit UI
├── backend.py         # LangGraph agent and graph logic
├── style_type.py      # Custom CSS styling
├── .env               # API keys (not committed)
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/kuntal2022/PharmaAi-bot.git
cd PharmaAi-bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run front_end.py
```

### 4. Enter your OpenAI API Key in the sidebar

---

## ⚠️ Disclaimer

This chatbot is an AI assistant and **may be wrong**. Always consult a licensed doctor or pharmacist before taking any medication. Self-medication can be harmful.

---

## 👨‍💻 Creator

**Kuntal Chakraborty**  
[GitHub](https://github.com/kuntal2022)
