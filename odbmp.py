import lvgl as lv # using an lvgl display for rich graphics
import display
import random
import time

display.init()
scr = lv.obj()

speed_label = lv.label(scr)
speed_label.set_text("Vehicle Speed: -- km/h")
speed_label.align(None, lv.ALIGN.CENTER, 0, -30)

rpm_label = lv.label(scr)
rpm_label.set_text("Engine RPM: --")
rpm_label.align(speed_label, lv.ALIGN.OUT_BOTTOM_MID, 0, 20)

def update_data(event):
    speed = random.randint(0, 200)
    rpm = random.randint(0, 8000)
    speed_label.set_text(f"Vehicle Speed: {speed} km/h")
    rpm_label.set_text(f"Engine RPM: {rpm}")

update_button = lv.btn(scr)
update_button.set_size(150, 50)
update_button.align(rpm_label, lv.ALIGN.OUT_BOTTOM_MID, 0, 30)
update_button_label = lv.label(update_button)
update_button_label.set_text("Get OBD Data")
update_button.set_event_cb(update_data)

lv.scr_load(scr)

while True:
    lv.task_handler()
    time.sleep(0.01)
