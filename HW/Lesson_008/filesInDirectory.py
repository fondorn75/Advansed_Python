import os
import json
import csv
import pickle

userPath = 'D:\\TEMP\\Advansed_Python\\HW\\Lesson_008\\'


def fileinDirectories(path) -> dict:
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [fileinDirectories(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
    return d


if __name__ == "__main__":
    print(fileinDirectories(userPath))
    with open('new_dir.json', 'w') as f:
        json.dump(fileinDirectories(userPath), f)

    temp = fileinDirectories(userPath)
    csvColumns = ['name', 'type', 'children']
    with open("dir.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csvColumns)
        writer.writeheader()
        for data in temp:
            writer.writerow(data)

    with open('myDir.pickle', 'wb') as f:
        pickle.dump(temp, f)

