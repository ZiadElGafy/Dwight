import os

def fix(path):
    fixed_path = ""
    for i in path:
        if i == '\\':
            fixed_path += '/'
        else:
            fixed_path += i
    
    fixed_path += " %s"
    
    return fixed_path

def driver():
    possible_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]

    for path in possible_paths:
        if os.path.exists(path):
            return fix(path)
        