import os
import sys
from collections import Counter
clear = lambda: os.system('cls')

class Main():

    # Klasse aller Operationen die der Taschenrechner durchführen kann
    class Operations():
        def __init__(self,uInput):
            self.uInput = uInput
            return
        
        # Klasse um User Input unterschiedlich Formatieren zu können
        class Convert():
            def __init__(self,uInput):
                self.data = uInput
                return
            
            # Convertierung string list to list with int items
            def StringListToIntList(self):
                list = self.data.split(",")
                li = []
                for i in list:
                    li.append(int(i))
                return li
        
        # Berechnung der relativen Haeufigkeit
        class RelativeHaufigkeit():
            def __init__(self,uInput):
                self.data = uInput
                
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
            
        # Berechnung des Medianwerts    
        class Medianwert():
            def __init__(self, user_input):
                self.data = user_input
                
            def Median(self):
                lis = sorted(self.data)
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
            
    # Beinhaltet für jede mögliche Option, die der User eingeben kann, ein Skript.
    # Skripte beeinhalten Option-Spezifische Inputs
    class Options():
        def __init__(self):
            self.header = Main.BodyFunctions()
        
        # Relative Häufigkeit
        def option1(self):
            clear()
            self.header.header()
            print(" Relative Häufigkeiten\n")
            print(" Geben sie beliebig viele Zahlen ein, die mit einem , getrennt sind:\n"
                  " Reihenfolge und doppelte Einträge werden automatisch in das korrekte Format verarbeitet.\n"
                  "\n Beispiel: 4,4,5,12,23,128,12,13,..\n")
            uInput = input(" Eingabe: ")
            conversion = Main.Operations.Convert(uInput)
            obj = Main.Operations.RelativeHaufigkeit(conversion.StringListToIntList())
            print("\n Ergebnis:\n")
            print(" Xi :",obj.Xi(),"\n",
                  "hxi:",obj.hxi(),"\n",
                  "fxi:",obj.fxi(obj.hxi()),"\n",
                  "Hxi:",obj.Hxi(obj.hxi()),"\n",
                  "Fxi:",obj.Fxi(obj.Hxi(obj.hxi()))
                  )
            return
    
        # Medianwert (Zentralwert)
        def option2(self):
            clear()
            self.header.header()
            print(" Medianwert\n")
            print(" Geben sie beliebig viele Zahlen ein, die mit einem , getrennt sind:\n"
                  " Reihenfolge und doppelte Einträge werden automatisch in das korrekte Format verarbeitet.\n"
                  "\n Beispiel: 1,2,3,12,8,10,..\n")
            uInput = input(" Eingabe: ")
            conversion = Main.Operations.Convert(uInput)
            
            obj = Main.Operations.Medianwert(conversion.StringListToIntList())
            print("\n Median: ",obj.Median())
            return
    
    # Klasse mit mit allen notwendigen Funktionen für den Body des Programms
    class BodyFunctions():
        def __init__(self):
            return
        
        # Überschrift vom Programm
        def header(self):
            print("### Statistic Calculator ### © Oliver Kubon ###")
            print("###############################################\n")
            return
        
        # Beinhaltet Auwahlmöglichkeiten
        def body(self):
            print(" Startseite \n")
            print(" Was möchten Sie berechnen?\n")
            print(" 1. Relative Häufigkeiten")
            print(" 2. Medianwert")
            print(" 3. Arithmetisches Mittel")
            return
        
        # Haendelt den allgemeinen User Input
        def user_input(self):
            choice=input("\n Eingabe: ")
            take = Main.Options()
            if choice == "1":
                take.option1()
            elif choice == "2":
                take.option2()
            elif choice == "3":
                take.option3()
            return
        
        # Exit
        def footer(self):
            uInput = input("\n Neu starten? [y/n]")
            if uInput == "n":
                sys.exit(0)
                return 
            elif uInput == "y":
                return True          
        
    # Body Klasse - Mainfunction
    class Body():
        def __init__(self):
            Bodyfunction = Main.BodyFunctions()
            while True:
                clear()
                Bodyfunction.header()
                Bodyfunction.body()
                Bodyfunction.user_input()
                Bodyfunction.footer()
        
Main.Body()
