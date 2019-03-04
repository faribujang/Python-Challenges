import os, random, string, sys, urllib.request as urllib

num_pics = 5
if len(sys.argv) > 1:
    num_pics = int(sys.argv[1])

while num_pics > 0:
    name = str.join(random.sample(str.letters+str.digits, 5)) + '.jpg'
    img = urllib.urlopen("http://i.imgur.com/" + name).read()
    if len(img) != 503: # 'image not found' is 503 bytes
        num_pics -= 1
        with open(os.path.join('output', name), "wb") as f:
            f.write(img)
        print("downloaded", name)