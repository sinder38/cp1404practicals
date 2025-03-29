"""
CP1404/CP5632 Practical
Program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_RATE = 1.60934


class MilesConverterApp(App):
    """App to convert miles to kilometres"""
    output = StringProperty()
    def build(self):
        """Build and return the root widget from KV file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        print("Handle calculate")
        miles = float(text)
        self.output = str(miles * MILES_TO_KM_RATE)

    def handle_increment(self, text, change):
        print("Handle increment")
        miles = float(text) + change
        self.root.ids.input_miles.text = str(miles)



MilesConverterApp().run()
