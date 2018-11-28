from skimage.measure import compare_ssim as ssim
import cv2


class CompareImages:
    def __init__(self, isStream, STREAM, SRC, TRG, WIDTH, HEIGHT, METHOD):
        self.isStream = isStream
        self.STREAM = STREAM
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.METHOD = METHOD
        self.SRC = SRC
        self.TRG = TRG
        self.compare_all_images()

    def get_file_names(self, ext=('jpg', 'jpeg', '.png', '.tiff')):
        import os

        filenames = []
        filectr = 0
        for idx, file in enumerate(os.listdir(self.TRG)):
            if file.endswith(ext):
                filenames.append(file)
                print('Found: |  {}  | on Index: |  {}  |'.format(file, filectr))
                filectr += 1

        print('\n')

        return filenames

    def compare_images(self, image1, image2):
        if self.METHOD == "FAISS":
            return 0

        elif self.METHOD == "SSIM":
            similarity = ssim(image1, image2)
            return similarity

        else:
            raise Exception("The suggested method is not implemented. Try another!")

    def compare_all_images(self):

        if not self.isStream:
            source_img = cv2.imread(self.SRC, 0)
        else:
            source_img = self.STREAM

        source_img = cv2.resize(source_img, (self.WIDTH, self.HEIGHT))

        target_files = self.get_file_names()

        target_probs = []
        for i, file in enumerate(target_files):
            target_img = cv2.imread(self.TRG + file, 0)
            target_img = cv2.resize(target_img, (self.WIDTH, self.HEIGHT))
            target_probs.append(self.compare_images(source_img, target_img))

        print(target_probs)

        return target_probs


if __name__ == "__main__":
    WIDTH = 180
    HEIGHT = 120
    METHOD = "SSIM"

    isStream = False
    STREAM = []

    SRC = "../data/source/add_block.jpg"
    TRG = "../data/target/"

    CompareImages(isStream, STREAM, SRC, TRG, WIDTH, HEIGHT, METHOD)
