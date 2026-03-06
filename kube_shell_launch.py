import subprocess, sys, os

python = sys.executable
script = os.path.join(os.path.dirname(__file__), "kub_shell.py")

subprocess.Popen(
    ["powershell", "-NoExit", "-Command", f"{python} '{script}' --shell"],
    creationflags=subprocess.CREATE_NEW_CONSOLE
)
