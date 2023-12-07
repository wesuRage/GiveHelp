import pyaudio, wave, keyboard, time

def record():
  audio = pyaudio.PyAudio()

  stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
  frames = []

  try:
    print("Recording in 3, 2, 1...")
    time.sleep(2)

    print("Recording...")

    while True:
      data = stream.read(1024)
      frames.append(data)

      if keyboard.is_pressed('q'):
        print("Recording done!")
        break
  except KeyboardInterrupt:
    pass

  stream.stop_stream()
  stream.close()
  audio.terminate()


  sound_file = wave.open("audio/input.mp3", "wb")
  sound_file.setnchannels(1)
  sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
  sound_file.setframerate(44100)
  sound_file.writeframes(b''.join(frames))
  sound_file.close()