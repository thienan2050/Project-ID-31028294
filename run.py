import os
path = '/home/pi/RPi/Project-ID-31028294'

media = []
temptFile = ''
temptFile = ''
index = 0

for file in os.listdir(path):
    if file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".mpeg") :
        media.append(os.path.join(path, file))

for root, dirs, files in os.walk(path):
    if 'tempt.txt' in files:
        f = open(path + '/tempt.txt')
        try:
            index = int(f.read())
            f.close()
        except:
            index = 0
            
with open(path + "/tempt.txt",'w') as f:
    f.write(str(index)) 
print('Play video '+ str(index))
print("omxplayer -o hdmi " + media[index])
os.system("omxplayer -o hdmi " + media[index])
index = (index + 1) % len(media)
with open(path + "/tempt.txt",'w') as f:
    f.write(str(index))



 
