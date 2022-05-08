# A guide through processing the data from raw video

The preprocessed data can be found in /data/preprocessed. Please refer to example code for how to load the preprocessed data.

However, if you want to process the data yourself, you may find this guide useful.

# Needed packages: 
* pytorch
* numpy
* h5py
* scipy
* pandas
* matplotlib
* jupyter
* OpenCV (cv2)

Download the smartphone oximetry data in the form of MP4 videos here: http://bit.ly/oxy-raw-z. Put the videos into data/raw-videos/raw folder, with videos for left hand in /Left and videos for right hand in /Right.

Run process_data_spo2.py. This script will process the MP4 video (averaging out the RGB values in each frame) using the OpenCV package: note that OpenCV is using BGR protocol for image processing, which might be different from tools.

Run add_Header() from header_data_spo2.py. The add_Header function will add RGB header to the csv files processed by the process_data_spo2 script.

Run preprocess_data_spo2.py to load all preprocessed RGB values and ground truth values and pack them into a single .h5 file.
