import unittest
import cv2
import numpy as np
from src.preprocessing import preprocess_image
from src.contour_detection import find_contours, calculate_contour_properties, filter_contours, draw_contours

class TestContourDetection(unittest.TestCase):
    def setUp(self):
        # Path to the test Image
        self.image_path = '/Users/rickgummy/sem-image-processing-toolkit/data/raw/C1-3_A_m06.tif'
        self.image = preprocess_image(self.image_path)

    def test_find_contours(self):
        contours = find_contours(self.image)
        self.assertIsNotNone(contours)
        self.assertGreater(len(contours), 0)

    def test_calculate_contour_properties(self):
        contours = find_contours(self.image)
        for contour in contours:
            perimeter, area, circularity = calculate_contour_properties(contour)

    def test_filter_contours(self):
        contours = find_contours(self.image)
        filtered_contours = filter_contours(contours)
        for contour in filtered_contours:
            perimeter, area, circularity = calculate_contour_properties(contour)
            """
            self.assertGreaterEqual(area, 100)
            self.assertLessEqual(area, 30000)
            self.assertGreaterEqual(circularity, 0.5)
            self.assertLessEqual(circularity, 1.5)
            """

    def test_preprocess_and_filter(self):
        # End to end test: preprocess, find, and filter contours
        filtered_contours = filter_contours(find_contours(self.image))
        self.assertGreater(len(filtered_contours), 0)

    def test_draw_contours(self):
        # Test drawing contours on the image
        original_image = cv2.imread(self.image_path, cv2.IMREAD_COLOR)
        self.assertIsNotNone(original_image, "Failed to load the original image")
        contours = find_contours(self.image)
        filtered_contours = filter_contours(contours)
        contour_image = draw_contours(original_image, filtered_contours)
        self.assertIsNotNone(contour_image)
        cv2.imwrite('tests/C1-3_A_m06_contoured_image.tif', contour_image)
        
if __name__ == '__main__':
    unittest.main()



