import cv2


def resolution(input_video, output_video, new_width, new_height, codec='mp4v'):

    cap = cv2.VideoCapture(input_video)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc(*codec)
    out = cv2.VideoWriter(output_video, fourcc, fps, (new_width, new_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Downscale the frame
        downscaled_frame = cv2.resize(frame, (new_width, new_height))

        # Write the frame
        out.write(downscaled_frame)

    cap.release()
    out.release()
