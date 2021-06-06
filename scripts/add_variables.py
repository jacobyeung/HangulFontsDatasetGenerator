import numpy as np
import os, sys, h5py

from hfd.variables import label_df

parser = argparse.ArgumentParser(description='Add latent annotations to h5s.')
parser.add_argument('folder', type=str, help='Folder to search for h5 files.')
parser.add_argument('fontsize', type=int, help='Fontsize.')

args = parser.parse_args()
folder = args.folder
fontsize =args.fontsize

files = []
for d, _, files in os.walk(folder):
    for fname in files:
        if '{}.h5'.format(fontsize) in fname:
            with h5py.File(os.path.join(d, fname)) as f:
                f.create_dataset('imf_style_labels', data=imf_style_labels)
