# cmt307-g12
Machine Learning CMT307 coursework project Group 12

# How to run this script:

You found this script inside the folder *cmt307-g12*.<br/>
For this script to run, you must include a **data** folder inside the same directory (*cmt307-g12* folder).The **data** folder can be downloaded using any of these two links:

<br/>

_Full version_ (recommended)
The link below contains all the source pictures to perform the analysis, but also the **checkpoints** from our own notebook runs. Original and transformed pictures will be loaded from these files instead of being built from the notebook, saving considerable time. 6.7 GB.

[Full version - Google drive shared folder](https://drive.google.com/drive/folders/10bMa-JVY9rUmmIhqowkU6JKAzJkwhEWt?usp=sharing)

_Light version_ (minimum requirements)
The link below contains only the ppm pictures from the train and test datasets, and the labels from the test set. The pictures will be decoded and transformed in your own machine/Colab session. 563 MB.

[Light version - OneDrive shared folder](https://cf-my.sharepoint.com/:f:/g/personal/mendoza-jimenezjc_cardiff_ac_uk/EoB0DfS8H_BJi1zNCLRflaIBlJUCf2_NRco5yRzg5gAN_w)



<br/>

If for whatever reason the links above don't work, you could also find the **data** folder in the [github repository](https://github.com/jm20389/cmt307-g12) (ligth version).

<br/>

Contents of **cmt307-g12** after you include the data folder:

<br/>

|     **Item**     |                                   **Description**                                  | **Required to run** |
|:----------------:|:----------------------------------------------------------------------------------:|:-------------------:|
|    main.ipynb    |                                Present python script                               |         Yes         |
|      data        |                     Folder containing data sources and pictures                    |         Yes         |
|      report      |               Folder to save pyplot pictures to be used in the report              |         No          |
|     README.md    |                            README file with instructions                           |         No          |
| requirements.txt | txt file listing required python modules/packages to run the script **main.ipynb** |         No          |

<br/>

This script is capable of detecting whether you are working in your local machine or in Google Colab, and will adjust the data directory addresses accordingly (section 0.2).

***
<br/>

<br/>

### Option A - Run locally using Jupyter Notebooks:

Download the **data** folder from the above link and paste it inside *cmt307-g12*. 
<br/>
Then the script can be run using Jupyer Notebooks from whatever location.

<br/>

### Option B - Run using Google Colab:

Download the **data** folder from the above link and paste it inside *cmt307-g12*. 
<br/>
For this script to run in Google Colab, **the folder cmt307-g12 must be placed in the ROOT of your Google Drive:**

<br/>

#%cd /content/gdrive/MyDrive


<br/>

### Option C - Github repository:

This project has been uploaded to github as a repository. You can **clone** this repository in your local machine or in your Google Drive:
<br/>
https://github.com/jm20389/cmt307-g12

If you run this repository in Google Colab, the **repository folder must be cloned in the ROOT of your Google Drive:**
<br/>

<br/>

1. In Google Colab, mount your drive first:
<br/>

#from google.colab import drive
#drive.mount('/content/gdrive')

2. Navigate through the Google Drive root:
<br/>

#%cd /content/gdrive/MyDrive
#!ls

3. Clone the repository using Git:
<br/>


#!git clone https://git_token@github.com/jm20389/cmt307-g12.git


***

</br>

_If you run into RAM issues..._

</br>

Due to the magnitude of this project, and depending on your machine or cloud session setup, you may run out of RAM memory. During section 0.2.2 , recovery functions are defined, to retrieve picture data from the **checkpoint files** (stored in the subfolder _data/numpy_). 

</br>

In the unlikely event that your session crashes, and provided you have all the checkpoint files available (either downloaded from the links provided or created from running sections 1 and 2), you can resume the analysis from Section 3 as follows: 

<br/>

From a fresh session, run sections **0.1, 0.2.1 and 0.2.2**, then open a new cell anywhere and run the function _RecoverEverything()_ . All required items to carry on from Section 3 will be loaded in the kernel to continue the analysis.
