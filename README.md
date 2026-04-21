🐾 Amigo de Patas WhatsApp Bot
Automation for veterinary customer service via WhatsApp

A rule-based WhatsApp bot built with FastAPI that simulates a real customer service assistant for a veterinary clinic.
It handles common requests, provides pricing information, and guides users through a structured appointment flow.

🚀 Overview
This project demonstrates how to build a deterministic, state-driven chatbot integrated with real-world communication channels.
The bot is designed for a fictional clinic “Veterinária Amigo de Patas”, and focuses on:

* automated responses based on keywords
* structured conversation flow
* input validation (date/time)
* simple appointment request handling
* real WhatsApp interaction via Twilio Sandbox

🛠️ Tech Stack
* Python
* FastAPI
* SQLite
* SQLAlchemy
* Pydantic
* Twilio (WhatsApp Sandbox)
* Ngrok 

🧠 Key Features
* Greeting and fallback system
* Consultation pricing
* Vaccine pricing (predefined set)
* Exam pricing (predefined set)
* Clinic hours and address
* Guided appointment flow (step-by-step)
* Input validation for date and time
* Draft → Pending appointment lifecycle
* Separation of concerns (routing, services, state machine)
* Real WhatsApp testing via Twilio

💬 Example Conversation

User: oi
Bot: Olá! Como posso ajudar?

User: consulta
Bot: A consulta custa R$ X

User: agendar
Bot: Qual o seu nome?

User: Carlos
Bot: Nome do pet?

User: Perry
Bot: Tipo de atendimento?

User: consulta
Bot: Qual data?

User: amanhã
Bot: Qual horário?

User: 15h
Bot: Solicitação registrada!

🧱 Architecture
The project follows a clean and modular structure:

app/
├── api/                # FastAPI routes
├── db/                 # Database setup
├── models/             # ORM models
├── repositories/       # Database access layer
├── services/           # Business logic
│   ├── intent_router
│   ├── scheduling_flow
│   └── message_handler
├── utils/              # Parsers and validators

Design Highlights
* Stateless routing layer
* State-driven conversation flow
* Deterministic logic (no AI dependency)
* Clear separation between parsing, logic, and response

🧪 Local Setup

1. Clone the repository
git clone https://github.com/SEU_USUARIO/amigo-de-patas-whatsapp-bot.git
cd amigo-de-patas-whatsapp-bot

2. Create virtual environment
python -m venv .venv

Activate:
.\.venv\Scripts\Activate.ps1

3. Install dependencies
pip install -r requirements.txt

4. Run the API
python -m uvicorn main:app --host 127.0.0.1 --port 8000

5. Access API docs
http://127.0.0.1:8000/docs

🧪 Manual Testing (Swagger)

Use endpoint:
POST /api/test-message

Example payload:
{
  "phone": "21999999999",
  "text": "oi"
}

📱 Real WhatsApp Testing (Twilio Sandbox)

1. Start ngrok
ngrok http 8000

Copy the HTTPS URL:

https://your-url.ngrok-free.dev

2. Configure Twilio Sandbox
In Twilio Console → WhatsApp Sandbox:

When a message comes in:
https://your-url.ngrok-free.dev/api/webhook/twilio

Method: POST

3. Connect your WhatsApp
Send to Twilio number:

join your-sandbox-code

4. Test messages

Send:

oi
consulta
vacina
exame
agendar

🔄 How It Works
1. User sends message via WhatsApp
2. Twilio receives message
3. Twilio sends webhook to FastAPI
4. Bot processes message
5. Response is returned as TwiML
6. Twilio delivers message back to user

⚠️ Important Notes
* Always ensure:
    * API is running
    * ngrok is active
    * Twilio URL is correct
* If ngrok restarts, update the URL in Twilio
* Avoid using --reload with Uvicorn

🔮 Future Improvements
* Admin dashboard (appointments + configuration)
* Real scheduling integration (calendar)
* Human handoff system
* Multi-clinic support
* Deployment to cloud environment
* Authentication and access control

🎯 Project Purpose
This project was built to demonstrate:

* backend architecture skills
* real-world API integration
* automation of business workflows
* clean code and maintainability
* ability to bridge local systems with external platforms

👨‍💻 Author

Developed as a portfolio project focused on automation and real-world integrations.

⭐ Final Insight
This project goes beyond a simple chatbot.

It demonstrates how to connect:

* backend systems
* structured logic
* and real communication channels

into a practical, production-oriented solution.