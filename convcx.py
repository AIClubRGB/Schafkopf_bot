import os
import io
CWD = os.getcwd()

#tr_path = os.path.join(CWD,'train')
def txt_producer(string):
    tr_path = os.path.join(CWD,string)
    #with io.open('train.txt','w',newline='\r\n') as tr:
    with io.open(string+'.txt','w',newline='\r\n') as tr:
        for file in os.listdir(tr_path):
            if file.endswith(".jpg"):
                #tr.write(os.path.join('data','obj',file+u'\n'))
                #tr.write(os.path.join('C:','cygwin64','home','Dell-XPS','darknet','data','obj',file+u'\n'))
                tr.write('data/obj/'+string+'/'+file+u'\n')
        
txt_producer('train')
txt_producer('val')
