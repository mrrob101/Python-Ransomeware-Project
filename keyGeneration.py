import rsa

publicKey, privateKey = rsa.newkeys(2048)


with open('publicKey.pem', 'wb') as p:
     p.write(publicKey.save_pkcs1('PEM'))
with open('privateKey.pem', 'wb') as p:
    p.write(privateKey.save_pkcs1('PEM'))

