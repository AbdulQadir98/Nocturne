from ultralytics import YOLO

def detect(model, input_data):
    frame = input_data
    results = model(frame)
    return results
        