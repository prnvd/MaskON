# MaskON
A simple python program to generate data for my face mask detection project. Uses faces without masks and overlaps a .png image of a mask on the face of the person.

The program uses faces of people as input and does some simple processing with the help of OpenCV to put a mask on the person's face. 

The input images are essentially the pictures of people (size between 100X100 to 200X200 pixels) and a .png file of a mask, which I created in photoshop and has a black background. 

The reuslts are almost all the time accurate, except for few times when the face recognition does not recognise the face due to the format of the image or the type of picture of the person's face. For example, if a side view of a person is given to the program as input, it will not work properly.

The data set of people's face that I used is not my own, so I do not own that.
