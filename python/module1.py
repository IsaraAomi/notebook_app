from .libmain.Image.process import *
from .libmain.IO.file import *

def module1(input_path="dummy_input_path", 
            output_path="dummy_output_path", 
            option="dummy_option"):
    input_image = load_image_file(input_path)
    output_image = rotate(input_image, option)
    save_image_file(output_path, output_image)

def main():
    module1()

if __name__ == '__main__':
    main()
