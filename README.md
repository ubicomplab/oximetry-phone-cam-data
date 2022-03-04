# Oximetry-phone-cam-data

## Purpose
**Open source data for smartphone camera oximetry, sensing SpO2 and hypoxemia risk on a clinically relevant spread of data**

This repository contains the open source data from the smartphone camera oximetry study by Hoffman et al in 2021 [include link when available].  It can be used to attempt to compute SpO2 and predict risk of hypoxemia using a smartphone camera via machine learning or analytical methods.  The data is the first gathered using a smartphone camera on a clinically relevant spread of SpO2 levels (65%-100%).

The data was gathered by researchers at the University of Washington and the University of California, San Diego, and is provided free and open source for the community to use for future projects.

## Getting Started
Clone the repo and run examples/visualization.ipynb to get started!

More example code can be found in the examples directory using the preprocessed data.  If you want to use the raw video data, please see the "Data Format" section below for info on how to download it.

### Needed packages: 
* pytorch
* sklearn
* scipy
* pandas
* matplotlib
* jupyter


## Data Format
There were 6 patients in this study (numbered 10001-10006).

The smartphone oximetry data was collected in the form of MP4 videos, downloadable from: http://bit.ly/oxy-raw-z.  Each frame's R, G, and B values were averaged to create the csv files in data/ppg-csv.

The ground truth data was collected from four standard pulse oximeters attached to the subjects' other fingers.  That data can be found in data/gt.

### Data Format Notes
* Camera framerate = 30 Hz
* Ground truth pulse oximeters framerate = 1 Hz
* Recording was started and stopped on the camera and the pulse oximeters at the same time

## Background
We performed a Varied Fractional Inspired Oxygen (Varied FiO2) study, which is a clinical development validation study in which test subjects are administered a controlled mixture of oxygen and nitrogen to lower their SpO2 level over a period of 12-16 minutes.  The patients had one finger from each hand on a phone camera, while the camera flash transmitted light through their fingertips for reflectance photoplethysmography at the Red, Green, and Blue wavelengths.

For more details, see the publication in npj Digital Medicine from 2022: [include link].

### Ideas
Go ahead and try different models:
* Analytical (eg. ratio-of-ratios)
* Deep Learning
* Linear Regression
* Or, think of your own!

### Ground Truth Labels
A metadata file can be found in data/gt/metadata.csv, which describes the fields listed in the metadata files.  A table is also included below:
| Label        | Description                                                           |
|--------------|-----------------------------------------------------------------------|
| SpO2 1       | SpO2 reading from PPG of pulse ox 1 (3900P TT+ 9.000/11.000) (%)      |
| SpO2 2       | SpO2 reading from PPG of pulse ox 2 (Nellcor N-600X V 1.6.0.0) (%)    |
| SpO2 3       | Unfilled signal from pulse ox 3 (Safety Oxim 3 ECG Datex-Ohmeda S5)   |
| SpO2 4       | SpO2 reading from PPG of pulse ox 4 (Nellcor N-600X V 1.6.0.0) (%)    |
| SpO2 5       | SpO2 reading from PPG of pulse ox 5 (Masimo Radical 7 Rainbow II) (%) |
| Pulse 1      | Heart rate from PPG of pulse ox 1 (3900P TT+ 9.000/11.000) (bpm)      |
| Pulse 2      | Heart rate from PPG of pulse ox 2 (Nellcor N-600X V 1.6.0.0) (bpm)    |
| Pulse 3      | Unfilled signal from pulse ox 3 (Safety Oxim 3 ECG Datex-Ohmeda S5)   |
| Pulse 4      | Heart rate from PPG of pulse ox 4 (Nellcor N-600X V 1.6.0.0) (bpm)    |
| Pulse 5      | Heart rate from PPG of pulse ox 5 (Masimo Radical 7 Rainbow II) (bpm) |
| PI 1         | Perfusion Index from PPG of pulse ox 1 (3900P TT+ 9.000/11.000)       |
| PI 2         | Perfusion Index from PPG of pulse ox 2 (Nellcor N-600X V 1.6.0.0)     |
| PI 3         | Unfilled signal from pulse ox 3 (Safety Oxim 3 ECG Datex-Ohmeda S5)   |
| PI 4         | Perfusion Index from PPG of pulse ox 4 (Nellcor N-600X V 1.6.0.0)     |
| PI 5         | Perfusion Index from PPG of pulse ox 5 (Masimo Radical 7 Rainbow II)  |
| ECG 3        | Heart rate from ECG of pulse ox 3 (Safety Oxim 3 ECG Datex-Ohmeda S5) |
| Rig FiO2     | Percentage of oxygen delivered to subjec in gas mixture (%)           |

## Citation
If you use this data or code in your project, please cite it.  Here's the ACM format:
* [Add citation later when it's ready.]

### License
This data is provided open-source via the MIT license.  For more details, see the license file.  We want you to use it for whatever creative projects you can come up with!  

