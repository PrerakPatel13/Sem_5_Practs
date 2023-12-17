def mergefiles(file1,file2,file3):
    with open("file1.txt",'r') as f1, open("file2.txt",'r') as f2, open("file3.txt",'w') as f3:
        line1=f1.readline().strip()
        line2=f2.readline().strip()
        while(line1 or line2):
            if(not line1):
                f3.write(line2+"\n")
                line2=f2.readline().strip()
            elif(not line2):
                f3.write(line1+"\n")
                line1=f1.readline().strip() 
            else:
                num1=int(line1)     
                num2=int(line2)    
                if(num2>num1):
                    f3.write(line1+"\n")
                    line1=f1.readline().strip() 
                else:
                    f3.write(line2+"\n")
                    line2=f2.readline().strip()

mergefiles('file1.txt','file2.txt','file3.txt')
