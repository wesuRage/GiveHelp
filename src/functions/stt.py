from pathlib import Path
from openai import OpenAI
import dotenv, os

dotenv.load_dotenv()
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

def stt():
  audio_file = open(Path(__file__).parent.parent.parent / "audio" / "input.mp3", "rb")
  transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
  )

  return transcript.text