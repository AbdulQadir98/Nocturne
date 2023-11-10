from queue import Queue
from threading import Thread, Event


class Stage:
    def __init__(self, name, buffer_size):
        self.name = name
        self.buffer_size = buffer_size
        self.input_buffer = Queue(maxsize=buffer_size)
        self.output_buffer = Queue(maxsize=buffer_size)
        # self.stop_event = Event()
        self.thread = Thread(target=self.run)
        self.thread.start()

    def __repr__(self):
        return f'<Stage name={self.name}>'

    def run(self):
        while True:
            # Get the next input from the input buffer.
            input_data = self.input_buffer.get()

            # Check if the stage has been stopped.
            if self.event.is_set():
                break

            # Process the input data.
            processed_data = self.process(input_data)

            # Put the processed data in the output buffer.
            self.output_buffer.put(processed_data)

    # def run(self):
    #     while not self.stop_event.is_set():
    #         # Get the next input from the input buffer.
    #         input_data = self.input_buffer.get()

    #         # Check if the stage has been stopped.
    #         if self.stop_event.is_set():
    #             break

    #         # Process the input data.
    #         processed_data = self.process(input_data)

    #         # Put the processed data in the output buffer.
    #         self.output_buffer.put(processed_data)

    #     # Signal that the stage has finished processing data.
    #     self.stop()

    # def stop(self):
    #     self.stop_event.set()

    def process(self, input_data):
        pass


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
        return processed_frame


class Pipeline:
    def __init__(self, stages):
        self.stages = stages
        # self.event = threading.Event()
        self.connect_stages()

    def connect_stages(self):
        for i in range(len(self.stages) - 1):
            print(self.stages[i])
            self.stages[i].output_buffer = self.stages[i + 1].input_buffer

    def run(self):
        # Start the first stage.
        self.stages[0].input_buffer.put('Start')

        # Wait for the last stage to finish.
        self.stages[-1].output_buffer.get()

        # Stop all of the stages.
        for stage in self.stages:
            stage.stop()

        # Wait for all of the threads to finish.
        for stage in self.stages:
            stage.thread.join()

    def stop(self):
        self.event.set()


def main():

    # Create the stages in the pipeline.
    resolution_stage = ResolutionStage()
    detect_stage = DetectStage()
    enhance_stage = EnhanceStage()

    # Create the pipeline.
    pipeline = Pipeline([resolution_stage, detect_stage, enhance_stage])

    # FOR TESTING STREAM
    data_stream = ["Frame 1", "Frame 2", "Frame 3", "Frame 4", "Frame 5"]

    # Input the data stream into the pipeline
    for data in data_stream:
        resolution_stage.input_buffer.put(data)

    pipeline.run()

    # event = threading.Event()
    # # Trigger the event to stop the pipeline.
    # event.set()
    # pipeline.stop()

    # Print the final frames


if __name__ == '__main__':
    main()
