import os, sys
from typing import Any
import cv2

from pandas import Series, DataFrame
from pandas.core.generic import NDFrame

sys.path.append("..")

import emtmlibpy.emtmlibpy as emtm
from emtmlibpy.emtmlibpy import EMTMResult

import numpy as np
import pandas as pd
from argparse import ArgumentParser

def main():
    """
    Main entry point
    :return:
    """
    print('main')

if __name__ == '__main__':
    parser = ArgumentParser('emobs')
    parser.add_argument('emobs_path', help='Path to the EMObs annotation file')
    parser.add_argument('-v', required=True, help='Path to the video to extract frames')
    
    args = parser.parse_args()
    exit(main(args) or 0)