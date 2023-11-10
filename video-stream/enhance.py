from cv2 import equalizeHist, cvtColor, COLOR_RGB2GRAY, COLOR_BGR2GRAY, COLOR_GRAY2RGB
from threading import Thread


def process_result(x, y, x2, y2, frame):
    w = x2-x
    h = y2-y
    pedestrian_region_RGB = frame[y:y+h, x:x+w]
    pedestrian_region_GRAY = cvtColor(
        pedestrian_region_RGB, COLOR_RGB2GRAY)
    enhanced_pedestrian_region = equalizeHist(pedestrian_region_GRAY)
    frame[y:y + h, x:x +
          w] = cvtColor(enhanced_pedestrian_region, COLOR_GRAY2RGB)


def enhance(frame, results):
    frame = cvtColor(frame, COLOR_BGR2GRAY)
    frame = cvtColor(frame, COLOR_GRAY2RGB)

    # Detected pedestrian bounding boxes
    pedestrians = results

    threads = []
    for bounding_boxes in pedestrians:
        boxes = bounding_boxes.boxes.xyxy.cpu().numpy().astype(int)
        for (x, y, x2, y2) in boxes:
            thread = Thread(
                target=process_result, args=(x, y, x2, y2, frame))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    return frame
