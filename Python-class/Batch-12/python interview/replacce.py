def repl():
    str=input("enter a  string")
    ch=input("enter char to replace")
    for i in str:
                
        if (i==ch):
            s=str.replace(i,"*")  
    
    print(s)
repl()


    
