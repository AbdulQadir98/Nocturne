import threading
from queue import Queue
from threading import Event


class Stage:
    def __init__(self, name, buffer_size):
        self.name = name
        self.buffer_size = buffer_size
        self.input_buffer = Queue(maxsize=buffer_size)
        self.output_buffer = Queue(maxsize=buffer_size)
        self.stop_event = Event()
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def run(self):
        while True:
            input_data = self.input_buffer.get()
            processed_data = self.process(input_data)

            self.output_buffer.put(processed_data)

    def process(self, input_data):
        pass

    def stop(self):
        self.stop_event.set()


class ResolutionStage(Stage):
    def __init__(self):
        print("ResolutionStage")
        super().__init__(name='Resolution', buffer_size=10)

    def process(self, frame):
        print("R", frame)
        processed_frame = frame
        return processed_frame


class DetectStage(Stage):
    def __init__(self):
        print("DetectStage")
        super().__init__(name='Detection', buffer_size=10)

    def process(self, frame):
        print("D", frame)
        processed_frame = frame
        return processed_frame


class EnhanceStage(Stage):
    def __init__(self):
        print("EnhanceStage")
        super().__init__(name='Enhance', buffer_size=10)

    def process(self, frame):
        print("E", frame)
        processed_frame = frame
        processed_frame = frame
        return processed_frame


class Pipeline:
    def __init__(self, stages):
        self.stages = stages
        self.connect_stages()

    def connect_stages(self):
        for i in range(len(self.stages) - 1):
            self.stages[i].output_buffer = self.stages[i + 1].input_buffer

    def run(self):
        self.stages[0].input_buffer.put('Start')

        self.stages[-1].output_buffer.get()

        for stage in self.stages:
            stage.stop()

        for stage in self.stages:
            stage.thread.join()

    def stop(self):
        for stage in self.stages:
            stage.stop()


def main():

    resolution_stage = ResolutionStage()
    detect_stage = DetectStage()
    enhance_stage = EnhanceStage()

    pipeline = Pipeline([resolution_stage, detect_stage, enhance_stage])

    # FOR TESTING STREAM
    data_stream = ["Frame 1", "Frame 2", "Frame 3", "Frame 4", "Frame 5"]

    for data in data_stream:
        detect_stage.input_buffer.put(data)

    pipeline.run()


if __name__ == '__main__':
    main()
