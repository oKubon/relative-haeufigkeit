# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:20:54 2020

@author: Oliver Kubon

Berechnung der empirischen Häufigkeit F(xi)/relative kumulierte Häufigkeit
Xi = Dauer Buchungsvorgang
hxi = absolute Häufigkeit
fxi = relative Häufigkeit
Hxi = kumulierte Häufigkeit
Fxi = relative kummulierte Häufigkeit
"""
import pprint
import pandas as pd


# Einlesen von Daten
def data(): 
    file = open("data.txt","r") # txt Datei wird eingelesen
    data = file.read().split(",") # Datensätze werden mit , getrennt
    data = sorted(data) # Sortierung von Datensätzen
    data = {"Xi":data} # Umwandlung in ein Dictionary
    return data


# Funktion zum entfernen von doppelten Werten in einer Lste
def clean_list(data,name):
    clean_list = []
    counted =[]
    for i in data[name]:
        if i not in counted:
            clean_list.append(i)
            counted.append(i)
    return clean_list


# h(xi) - absolute Häufigkeit
def hxi(data): 
    hxi_list = [] # Liste mit hxi Werten die später zur Hauptliste geupdatet wird
    counted = [] # Liste mit allen Zahlen die schon gezählt wurden
    for i in data["Xi"]: # Zählt hoch wie oft eine Zahl vorhanden ist
        if i not in counted:
            count = data["Xi"].count(i)
            counted.append(i)
            hxi_list.append(count)
    hxi = {"hxi":hxi_list} # Umwandlung der Liste in ein Dict
    data = {"Xi":clean_list(data,"Xi")} # Säuberung doppelter Einträge in den Daten
    data.update(hxi) # Zusammenfügung der hxi Daten mit den Xi Daten
    return data


# f(xi) - relative Häufigkeit
def fxi(data):
    fxi_list = []
    hxi_sum = sum(data["hxi"]) # Summe der absoluten Häufigkeiten h(xi)
    for i in data["hxi"]:
        result = round(i / hxi_sum,2)
        fxi_list.append(result)
    fxi = {"fxi":fxi_list}
    data.update(fxi)
    return data


# H(xi) - kummulierte Häufigkeit
def Hxi(data):
    Hxi_list = []
    n = 0
    for i in data["hxi"]:
       n += i 
       Hxi_list.append(n)
    Hxi = {"Hxi":Hxi_list}
    data.update(Hxi)
    return data


# F(xi) - relative kumulierte Häufigkeit
def Fxi(data):
    Fxi_list = []
    hxi_sum = sum(data["hxi"])    
    for i in data["Hxi"]:
        result = round(i / hxi_sum,2)
        Fxi_list.append(result)
    Fxi = {"Fxi":Fxi_list}
    data.update(Fxi)
    return data


#Hauptfunktion
def main():
    # Speichert die ausgeführten Funktionen in mydict
    mydict = Fxi(Hxi(fxi(hxi(data()))))
    print(mydict)
    # Erstellt aus dem fertigen Dictionary eine csv Datei im selben Verzeichnis
    (pd.DataFrame.from_dict(data=mydict, orient='index')
     .to_csv('new_data.csv', header=False))

    return True


main()


