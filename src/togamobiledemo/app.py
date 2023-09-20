"""
A Toga Mobile Demo
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class TogaMobileDemo(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        self.main_box = toga.Box()
        self.x = 0
        # btn1 = toga.Button(text="Clicker", on_press=self.click)
        btnnew = toga.Button(text="New Window", on_press= self.newwindow)
        # self.text = toga.Label(text=f"You pressed this button {self.x} times.")
        # self.main_box.add(self.text)
        # self.main_box.add(btn1)
        self.main_box.add(btnnew)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()
    def newwindow(self,widget):
        bx = toga.Box()
        lbl = toga.Label("2 Window")
        bx.add(lbl)
        self.second_window = toga.Window(title="New Window")
        self.second_window.content = bx
        self.second_window.show()

    
    

    def click(self, widget):
        self.x += 1
        self.text = f"You pressed this button {self.x} times."


def main():
    return TogaMobileDemo()
