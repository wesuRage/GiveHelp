from openai import OpenAI
import dotenv, os

dotenv.load_dotenv()
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

def gpt(prompt):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "Não faça respostas muito longas. De 2 a 3 linhas está ótimo, resuma o conteúdo."},
      {"role": "user", "content": prompt}
    ]
  )

  content = completion.choices[0].message.content
  return content