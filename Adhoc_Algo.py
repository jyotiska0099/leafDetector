# SIFT/ORB algorithm for identification plants by images.
# Implemented by - ashish.me08@gmail.com


import sys
from PIL import Image, ImageFilter, ImageDraw
import operator as op
from optparse import OptionParser
import cv2
import matplotlib.pyplot as plt
from os.path import basename
import glob
import os
from tkinter import messagebox
from tkinter import filedialog
import ntpath







def detect_Adh(imageName,imagePath):



  print ('Identifying image, please wait... (can take some minutes)')

  im1 = cv2.imread(imagePath+'/'+imageName)

  #fl=filedialog.askdirectory(initialdir="/", title="Select Image Database")
  #messagebox.showinfo("Folder Selected", fl)
  fl = 'static/img/ImageSet'
  print(fl)
  I_B = glob.glob(fl + '/' + '*.jpg')
  #print("Selected Image Base list",I_B)
  ind1=[]

  for n in I_B:
    ind1.append(ntpath.basename(n))

  #print("Selected Images from Image Base",ind1)
  Max=0
  FileName=""
  Images=len(ind1)
  A=[0]*(Images+1)
  for IF in ind1:

    im2=cv2.imread(fl+'/'+IF)

    #sift = cv2.xfeatures2d.SIFT_create()
    orb = cv2.ORB_create()

  # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(im1, None)
    kp2, des2 = orb.detectAndCompute(im2, None)

  # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

  # Match descriptors.
    #print("DES1", des1)
    #print("DES2", des2)

    matches = bf.match(des1, des2)



  # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)
  #img3 = cv2.drawMatches(im1, kp1, im2, kp2, matches[:], None, flags=2)
  #print(img3)
  #plt.imshow(img3), plt.show()


    m=matches[-1]
    i=1
    count=0
    while matches[i]!=m:
      count=count+1
      i=i+1
    if Max<count:
      Max=count
      FileName=IF
    #print("number of matches",count)
    #print("File Name with Matches", IF)
    #F = IF.split("_", maxsplit=1)[0]
    #A[int(F[-1])]=A[int(F[-1])]+count


  #print(A)
  #print("total matches",max(A))
  #F=A.index(max(A))
  #FileName='000'+str(F)




  #base = os.path.basename(imageName)
  #rn=os.path.splitext(base)[0]

  #out=rn+'.txt'

  #print ('Output is saved in file -',out)

  F=FileName.split("_", maxsplit=1)[0]
  #print(F)

  return fl+'/'+F, FileName

