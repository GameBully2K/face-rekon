import face_recognition
import cv2

known_image = face_recognition.load_image_file(f"content/lqReference.jpg")
biden_encoding = face_recognition.face_encodings(known_image)[0]
cv2.imshow('ref', known_image)

distanceAvrg = 0
for i in range(1, 6):
    unknown_image = face_recognition.load_image_file(f"content/{i}.jpg")
    cv2.imshow('image', unknown_image)
    cv2.waitKey(0)
    cv2.destroyWindow('image')
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces([biden_encoding], unknown_encoding, tolerance=0.49)
    distance = face_recognition.face_distance([biden_encoding], unknown_encoding)[0]
    distanceAvrg += distance
    print(results, distance)
distanceAvrg /= 5
print(f"Average distance: {distanceAvrg}")
cv2.waitKey(0)
cv2.destroyAllWindows()

# Load the jpg files into numpy arrays
# known_image = face_recognition.load_image_file("content/lqReference.jpg")
# biden_encoding = face_recognition.face_encodings(known_image)[0]

# unknown_images =[]
# for i in range(1, 6):
#     unknown_images.append(face_recognition.load_image_file("content/{i}.jpg"))
# unknown_encodings = face_recognition.face_encodings(unknown_images)

# results = []
# for unknown_encoding in unknown_encodings:
#     results.append(face_recognition.compare_faces([biden_encoding], unknown_encoding ))

# print(biden_encoding)

