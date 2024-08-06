import unittest
import cv2
import numpy as np
import os
from src.preprocessing import load_image, convert_to_grayscale, enhance_contrast, apply_gaussian_blur, apply_threshold, preprocess_image

class TestPreprocessing(unittest.TestCase):
    def setUp(self):
        self.image_path = '/Users/rickgummy/sem-image-processing-toolkit/data/raw/C1-3_A_m06.tif'
        self.image = cv2.imread(self.image_path)
        if self.image is None:
            raise FileNotFoundError(f"Image at path {self.image_path} not found.")
            
    def display_image(self, image, title):
        plt.imshow(image, cmap='gray')
        plt.title(title)
        plt.show()

    def test_load_image(self):
        image = load_image(self.image_path)
        self.assertIsNotNone(image)

    def test_convert_to_grayscale(self):
        gray_image = convert_to_grayscale(self.image)
        self.assertEqual(len(gray_image.shape), 2)
        cv2.imwrite('tests/gray_image.tif', gray_image)

    def test_enhance_contrast(self):
        gray_image = convert_to_grayscale(self.image)
        enhanced_image = enhance_contrast(gray_image)
        self.assertEqual(enhanced_image.shape, gray_image.shape)
        cv2.imwrite('tests/enhanced_image.tif', enhanced_image)

    def test_apply_gaussian_blur(self):
        gray_image = convert_to_grayscale(self.image)
        blurred_image = apply_gaussian_blur(gray_image)
        self.assertEqual(blurred_image.shape, gray_image.shape)
        cv2.imwrite('tests/blurred_image.tif', blurred_image)

    def test_apply_threshold(self):
        gray_image = convert_to_grayscale(self.image)
        threshold_image = apply_threshold(gray_image)
        self.assertEqual(threshold_image.shape, gray_image.shape)
        cv2.imwrite('tests/threshold_image.tif', threshold_image)
    
    def test_preproess_image(self):
        threshold_image = preprocess_image(self.image_path)
        self.assertIsNotNone(threshold_image)
        cv2.imwrite('tests/preprocessed_image.tif', threshold_image)

if __name__ == '__main__':
    unittest.main()


