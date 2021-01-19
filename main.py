from kivy.config import Config
Config.set('graphics', 'resizable', True)
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.button import MDRaisedButton
#from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.toast import toast
import time
import webbrowser
from plyer import flash
from android.permissions import request_permissions, Permission, check_permission

flash_status = 0
theme_mode = 0


class Tab(MDTabsBase, FloatLayout):
    pass


class Disco(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.screen_manager = ScreenManager()
        self.base_screen_1 = Screen(name="main")
        self.screen = BoxLayout(orientation='vertical')
        self.menu = DropDown(auto_width=False, width=190)
        btn_1_for_menu = Button(text="Theme",
                                color=[0, 0.5, 5, 1],
                                background_color=[255, 2.2, 0, 1],
                                size_hint=(None, None),
                                height=150,
                                width=180,
                                on_press=self.pressed_modes)
        btn_2_for_menu = Button(text="About",
                                color=[0, 0.5, 5, 1],
                                background_color=[255, 2.2, 0, 1],
                                size_hint=(None, None),
                                height=150,
                                width=180,
                                on_press=self.pressed_about_us)
        btn_3_for_menu = Button(text="Exit",
                                color=[0, 0.5, 5, 1],
                                background_color=[255, 2.2, 0, 1],
                                size_hint=(None, None),
                                height=150,
                                width=180,
                                on_press=self.pressed_exit)
        self.menu.add_widget(btn_1_for_menu)
        self.menu.add_widget(btn_2_for_menu)
        self.menu.add_widget(btn_3_for_menu)
        self.bar = MDToolbar(title="DISCO", pos_hint={'top': 1})
        self.bar.specific_text_color = self.theme_cls.accent_color
        self.bar.right_action_items = [
            ["dots-vertical", lambda x: self.menu.open(x)]]
        self.screen.add_widget(self.bar)
        # self.menu = MDDropdownMenu(width_mult=3)
        #self.menu.items.append({"viewclass": "MDMenuItem", "text": "Dark/Light mode", "callback": self.pressed_modes})
        #self.menu.items.append({"viewclass": "MDMenuItem", "text": "About us", "callback": self.pressed_about_us})

        self.btn_to_turn_flash_on_off = MDIconButton(icon="flash_off.png", pos_hint={
                                                     'center_x': 0.5, 'center_y': 0.5}, on_press=self.action_flash)
        self.btn_to_turn_flash_on_off.height = 235
        self.btn_to_turn_flash_on_off.width = 180

        self.for_second_page = self.second_page(self)

        self.for_third_page = self.third_page(self)

        self.tab_1 = Tab(text="Bulb")
        self.tab_2 = Tab(text="Disco")
        self.tab_3 = Tab(text="Rainbow")
        self.tabs = MDTabs()
        self.tabs.text_color_normal = self.theme_cls.accent_color
        self.tab_1.add_widget(self.btn_to_turn_flash_on_off)
        self.tab_2.add_widget(self.for_second_page)
        self.tab_3.add_widget(self.for_third_page)
        self.tabs.add_widget(self.tab_1)
        self.tabs.add_widget(self.tab_2)
        self.tabs.add_widget(self.tab_3)
        self.screen.add_widget(self.tabs)
        self.base_screen_1.add_widget(self.screen)
        self.screen_manager.add_widget(self.base_screen_1)

        self.base_screen_2_red = Screen(name="red")
        self.base_screen_2_brown = Screen(name="brown")
        self.base_screen_2_yellow = Screen(name="yellow")
        self.base_screen_2_green = Screen(name="green")
        self.base_screen_2_aqua = Screen(name="aqua")
        self.base_screen_2_blue = Screen(name="blue")
        self.base_screen_2_violet = Screen(name="violet")
        self.show_btn_red = Button(background_color=(
            255, 0, 0, 1), on_press=self.quit_secondary_screen)
        self.show_btn_brown = Button(background_color=(
            255, 2.2, 0, 10), on_press=self.quit_secondary_screen)
        self.show_btn_yellow = Button(background_color=(
            255, 255, 0, 1), on_press=self.quit_secondary_screen)
        self.show_btn_green = Button(background_color=(
            0, 255, 0, 1), on_press=self.quit_secondary_screen)
        self.show_btn_aqua = Button(background_color=(
            0, 255, 255, 1), on_press=self.quit_secondary_screen)
        self.show_btn_blue = Button(background_color=(
            0, 0, 255, 1), on_press=self.quit_secondary_screen)
        self.show_btn_violet = Button(background_color=(
            255, 0, 64, 1), on_press=self.quit_secondary_screen)
        self.base_screen_2_red.add_widget(self.show_btn_red)
        self.base_screen_2_brown.add_widget(self.show_btn_brown)
        self.base_screen_2_yellow.add_widget(self.show_btn_yellow)
        self.base_screen_2_green.add_widget(self.show_btn_green)
        self.base_screen_2_aqua.add_widget(self.show_btn_aqua)
        self.base_screen_2_blue.add_widget(self.show_btn_blue)
        self.base_screen_2_violet.add_widget(self.show_btn_violet)
        self.screen_manager.add_widget(self.base_screen_2_red)
        self.screen_manager.add_widget(self.base_screen_2_brown)
        self.screen_manager.add_widget(self.base_screen_2_yellow)
        self.screen_manager.add_widget(self.base_screen_2_green)
        self.screen_manager.add_widget(self.base_screen_2_aqua)
        self.screen_manager.add_widget(self.base_screen_2_blue)
        self.screen_manager.add_widget(self.base_screen_2_violet)

        return self.screen_manager

    def action_flash(self, obj):
        global flash_status
        if check_permission('android.permission.CAMERA'):
            self.tab_1.remove_widget(self.btn_to_turn_flash_on_off)
            if flash_status == 0:
                self.btn_to_turn_flash_on_off = MDIconButton(icon="flash_on.png", pos_hint={
                                                             'center_x': 0.5, 'center_y': 0.5}, on_press=self.action_flash)
                self.tab_1.add_widget(self.btn_to_turn_flash_on_off)
                flash_status = 1
                self.btn_to_turn_flash_on_off.height = 220
                self.btn_to_turn_flash_on_off.width = 220
                flash.on()
            else:
                self.btn_to_turn_flash_on_off = MDIconButton(icon="flash_off.png", pos_hint={
                                                             'center_x': 0.5, 'center_y': 0.5}, on_press=self.action_flash)
                self.tab_1.add_widget(self.btn_to_turn_flash_on_off)
                flash_status = 0
                self.btn_to_turn_flash_on_off.height = 235
                self.btn_to_turn_flash_on_off.width = 180
                flash.off()
                flash.release()
        else:
            request_permissions([Permission.CAMERA])
            pass

    def pressed_about_us(self, obj):
        self.dialog = MDDialog(title="About app", text="DISCO app is a flash light accessing app with multiple features.\n"
                               "Created by AKASH A.\n"
                               "Follow the developer on\n", size_hint=(0.8, 0.7), radius=[5, 30, 5, 30],
                               buttons=[
                                   MDIconButton(icon='instagram', on_press=self.instagram), MDIconButton(
                                       icon='github-circle', on_press=self.github),
                                   MDIconButton(icon='linkedin', on_press=self.linkedin), MDIconButton(
                                       icon='youtube', on_press=self.youtube),
                                   MDRaisedButton(
                                       text="Mmm", on_press=self.dialog_close)
                               ]
                               )
        self.dialog.open()

    def instagram(self, obj):
        webbrowser.open('https://www.instagram.com/akash.a.2020')

    def linkedin(self, obj):
        webbrowser.open('https://www.linkedin.com/in/akash-a-37334217a')

    def github(self, obj):
        webbrowser.open('https://github.com/Akash-Peace')

    def youtube(self, obj):
        webbrowser.open(
            'https://www.youtube.com/channel/UCSIuPNPq55-7_OoQelMXkfw')

    def dialog_close(self, obj):
        self.dialog.dismiss()

    def pressed_modes(self, obj):
        global theme_mode
        if theme_mode == 0:
            theme_mode = 1
            self.theme_cls.theme_style = "Dark"
        else:
            theme_mode = 0
            self.theme_cls.theme_style = "Light"

    def pressed_exit(self, obj):
        self.get_running_app().stop()

    def second_page(self, obj):

        self.second_pd_screen = Screen()
        self.text_field_1_for_timegap_to_blink = MDTextField(pos_hint={'center_x': 0.33, 'center_y': 0.85},
                                                             size_hint=(None, None), width=300)
        self.text_field_1_for_timegap_to_blink.hint_text = 'Time gap'
        self.text_field_1_for_timegap_to_blink.helper_text = 'Mention the time gap (in seconds) to blink flash. Eg: 1'
        self.text_field_1_for_timegap_to_blink.helper_text_mode = 'persistent'
        self.text_field_2_for_timegap_to_hold_blink = MDTextField(pos_hint={'center_x': 0.33, 'center_y': 0.65},
                                                                  size_hint=(None, None), width=300)
        self.text_field_2_for_timegap_to_hold_blink.hint_text = 'Hold flash'
        self.text_field_2_for_timegap_to_hold_blink.helper_text = 'Mention the time gap (in seconds) to hold flash. Eg: 1'
        self.text_field_2_for_timegap_to_hold_blink.helper_text_mode = 'persistent'
        self.text_field_3_for_count_of_blink = MDTextField(pos_hint={'center_x': 0.42, 'center_y': 0.45},
                                                           size_hint=(None, None), width=300)
        self.text_field_3_for_count_of_blink.hint_text = 'Blink count'
        self.text_field_3_for_count_of_blink.helper_text = 'Mention the count of flash blink. Eg: 2'
        self.text_field_3_for_count_of_blink.helper_text_mode = 'persistent'
        self.second_pd_screen.add_widget(
            self.text_field_1_for_timegap_to_blink)
        self.second_pd_screen.add_widget(
            self.text_field_2_for_timegap_to_hold_blink)
        self.second_pd_screen.add_widget(self.text_field_3_for_count_of_blink)
        self.btn_to_activate_disco_mode = MDRaisedButton(text="Party", pos_hint={'center_x': 0.5, 'center_y': 0.15},
                                                         size_hint=(None, None), width=300, on_press=self.party_starts)
        self.btn_to_activate_disco_mode.text_color = self.theme_cls.accent_color
        self.alert_btn = MDIconButton(icon='alert', pos_hint={
                                      "center_x": 0.5, "center_y": 0.3}, on_press=self.alert_dialog)
        self.alert_btn.md_bg_color = [1, 0, 0, 1]
        self.alert_btn.user_font_size = "20sp"
        self.second_pd_screen.add_widget(self.alert_btn)
        self.second_pd_screen.add_widget(self.btn_to_activate_disco_mode)
        return self.second_pd_screen

    def alert_dialog(self, obj):
        self.dialog = MDDialog(title="CAUTION",
                               text="Hi, you want to be sure about your count and time gap of flash blink "
                                    "because this app will be freeze until the count ends. "
                                    "In case, if you want to quit this flash blink while "
                                    "it is in active then just restart the app.", size_hint=(0.8, 0.7), radius=[5, 30, 5, 30],
                               buttons=[MDRaisedButton(text="Oh", on_press=self.dialog_close)])
        self.dialog.open()

    def party_starts(self, obj):
        if check_permission('android.permission.CAMERA'):
            timegap = self.text_field_1_for_timegap_to_blink.text
            holdflash = self.text_field_2_for_timegap_to_hold_blink.text
            blinkcount = self.text_field_3_for_count_of_blink.text
            try:
                timegap = float(timegap)
                holdflash = float(holdflash)
                blinkcount = int(blinkcount)
                for i in range(blinkcount):
                    flash.on()
                    time.sleep(holdflash)
                    flash.off()
                    flash.release()
                    time.sleep(timegap)
            except:
                if timegap and holdflash and blinkcount:
                    toast("Only Numbers Allowed")
                else:
                    toast("Don't Leave Blank Space")
        else:
            request_permissions([Permission.CAMERA])
            pass

    def third_page(self, obj):

        self.color_list_screen = BoxLayout()
        # in rgba that a is opacity which is want to be more than 0
        self.btn_red = Button(background_color=(
            255, 0, 0, 1), on_press=self.red)
        self.btn_brown = Button(background_color=(
            255, 2.2, 0, 10), on_press=self.brown)
        self.btn_yellow = Button(background_color=(
            255, 255, 0, 1), on_press=self.yellow)
        self.btn_green = Button(background_color=(
            0, 255, 0, 1), on_press=self.green)
        self.btn_aqua = Button(background_color=(
            0, 255, 255, 1), on_press=self.aqua)
        self.btn_blue = Button(background_color=(
            0, 0, 255, 1), on_press=self.blue)
        self.btn_violet = Button(background_color=(
            255, 0, 64, 1), on_press=self.violet)
        self.color_list_screen.add_widget(self.btn_red)
        self.color_list_screen.add_widget(self.btn_brown)
        self.color_list_screen.add_widget(self.btn_yellow)
        self.color_list_screen.add_widget(self.btn_green)
        self.color_list_screen.add_widget(self.btn_aqua)
        self.color_list_screen.add_widget(self.btn_blue)
        self.color_list_screen.add_widget(self.btn_violet)

        return self.color_list_screen

    def red(self, obj):
        toast("RED - Click anywhere to exit")
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.transition.duration = 1
        self.screen_manager.current = 'red'

    def brown(self, obj):
        toast("ORANGE - Click anywhere to exit")
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.transition.duration = 1
        self.screen_manager.current = 'brown'

    def yellow(self, obj):
        toast("YELLOW - Click anywhere to exit")
        self.screen_manager.transition.direction = 'up'
        self.screen_manager.transition.duration = 1
        self.screen_manager.current = 'yellow'

    def green(self, obj):
        toast("GREEN - Click anywhere to exit")
        self.screen_manager.transition.direction = 'down'
        self.screen_manager.transition.duration = 1
        self.screen_manager.current = 'green'

    def aqua(self, obj):
        toast("AQUA - Click anywhere to exit")
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.transition.duration = 1
        self.screen_manager.current = 'aqua'

    def blue(self, obj):
        toast("BLUE - Click anywhere to exit")
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.transition.duration = 1
        self.screen_manager.current = 'blue'

    def violet(self, obj):
        toast("VIOLET - Click anywhere to exit")
        self.screen_manager.transition.direction = 'up'
        self.screen_manager.transition.duration = 1
        self.screen_manager.current = 'violet'

    def quit_secondary_screen(self, obj):
        self.screen_manager.current = 'main'


if __name__ == "__main__":
    Disco().run()
