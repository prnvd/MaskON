# MaskON
A simple python program to generate data for my face mask detection project, uses a without masks and overlaps a .png image of a mask on the face of the person.
The program in this file is for just one image of a person, it can be modified to run over multiple images.

The program uses the face of people as input and does some simple processing with the help of OpenCV to put a mask on the person's face. 

The input image is essentially the picture of a person (it is recommened that image be resized to 250X250 pixels ) and a .png file of a mask, which I created in photoshop and has a black background. 

The program can be made to run over multiple images in any folder by a small addition to the program. But this sometimes doee not yield an accurate result.
The program may not work in certain cases, this may be due to the format/size of the images.

The cascade classifier I used is also attached here. I do not own classifier. I am not using any of this for monetary benefit.

