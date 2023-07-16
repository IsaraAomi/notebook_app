import cv2

def load_image_file(file_path):
    image = cv2.imread(file_path)
    return image

def save_image_file(file_path, image):
    cv2.imwrite(file_path, image)
