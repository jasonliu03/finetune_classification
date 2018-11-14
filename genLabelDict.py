import os
cwd = os.getcwd()

classes = "man women".split()
def genLabelDict():
    labelDict = {}
    for index, name in enumerate(classes):
        class_path = cwd +"/"+ name+"/"
        for img_name in sorted(os.listdir(class_path)):
            img_path = class_path + img_name
            labelDict[img_path] = index
    return labelDict
