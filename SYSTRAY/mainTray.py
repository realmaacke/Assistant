from infi.systray import SysTrayIcon

import UI.window as ui
import config


def settings(systray):
    pass

def shutdown(systray):
    config.VOICE_ACTIVATED = False

def open(systray):
    window = ui.App()


def app():
    app = ui.App()
    app.mainloop()


menu_options = (("open", None, open),
                ("Settings", None, settings))

systray = SysTrayIcon("icon.ico", "Assistant", menu_options, on_quit=shutdown, default_menu_index=1)