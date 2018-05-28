#########################################################################################
#function:	func1 = pixelGetter(arg1)
#		func2 = pileUp(arg1,arg2,arg3,arg4,arg5)
#About:		This file define function that be able to superposer two images.
#		func1 is the function to insert array pixel of image.
#		func2 is the function of superpose images.
#Argument:	func1.arg1 = 'image file name except extension'
#		func2.arg1 = 'pixelGetter of pic1', func2.arg2 = 'pixelGetter of pic2', func2.arg3 = 'it is a part of a image to superpose. however, one out of two', func2.arg4 = 'it is a part of a image to superpose. however, two out of two', func2.arg5 = 'output image of superposed.'
#Create:	Yuki FURUTA 20180429
#Edit:		xxxxxx
#########################################################################################

#install pillow and numpy
from PIL import Image
import numpy as np

#function to insert array pixel of image
def pixelGetter(img):
	#open image
	img = Image.open(img)
	
	#insert size of image (vertical x horizontal)
	#it is 320 x 180.
	size = img.size
	#print(size[0])
	#print(size[1])

	#retuen definition to insert variable of array
	img_pixels = []
	for x in range(size[0]):
		for y in range(size[1]):
			#get information of pixel order by top-left of image
			#information of 1pixel is (r, g, b, Transparency)
			#it is inserted this information by append
			img_pixels.append(img.getpixel((x,y)))

	#return array of informed pixel
	return img_pixels

#function of superpose images
def pileUp(pic1, pic2, input_image1, input_image2, output_image):
	#open two images
#	img  = Image.open("./image_dir/img_000033_000117.png")
#	img2 = Image.open("./image_dir/img_000033_000119.png")
	img  = Image.open(input_image1)
#	img  = Image.open("../data/input/train_png/img_000033_000117.png")
	img2 = Image.open(input_image2)
#	img2 = Image.open("../data/input/train_png/img_000033_000119.png")

	#input size of images
	size = img.size
	size2 = img2.size

	#definition variable to superpose images
	#actually, make new other image from two input images
	#so, it is need to define variable for inserted 3rd image.
	#input (320x180), because thay are same size.
	new_img = Image.new("RGBA", size)

	#treatment superpose images
	#to superpose images is sum each a pixel of in the treatment .
	#it is same principle as to become dark-red that transparent underlays superpose.
	#thus, (R, g, b) of the pixcels of the same position of image are added together 
	i = 0
	for x in range(size[0]):
		for y in range(size[1]):
			r = pic1[i][0] + pic2[i][0]
			g = pic1[i][1] + pic2[i][1]
			b = pic1[i][2] + pic2[i][2]

			#for an array containing pixel information, it does not match the format to display image.
			#thus, convert it to the image display format using "putpixel"
			new_img.putpixel((x, y), (r, g, b, 255))
			i += 1

	#display images superposed by retuen
#	print(type(new_img))
	new_img.save(output_image)
#	return new_img.show()

#pic1 = pixelGetter("./image_dir/img_000033_000117.png")
#pic2 = pixelGetter("./image_dir/img_000033_000119.png")
#pic1 = pixelGetter("../data/input/train_png/img_000033_000117.png")
#pic2 = pixelGetter("../data/input/train_png/img_000033_000119.png")

#pileUp(pic1, pic2)


