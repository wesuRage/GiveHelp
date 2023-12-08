import time
from functions import gpt, record, play, stt, tts

def main():
  print("Recording in 3, 2, 1...")
  time.sleep(2)

  print("Recording...")
  record.record()
  print("Recording done!")

  print("Getting response...")
  play.play("C:\\Users\\userr\\Documentos\\cristina\\audio\\aguarde.mp3")
  response_gpt = gpt.gpt(stt.stt())

  print("Getting audio...")
  tts.tts((response_gpt))

  print("Audio done!")
  play.play("C:\\Users\\userr\\Documentos\\cristina\\audio\\output.mp3")

if __name__ == "__main__":
  main()
