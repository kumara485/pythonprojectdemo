import pandas as pd 

def showDF():
    l=["kumar","kiran","sita"]
    df= pd.DataFrame(l)
    print(df)
    

def sayHello():
    print("hello world")
    showDF()
    
    
    

def main():
    sayHello()


if __name__ == '__main__':
    main()