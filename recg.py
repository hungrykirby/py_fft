import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2        #モノラル
RATE = 102400        #サンプルレート
CHUNK = 2**12       #データ点数
RECORD_SECONDS = 2 #録音する時間の長さ
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                input_device_index=0,   #デバイスのインデックス番号
                frames_per_buffer=CHUNK)
print ("recording...")

frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print ("finished recording")

stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
