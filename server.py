from flask import Flask, request, jsonify
import base64
import face_recognition
from io import BytesIO

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/compare', methods=['POST'])
def compare():
    # get the data
    refImage = face_recognition.load_image_file("content/lqReference.jpg")
    refEncoding = face_recognition.face_encodings(refImage)[0]
    
    images = request.json['images']
    distances = []
    index= 0
    mindistance=1
    for base64Image in images:
        if base64Image.startswith('data:image'):
            base64Image = base64Image.split('base64,')[1]
        image_data = base64.b64decode(base64Image)
        image = face_recognition.load_image_file(BytesIO(image_data))
        image_encoding = face_recognition.face_encodings(image)[0]
        distance = face_recognition.face_distance([refEncoding], image_encoding)[0] 
        if distance<mindistance:
            mindistance = distance
            index = len(distances)
        distances.append(distance)

    average = sum(distances) / len(distances)
    decision = average < 0.48
    result = {
        "result": str(decision),
        "best": index,
        "average": average,       
        "distances": distances,
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    