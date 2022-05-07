# preprocess_data_spo2.py
# Library to create .h5 tensors from spo2 data in csv format

# Imports --------------------------------------------

import numpy as np
import torch
import h5py
import pandas as pd

# Presets --------------------------------------------

PATIENT_NUMS = ['100001', '100002', '100003', '100004', '100005', '100006']

PROCESSED_DATA_DIR = '..//data//ppg-csv//'
FEATS = ["left-r","left-g","left-b","right-r","right-g","right-b"]

GROUNDTRUTH_DATA = '..//data//gt//'
GT_ROWS = ['sp02_1', 'sp02_2', 'sp02_3', 'sp02_4', 'sp02_5']

# Functions --------------------------------------------

"""
Load patient data functions
"""
# Assumes 0,1,2 feats are for left hand and 3,4,5 feats are for right hand
def load_data_for_patient(pnum):
    # Read data from Left
    fpath_left = PROCESSED_DATA_DIR + 'Left/' + pnum + '.csv'
    data_left = torch.tensor(np.loadtxt(fpath_left).transpose())

    # read data from Right
    fpath_right = PROCESSED_DATA_DIR + 'Right/' + pnum + '.csv'
    data_right = torch.tensor(np.loadtxt(fpath_right).transpose())

    # Stack uneven tensors into single tensor
    data = torch.zeros((6,max(data_left.shape[1], data_right.shape[1])))
    data[:3,:data_left.shape[1]] = data_left
    data[3:,:data_right.shape[1]] = data_right

    return data

import matplotlib.pyplot as plt
def load_data():
    # Load processed input data
    all_patient_data = [load_data_for_patient(pnum) for pnum in PATIENT_NUMS]
    max_len = max([pdata.shape[1] for pdata in all_patient_data])
    dataset = torch.zeros((len(all_patient_data), len(FEATS), max_len))
    for i, pdata in enumerate(all_patient_data):
        dataset[i, :, :pdata.shape[1]] = pdata.unsqueeze(0)

    return dataset


"""
Load groundtruth data functions
"""
def load_groundtruth_for_patient(pnum):
    fpath = GROUNDTRUTH_DATA + pnum + '.csv'
    datContent = [i.strip().split() for i in open(fpath).readlines()]
    rows = []

    for row in datContent[1:-1]:
        timestamp = row[0]
        sp02_1 = float(row[1])
        sp02_2 = float(row[2])
        sp02_3 = float(row[3])
        sp02_4 = float(row[4])
        sp02_5 = float(row[5])
        rows.append([sp02_1, sp02_2, sp02_3, sp02_4, sp02_5])

    data = torch.tensor(rows).transpose(0,1)
    return data


def load_groundtruth():
    all_patient_gt = [ load_groundtruth_for_patient(pnum) for pnum in PATIENT_NUMS]
    max_len = max([gtdata.shape[1] for gtdata in all_patient_gt])
    gt_data = torch.zeros((len(all_patient_gt), len(GT_ROWS), max_len))
    for i, gtdata in enumerate(all_patient_gt):
        gt_data[i, :, :gtdata.shape[1]] = gtdata.unsqueeze(0)
    return gt_data

def build_data_and_groundtruth():
    FPS = 30
    dataset = load_data()
    groundtruth = load_groundtruth()
    clip_to = min(groundtruth.shape[2]*FPS, dataset.shape[2])
    groundtruth = groundtruth.index_select(2,torch.arange(0,clip_to//30, dtype=torch.int64))
    dataset = dataset.index_select(2,torch.arange(0,clip_to, dtype=torch.int64))

    with h5py.File('..//data//preprocessed//all_uw_data.h5', 'w') as f:
        dset = f.create_dataset("dataset", tuple(dataset.shape), dtype='f')
        dset[:] = dataset
        dset.attrs['features_key'] = FEATS

        gt = f.create_dataset("groundtruth", tuple(groundtruth.shape), dtype='f')
        gt[:] = groundtruth
        gt.attrs['gt_keys'] = GT_ROWS

def load_data_and_groundtruth():
    build_data_and_groundtruth()
    with h5py.File('..//data//preprocessed//all_uw_data.h5', 'r') as f:
        data = f['dataset'][:]
        gt = f['groundtruth'][:]
    return data, gt

# Code to run --------------------------------------------

if __name__ == '__main__':
    data, gt = load_data_and_groundtruth()