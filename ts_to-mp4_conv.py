import subprocess
import os
import ffmpeg
import time

debut = time.time()

dirPath = r"CHEMIN"
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]


i=0
somme=0
while i<len(result):
    path_to_conv=dirPath + "/"+result[i]
    
    sorti="/home/pc/Bureau/test/"+result[i]+".mp4"
    #sorti=path_to_conv+".mp4"    
    subprocess.run(['ffmpeg', '-i', path_to_conv, sorti])
    supr="rm "+path_to_conv
    os.system(supr)
    #command="ffmpeg -i "+path_to_conv+" c:v libx264 -c:a aac "+sorti
    #os.system(command)
    
    somme+=1
    i+=1

print("Il y'a : ", somme, " fichier converti en mp4")
print("Sa vous a pris ",time.time() - debut)
