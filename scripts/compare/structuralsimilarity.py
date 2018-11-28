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

	def compare_images(self, image1, image2, method):
		if self.method == "FAISS":
			return 1

		elif self.method == "SSIM":
			similarity = ssim(image1, image2)
			print("SSIM: %.2f" % similarity)
			return similarity


	def compare_all_images(self, source_img, target_imgs):
		source_img = cv2.resize(source_img, (WIDTH, HEIGHT))

		target_probs = []
		for target_img in target_imgs:
			target_img = cv2.resize(target_img, (self.WIDTH, self.HEIGHT))
			self.compare_images(source_img, target_img, self.METHOD)

		return target_probs

if __name__ == "__main__":
	WIDTH = 512
	HEIGHT = 512
	METHOD = "SSIM"

	SRC = cv2.imread("../../data/source/add_block.jpg", 0)
	TRG = cv2.imread("../../data/target/add_block.png", 0)

	CompareImages(SRC, TRG, WIDTH, HEIGHT, METHOD)