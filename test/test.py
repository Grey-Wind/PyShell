from PyShell.Shell import Shell

user_input = input("请输入一个数字：")

number = int(user_input)

if number == 1:
    Shell("ipconfig")
elif number == 2:
    Shell("ipconfig", args=['/flushdns'])
elif number == 3:
    Shell("ipconfig", count=5)
elif number == 4:
    print("read mode had been deleted")
elif number == 5:
    Shell("ipconfig", lib="os-lib")
else:
    print("输入的数字无效")
