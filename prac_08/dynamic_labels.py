"""
CP1404/CP5632 Practical
Dynamic Labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelApp(App):
    """Main program - Kivy app to dynamically display labels"""

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ["name1", "name2", "name3", "name4"]

    def build(self):
        """Build and return the root widget from KV file"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data in the GUI"""
        for name in self.names:
            self.root.ids.main.add_widget(Label(text=name))


DynamicLabelApp().run()
