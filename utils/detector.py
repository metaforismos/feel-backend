import face_recognition
import numpy as np

def detect_image_type(image):
    image_np = np.array(image)
    face_locations = face_recognition.face_locations(image_np)

    if len(face_locations) == 0:
        return "scene"
    elif len(face_locations) == 1:
        return "single_face"
    else:
        return "group"