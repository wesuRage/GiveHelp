from functions import gpt, record, play, stt, tts

def main():
  record.record()

  response_gpt = gpt.gpt(stt.stt())

  tts.tts((response_gpt))

  play.play()

if __name__ == "__main__":
  main()