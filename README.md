# FindCropOfAnImage
Find Crop Of An Image

#Images_crops_association
Code is written in python language
# packages needed:
1) cv2(opencv) : All major task done using opencv like reading image ,
template matching.
to install opencv use : pip install opencv-python
2) glob : looping on files in a folder
3) time : for counting of processing time
4) argparse : argument parser for python
5) json : for json operation like dictionary to json and dumping into files.
# Approach:
Used template matching using OpenCv to detect the crops with location and %
match value.
Template matching is like sliding the crops on full image and counting the
difference between both if it is less or near to zero then there is a match at
that location.
# Assumptions:
I am assuming that a crop can not be bigger then the full image so applied
an image shape checker.
As the crops are cropped from the same image so match will be higher
around 99.9% or 100%, but still i am using threshold as 98%.
# How To Run The Code:
main.py is the file where all code is written.
we can run it from terminal with some parameters like folder location of full
images and crops and also output json file name
extract MAD.zip file
# ##################
$python main.py -c sample_testset/crops/ -f sample_testset/images/ -o
out.json
—help
-c : crops location
-f : full image location
-o : output file name
