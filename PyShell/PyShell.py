import subprocess

class PyShell:
    def __init__(self, command, count):
        self.command = command
        self.count = count

    def start(self):
        for _ in range(self.count):
            subprocess.run(self.command, shell=True)
