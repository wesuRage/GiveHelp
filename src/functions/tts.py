from pathlib import Path
from openai import OpenAI
import dotenv, os

dotenv.load_dotenv()
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

def tts(prompt):
  speech_file_path = Path(__file__).parent.parent.parent / "audio" / "output.mp3"
  response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=prompt
  )
  response.stream_to_file(speech_file_path)
