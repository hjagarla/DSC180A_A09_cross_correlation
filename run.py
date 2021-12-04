#!/usr/bin/env python

import sys
import json

sys.path.insert(0, 'src/data')
sys.path.insert(0, 'src/analysis')
sys.path.insert(0, 'src/model')

from etl import get_data
from analysis import compute_aggregates
from model import train


def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'.

    `main` runs the targets in order of data=>analysis=>model.
    '''

    if 'test' in targets:
        convert_notebook(**eda_config)

    return


if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)
