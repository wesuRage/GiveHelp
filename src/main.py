import time
from functions import gpt, record, play, stt, tts

def main():
  print("Recording in 3, 2, 1...")
  time.sleep(2)

  print("Recording...\n")
  record.record()
  print("Recording done!\n")

  print("Getting response...\n")
  response_gpt = gpt.gpt(stt.stt())


  print("Getting audio...\n")
  tts.tts((response_gpt))

  print("Audio done!")
  play.play()

if __name__ == "__main__":
  main()