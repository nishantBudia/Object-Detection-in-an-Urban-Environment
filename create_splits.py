import argparse
import glob
import os
import random

import numpy as np
import shutil
import random

from utils import get_module_logger


def split(dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    list_names = os.listdir(dir+"processed/")
    random.shuffle(list_names)
    for i in range (len(list_names)):
        if i<80:
            shutil.copy(dir+"processed/"+list_names[i],dir+"train/")
        elif i <95 and i>=80:
            shutil.copy(dir+"processed/"+list_names[i],dir+"val/")
        else :
            shutil.copy(dir+"processed/"+list_names[i],dir+"test/")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.dir)