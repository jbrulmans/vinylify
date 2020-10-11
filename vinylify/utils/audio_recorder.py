import os
import sounddevice as sd
from scipy.io.wavfile import write


class AudioRecorder:

    def __init__(self):
        """
        Records audio clips
        """
