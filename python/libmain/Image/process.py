import cv2

def rotate(input_image, option="right"):
    if (option.lower() == "right"):
        rotated_image = cv2.rotate(input_image, cv2.ROTATE_90_CLOCKWISE)
    else:
        rotated_image = cv2.rotate(input_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return rotated_image
