from PIL import Image

def route_analysis(image: Image.Image, image_type: str):
    if image_type == "single_face":
        return {"emotion": "happy"}  # dummy fallback
    elif image_type == "group":
        return {"group_emotion": "joyful"}  # dummy fallback
    else:
        return {"scene_description": "A beautiful landscape"}  # dummy fallback