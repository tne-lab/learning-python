from scipy import signal

'''
How Mark S did this.
From "https://scipy-cookbook.readthedocs.io/items/ButterworthBandpass.html"
'''
def butter_bandpass(lowcut, highcut, fs, order=2):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=2):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    filteredData = signal.lfilter(b, a, data)
    return filteredData

