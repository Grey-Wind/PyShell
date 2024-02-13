import subprocess
import os

class PyShell:
    def __init__(self, command, count):
        self.command = command
        self.count = count

    def __call__(self):
        for _ in range(self.count):
            if self.lib == "subprocess-lib":
                subprocess.run(self.command, shell=False)
            elif self.lib == "os-lib":
                os.system(self.command)

def Shell(command, args=None, count=1, lib="subprocess-lib"):
    """启动Shell

    参数:
        command (_type_): 要执行的命令
        args (_type_, optional): 参数，可选项，默认为NONE
        count (int, optional): 执行次数，可选项，默认为1
        read (bool, optional): 是否读取输出，仅在lib="subprocess-lib"时可用
        lib (str, optional): 选择使用的lib，可为subprocess-lib或os-lib，默认为subprocess-lib
    """
    if args:
        command = f"{command} {' '.join(args)}"
    
    shell = PyShell(command, count)
    shell.lib = lib

    shell()
