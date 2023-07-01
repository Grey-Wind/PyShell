import PyShell

shell = PyShell.PyShell("echo 'Hello, World!'", 3)
shell.start()

shell = PyShell.PyShell("ipconfig", 2)
shell.start()

shell = PyShell.PyShell("ping grey-wind.github.io", 1)
shell.start()