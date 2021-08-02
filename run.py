import os
media = []
temptFile = ''
temptFile = ''
for t in os.listdir(os.getcwd()):
    if t.endswith(".txt"):
        temptFile = os.path.join(os.getcwd(), t)
        with open(temptFile, 'r') as r:
            index = int(r.read())
            print("Play video " + str(index))
            
if temptFile == '':        
    index = 0
    print("Play video " + str(index))

    
for file in os.listdir(os.getcwd()):
    if file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".mpeg") :
        media.append(os.path.join(os.getcwd(), file))


print("omxplayer -o hdmi "+media[index])
os.system("omxplayer -o hdmi "+media[index])
index = (index + 1) % len(media)
with open("tempt.txt",'w') as f:
    f.write(str(index))
#os.system("omxplayer -o hdmi "+media[index])


 
