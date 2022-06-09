## txt files ##
words1 = ['shoes', 'mask', 'upon', 'lisp', 'beak', 'crouched', 'rodeo', 'impolite', 'gusto', 'gauze']
with open('lvl1.txt', 'w') as f:
    for word in words1:
        f.write(word)
        f.write('\n')

words2 = ['bustling', 'drone', 'vibrant', 'exception', 'notification', 'surrounded', 'orientation', 'columns', 'wretched', 'invigorating']
with open('lvl2.txt', 'w') as f:
    for word in words2:
        f.write(word)
        f.write('\n')
        
words3 = ['demeanor', 'morbidity', 'torturous', 'abdomen', 'liability', 'instinctive', 'heirloom', 'impertinent', 'assassinate', 'embroidery']
with open('lvl3.txt', 'w') as f:
    for word in words3:
        f.write(word)
        f.write('\n')