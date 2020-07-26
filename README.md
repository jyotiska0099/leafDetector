*****************  READ CAREFULLY TO RUN THE APPLICATION PROPERLY  ******************


## Welcome to the leaf classifier web-app version 1.0
	it takes an image from the user using a web-app, pass it to a server and display the output

necessary packages to run the flask backend server: flask, opencv-python, numpy, os.
install them using pip or conda, (hint: type in terminal="pip install flask")

## directory tree till now:
	-app
		-__pycache__
		-static
			-css
				-style.css
			-img
				-ImageSet (reference image set)
				-start.jpg
			-uploads (Uploaded Images will be stored here)
		-templates
			-public
				-upload_image.html
		-Adhoc_Algo.py
		-__init__.py
		-README.md



# To run the application:

 1. Start the backend server:
 	1.1 Go inside the app folder 
 	1.2 type in terminal = "python __init__.py"
 	( The flask server will run at localhost at port 5000 )
 	
 2. Open web browser
 3. Search in addressbar = "http://localhost:5000" (The landing page will show up)
	< you can also run it in your mobile phone if it's connected in the same wi-Fi network, camera can be also accessed. just in place of localhost write the ip address of your computer (to know it, in linux type "ifconfig", in windows type "ipconfig") >

 4. Select an image
 5. Press the upload button ( The image will store in "static/uploads/")
