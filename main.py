
import os
import config

# assistant
import Assistant.functions as functions
import Assistant.operations.os.Close as close
import Assistant.operations.os.Open as open
import Assistant.operations.assistant.browse as browse

# sys tray
import SYSTRAY.mainTray as tray


# ui 


if __name__ == '__main__':
    tray.systray.start()