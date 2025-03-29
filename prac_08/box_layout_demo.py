from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Demo app showcasing BoxLayout functionality"""

    def build(self):
        """Build and return the root widget from KV file"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Update label with greeting using input text"""
        # print('test')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear both input and output fields"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
