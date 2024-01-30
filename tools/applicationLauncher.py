from AppOpener import open, close

def open_app(app_name):
    open(app_name, match_closest = True)

def close_app(app_name):
    close(app_name, match_closest = True)