from typing import Optional
from nemoguardrails.actions import action
import json

@action(is_system_action=True)
async def check_blocked_terms(context: Optional[dict] = None):
    user_input = context.get("user_message")
    path = "/content/drive/MyDrive/NM CNPM/RAG/guardrails/bad_words.json"
    with open(path, 'r') as fIn:
      data = json.load(fIn)
    blocked_phrases = [key for key in data]
    for phrase in blocked_phrases:
        if phrase in user_input.lower():
            return False

    return True


