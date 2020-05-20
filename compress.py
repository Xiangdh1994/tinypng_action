import tinify
import os

tinify.key = 'n5LFT9F3g2xp54zRRPCZdsdyRPqnQD2Q'

srcDir = "./src"

desDir = "./compressed"

if not os.path.exists(desDir):
    os.makedirs(desDir)

imgs = os.listdir(srcDir)
for img in imgs:
    if ".jpeg" in img or ".jpg" in img or ".png" in img:
        print(img)
        tinify.from_file("%s/%s" % (srcDir, img)).to_file("%s/%s" % (desDir, img))
print("done")
