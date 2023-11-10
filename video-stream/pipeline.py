import threading
from queue import Queue
from threading import Event
from ultralytics import YOLO
from enhance import enhance
from resolution import resolution
# from detect import detect


class Stage:
    def __init__(self, name, buffer_size):
        self.name = name
        self.buffer_size = buffer_size
        self.input_buffer = Queue(maxsize=buffer_size)
        self.output_buffer = Queue(maxsize=buffer_size)
        # self.stop_event = Event()
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def __repr__(self):
        return f'<Stage name={self.name}>'

    def run(self):
        while True:
            input_data = self.input_buffer.get()

            if self.event.is_set():
                break

            processed_data = self.process(input_data)

            self.output_buffer.put(processed_data)

    # Override this method in the concrete stage classes.
    def process(self, input_data):
        pass


class ResolutionStage(Stage):
    def __init__(self, input_video, output_video, new_width, new_height, codec='mp4v'):
        super().__init__(name='Resolution', buffer_size=10)
        self.input_video = input_video
        self.output_video = output_video
        self.new_width = new_width
        self.new_height = new_height
        self.codec = codec

    def process(self, input_data):
        resolution(self.input_video, self.output_video,
                   self.new_width, self.new_height, self.codec)


class DetectStage(Stage):
    def __init__(self, model):
        super().__init__(name='Detection', buffer_size=10)
        self.model = model

    def process(self, input_data):
        frame = input_data
        results = self.model(frame)
        return results


class EnhanceStage(Stage):
    def __init__(self):
        super().__init__(name='Enhance', buffer_size=10)

    def process(self, input_data):
        frame, results = input_data
        enhanced_frame = enhance(frame, results)
        return enhanced_frame


class Pipeline:
    def __init__(self, stages):
        self.stages = stages

    def run(self):

        self.stages[0].input_buffer.put('Start')

        self.stages[-1].output_buffer.get()

        for stage in self.stages:
            stage.thread.join()


def main():
    # Define the buffer size.
    buffer_size = 10

    # Create the stages in the pipeline.
    resolution_stage = ResolutionStage(
        input_video='video1.mp4', output_video='output.mp4', new_width=576, new_height=1024)
    detect_stage = DetectStage(model=YOLO('yolov8s.pt'))
    enhance_stage = EnhanceStage()

    # Create the pipeline.
    pipeline = Pipeline([resolution_stage, detect_stage, enhance_stage])

    # with statement - to ensure that the thread attribute of the Stage class is always closed. This will prevent any resource leaks.
    # Run the pipeline.
    # with pipeline:
    pipeline.run()


if __name__ == '__main__':
    main()
