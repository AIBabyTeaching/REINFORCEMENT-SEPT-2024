from app.utils.nao_utils import (
    close_hand,
    say_text,
    record_audio,
    fetch_audio
)

def execute_speech_and_audio(text = "What can I do for you, Ahmed?"):
    say_text(text)
    record_audio()
    fetch_audio()

def execute_close_hand(use_subprocess=False):
    if use_subprocess:
        return close_hand()
    else:
        close_hand()
        return "Hand closed successfully using direct method."
