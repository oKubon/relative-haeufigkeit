# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:20:54 2020

@author: Oliver Kubon

Dieses Programm beinhaltet mehrere Optionen, um Statistische Werte auszurechnen. 
Folgende Berechnungen sind derzeit möglich:
- Realtive Häufigkeit
- Medianwert
- Arithmetisches Mittel (AM) und gewogenes Arithmetisches Mittel (GAM)

"""
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
                self.BodyFunction = Main.BodyFunctions()
                
            def Main(self):
                clear()
                self.BodyFunction.header()
                print(" Relative Häufigkeiten")
                print(" #####################\n")
                print(" Geben sie beliebig viele Zahlen ein, die mit einem , getrennt sind:\n"
                      " Reihenfolge und doppelte Einträge werden automatisch in das korrekte Format verarbeitet.\n"
                      "\n Beispiel: 4,4,5,12,23,128,12,13\n")
                uInput = input(" Eingabe: ")
                convert = Main.Operations.Convert(uInput)
                obj = Main.Operations.RelativeHaufigkeit(convert.StringListToIntList())
                print("\n Ergebnis:\n")
                print(" Xi :",obj.Xi(),"\n",
                      "hxi:",obj.hxi(),"\n",
                      "fxi:",obj.fxi(obj.hxi()),"\n",
                      "Hxi:",obj.Hxi(obj.hxi()),"\n",
                      "Fxi:",obj.Fxi(obj.Hxi(obj.hxi()))
                      )
                return
                
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
            def __init__(self, uInput):
                self.data = uInput
                self.BodyFunction = Main.BodyFunctions()
                
            # Medianwert (Zentralwert)
            def Main(self):
                clear()
                self.BodyFunction.header()
                print(" Medianwert")
                print(" ##########\n")
                print(" Geben sie beliebig viele Zahlen ein, die mit einem , getrennt sind:\n"
                      " Reihenfolge und doppelte Einträge werden automatisch in das korrekte Format verarbeitet.\n"
                      "\n Beispiel: 1,2,3,12,8,10\n")
                uInput = input(" Eingabe: ")
                convert = Main.Operations.Convert(uInput)
                obj = Main.Operations.Medianwert(convert.StringListToIntList())
                print("\n Median: ",obj.Median())
                return
                
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
            
        # Berechnung des Aritmetischen Mittels (AM)
        class AM():
            def __init__(self,ls1):
                self.ls1 = ls1
                self.BodyFunction = Main.BodyFunctions()
            
            
            def Main(self):
                clear()
                self.BodyFunction.header()
                print(" Arithmetisches Mittel")
                print(" ######################\n")
                print(" Geben sie beliebig viele Zahlen ein, die mit einem , getrennt sind:\n"
                      "\n Beispiel: 20,25,28\n")
                uInput1 = input(" Eingabe: ")
                convert1 = Main.Operations.Convert(uInput1)
                self.ls1 = convert1.StringListToIntList()
                obj = Main.Operations.AM(self.ls1)
                print("\n Arithmetisches Mittel (AM):",obj.AMcalc())
                return
            
            # Berechnug Arithmetisches Mittel (AM)
            def AMcalc(self):
               result = int(sum(self.ls1)/len(self.ls1))
               return result
    
        # Berechnung des gewogenem Aritmetischen Mittels (GAM)
        class GAM():
            def __init__(self,ls1,ls2):
                self.ls1 = ls1
                self.ls2 = ls2
                self.BodyFunction = Main.BodyFunctions()
                
            # GAM Main
            def Main(self):
                clear()
                self.BodyFunction.header()
                print(" Gewogenes Arithmetisches Mittel")
                print(" ######################\n")
                print(" Geben sie zwei Listen mit beliebig viele Zahlen ein, die mit einem , getrennt sind:\n"
                      " Hinweis! --> Achten Sie darauf, dass beide Listen gleich viele Einträge haben!\n"
                      "              Listen stehen in Beziehung zueinander."
                      "\n Beispiel:\n"
                      "\n Liste 1: 20,25,28\n"
                      " Liste 2: 4,3,6\n")
                uInput1 = input(" Eingabe: ")
                uInput2 = input(" Eingabe: ")
                convert1 = Main.Operations.Convert(uInput1)
                convert2 = Main.Operations.Convert(uInput2)
                self.ls1 = convert1.StringListToIntList()
                self.ls2 = convert2.StringListToIntList()
                obj = Main.Operations.GAM(self.ls1,self.ls2)
                print("\n Gewogenes arithmetisches Mittel (GAM):",obj.GAMcalc())
                return
            
            # Berechnug Gewogenes arithmetisches Mittel (GAM)
            def GAMcalc(self):
                x = 0
                for i in range (0, len(self.ls1)):
                    x += self.ls1[i]*self.ls2[i]
                        
                result = round(float(x / sum(self.ls1)),2)
                return result
            
        # Berechnung des geometrischen Mittels (GM)
        class GM():
            def __init__(self,uInput):
                self.data = uInput
                self.BodyFunction = Main.BodyFunctions()
                
            def Main(self):
                clear()
                self.BodyFunction.header()
                print(" Geometrisches Mittel")
                print(" ######################\n")
                print(" Geben sie beliebig viele Zahlen ein, die mit einem , getrennt sind:\n"
                      " \nAchten Sie dabei auf die richtige Komma und Punkt setzung!\n"
                      "\n Beispiel: 120000,138000,165600,157320,188784,235980\n")
                uInput = input(" Eingabe: ")
                convert = Main.Operations.Convert(uInput)
                self.data = convert.StringListToIntList()
                obj = Main.Operations.GM(self.data)
                print("\n Geometrisches Mittel (GM):",obj.GMcalc())
                return
            
            def GMcalc(self):
                data = {"Data" : sorted(self.data)}
                return data
        
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
            print(" Startseite")
            print(" ----------\n")
            print(" Was möchten Sie berechnen?\n")
            print(" 1. Relative Häufigkeiten")
            print(" 2. Medianwert")
            print(" 3. Arithmetisches Mittel")
            print(" 4. Gewogenes Arithmetisches Mittel")
            print(" 5. Geometrisches Mittel")
            return
        
        # Haendelt den allgemeinen User Input
        def user_input(self):
            uInput=input("\n Eingabe: ")
            if uInput == "1":
                take = Main.Operations.RelativeHaufigkeit(uInput)
                take.Main()
            elif uInput == "2":
                take = Main.Operations.Medianwert(uInput)
                take.Main()
            elif uInput == "3":
                take = Main.Operations.AM(uInput)
                take.Main()
            elif uInput == "4":
                take = Main.Operations.GAM(uInput,uInput)
                take.Main()
            elif uInput == "5":
                take = Main.Operations.GM(uInput)
                take.Main()
            return
        
        # Exit
        def footer(self):
            uInput = input("\n Neu starten? [y/n]: ")
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
