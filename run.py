#!/usr/bin/env python
# run:
# conda env create -f environment.yml
# conda activate ccenvironment


import sys
import subprocess
import json
from os import listdir
from os.path import isfile, join

sys.path.insert(0, 'src/data')
sys.path.insert(0, 'src/analysis')
sys.path.insert(0, 'src/model')

from cross_correlation import load_audio
from cross_correlation import spectrogram
from cross_correlation import template
from cross_correlation import correlation
from cross_correlation import test

import warnings



def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'.

    `main` runs the targets in order of data=>analysis=>model.
    '''

    data_param = open('data-params.json')
    data_config = json.load(data_param)
    temp_path = data_config['temp_path']
    clip_directory = data_config['clip_paths']
    clip_paths = [clip_directory + f for f in listdir(clip_directory) if isfile(join(clip_directory, f))]

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
        temp = template(temp_path)
        model = correlation(technique, threshold_type, threshold_const, threshold_min, bi_dir, window_size)
        for clip_path in clip_paths:
            try:
                audio = load_audio(clip_path)
                tf_audio = spectrogram(audio)
                output = test(clip_path, tf_audio, temp, audio, model)
                print(clip_path, output)
            except:
                continue


if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)
