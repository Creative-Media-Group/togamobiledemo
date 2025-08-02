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
        btn1 = toga.Button(
            text="Clicker",
            on_press=self.click,
            style=Pack(margin=10, flex=1),
        )
        btnnew = toga.Button(
            text="New Window",
            on_press=self.newwindow,
            style=Pack(margin=10, flex=1),
        )
        img = toga.ImageView(
            image=toga.Image(src=f"{self.path}/resources/togamobiledemo.png")
        )
        self.text = f"You pressed this button {self.x} times."
        self.maintext = toga.Label(
            text=self.text,
            style=Pack(margin=10, flex=1),
        )
        # add widgets
        self.main_box.add(btn1)
        self.main_box.add(btnnew)
        self.main_box.add(img)
        self.main_box.add(self.maintext)
        # config
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    async def newwindow(self, widget):
        apptitle = toga.App().formal_name
        appauthor = toga.App().author
        appdescription = toga.App().description
        appwebsite = toga.App().home_page
        await self.main_window.dialog(
            toga.InfoDialog(
                title=apptitle,
                message=f"App: {apptitle}\nAuthor: {appauthor}\nDescribtion: {appdescription}\nWebsite: {appwebsite}",
            )
        )

    def click(self, widget):
        self.x += 1
        self.maintext.text = f"You pressed this button {self.x} times."

    def abt(widget):
        toga.App.about()


def main():
    return TogaMobileDemo()
