#########################################################################################
#function:    func1 = video_2_frames(arg1,arg2,arg3,arg4)
#             func2 = 
#About:       This file define function to convert video to png separationg by flame.
#Argument:    arg1 = 'video file name except extension', arg = 'it is directory that is stored input video file', arg3 = 'it is directory that will be stored output image file' arg4 = 'extension of video.'
#Create:      Yuki FURUTA 20180429
#Edit:        xxxxxx
#########################################################################################

#pip3 install opencv-python
import os
import shutil
import cv2

#def video_2_frames(video_file='./000001.mpg', image_dir='./image_dir/', image_file='img_000001_%s.png'):
def video_2_frames(arg_video_file_name='./000001', arg_video_in_dir='video_in_dir' , arg_image_out_dir='image_out_dir', arg_ext=''):

    video_in_dir='./' + arg_video_in_dir + '/'
    image_out_dir='./' + arg_image_out_dir + '/'
    image_out_file=image_out_dir + 'img_' + arg_video_file_name + '_%s.png'
    video_file=video_in_dir + arg_video_file_name + '.' + arg_ext

    # Delete the entire directory tree if it exists.
#    if os.path.exists(video_in_dir):
#        shutil.rmtree(video_in_dir)  

    # Make the directory if it doesn't exist.
    if not os.path.exists(video_in_dir):
        os.makedirs(video_in_dir)

    # Delete the entire directory tree if it exists.
#    if os.path.exists(image_out_dir):
#        shutil.rmtree(image_out_dir)  

    # Make the directory if it doesn't exist.
    if not os.path.exists(image_out_dir):
        os.makedirs(image_out_dir)

    # Video to frames
    i = 0
    cap = cv2.VideoCapture(video_file)
    while(cap.isOpened()):
        flag, frame = cap.read()  # Capture frame-by-frame
        if flag == False:  # Is a frame left?
            break
        cv2.imwrite(image_out_file % str(i).zfill(6), frame)  # Save a frame
        print('Save', image_out_file % str(i).zfill(6))
        i += 1

    cap.release()  # When everything done, release the capture

#video_2_frames('000033','image_dir')
