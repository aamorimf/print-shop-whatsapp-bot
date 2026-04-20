# 🐾 Amigo de Patas — WhatsApp Bot

> A rule-based WhatsApp bot for a fictional veterinary clinic, built with Python and FastAPI.

---

## Overview

**Amigo de Patas** is a deterministic, keyword-driven WhatsApp bot designed for the fictional veterinary clinic *Veterinária Amigo de Patas*. It answers common questions about services, pricing, clinic hours, and address — and guides users through a simple appointment request flow using a state machine.

No LLMs. No AI. Just clean, predictable Python.

This project was built as a portfolio piece to demonstrate applied knowledge of:
- Clean Architecture principles in a Python web service
- State-driven conversation flows without external AI dependencies
- FastAPI, SQLAlchemy ORM, and SQLite for lightweight, deployable backends
- Practical API design ready for real WhatsApp integration via Twilio or Meta Webhooks

---

## Features

| Feature | Details |
|---|---|
| 💬 Greeting & Fallback Menu | Displays a help menu when user intent is unclear |
| 💉 Vaccine Pricing | Lists all available vaccines and prices |
| 🩺 Consultation Pricing | Returns general consultation fee |
| 🔬 Exam Pricing | Returns full exam catalog with prices |
| 🕒 Clinic Hours | Monday–Friday and Saturday schedules |
| 📍 Clinic Address | Returns the clinic location |
| 📅 Appointment Request | Guided, multi-step flow to collect tutor/pet/service/date/time |
| ✅ Input Validation | Rejects vague date and time answers |
| 🗃️ Draft Lifecycle | Appointments saved as `DRAFT` → `PENDING_CONFIRMATION` |
| 🧪 Swagger Testing | `/api/test-message` for direct testing via Swagger UI |
| 🌐 Simulated Webhook | `/api/webhook` mimics Meta/Twilio payload structure |

---

## Demo Flow

```
User:  "quero agendar"
Bot:   "Ótimo! Para começarmos, qual é o seu nome?"

User:  "Carlos"
Bot:   "Prazer, Carlos! Qual é o nome do seu pet?"

User:  "Rex"
Bot:   "O que o Rex precisa hoje? (Consulta, Vacina ou Exames)"

User:  "vacina"
Bot:   "Perfeito! Para qual data? (ex: hoje, amanha, quarta, 15/04)"

User:  "qualquer dia"
Bot:   "Data inválida ou muito vaga. Por favor digite algo como: 'hoje', 'amanha', 'quinta' ou '15/04'."

User:  "sexta"
Bot:   "E qual período ou horário de preferência? (ex: manha, tarde, 15h, 10:30)"

User:  "tarde"
Bot:   "Pronto, Carlos! Recebemos sua solicitação de vacina para o Rex em sexta (tarde).
        ⚠️ Um atendente entrará em contato em breve para confirmar o horário exato!"
```

> At any point in the flow, the user can type **"cancelar"** to reset and return to the main menu.

---

## Architecture

```
amigo_de_patas_bot/
├── app/
│   ├── api/
│   │   └── webhook_router.py        # Webhook + test endpoints
│   ├── core/
│   │   ├── constants.py             # Single source of truth: prices, hours, address
│   │   └── enums.py                 # ConversationState + AppointmentStatus enums
│   ├── db/
│   │   └── database.py              # SQLite engine, session factory, init
│   ├── models/
│   │   └── schema.py                # SQLAlchemy + Pydantic models
│   ├── repositories/
│   │   ├── client_repository.py     # Client CRUD + state update
│   │   └── appointment_repository.py # Draft lifecycle management
│   ├── services/
│   │   ├── message_handler.py       # Central orchestrator (IDLE vs. in-flow)
│   │   ├── intent_router.py         # Stateless keyword → response routing
│   │   ├── scheduling_flow.py       # State machine: step-by-step appointment
│   │   └── response_builder.py      # Message formatting from constants
│   └── utils/
│       └── text_parser.py           # Text cleaning + date/time validation (regex)
├── main.py                          # FastAPI app entry point
├── requirements.txt
└── README.md
```

**Key Separation of Concerns:**
- `intent_router` handles all stateless intents (prices, hours, address)
- `scheduling_flow` owns state transitions and input validation
- `message_handler` decides which path a message takes
- `response_builder` formats all output strings — business logic never builds strings directly

---

## Tech Stack

| | |
|---|---|
| **Language** | Python 3.11+ |
| **Framework** | FastAPI |
| **ORM** | SQLAlchemy 2.x |
| **Database** | SQLite (local file) |
| **Validation** | Pydantic v2 |
| **Server** | Uvicorn |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/aamorimf/amigo-de-patas-whatsapp-bot.git
cd amigo-de-patas-whatsapp-bot

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# or: source .venv/bin/activate  # Linux/macOS

# Install dependencies
pip install -r requirements.txt
```

---

## Running Locally

```bash
python main.py
```

The server starts at `http://localhost:8000`.  
The SQLite database file (`amigo_de_patas.db`) is created automatically on first run.

**Interactive API docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Testing via Swagger

Open [http://localhost:8000/docs](http://localhost:8000/docs) and use the **`POST /api/test-message`** endpoint.

### `/api/test-message` — Simple test endpoint

```json
{
  "phone": "21999999999",
  "text": "quero agendar"
}
```

### `/api/webhook` — Simulated webhook endpoint

```json
{
  "phone_number": "21999999999",
  "message": "quero saber sobre vacinas"
}
```

Both endpoints return the bot's reply in the `response` field.

---

## Optional: Real WhatsApp Testing with Twilio Sandbox

To test with a real WhatsApp number during development:

1. Create a free [Twilio account](https://www.twilio.com/try-twilio)
2. Activate the **Twilio Sandbox for WhatsApp**
3. Expose your local server with [ngrok](https://ngrok.com/): `ngrok http 8000`
4. Set the Twilio Sandbox webhook URL to: `https://<your-ngrok-id>.ngrok.io/api/webhook`
5. Adapt the `handle_whatsapp_message` function in `webhook_router.py` to parse Twilio's `Form` payload format instead of JSON

> This project uses a simplified JSON payload for demo purposes. Adapting it to Twilio or the Meta Graph API requires only minimal changes to the webhook parser.

---

## Future Improvements

- [ ] Adapt `/api/webhook` to fully parse Meta Graph API payload format
- [ ] Add Twilio Sandbox integration as a ready-to-use config flag
- [ ] Lightweight admin panel (Streamlit or Jinja2) to view appointments
- [ ] Migrate SQLite to PostgreSQL for cloud deployment (Railway / Render)
- [ ] Add unit tests for intent routing and scheduling flow validation

---

## Author

Built by **Alessandro Amorim** as a portfolio project.  
Demonstrating applied Python backend engineering, clean architecture, and practical API design.

[![GitHub](https://img.shields.io/badge/GitHub-aamorimf-181717?logo=github)](https://github.com/aamorimf)

---

*This project uses a fictional clinic and fictional data for portfolio and educational purposes only.*
