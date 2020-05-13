# Face-Recognition-Android-API-using-flask-server

## --> Steps

#### 1- Mobile app will do a post request to server and send a picture in request
#### 2- Method from server side that is handeling post request will recieve image by using code given below

```
import flask
import werkzeug

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():

	# To retrieve image that is sent from android app and is placed inside image folder
    imagefile = flask.request.files['image']

	# to retrieve image name    
    filename = werkzeug.utils.secure_filename(imagefile.filename)

    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(filename)

    return "Image Uploaded Successfully" 

app.run(host="0.0.0.0", port=5000, debug=True)
```
#### 3- After recieving image from android app You will do image recognition procedure on retrieved image (whose name is imagefile as given above )

#### 4- After Recognizing image you will print the name of the file to which it got matched.
