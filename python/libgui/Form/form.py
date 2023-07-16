import os, datetime, subprocess
import ipywidgets as widgets
from IPython.display import display, clear_output, HTML

from python.module1 import *
from python.libmain.Image.process import *
from python.libmain.IO.file import *
from python.libgui.Form.common import *

class FormModule1:
    def __init__(self) -> None:
        self.__module_name = "Module1"
        self.__form = None
        self.__input_path = None
        self.__output_path = None
        self.__option = None

    @property
    def module_name(self):
        return self.__module_name
    
    def __set_input_info(self, output_widget, input_path, output_path, option):
        self.__input_path = input_path
        self.__output_path = output_path
        self.__option = option
        with output_widget:
            clear_output(wait=True)
            print(f"[{self.module_name}] Input Path: {self.__input_path}")
            print(f"[{self.module_name}] Output Path: {self.__output_path}")
            print(f"[{self.module_name}] Option: {self.__option}")

    def __run(self, output_widget):
        module1(self.__input_path, self.__output_path, self.__option)
        with output_widget:
            clear_output(wait=True)
            print(f"[{self.module_name}] Complete Run: Option={self.__option}: {datetime.datetime.now()}")
    
    def create_form(self, input_path, output_path):
        # create dropdown menu
        dropdown = widgets.Dropdown(
            options=["right", "left"],
            value="right",
            description="Option:",
        )
        dropdown.layout.width = "200px"

        # create output area
        output_widget1 = widgets.Output()
        output_widget2 = widgets.Output()
        output_widget3 = widgets.Output()

        # create button1
        button1 = widgets.Button(description=f"Set Input Info")
        button1.on_click(lambda _: self.__set_input_info(output_widget1, input_path, output_path, dropdown.value))

        # create button2
        button2 = widgets.Button(description=f"Run")
        button2.on_click(lambda _: self.__run(output_widget2))

        # create button3
        button3 = widgets.Button(description=f"Show Result")
        button3.on_click(lambda _: show_result(output_widget3, self.__module_name, self.__output_path))

        form_items = [
            dropdown,
            button1,
            button2,
            button3,
            output_widget1,
            output_widget2,
            output_widget3,
        ]
        self.__form = widgets.VBox(form_items, layout=widgets.Layout(width="800px"))

        display(self.__form)

class FormModule2:
    def __init__(self) -> None:
        self.__module_name = "Module2"
        self.__form = None
        self.__input_path = None
        self.__output_path = None
        self.__brihtness = None
        this_file_dir = os.path.dirname(os.path.abspath(__file__))
        self.__cpp_dir = os.path.join(this_file_dir, "..", "..", "..", "cpp")

    @property
    def module_name(self):
        return self.__module_name
    
    def __set_input_info(self, output_widget, input_path, output_path, brihtness):
        self.__input_path = input_path
        self.__output_path = output_path
        self.__brihtness = brihtness
        with output_widget:
            clear_output(wait=True)
            print(f"[{self.module_name}] Input Path: {self.__input_path}")
            print(f"[{self.module_name}] Output Path: {self.__output_path}")
            print(f"[{self.module_name}] Brightness: {self.__brihtness}")

    def __build(self, output_widget):
        self.__clean()
        current_dir = os.getcwd()
        try:
            os.chdir(self.__cpp_dir)
            os.mkdir("build")
            os.chdir("build")
            subprocess.run(["cmake", ".."], check=True)
            subprocess.run(["make"], check=True)
            os.chdir("..")
        finally:
            os.chdir(current_dir)
        with output_widget:
            clear_output(wait=True)
            print(f"[{self.__module_name}] Complete Build: {datetime.datetime.now()}")

    def __run(self, output_widget, input_path, output_path, brightness):
        current_dir = os.getcwd()
        try:
            os.chdir(self.__cpp_dir)
            os.chdir("build")
            subprocess.run(["./main", input_path, output_path, str(brightness)], check=True)
            os.chdir("..")
        finally:
            os.chdir(current_dir)
        with output_widget:
            clear_output(wait=True)
            print(f"[{self.__module_name}] Complete Run: Brightness={brightness}: {datetime.datetime.now()}")

    def __clean(self):
        current_dir = os.getcwd()
        try:
            os.chdir(self.__cpp_dir)
            subprocess.run(["rm", "-rf", "build"], check=True)
        finally:
            os.chdir(current_dir)
    
    def create_form(self, input_path, output_path):
        # create slider
        slider = widgets.IntSlider(min=0, max=255, step=1, description='Brightness')

        # create output area
        output_widget1 = widgets.Output()
        output_widget2 = widgets.Output()
        output_widget3 = widgets.Output()
        output_widget4 = widgets.Output()

        # create button1
        button1 = widgets.Button(description=f"Set Input Info")
        button1.on_click(lambda _: self.__set_input_info(output_widget1, input_path, output_path, slider.value))

        # create button2
        button2 = widgets.Button(description="Build")
        button2.on_click(lambda _: self.__build(output_widget2))

        # create button3
        button3 = widgets.Button(description="Run")
        button3.on_click(lambda _: self.__run(output_widget3, self.__input_path, self.__output_path, self.__brihtness))

        # create button4
        button4 = widgets.Button(description="Show Result")
        button4.on_click(lambda _: show_result(output_widget4, self.__module_name, self.__output_path))

        # create button5
        button5 = widgets.Button(description="Clean")
        button5.on_click(lambda _: self.__clean())

        form_items = [
            slider,
            button1,
            button2,
            button3,
            button4,
            button5,
            output_widget1,
            output_widget2,
            output_widget3,
            output_widget4
        ]
        self.__form = widgets.VBox(form_items, layout=widgets.Layout(width="800px"))

        display(self.__form)
        