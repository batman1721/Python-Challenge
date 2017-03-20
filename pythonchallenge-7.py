#Python Challenge 7

from PIL import Image

img = Image.open('oxygen.png')
width= img.width
height= img.height

#img.getpixel((0,0))
row=[]
for i in xrange(0,width):
    row.append(img.getpixel((i,height/2)))

#print row[::7]
ords = [r for r, g, b, a in row if r == g == b]
#print ords

print "".join(map(chr, ords))
