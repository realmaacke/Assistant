from AppOpener import open

def open_app(app_name):
    try:
        open(app_name, match_closest=True)
        return(app_name + "opened")
    
    except Exception as e:
        return("app not found")