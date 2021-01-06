from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKm(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        value = self.get_valid_miles()
        conversion = value * MILES_TO_KM
        self.root.ids.output_label.text = str(conversion)

    def handle_increment(self, change):
        value = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(value)

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0


ConvertMilesKm().run()
