import tkinter 
from APIs import *

def main():
    bb = bbSearch(input("Enter search query(BestBuy): "))
    bb.display()
    tesco = tescoSearch(input("Enter search query(Tesco): "))
    tesco.display()
        
main()