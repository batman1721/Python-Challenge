#Pythonchallenge 1

##code='''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
code='map'

key='abcdefghijklmnopqrstuvwxyz'
shift=2

decrypted=''
for i in xrange(0,len(code)):
    if code[i] in key:
        decrypted+=key[(key.index(code[i])+shift)%len(key)]
    else:
        decrypted+=code[i]

print decrypted
