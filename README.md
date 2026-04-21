# 🖨️ Atlas — WhatsApp Print Shop Bot
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![Status](https://img.shields.io/badge/status-in%20development-orange)

Deterministic WhatsApp chatbot for print shop customer service

A state-machine based WhatsApp bot built with FastAPI, designed to automate customer service and budget collection for print shops.

🚀 Overview
This project demonstrates how to build a deterministic, state-driven chatbot focused on structured customer interactions.

Instead of relying on AI or keyword guessing, the bot uses a finite state machine (FSM) to guide the user step-by-step and collect complete order data.

## 🧩 Why this project?

Most chatbots rely on AI or keyword matching, which can lead to unpredictable behavior.

This project was designed to demonstrate a different approach:

- Deterministic logic
- Full control over conversation flow
- Business-oriented interaction
- Reliable data collection

The goal is to show how structured automation can solve real-world problems efficiently.

🧠 Key Features
* Fully deterministic state machine
* Menu-driven navigation (1, 2, 3)
* Structured budget collection:
    * setor (offset, sign, sublimação)
    * produto
    * tamanho
    * quantidade
* Persistent conversation context (per user)
* Fallback system (error + state repeat)
* WhatsApp integration via Twilio
* Clean architecture (services, repositories, state engine)

💬 Example Conversation

User: oi

Bot:
Olá! Seja bem-vindo 👋
Sou o assistente virtual da gráfica.

1️⃣ Fazer um orçamento
2️⃣ Tirar dúvidas
3️⃣ Falar com atendente

User: 1

Bot:
Perfeito! Sobre qual tipo de produto você deseja orçamento?

1️⃣ Impressos (offset)
2️⃣ Comunicação visual (sign)
3️⃣ Sublimação

User: 1
User: cartão de visita
User: 9x5
User: 1000

Bot:
Perfeito! Só confirmando:

Produto: cartão de visita
Tamanho: 9x5
Quantidade: 1000

🧱 Architecture

app/
├── api/
├── core/
│   ├── enums.py
│   └── state_config.py
├── db/
├── models/
├── repositories/
├── services/
│   ├── state_machine.py
│   └── message_handler.py

⚙️ Tech Stack
* Python
* FastAPI
* SQLite
* SQLAlchemy
* Twilio API (WhatsApp)
* Ngrok

🔄 How It Works
1. User sends message via WhatsApp
2. Twilio forwards message to API
3. State Machine processes input
4. Context is updated in database
5. Response is generated
6. Twilio sends reply back

🧪 Local Setup

git clone https://github.com/SEU_USUARIO/print-shop-whatsapp-bot.git
cd print-shop-whatsapp-bot

python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

python -m uvicorn main:app --host 127.0.0.1 --port 8000

📱 WhatsApp Testing (Twilio)

ngrok http 8000

Configure:

https://YOUR_NGROK_URL/api/webhook/twilio

Send:

join your-code

⚠️ Important Notes
* Do not use --reload
* Keep ngrok running
* Update URL if ngrok changes

🎯 Design Principles
* No AI dependency
* Predictable flow
* Business-driven logic
* Data-first interaction

🔮 Future Improvements
* Admin dashboard
* Multi-client support
* CRM integration
* Order tracking
* Cloud deployment

🧠 Project Purpose
This project demonstrates:

* backend architecture
* state machine design
* real-world API integration
* automation of business workflows

⭐ Final Insight
This is not just a chatbot.

It is a structured customer service system designed to:

capture → organize → convert