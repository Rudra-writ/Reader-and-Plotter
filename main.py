import numpy as np
from module import functions as fn
print("Hello and welcome!!\n")
print("Please type 'manual' for manual entry of measurement data, 'dataset' for entry from CSV file or type 'random' for random generation: \n")
choice = input()
if choice == 'manual':
    x , y = fn.PayListManually()
elif choice == 'dataset':
    x , y = fn.PayListDataset()
else:
    print("\nPlease enter the Number of data to be generated:\n")
    number = input()
    x , y = fn.PayListRandom(int(number))
print("\nPlease type 'y' for connected plot or 'n' for unconnected plot\n")
choice = input()
if choice == 'y':
    fn.MeasurementPlotting(x, y ,'o', True)
else:
    fn.MeasurementPlotting(x, y ,'o', False)
print("\nPlease enter a file name of type '.txt' to save the measurement data\n")
choice = input()
fn.WriteToFile(x,y,choice)
fn.ReadFromFile(choice)


    