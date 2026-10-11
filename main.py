from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from datetime import datetime
import calendar

class ClockApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.time_label = Label(
            text='0:00:00',
            font_size='48sp',
            color=(1, 1, 1, 1),
            size_hint_y=0.4
        )
        self.layout.add_widget(self.time_label)

        self.date_label = Label(
            text='',
            font_size='14sp',
            color=(0.6, 0.6, 0.6, 1),
            size_hint_y=0.2
        )
        self.layout.add_widget(self.date_label)

        self.cal_label = Label(
            text='',
            font_size='14sp',
            color=(1, 1, 1, 1),
            size_hint_y=0.4,
            halign='center',
            valign='middle'
        )
        self.layout.add_widget(self.cal_label)

        Clock.schedule_interval(self.update_time, 1)
        self.update_time(0)
        return self.layout

    def update_time(self, dt):
        now = datetime.now()
        self.time_label.text = now.strftime('%H:%M:%S')
        months = ['января','февраля','марта','апреля','мая','июня',
                  'июля','августа','сентября','октября','ноября','декабря']
        self.date_label.text = f"{now.day} {months[now.month-1]} {now.year} г."

        cal = calendar.monthcalendar(now.year, now.month)
        month_names = ['Январь','Февраль','Март','Апрель','Май','Июнь',
                       'Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
        text = f"{month_names[now.month-1]} {now.year}\n\n"
        text += "Пн Вт Ср Чт Пт Сб Вс\n"
        for week in cal:
            text += "  ".join(f"{d:2d}" if d != 0 else "  " for d in week) + "\n"
        self.cal_label.text = text

if __name__ == '__main__':
    ClockApp().run()
