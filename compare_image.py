# -*- coding: utf-8 -*-

# http://stackoverflow.com/questions/14404731/pyhon-image-comparison-regardless-of-size
# http://www.guguncube.com/1656/python-image-similarity-comparison-using-several-techniques
from PIL import Image
from numpy import average, linalg, dot
import time
 
 
def main():
  
    t1=time.time()
    ress= image_similarity_vectors_via_numpy1()
    myoutput      =  'F:/data/xcar/output_sim.txt'
    with open(myoutput, 'w') as file:  
        for res in ress:
            file.write(str(res['res']) + res['img1'] + res['img2'] + '\n')
    
 
    t2=time.time()
    print('time:'+str(t2 - t1))
 
def image_similarity_vectors_via_numpy1():

    image_urls = [ 
'F:/data/xcar/img/small/4_s7258_120.jpg',
'F:/data/xcar/img/small/3014_s7247_120.jpg',
'F:/data/xcar/img/small/1645_s3202_120.jpg',
'F:/data/xcar/img/small/957_s6161_120.jpg',
'F:/data/xcar/img/small/7_s7213_120.jpg'
  ]
    images = [
Image.open(image_urls[0]),
Image.open(image_urls[1]),
Image.open(image_urls[2]),
Image.open(image_urls[3]),
Image.open(image_urls[4]) 
    ]
    vectors = []
    norms = []
    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        norms.append(linalg.norm(vector, 2))
 
    res = []
    for i in range(5):
        for j in range(5):
            if (i == j) :
                continue
            else:
                res1 = dot(vectors[i] / norms[i], vectors[j] / norms[j])    
                couple = {}
                couple = {'res':res1, 'img1':image_urls[i], 'img2' : image_urls[j]}
                res.append(couple)
    return res

def get_thumbnail(image, size=(60,45), greyscale=False):
    #get a smaller version of the image - makes comparison much faster/easier
    image = image.resize(size, Image.ANTIALIAS)
    if greyscale:
        #convert image to greyscale
        image = image.convert('L')
    return image
  
 
if __name__ == "__main__":
    main()
