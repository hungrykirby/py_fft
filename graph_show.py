import numpy as np
from scipy import signal
from pylab import *

class Show_Graphs:
    def __init__(self, N):
        self.N = N

    def set_start(self, start):
        self.start = start

    def set_win(self, win):
        self.win = win

    def set_x(self, x):
        self.x = x

    def set_resyn_sig(self, resyn_sig):
        self.resyn_sig = resyn_sig

    def set_freqList(self, freqList):
        self.freqList = freqList

    def set_amplitude_pectrum(self, amplitudeSpectrum):
        self.amplitudeSpectrum = amplitudeSpectrum

    def set_phase_spectrum(self, phaseSpectrum):
        self.phaseSpectrum = phaseSpectrum

    def draw(self):
        # 1.元の波形を描画
        figure(figsize=(8, 8))
        subplot(511)  # 5行1列のグラフの1番目の位置にプロット
        subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.5)
        plot(range(self.start, self.start + self.N), self.x[self.start:self.start + self.N])
        axis([self.start, self.start + self.N, -1.0, 1.0])
        xlabel("Fig 1. Original Wave / time [sample]")
        ylabel("amp")

        # 2.窓関数を通した波形を描画
        subplot(512)  # 5行1列のグラフの2番目の位置にプロット
        plot(range(self.start, self.start + self.N), self.x[self.start:self.start + self.N] * self.win)
        axis([self.start, self.start + self.N, -1.0, 1.0])
        xlabel("Fig 2. through window Wave / time [sample]")
        ylabel("amp")

        # 3.振幅スペクトルを描画
        subplot(513)
        plot(self.freqList, self.amplitudeSpectrum, linestyle='-')
        axis([0, 3000, 0, 600])
        xlabel("Fig 3.  frequency [Hz]")
        ylabel("amp spect.")

        # 4.位相スペクトルを描画
        subplot(514)
        plot(self.freqList, self.phaseSpectrum, linestyle='-')
        axis([0, 3000, -np.pi, np.pi])
        xlabel("Fig 4.  frequency [Hz]")
        ylabel("phase spect.")

        # 5.元の波形を描画
        subplot(515)  # 5行1列のグラフの5番目の位置にプロット
        plot(range(self.start, self.start + self.N), self.resyn_sig[self.start:self.start + self.N])
        axis([self.start, self.start + self.N, -1.0, 1.0])
        xlabel("Fig 5. resynth Wave / time [sample]")
        ylabel("amp")

        #show()
        savefig("aaa.png")
