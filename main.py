try:
    import scripts.compare as cmp
    import scripts.gen_matlab as gm

except ModuleNotFoundError:
    import compare as cmp
    import gen_matlab as gm

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
            print() #stream = "OpenCV input"
        else:
            stream = []

        # 2. GET BOUNDARIES FOR BLOCKS

        # 3. CROP IMAGE

        # 4. COMPARE WITH DATA/TARGET
        cmp.CompareImages(self.isStream,
                          stream,
                          self.SRC,
                          self.TRG,
                          self.WIDTH,
                          self.HEIGHT,
                          self.METHOD)

        # 5. RUN MATLAB GEN

if __name__ == "__main__":
    WIDTH = 180
    HEIGHT = 120
    METHOD = "SSIM"

    isStream = False

    SRC = "data/source/add_block.jpg"
    TRG = "data/target/"

    RunGen(isStream, SRC, TRG, WIDTH, HEIGHT, METHOD)