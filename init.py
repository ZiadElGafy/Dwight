import subprocess

commands = [
    "pip install -r requirements.txt",
    "python chatbot/train.py",
    "python main.py"
]

for command in commands:
    subprocess.call(command)