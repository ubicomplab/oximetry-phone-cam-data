# Oximetry-phone-cam-data

## Purpose
**Open source data for smartphone camera oximetry, sensing SpO2 and hypoxemia risk on a clinically relevant spread of data**

This repository contains the open source data from the smartphone camera oximetry study by Hoffman et al in 2021 [include link].  It can be used to attempt to compute SpO2 and predict risk of hypoxemia using a smartphone camera via machine learning or analytical methods.  The data is the first gathered using a smartphone camera on a clinically relevant spread of SpO2 levels (65%-100%).

The data was gathered by researchers at the University of Washington and the University of California, San Diego, and is provided free and open source for the community to use for future projects.

## Getting Started
Clone the repo and run examples/visualization.ipynb to get started!

More example code can be found in the examples directory using the preprocessed data.  If you want to use the raw video data, please see the "Data Format" section below for info on how to download it.

### Needed packages: 
* [fill out on a fresh run]

## Data Format
There were 6 patients in this study (numbered 10001-10006).

The smartphone oximetry data was collected in the form of MP4 videos, downloadable from: http://bit.ly/oxy-raw-z.  Each frame's R, G, and B values were averaged to create the csv files in data/ppg-csv.

The ground truth data was collected from a few standard pulse oximeters attached to the subjects' other fingers.  That data can be found in data/gt.

### Data Format Notes
* Camera framerate = 30 Hz
* Ground truth pulse oximeters framerate = 1 Hz
* Recording was started and stopped on the camera and the pulse oximeters at the same time

## Background
SpO
We performed a Varied Fractional Inspired Oxygen (Varied FiO2) study, which is a clinical development validation study in which test subjects are administered a controlled mixture of oxygen and nitrogen to lower their SpO2 level over a period of 12-16 minutes.  The patients had one finger from each hand on a phone camera, while the camera flash transmitted light through their fingertips for reflectance photoplethysmography at the Red, Green, and Blue wavelengths.

For more details, see the publication in npj Digital Medicine from 2021: [include link].

### Ideas
Go ahead and try different models:
* Analytical (eg. ratio-of-ratios)
* Deep Learning
* Linear Regression
* Or, think of your own!

## Citation
If you use this data or code in your project, please cite it.  Here's the ACM format:
* [Add citation later when it's ready.]

### License
This data is provided open-source via the MIT license.  For more details, see the license file.  We want you to use it for whatever creative projects you can come up with!  

