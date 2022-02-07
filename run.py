#!/usr/bin/env python
# run:
# conda env create -f environment.yml
# conda activate ccenvironment


import sys
import subprocess
import json

sys.path.insert(0, 'src/data')
sys.path.insert(0, 'src/analysis')
sys.path.insert(0, 'src/model')

from cross_correlation import load_audio
from cross_correlation import spectrogram
from cross_correlation import template
from cross_correlation import correlation
from cross_correlation import test


def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'.

    `main` runs the targets in order of data=>analysis=>model.
    '''

    data_config = "data/test/ScreamingPiha2.wav"
    if 'data' in targets:
        audio = load_audio(data_config)
        temp = template(audio)
        temp

    if 'analysis' in targets:
        audio = load_audio(data_config)
        tf_audio = spectrogram(audio)
        tf_audio

    if 'model' in targets:
        correlation()

    if 'test' in targets:
        audio = load_audio(data_config)
        tf_audio = spectrogram(audio)
        temp = template(audio)
        model = correlation()
        output = test(data_config, tf_audio, temp, audio, model)
        output

if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)
