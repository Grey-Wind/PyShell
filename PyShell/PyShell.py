import subprocess

class PyShell:
    def __init__(self, command, count):
        self.command = command  # 存储命令 / Store the command
        self.count = count  # 存储执行次数 / Store the execution count

    def __call__(self):
        for _ in range(self.count):
            subprocess.run(self.command, shell=False)  # 使用 subprocess 执行命令 / Execute command using subprocess

def Shell(command, count):
    shell = PyShell(command, count)  # 实例化 PyShell / Instantiate PyShell
    shell()  # 调用实例对象，相当于执行命令 / Call the instance object, which is equivalent to executing the command

# 直接调用 Shell 函数执行命令 / Directly call the Shell function to execute the command
Shell("ipconfig", 3)
