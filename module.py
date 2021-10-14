import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
class functions:
    def __init__(self):
        pass
    try: 
        def PayListManually(): 
            x = list() 
            y= list()  
            print("\nEnter values of x and enter 'done' at the end\n")
            while True:
                a = input()
                if  str(a) == 'done':
                    break
                else:
                    x.append(a)
                
            print("\nEnter values of y and enter 'done' at the end\n")
            while True:
                b = input()
                if  str(b) == 'done':
                    break
                else:
                    if len(y)<len(x):
                        y.append(b)
                    else:
                        raise Exception("\nError: The number of 'y' values should be equal to number of 'x' values\n")
            if len(x) == len(y):
                return list(map(int,x)) , list(map(int,y))
            else:
                raise Exception("\nError: The number of 'y' values should be equal to number of 'x' values\n")      
    except:
        print("Some error occured")
        
    def PayListDataset():
        data = pd.read_csv('D:/data.csv')
        values = data.to_numpy()
        x = values[:,0]
        y = values[:,1]
        return x,y
        
        
    
    def PayListRandom(number):
         x = np.random.randint(0,100,size=number)
         y = np.random.randint(0,100,size=number)
         return x,y
     
    def MeasurementPlotting(listeX,listeY,linie,connected):
        if connected:
            plt.plot(listeX,listeY,marker=linie)
            plt.xlabel('X values')
            plt.ylabel('Y values')
            plt.show()
        else:
            plt.plot(listeX,listeY,linie)
            plt.show()
            
    def WriteToFile(listeX,listeY,filename):
        f = open(filename, "w")
        zipped = [listeX, listeY]
        for x in zip(*zipped):
            f.write("{0}\t{1}\n".format(*x))
        f.close()
        
    def ReadFromFile(filename):
        print("\ncontent of the file with the name {}:".format(filename))
        c = 0
        f = open(filename, 'r')
        lines = f.readlines()
        for x in lines:
            c = c + 1
            print("{}\t\t\t{}".format(c,x))
