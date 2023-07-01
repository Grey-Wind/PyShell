import os
import subprocess

class PyShell:
    def __init__(self, command, count):
        self.command = command
        self.count = count

    def start(self):
        for _ in range(self.count):
            pid = os.fork()
            if pid == 0:
                subprocess.call(self.command, shell=True)
                os._exit(0)
