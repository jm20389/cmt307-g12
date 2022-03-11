#!/usr/bin/env python
# coding: utf-8

# # Import required modules:

# In[5]:


import numpy as np
import os
import matplotlib.pyplot as plt

# other alternatives to load plt
#from scipy.misc import imread
#from scipy.misc import imread, imsave, imresize
#from skimage import io

import pandas as pd


# # Source training and test image files:

# In[6]:


train_dir = "data/train/"
test_dir = "data/test/"


# ***

# # Training set

# ### Obtain labels: For each different category:

# In[7]:


class_names = [
"Max Speed 20 km/h",
"Max Speed 30 km/h",
"Max Speed 50 km/h",
"Max Speed 60 km/h",
"Max Speed 70 km/h",
"Max Speed 80 km/h",
"End of 80 km/h zone",
"Max Speed 100 km/h",
"Max Speed 120 km/h",
"No passing",
"No passing for vehicles over 3.5 tonnes",
"Priority",
"Priority road",
"Yield",
"Stop",
"Road closed",
"Vehicles over 3.5 tonnes prohibited",
"Do not enter",
"General danger",
"Left curve",
"Right curve",
"Double curve",
"Uneven road surface",
"Slippery when wet or dirty",
"Road narrows",
"Roadworks",
"Traffic signals ahead",
"Pedestrians",
"Watch for children",
"Bicycle crossing",
"Ice - snow",
"Wild animal crossing",
"End of all restrictions",
"Turn right ahead",
"Turn left ahead",
"Ahead only",
"Ahead or turn right only",
"Ahead or turn left only",
"Pass by on right",
"Pass by on left",
"Roundabout",
"End of no passing zone",
"End of no passing zone for trucks"
]


# ### Label all training pictures (y_train)

# In[8]:


y_train = []

for folder in os.listdir(train_dir):
    
    pictures = [pic for pic in os.listdir(train_dir + "/" + folder) if pic.split(".")[-1] == "ppm" ] # filter out non-ppm files
    
    for picture in pictures:
        y_train.append(class_names[int(folder)]) # translates ClassId figure into label name, for example class_names[int(000000)] = 'Max Speed 20 km/h'

        
y_train = np.array(y_train)


# ### Create a function to decode all ppm pictures from a given directory into a numpy array;

# In[10]:


#Create a filtered list of .ppm files, then call plt.imread on the resulting list.

def PpmToNumpy(directory):
    
    '''
    Given a host directory containing ppm pictures, converts the pictures into a numpy array, returning an array with the whole list of pictures.

    Params:
    String containing a directory address.

    Returns:
    numpy array whose items are decoded ppm pictures (np.array)

    '''

    files = os.listdir(directory)
    files = [file for file in files if file.split(".")[1] == "ppm"] # to ensure only ppm images are called
    
    return np.array([plt.imread(directory + file) for file in files], dtype=object)
                       


# ### Build training dataset (x_train)

# In[11]:


all_images = [ PpmToNumpy(train_dir + "/" + folder + "/") for folder in os.listdir(train_dir)]

x_train = np.concatenate(all_images, axis=0, out=None, dtype=None, casting="same_kind")


# ### Show pictures - trial cell:
index = 12312

plt.figure()
plt.imshow(x_train[index, ], cmap = 'gray')
plt.title(y_train[index])
plt.show()
# In[31]:


type(x_train[0].shape[0])


# In[35]:


# Train summary file:

train_summary = dict.fromkeys(["Width", "Height", "ClassId"], [])
widths = []
heights = []

for picture in x_train:
    widths.append(picture.shape[0])
    heights.append(picture.shape[1])

train_summary["Width"] = widths
train_summary["Height"] = heights
train_summary["ClassId"] = y_train
 
train_summary_df = pd.DataFrame( train_summary)
train_summary_df.head(50)


# ***

# # Test set

# In[55]:


test_meta = pd.read_csv("data/Test.csv")
test_meta.head(20)


# In[63]:


y_test = np.array(test_meta["ClassId"].apply(lambda x: class_names[x]))

y_test


# In[64]:


x_test = PpmToNumpy(test_dir)


# ## Show pictures - trial cell:
index = 9796

plt.figure()
plt.imshow(x_test[index, ], cmap = 'gray')
plt.title(y_test[index])
plt.show()