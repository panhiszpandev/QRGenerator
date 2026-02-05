from PIL import Image
import glob

fileDirs = glob.glob("./*.png")
fileNames = []
images = []

for fileDir in fileDirs:
    print('\n'+fileDir)
    fileNames.append(fileDir.replace('./',''))

for fileName in fileNames:
    images.append(Image.open(fileName))

bigImage = Image.new('RGB', (800, 1200))

i = 0
j = 0
for singleImage in images:
    print(i)
    print(j)
    if i > 3:
        i = 0
        j = j + 1
    bigImage.paste(singleImage, (200*i, 200*j))
    i = i + 1

bigImage.save('bigImage.png')



