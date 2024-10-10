from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRectangleFlatButton
import random

KV = '''
MDBoxLayout:
    orientation: 'vertical'
    padding: dp(20)
    spacing: dp(20)
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1  # Black background
        Rectangle:
            pos: self.pos
            size: self.size

    MDLabel:
        text: "OBD Data Dashboard"
        halign: "center"
        font_style: "H4"
        color: 0, 1, 0, 1  # Green color

    MDGridLayout:
        cols: 3
        adaptive_height: True
        spacing: dp(10)
        padding: dp(10)

        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            size: dp(150), dp(200)
            padding: dp(10)
            elevation: 8

            MDLabel:
                text: "Vehicle Speed"
                font_style: "H6"
                halign: "center"
                color: 0, 1, 0, 1  # Green color

            MDLabel:
                id: speed_label
                text: "-- km/h"
                halign: "center"
                font_style: "H4"
                color: 0, 1, 0, 1  # Green color

        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            size: dp(150), dp(200)
            padding: dp(10)
            elevation: 8

            MDLabel:
                text: "Engine RPM"
                font_style: "H6"
                halign: "center"
                color: 0, 1, 0, 1  # Green color

            MDLabel:
                id: rpm_label
                text: "-- RPM"
                halign: "center"
                font_style: "H4"
                color: 0, 1, 0, 1  # Green color

        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            size: dp(150), dp(200)
            padding: dp(10)
            elevation: 8

            MDLabel:
                text: "Fuel Level"
                font_style: "H6"
                halign: "center"
                color: 0, 1, 0, 1  # Green color

            MDLabel:
                id: fuel_label
                text: "-- %"
                halign: "center"
                font_style: "H4"
                color: 0, 1, 0, 1  # Green color

        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            size: dp(150), dp(200)
            padding: dp(10)
            elevation: 8

            MDLabel:
                text: "Engine Temp"
                font_style: "H6"
                halign: "center"
                color: 0, 1, 0, 1  # Green color

            MDLabel:
                id: temp_label
                text: "-- °C"
                halign: "center"
                font_style: "H4"
                color: 0, 1, 0, 1  # Green color

        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            size: dp(150), dp(200)
            padding: dp(10)
            elevation: 8

            MDLabel:
                text: "Throttle Position"
                font_style: "H6"
                halign: "center"
                color: 0, 1, 0, 1  # Green color

            MDLabel:
                id: throttle_label
                text: "-- %"
                halign: "center"
                font_style: "H4"
                color: 0, 1, 0, 1  # Green color

        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            size: dp(150), dp(200)
            padding: dp(10)
            elevation: 8

            MDLabel:
                text: "Battery Voltage"
                font_style: "H6"
                halign: "center"
                color: 0, 1, 0, 1  # Green color

            MDLabel:
                id: battery_label
                text: "-- V"
                halign: "center"
                font_style: "H4"
                color: 0, 1, 0, 1  # Green color

    MDRectangleFlatButton:
        text: "Refresh Data"
        pos_hint: {"center_x": 0.5}
        on_release: app.refresh_data()
'''

class OBBDashboardApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def refresh_data(self):
        speed = random.randint(0, 200)
        rpm = random.randint(0, 8000)
        fuel = random.randint(0, 100)
        temp = random.randint(60, 120)
        throttle = random.randint(0, 100)
        battery_voltage = round(random.uniform(11.5, 14.5), 2)

        self.root.ids.speed_label.text = f"{speed} km/h"
        self.root.ids.rpm_label.text = f"{rpm} RPM"
        self.root.ids.fuel_label.text = f"{fuel} %"
        self.root.ids.temp_label.text = f"{temp} °C"
        self.root.ids.throttle_label.text = f"{throttle} %"
        self.root.ids.battery_label.text = f"{battery_voltage} V"

if __name__ == "__main__":
    OBBDashboardApp().run()
