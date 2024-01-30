from tools.applicationLauncher import *

def driver(prompt):
    operation, app_name = prompt.split(' ', 1)
    if operation == 'open' or operation == 'launch' or operation == 'start' or operation == 'run' or operation == 'execute':
        open_app(app_name)
    elif operation == 'close' or operation == 'quit' or operation == 'exit' or operation == 'stop' or operation == 'end' or operation == 'terminate':
        close_app(app_name)