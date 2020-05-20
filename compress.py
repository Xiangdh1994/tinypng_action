import tinify
import os
import sys

tinify.key = 'n5LFT9F3g2xp54zRRPCZdsdyRPqnQD2Q'

def resize(w, h):
    srcDir = "./src"
    desDir = "./compress"

    if not os.path.exists(desDir):
        os.makedirs(desDir)

    imgs = os.listdir(srcDir)
    for img in imgs:
        if ".jpeg" in img or ".jpg" in img or ".png" in img:
            print(img)
            source = tinify.from_file("%s/%s" % (srcDir, img))
            if w > 0 and h > 0:
                print("compress to: %d %d" % (w, h))
                resized = source.resize(
                    method="fit",
                    width=w,
                    height=h
                )
                pass
                #resized.to_file("%s/%s" % (desDir, img))
            else:
                pass
                #source.to_file("%s/%s" % (desDir, img))
    print("done")

if __name__ == "__main__":
    paramsCount = len(sys.argv)
    c = ""
    w = 0
    h = 0
    if paramsCount > 1:
        c = sys.argv[1]
    if c == "compress":
        if paramsCount > 3:
            if sys.argv[2].isdigit():
                w = int(sys.argv[2])
            if sys.argv[3].isdigit():
                h = int(sys.argv[3])
        resize(w, h)

