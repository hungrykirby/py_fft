import wave
import numpy as np
import scipy.fftpack
from scipy import signal
from pylab import *
import graph_show

if __name__ == "__main__":
    wf = wave.open("data/file.wav", "r")
    fs = wf.getframerate()  # サンプリング周波数 上のサンプルでは48K
    x = wf.readframes(wf.getnframes())
    x = frombuffer(x, dtype="int16") / 1500.0
    wf.close()

    start = 0  # サンプリングする開始位置
    N = 2 ** 12

    # サンプリング数にあったハニング窓を準備します。
    win = signal.hann(N)

    # FFTを実行してスペクトラム情報を獲得します。
    spectrum = scipy.fftpack.fft(x[start:start + N] * win)
    freqList = scipy.fftpack.fftfreq(N, d=1.0 / fs)

    # 振幅と位相をグラフ表示するために抽出します。
    amplitudeSpectrum = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in spectrum]  # 振幅スペクトル
    phaseSpectrum = [np.arctan2(int(c.imag), int(c.real)) for c in spectrum]  # 位相スペクトル

    # スペクトラム情報から元の波形に復元します。
    resyn_sig = ifft(spectrum)

    sg = graph_show.Show_Graphs(N)
    sg.set_x(x)
    sg.set_freqList(freqList)
    sg.set_win(win)
    sg.set_phase_spectrum(phaseSpectrum)
    sg.set_start(start)
    sg.set_resyn_sig(resyn_sig)
    sg.set_amplitude_pectrum(amplitudeSpectrum)
    sg.draw()
