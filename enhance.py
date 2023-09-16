import cv2
from cv2 import equalizeHist
import threading


def process_result(x, y, x2, y2, frame):
    w = x2-x
    h = y2-y
    pedestrian_region_RGB = frame[y:y+h, x:x+w]
    pedestrian_region_GRAY = cv2.cvtColor(
        pedestrian_region_RGB, cv2.COLOR_RGB2GRAY)
    enhanced_pedestrian_region = equalizeHist(pedestrian_region_GRAY)
    frame[y:y + h, x:x +
          w] = cv2.cvtColor(enhanced_pedestrian_region, cv2.COLOR_GRAY2RGB)


def enhance(frame, results):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)

    # Detected pedestrian bounding boxes
    pedestrians = results

    # Create and start threads
    threads = []
    for bounding_boxes in pedestrians:
        boxes = bounding_boxes.boxes.xyxy.cpu().numpy().astype(int)
        for (x, y, x2, y2) in boxes:
            thread = threading.Thread(
                target=process_result, args=(x, y, x2, y2, frame))
            threads.append(thread)
            thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return frame
