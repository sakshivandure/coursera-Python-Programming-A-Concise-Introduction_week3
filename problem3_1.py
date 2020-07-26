def problem3_1(txtfilename):
    t=open(txtfilename)
    charct=0
    for line in t:
        print(line,end="")
        charct+=len(line)
    print('\n')
    print('There are',charct,'letters in the file.')
    t.close()