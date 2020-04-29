import os
from collections import Counter
import math
clear = lambda: os.system('cls')

# Klasse aller Operationen die der Taschenrechner durchführen kann
class Calculator():
    class PlusMinus(): 
        def __init__(self,a,b):
            self.a = a
            self.b = b
        def add(self):
            return self.a+self.b
        def mul(self):
            return self.a*self.b
        def div(self):
            return self.a/self.b
        def sub(self):
            return self.a-self.b
       
    class RelativeHaufigkeit():
        def __init__(self,user_input):
            self.data = user_input
            
        # Liste der Eingabe ohne doppelte Werte
        def Xi(self):
            data = {"Xi" : sorted(self.data)}
            return list(dict.fromkeys(data["Xi"]))
        
        # absolute Häufigkeit
        def hxi(self):
            data = {"hxi":dict(Counter(sorted((self.data))))}
            hxi_list = []
            for value in data["hxi"]:
                hxi_list.append(data["hxi"][value])
            return hxi_list
        
        # relative Häufigkeit
        def fxi(self,hxi_list):
           fxi_list = []
           hxi_sum = sum(hxi_list)
           for i in hxi_list:
               result = round(i / hxi_sum,2)
               fxi_list.append(result)
           return fxi_list
       
        # kumulierte Häufigkeit
        def Hxi(self,hxi_list):
            Hxi_list = []
            value = 0
            for i in range(0, len(hxi_list)):
                value += hxi_list[i]
                Hxi_list.append(value)
            return Hxi_list
        
        # relative kummulierte Häufigkeit
        def Fxi(self,Hxi_list):
            Fxi_list = []
            hxi_sum = Hxi_list[-1]
            for i in Hxi_list:
                result = round(i / hxi_sum,2)
                Fxi_list.append(result)
            return Fxi_list
     
    class Medianwert():
        def __init__(self, user_input):
            self.data = user_input
            
        def Median(self):
            lis = self.data
            leng = len(self.data)
            
            if (leng % 2) != 0:
                loc = int((leng) / 2)
                median = lis[loc]
            else:
                median = []
                loc1 = int((leng / 2) - 1)
                loc2 = int(((leng / 2) + 1) - 1)
                median = [lis[loc1],lis[loc2]]
            return median
        
# Überschrift vom Programm
def header():
    print("### Taschenrechner9000 ### Autor: Oliver Kubon ###")
    print("##################################################\n")
    return

# Convertet einen string mit zahlen und komma in int um
def ConvertToInt(user_input):
    list = user_input.split (",")
    li = []
    for i in list:
        li.append(int(i))
    return li  
        
# Einfache Berechnung
def choice1():
    clear()
    print("### Taschenrechner9000 ###\n")
    print(" Einfache Berechnungen\n")
    print("Geben Sie zwei Zahlen ein:\n")
    a = int(input("Eingabe: "))
    b = int(input("Eingabe: "))
    obj = Calculator.PlusMinus(a,b)
    print("\nWas möchten Sie berechnen?\n")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    choice=int(input("\nEingabe: "))
    if choice==1:
        print("\nErgebnis: ",obj.add())
    elif choice==2:
        print("\nErgebnis: ",obj.sub())
    elif choice==3:
        print("\nErgebnis: ",obj.mul())
    elif choice==4:
        print("\nErgebnis: ",round(obj.div(),2))
    return

# Relative Häufigkeit
def choice2():
    clear()
    header()
    print(" Relative Häufigkeiten\n")
    print("Geben sie beliebig viele Zahlen ein, die mit einem , getrennt sind:\nBeispiel: 4,5,12,23,..,..\n")
    user_input = input("Eingabe: ")
    obj = Calculator.RelativeHaufigkeit(ConvertToInt(user_input))
    print("\nErgebnis:\n")
    print(" Xi :",obj.Xi(),"\n",
          "hxi:",obj.hxi(),"\n",
          "fxi:",obj.fxi(obj.hxi()),"\n",
          "Hxi:",obj.Hxi(obj.hxi()),"\n",
          "Fxi:",obj.Fxi(obj.Hxi(obj.hxi()))
          )
    return

# Medianwert (Zentralwert)
def choice3():
    clear()
    header()
    print(" Medianwert\n")
    user_input = input("Eingabe: ")
    obj = Calculator.Medianwert(ConvertToInt(user_input))
    print("\nMedian: ",obj.Median())
    return

# Hauptfunktion
def main():
    clear()
    header()
    print(" Startseite \n")
    print(" Was möchten Sie berechnen?\n")
    print(" 1. Einfache Berechnungen(+-/*)")
    print(" 2. Relative Häufigkeiten")
    print(" 3. Median")
    choice=input("\n Eingabe: ")
    if choice == "1":
        choice1()
    elif choice == "2":
        choice2()
    elif choice == "3":
        choice3()
    input("\nMit Enter beenden..")
    return True


main()
        
        
        