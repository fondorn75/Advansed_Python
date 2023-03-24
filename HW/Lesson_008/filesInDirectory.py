import os

userPath = 'D:\\TEMP\\Advansed_Python\\HW\Lesson_007\\'


def fileinDirectories(path, level=1):
    print('Level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('Спускаемся', path + '\\' + i)
            fileinDirectories(path + '\\' + i, level + 1)
            print('Возвращаемся в', path)


if __name__ == "__main__":
    fileinDirectories(userPath)
