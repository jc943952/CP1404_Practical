"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder


from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934  # Correct constant name

class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculate(self):
        """Update the output label based on the input miles"""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(round(result, 3))  # rounded nicely

    def handle_increment(self, change):
        """Handle Up/Down buttons"""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Return float value of input or 0.0 if invalid"""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0

MilesConverterApp().run()