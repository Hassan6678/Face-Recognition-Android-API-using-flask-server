import flask
import werkzeug
import json

def face_rec(unknow_image):
    import face_recognition
    from PIL import Image, ImageDraw

    image_of_Hassan = face_recognition.load_image_file('./image/Hassan.jpg')
    Hassan_face_encoding = face_recognition.face_encodings(image_of_Hassan)[0]

    image_of_Asad = face_recognition.load_image_file('./image/Asad.jpg')
    Asad_face_encoding = face_recognition.face_encodings(image_of_Asad)[0]


    #  Create arrays of encodings and names
    known_face_encodings = [
        Hassan_face_encoding,
        Asad_face_encoding,
    ]

    known_face_names = [
        "Hassan",
        "Asad"
    ]

    # Load test image to find faces in
    test_image = face_recognition.load_image_file(unknow_image)

    # Find faces in test image
    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)

    # Convert to PIL format
    pil_image = Image.fromarray(test_image)

    # Loop through faces in test image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown Person"

        # If match
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

    return name


app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle_request():
    '''
    # To retrieve image that is sent from android app and is placed inside image folder
    imagefile = flask.request.files['image']

    # to retrieve image name
    filename = werkzeug.utils.secure_filename(imagefile.filename)

    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(filename)
    '''

    # Asad Bhai
    image = './image/Asad_test_2.jpg'
    name = face_rec(image)
    resp_data = {'name': name}

    return json.dumps(resp_data['name'])

    #return "Image Uploaded Successfully"


app.run(host="0.0.0.0", port=5000, debug=True)
