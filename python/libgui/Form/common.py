import os, cv2
from IPython.display import display, Image, clear_output

def show_result(output_widget, module_name, file_path):
    _, ext = os.path.splitext(file_path)
    img = cv2.imread(file_path)
    _, buf = cv2.imencode(ext, img)
    with output_widget:
        clear_output(wait=True)
        print(f"[{module_name}] {file_path}")
        display(Image(data=buf.tobytes(), width=400))
