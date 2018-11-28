from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import cv2


class CompareImages:
    def __init__(self, SRC, TRG, WIDTH, HEIGHT, METHOD):
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
        if self.method == "FAISS":
            return 0

        elif self.method == "SSIM":
            similarity = ssim(image1, image2)
            print("SSIM: %.2f" % similarity)
            return similarity

        else:
            raise Exception("The suggested method is not implemented. Try another!")

    def compare_all_images(self):
        source_img = cv2.imread(self.SRC)
        source_img = cv2.resize(source_img, (self.WIDTH, self.HEIGHT))

        target_files = self.get_file_names()

        target_probs = []
        for i, file in target_files:
            target_img = cv2.imread(self.TRG[i])
            target_img = cv2.resize(target_img, (self.WIDTH, self.HEIGHT))
            self.compare_images(source_img, target_img)

        return target_probs


if __name__ == "__main__":
    WIDTH = 512
    HEIGHT = 512
    METHOD = "SSIM"

    SRC = "../data/source/add_block.jpg"
    TRG = "../data/target/"

    CompareImages(SRC, TRG, WIDTH, HEIGHT, METHOD)
