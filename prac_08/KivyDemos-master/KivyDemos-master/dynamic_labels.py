from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        self.title = "Dynamic Labels Demo"
        root = Builder.load_file("dynamic_labels.kv")

        for name in self.names:
            lbl = Label(
                text=name,
                font_size=32,
                size_hint_y=None,
                height=50
            )
            root.ids.main.add_widget(lbl)

        return root


if __name__ == "__main__":
    DynamicLabelsApp().run()