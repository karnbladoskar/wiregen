import cv2
import time
import numpy as np
import sys

sys.path.append('/scripts')

try:
    import scripts.compare as cmp
    import scripts.gen_matlab as gml

except ModuleNotFoundError:
    import compare as cmp
    import gen_matlab as gml

class RunGen:
    def __init__(self, isStream, SRC, TRG, WIDTH, HEIGHT, METHOD):
        self.isStream = isStream
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.METHOD = METHOD
        self.SRC = SRC
        self.TRG = TRG

        self.run()

    def run(self):
        # 1. GET INPUT FRAMES
        if isStream:
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                cv2.imshow('Wiregen', frame)

                """
                # 2. GET BOUNDARIES FOR BLOCKS

                # 3. CROP IMAGE
                cropped_frame = [] # Cropped image goes here

                # 4. COMPARE WITH DATA/TARGET
                target_probs = cmp.CompareImages(self.isStream,
                                                  cropped_frame,
                                                  self.SRC,
                                                  self.TRG,
                                                  self.WIDTH,
                                                  self.HEIGHT,
                                                  self.METHOD)

                """
                # 5. RUN MATLAB GEN
                gml.GenMatlab(block_w=30, block_h=30)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

        else:
            stream = []


if __name__ == "__main__":
    WIDTH = 180
    HEIGHT = 120
    METHOD = "SSIM"

    isStream = True

    SRC = "data/source/add_block.jpg"
    TRG = "data/target/"

    RunGen(isStream, SRC, TRG, WIDTH, HEIGHT, METHOD)