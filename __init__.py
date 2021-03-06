#Backend Server code -> check the readme file for more info
#import the necessary packages
import os
import natsort
from flask import Flask, request, Response, render_template
import numpy as np
import cv2
from Adhoc_Algo import detect_Adh


#create a flask app
app = Flask(__name__)
#configure the route
@app.route('/', methods=['POST','GET'])

def upload_image():
	#default message and image of the homepage
	msg = "We live in a beautiful world. Filled with amazing things and opportunities yet we hardly acknowledge them. Here you can find some information of the plants around you."
	imagePath = "static/img/start.jpg"
	ref = 'static/img/leaf.png'
	t1 = ''
	t2 = ''

	#check if data is coming through post request
	if request.method == "POST":
		if request.files:
			#retrieve image from client
			r = request
			# convert string of image data to uint8
			nparr = np.fromstring(r.files['leaf_image'].read(), np.uint8)
			# decode image
			img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

			#do some fancy processing in the function
			msg, imagePath, ref = fun_processing(img)
			t1='Uploaded Image'
			t2='Matched Image'

	return render_template("public/upload_image.html", message_from_backend=msg, imagePath=imagePath, matched_image=ref, image_tag_1=t1, image_tag_2=t2)

#The function
def fun_processing(img):
	
	#Resize the image
	r = 512.0 / img.shape[1]
	dim = (512, int(img.shape[0] * r))
	resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
	
	#find out if the directory is empty or not
	paths = natsort.natsorted(os.listdir('static/uploads/'))
	if paths == []:
		file_number = 1
	else:
		last_path = paths[-1]
		file_number = ''
		for i in last_path:
			if i == '.':
				break
			else:
				file_number += i 
		file_number = int(file_number)
		file_number += 1

	storagePath = ('static/uploads/%s.jpg'%file_number)
	#save the image
	cv2.imwrite(storagePath, resized)

	#check for adhoc
	fileName = os.path.basename(storagePath)
	filePath = str(storagePath).replace(fileName,'')

	imageResultPath, ref =detect_Adh(fileName, filePath)
	#get the path to the txt file 
	result=imageResultPath+".txt"
	ref = "static/img/ImageSet/"+ref
	#open and read the txt file
	try:
		with open(result) as f :
			msg = f.read()
	except Exception:
		msg = 'File not found'

	return msg, storagePath, ref

#start the server
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
