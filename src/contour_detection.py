import cv2
import numpy as np

def find_contours(image):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def calculate_contour_properties(contour):
    perimeter = cv2.arcLength(contour, True)
    area = cv2.contourArea(contour)
    if perimeter == 0:
        circularity = 0
    else:
        circularity = (4 * np.pi * area) / (perimeter ** 2)

    return perimeter, area, circularity

def filter_contours(contours, min_area = 100, max_area = 30000, min_circularity = 0.5, max_circularity = 1.5):
    filtered_contours = []
    for contour in contours:
        perimeter, area, circularity = calculate_contour_properties(contour)
        if ((min_area <= area <= max_area) and (min_circularity <= circularity <= max_circularity)) or (min_area <= area <= max_area):
            filtered_contours.append(contour)
    return filtered_contours

def draw_contours(image, contours, color = (255, 0, 255), thickness = 2):
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, contours, -1, color, thickness)
    return image_with_contours