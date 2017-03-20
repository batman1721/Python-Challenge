#Python Challenge 6

import zipfile, re

ans='90052'
archive = zipfile.ZipFile('channel.zip', 'r')
comentarios=[]
while True:
    resultado=archive.read(ans+'.txt')#.decode('utf-8')
    comentarios.append(archive.getinfo(ans+'.txt').comment.decode('utf-8'))
    numero=re.search('Next nothing is (\d+)', resultado)
    if numero==None:
        break
    ans=numero.group(1)

print ans
print ''.join(comentarios)
