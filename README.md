# cmt307-g12

Machine Learning CMT307 module coursework - Group 12. Cardiff University.

Machine Learning image classification project. The dataset used is the German Traffic Sign Recognition Benchmark (GTSRB), which contains 43 classes of traffic signs, split into 39,209 training images and 12,630 test images. The images have varying light conditions and rich backgrounds.
https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/published-archive.html

- main.ipynb: main python notebook performing tasks T1, T2 and T3. 

  - Data acquisition from ppm pictures.
  - Data preprocessing converting ppm pictures into numpy arrays.
  - Descriptive statistics from the decoded pictures dataset:
      Number of pictures per category (type of traffic sign), pixel intensity distribution (on scale 0-255), visualization of 25 random pictures.
      
  - Implementation of a Convolutional Neural Network for image classification.

- data: folder containing traffic sign pictures, in ppm format.
   - train: Set of training pictures, organized in folders corresponding to each category.
   - test: Set of test pictures, containing random traffic sign pictures from different categories.
   - numpy: Checkpoint folder, contains the transformed train and test picture dataset, converted to numpy arrays using pyplot.imread
 
 - resources: University academic paperwork with instructions about how to submit the project.
 
 - saved_models: Checkpoint folder to store already run keras models - CNN architecture.
