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

    data_param = open('data-params.json')
    data_config = json.load(data_param)
    temp_path = data_config['temp_path']
    clip_path = data_config['clip_path']

    model_param = open('model-params.json')
    model_config = json.load(model_param)
    technique = model_config['technique']
    threshold_type = model_config['threshold_type']
    threshold_const = model_config['threshold_const']
    threshold_min = model_config['threshold_min']
    bi_dir = model_config['bi_directional_jump']
    window_size = model_config['window_size']

    if 'data' in targets:
        audio = load_audio(clip_path)
        temp = template(audio)
        temp

    if 'analysis' in targets:
        audio = load_audio(clip_path)
        tf_audio = spectrogram(audio)
        tf_audio

    if 'model' in targets:
        correlation(technique, threshold_type, threshold_const, threshold_min, bi_dir, window_size)


    if 'test' in targets:
        temp_clip = load_audio(temp_path)
        audio = load_audio(clip_path)
        tf_audio = spectrogram(audio)
        temp = template(audio)
        model = correlation(technique, threshold_type, threshold_const, threshold_min, bi_dir, window_size)
        output = test(clip_path, tf_audio, temp, audio, model)
        output

if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)
