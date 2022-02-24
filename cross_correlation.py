import librosa
import librosa.display
from scipy import signal
from scipy import misc
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import math
import audioread

from PyHa.statistics import *
from PyHa.IsoAutio import *
from PyHa.visualizations import *



def load_audio(clip_path):
    ''' takes a clip path and returns the audio'''
    y, sr = librosa.load(clip_path, sr=12000)
    return y

def spectrogram(y):
    ''' takes an audio clip, transforms it, and displays
        the spectrogram and the transformed audio clip'''
    S = np.abs(librosa.stft(y))
    fig, ax = plt.subplots()
    img = librosa.display.specshow(librosa.amplitude_to_db(S,ref=np.max), x_axis='time', ax=ax)
    plt.title("Piha audio clip")
    plt.ylabel("Frequency (0-6kHz)")
    return S

def template(path):
    ''' takes an audio clip (transformed), selects a portion to
        create the template, and returns the template'''
    template = np.load(path + '.npy')
    return template

def correlation(technique, threshold_type, threshold_const, threshold_min, bi_dir, window_size):
    isolation_parameters = {
        "technique" : technique,
        "threshold_type" : threshold_type,
        "threshold_const" : threshold_const,
        "threshold_min" : threshold_min,
        "bi_directional_jump" : bi_dir,
        "window_size" : window_size
        }
    return isolation_parameters

def test(clip_path, S, template, y, params):
    ''' takes the path of the audio clip, the transformed audio
        clip, and the template to perform the cross-correlation
        to display the local_score_visualization, and returns
        the dataframe'''
    SAMPLE_RATE, SIGNAL = audio.load_wav(clip_path)
    if len(SIGNAL.shape) == 2:
        # averaging the two channels together
        SIGNAL = SIGNAL.sum(axis=1) / 2
        
    # downsample the audio if the sample rate > 44.1 kHz
    # Force everything into the human hearing range.

    if SAMPLE_RATE > 44100:
        rate_ratio = 44100 / SAMPLE_RATE
        SIGNAL = scipy_signal.resample(
            SIGNAL, int(len(SIGNAL) * rate_ratio))
        SAMPLE_RATE = 44100

    corr = signal.correlate2d(S,template,boundary='symm',mode='same')
    corr_reduced_max = np.amax(corr,axis=0)
    local_score = corr_reduced_max/max(corr_reduced_max)

    test_df = steinberg_isolate(corr_reduced_max/max(corr_reduced_max),y,12000,"test_dir","test_file",params)
    local_line_graph(local_score, clip_path, SAMPLE_RATE, SIGNAL, automated_df = test_df, premade_annotations_df=pd.DataFrame())
    # local_score_visualization(local_score, clip_path, automated_df = test_df)
    return test_df
