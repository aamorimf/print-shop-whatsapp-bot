from sqlalchemy.orm import Session
from app.models.schema import Client
from app.core.enums import ConversationState
from datetime import datetime

def get_or_create_client(db: Session, phone_number: str) -> Client:
    client = db.query(Client).filter(Client.phone_number == phone_number).first()
    if not client:
        client = Client(
            phone_number=phone_number,
            current_state=ConversationState.INICIO.value
        )
        db.add(client)
        db.commit()
        db.refresh(client)
    return client

def update_client_state(db: Session, client: Client, new_state: ConversationState):
    client.current_state = new_state.value
    db.commit()
    db.refresh(client)

def update_last_interaction(db: Session, client: Client):
    client.last_interaction_at = datetime.utcnow()
    db.commit()
    db.refresh(client)
