"""
CP1404/CP5632 Practical
Program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder


class MilesConverterApp(App):
    """App to convert miles to kilometres"""

    def build(self):
        """Build and return the root widget from KV file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


MilesConverterApp().run()
