from PIL import Image
import os

k=1
for f in os.listdir():
    if f.endswith(".jpg"):
        file=Image.open(f)
        fn,fe=os.path.splitext(f)
        resiz=file.resize((1000,1000))
        # print(fn)
        resiz.save("resized/{}{}{}".format(fn,"-"+str(k),fe))
        k+=1

