"""
A Toga Mobile Demo
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.paths import Paths


class TogaMobileDemo(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        self.main_box = toga.Box()
        # Variables
        self.path = Paths().app
        self.x = 0
        # Widgets
        btn1 = toga.Button(text="Clicker", on_press=self.click)
        btnnew = toga.Button(text="New Window", on_press=self.newwindow)
        img = toga.ImageView(
            image=toga.Image(path=f"{self.path}/resources/togamobiledemo.png")
        )

        # add widgets
        self.main_box.add(btn1)
        self.main_box.add(btnnew)
        self.main_box.add(img)
        # config
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def newwindow(self, widget):
        apptitle = toga.App().formal_name
        appauthor = toga.App().author
        appdescription = toga.App().description
        appwebsite = toga.App().home_page
        self.main_window.info_dialog(
            title=apptitle,
            message=f"App: {apptitle}\nAuthor: {appauthor}\nDescribtion: {appdescription}\nWebsite: {appwebsite}",
        )

    def click(self, widget):
        self.text = ""
        del self.text
        self.x += 1
        self.text = f"You pressed this button {self.x} times."
        self.maintext = toga.Label(text=self.text)
        self.main_box.add(self.maintext)

    def abt(widget):
        toga.App.about()


def main():
    return TogaMobileDemo()
