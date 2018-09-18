# coding:  utf-8


def  countDown(i):
    print(i)
    if(i<=0):
        return 
    else:
        countDown(i-1)
        

if __name__ == "__main__":
    
    countDown(10)