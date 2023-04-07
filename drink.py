import time

class Py3status:
    water_reminder = False
    last_reminder_time = 0
    
    def water_timer(self):
        current_time = time.time()
        if not self.water_reminder and (time.localtime().tm_min % 30 == 0) an>
            self.water_reminder = True
            self.last_reminder_time = current_time
        elif self.water_reminder and current_time - self.last_reminder_time >>
            self.water_reminder = False
        if self.water_reminder:
            return {
                'full_text': 'Thirsty?  Drink water    ',
                'color': '#00FF00'
            }
        else:
            return {
                'full_text': '  ',
                'color': '#FFFFFF'
            }

    def on_click(self, event):
        if event['button'] == 1:
            self.last_reminder_time = time.time() - 1800
            self.water_reminder = False
