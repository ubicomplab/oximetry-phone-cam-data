# process_data_spo2.py
# Library to support retrieving data from SpO2 dataset
# Link to paper when published

# Imports --------------------------------------------

import numpy as np
from scipy.signal import find_peaks
from matplotlib import pyplot as plt
from pathlib import Path
import cv2

# Flags --------------------------------------------

loadDataFlag = 0 # 0 for loading and computing from raw videos (and saving), 1 for loading from csvs in Data/Data

# Presets --------------------------------------------

dataLoc = './/data//raw-videos//raw//raw' # extract as seen in README-videos.md
dataDir = Path.home().joinpath(Path.cwd().parent,dataLoc)
procLoc = './/data//ppg-csv' # processed data location
procDir = Path.home().joinpath(Path.cwd().parent,procLoc)
patientNums = np.arange(100001,100007,1)

# Functions --------------------------------------------

# Function to build left and right dirs based on a core dir
def createLtRt(dataDir):
    dataDirLt = Path.home().joinpath(dataDir,'Left')
    dataDirRt = Path.home().joinpath(dataDir,'Right')
    return [dataDirLt,dataDirRt]

# Function to return the path of a file
# given a directory, patient number and file type
def findFile(path,num,type):
    fileList = list(Path(path).rglob('*'+type))
    for f in fileList:
        if str(num) in f.name:
            file = f
        else: # couldn't find the file
            #print('Could not find file num:'+str(num)+' with path:'+str(type)+' at path:'+str(path.name))
            pass
    return file

# Function to return an array of R, G, B values
# from a raw video input
# Output is array of average R, G, B for length of video
def getRawRGB(patientNum,dataDir):
    rawFile = findFile(dataDir,patientNum,'.mp4')
    rawVid = cv2.VideoCapture(rawFile.as_posix())
    vidLen = int(rawVid.get(cv2.CAP_PROP_FRAME_COUNT))
    rgbArray = np.zeros([vidLen,3])
    print('processing ' +str(rawFile.name))
    count = 0
    success = 1
    while count<vidLen:
        success, image = rawVid.read()
        # process the image for R, G, B
        R0 = np.mean(image[:,:,0])
        G1 = np.mean(image[:,:,1])
        B2 = np.mean(image[:,:,2])
        rgbArray[count] = [R0,G1,B2]
        count += 1
    return rgbArray

# Function to create and return a plot of the R, G, B values
def plotRGB(rgb,num):
    colors = ['red','green','blue']
    pltTitle = 'RGB Plot for ' + str(num)
    pltXLabel = 'Frame'
    pltYLabel = 'Received Lumen Value'
    for i, color in enumerate(colors,start=0):
        plt.plot(rgb[:,i],color=color,label=str(color))
    plt.legend(loc='upper left')
    plt.gca().set(title=pltTitle,xlabel=pltXLabel,ylabel=pltYLabel)
    #plt.show()
    return plt

# Function to save the processed RGB to a csv with a certain filename
# Inputs: RGB array to save, filename (subject num), path to save, hand (0=Lt,1=Rt)
def saveRGB(rgb,fname,path,hand):
    handLabel = 'Right'
    if hand == 0:
        handLabel = 'Left'
    if path.exists(): # check if folders exist
        pass
    else: # create them if not
        path.mkdir()
    csvExt = fname+'.csv'
    csvName = Path.home().joinpath(path,csvExt)
    if csvName.exists(): # check if files already exist
        return 1
    else: # save the files if they don't
        np.savetxt(csvName,rgb)
        plotTitle = fname + ' ' + handLabel
        plt = plotRGB(rgb,plotTitle)
        pngExt = fname+'.png'
        pngName = Path.home().joinpath(path,pngExt)
        plt.savefig(pngName)
        plt.clf()
    return 0

# Function to walk through list of patient numbers and process them, saving their data as csvs and pngs
def procRawData(nums,loadData=loadDataFlag,dataDir=dataDir,procDir=procDir):
    print('Processing raw data with loadDataFlag=' + str(loadData) +'. Please wait ...')
    dataDirs = createLtRt(dataDir)
    procDirs = createLtRt(procDir)
    rgbData = { } # dictionary for accessing each patients' data
    for num in nums:
        RGB2 = { }
        for i in [0,1]: # 0 is Left, 1 is Right
            if (loadData == 0):
                RGB = getRawRGB(num,dataDirs[i])
            elif (loadData == 1): #load data
                loadSuccess,RGB = loadRGB(num,procDirs[i])
            filename = (str(num))
            save_result = saveRGB(RGB,filename,procDirs[i],i)
            RGB2[i] = RGB
        rgbData[num] = RGB2
    print('Files are saved in ' + str(procDir))
    return rgbData

# Code to run --------------------------------------------

if __name__ == '__main__':
    rgbData = procRawData(patientNums,loadDataFlag) # plot all patients