from sqlalchemy.orm import Session
from app.repositories import client_repository as client_repo
from app.services.state_machine import process_state_machine
from datetime import datetime, timedelta
from app.core.enums import ConversationState
from app.repositories import quote_repository as quote_repo

def process_incoming_message(db: Session, phone_number: str, message: str) -> str:
    """
    Entrypoint principal das regras de negócios.
    Redireciona todo o tráfego para a rotina da máquina de estados.
    """
    client = client_repo.get_or_create_client(db, phone_number)
    
    # Inactivity check
    now = datetime.utcnow()
    if client.last_interaction_at:
        if now - client.last_interaction_at > timedelta(minutes=30):
            client_repo.update_client_state(db, client, ConversationState.INICIO)
            quote_repo.reset_quote(db, client.id)
            client.current_state = ConversationState.INICIO.value

    client_repo.update_last_interaction(db, client)
    
    return process_state_machine(db, client, message)

