from tensorflow.keras.models import model_from_json,load_model
import numpy as np
import tensorflow as tf
import cv2
from PIL import Image
from PIL import ImageFile
import random
import dlib
import os
from django.shortcuts import render,redirect,HttpResponse

class FaceModel(object):
    IMG_SIZE = 128

    def __init__(self,model_json_file,model_weights_file,img_files):

        # Loading Model
        with open('embeddings.csv',"r") as embeddings:
            self.model.load_weights('embeddings.csv')

        # Loading Images
        self.images = cv2.imread(img_files)
        
    def get_img_locations(dets):
        img_lst=[]

        for i, d in enumerate(dets):
            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(i, d.left(), d.top(), d.right(), d.bottom()))
            dim = (d.left(), d.top(), d.right(), d.bottom())
            img_lst.append(dim)
        
        return img_lst
    
    def construct_image(img_loc, img_arr):
        left, top, right, bottom = img_loc
        face_image = img_arr[top:bottom, left:right]
        pil_img = Image.fromarray(face_image)
        
        return pil_img
    
    def preprocessImg(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        roi_img = None
        detector = dlib.get_frontal_face_detector()
        ## Detecting Face 
        try:
            img_arr = dlib.load_rgb_image(self.image)
            im = Image.open(self.image)
            img_arr = np.asarray(im)
            
            dets = detector(img_arr, 1)
            print("Number of faces detected: {}".format(len(dets)))
            image_locations = get_img_locations(dets)
            
            if len(dets)==0:
                print(f"No Face detected for given image ,Try again with new img :(")
                return "noFace",None
            
            else:
                for (x,y,w,h) in dets:
                    for img_loc in image_locations:
                        pil_img=construct_image(img_loc,img_arr)

                    pil_img.save('media/cropped_img/pulled_img/' + 'file'+ str(j) + str(j) + '.jpg')
        except Exception as _:
            print("An Error Ocurred, Please Try Again :(")
            return "exception",None
        

   

