import os
from ocr import ocr
import time
import shutil
import numpy as np
from PIL import Image
from glob import glob
import cv2
from numpy import array

def single_pic_proc(image_file):
    # image opening with pil module, casting it in numpy array.
    image = np.array(Image.open(image_file).convert('RGB'))
    result, image_framed = ocr(image)
    return result,image_framed

def dis(image):
    cv2.imshow('image', image)
    cv2.waitKey()
    if cv2.waitKey(100000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

if __name__ == '__main__':
    import sys
    if len(sys.argv)>=2:
        filename = sys.argv[1] 
        if filename.endswith('jpg') or filename.endswith('png') or filename.endswith('jpeg') or filename.endswith('pdf'):
            result, image_framed = single_pic_proc(filename)
            print(result)
            f = open("demofile2.txt", "a")
       
            for i in result:
                print(result[i][1]+",",)
                f.write(result[i][1]+",")
                f.write("\n")
            f.close() 
            
            dis(image_framed)
