import psutil
def close_app(app_name):
    running_apps=psutil.process_iter(['pid','name']) #returns names of running processes
    found=False
    for app in running_apps:
        sys_app=app.info.get('name').split('.')[0].lower()

        if sys_app in app_name.split() or app_name in sys_app:
            pid=app.info.get('pid') #returns PID of the given app if found running
            
            try: #deleting the app if asked app is running.(It raises error for some windows apps)
                app_pid = psutil.Process(pid)
                app_pid.terminate()
                found=True
            except: pass
            
        else: pass
    if not found:
        return("application not found")
    else:
        return(app_name + "closed")

close_app("Notepad")