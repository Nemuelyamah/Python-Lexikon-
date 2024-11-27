#Abschnitt 1#
print("Hallo Welt")  # print um den Satz auszugeben /Um ein Satz auszugeben mithilfe von Strings ""

print(7) #Eine Zahl wird ausgegeben

print(3.4) #Gleitkommazahl wird bei Python als Punkt dargestellt

print('Hallo Welt') #Eine andere Variante Strings zu schreiben

print( "Hallo" + "Welt") #Strings verbinden

age = 20 #Haben einer Variabel einen Wert gegeben. In diesem Fall haben wir 20 in der Variabel age zugewiesen

print(age) #Geben den Wert der Vairiabel aus

age = 21 #überschreiben den Wert und ändern in damit

name = "Nemuel" #Können den auch Strings Variabeln zuweisen

#Abschnitt 2 #

# int: Datentyp für Ganzzahlen

int_variabel = 100  #mit einem _ kann man Wörter verbinden

# float: Datentyp für Gleitkommazahlen

float_variabel = 13.10

# str: Datentyp für Strings

str_variabel = "Nemuel"

#Abschnitt 3 #
print("Anfang des Programmes") 
name = input()  #input Funktion/mit den Runden Klammern wird eine Funktion aufgerufen/ geben der Funktion einen Namen 
print("Mein Name ist " + name) 
age = input () 
print("Mein Alter ist " + age) 
print("Ende des Programmes")



print("Start") 
name = input("Bitte gebe deinen Namen ein:   ") # mithilfe von String kann man den Sinn einer Funktion verdeutlichen

#Abschnitt 4#
print("Willkommen zum Addieren von Programmenn")
value1 = input("Erste Zahl angeben:  ")
value2 = input("Zweite Zahl angeben: ") 
print(value1 + value2)                            #??????????????    #damit kann man zwei Zahlen kombinieren bzw verkettet

print(type(value2))   #???????????? # type zeigt uns um welchen Datentypen handelt #dadurch das es sich hier um ein String geht werden die zaheln verbunden

wert1 = input() 
wert2 = input()

print(wert1 + wert2)

print(int(wert1) + int(wert2)) # damit können die Werte addiert werden weil die jeweiligen Werte in int umgewandelt werden

wert1 = int(input())
wert2 = int(input()) #eine Variante die etwas schneller geht # das geht auch mit allen anderen Datentypen wie z.b float 
print (wert1 + wert2)

#Abschnitt 5#
print(1 < 5) # Vergleichen zwei Zahlen mit einem Operator >,<,==,<= # indemfall handelt es sich es um Datentyp bool

print(type(1<5))  # lassen uns anzeigen um welchen Datentypen es sich handelt

print (1==2) # Gleich Operator


print (1 != 2) #Ungleich Operator


print ((2+3)*2 == 10) # mehrer Sachen könne auch verglichen werden


#Abschnitt 6 #

age = int(input("Bitte gebe dein alter ein:  "))  # er wird eine Zahl eingeben und deswegen als int

if age < 18:         #nur wenn die Bedingung nach dem if Anweisung also im Beispiel: age < 18 erfüllt wird ->  die darunter geschriebene Zeile ausgeführt 
    print("Achtung, der Nutzer ist unter 18!") 

print("Pogrammende")


#Abschnitt 7 #

age = int(input("Bitte gebe dein alter ein:  "))  

if age < 18:         
    print("Achtung, der Nutzer ist unter 18!") 

elif age == 18:                                     #Falls die Anweisung if nicht Stimmt dann wird elif ausgeführt 
    print("Der Nutzer ist exakt 18") #man kann so viele elif Zweige ausführen wie man möchte 

else:                                        #sollte die elif Anweisung nicht Stimmen dann wird else ausgeführt 
    ("Nutzer ist volljährig") 

print("Pogrammende")


#Abschnitt 7# Erstes Projekt#Geburtstag Generator#

print ("---Wilkommen zu Geburtstag Generator") 
name = input("Name der grüßenden Person:  ") 
age = input("Alter der grüßenden Person:  ") 
sender = input("Name des Absenders:       ") 

print("Sehr geehrte/-r " + name + ",") 
print("Ich wünsche dir alles gute zum" + age + "ten Geburtstag") 
print("Ich hoffe du genießt diesen Tag und kriegts viele schöne Geschenke bekommst.") 
print("Zudem wünsche ich dir viel Glücke und Liebe in deinem Leben") 

print ("Liebe Grüße") 
print (sender) 


# Abschnitt 11 #
# print usw. sind build in Functions sind schon vordefinierte Funktionen die man nicht selber def bzw coden muss

def say_hello():      # als erstes kommt def (steht für Definition)/danach den Bezeichner(kann man sich aussuchen)/(): danach diese Zeichen
    print("Hallo Meister Nemuel")
    print("Willkomen zurück")      #Die zwei Zeilen unter dem def sind der Funktionskörper und definieren die Funktion/Diese Anweisungen werden dann ausgeführt wenn wir die Funktion ausführen

say_hello()                 #damit ruft man die Funktion auf/als erstes den Funktionnamen und dann die ()

print("Test")
say_hello()      #Die Funktion kann auch mehrfach aufgerufen werden

#Abschnitt 12 #

def say_hello(name):  #Führen hier einen Parameter herein damit die Funktion nicht mehr Statisch ist
    print("Hello " + name) #fügen hier den Parameter mit dem String mit einem + zusammen ?
    print("Willkommen zurück")

say_hello("Nemuel") #In diesem Fall ist Meister Nemuel ein Argument was in die Funktion eingegeben wird/Kann beliebig sein

#Machen wir das ganze mit zwei Parametern in einer Funktion

def say_hello(first_name, last_name): # um zwei Parameter zu haben kann man die ganz einfach mit einem Komma trennen
    print("Hello " + first_name + " " +  last_name) #Um hier die Ausgabe Sinnvoll zu machen, machen wir einen leeren String zwischen die Parameter und verbinden alles mit einem +

print("Willkommen zurück")
say_hello("Nemuel", "Yamah") #Um beiden Parameter auszugeben, müssen wir sie mit einem Komma trennen und sie als getrennte Strings aufschreiben

#Funktionen mit Rückgabewert
#Jede Funktion besitzt einen Rückgabewert
def say_hello(first_name, last_name):
    print("Hello " + first_name + " " +  last_name)


print(type(say_hello("Nemuel", "Yamah"))) # Weil kein Wert ausgeben wird, ist das ein None Type

def maximum(a, b)


# Abschnitt 13
Eingabeprüfung mit isdigit():
Wir stellen sicher, dass die Eingabe eine Zahl ist, bevor wir sie in int umwandeln.
Bsp: Mit lstrip('-') prüfen wir auch negative Zahlen.


# 14. Ausgabe von Daten
print("Hello, World!")  # Gibt "Hello, World!" auf der Konsole aus

# 15. Bedingte Anweisungen
x = 5
if x > 0:  # Prüft, ob x größer als 0 ist
    print("Positive")
elif x == 0:  # Prüft, ob x gleich 0 ist
    print("Zero")
else:  # Führt aus, wenn keine der obigen Bedingungen zutrifft
    print("Negative")

# 16. Schleife über eine Sequenz
for i in range(5):  # Iteriert von 0 bis 4
    print(i)

# 17. Schleife mit Bedingung
x = 0
while x < 3:  # Führt die Schleife aus, solange x kleiner als 3 ist
    print(x)
    x += 1  # Erhöht x um 1

# 18. Funktionsdefinition
def greet(name):  # Definiert eine Funktion mit einem Parameter "name"
    return f"Hello, {name}"  # Gibt eine Begrüßungsnachricht zurück

# 19. Rückgabe aus einer Funktion
result = greet("Alice")  # Ruft die Funktion auf und speichert das Ergebnis
print(result)  # Gibt "Hello, Alice" aus

# 20. Module einbinden
import math  # Importiert das Modul "math"
print(math.sqrt(16))  # Gibt die Quadratwurzel von 16 aus

# 21. Fehlerbehandlung
try:
    x = int("a")  # Versucht, "a" in eine Zahl umzuwandeln (führt zu einem Fehler)
except ValueError:  # Fängt den Fehler ab
    print("Fehler bei der Konvertierung!")

# 22. Schleife beenden
for i in range(10):  # Iteriert von 0 bis 9
    if i == 5:  # Beendet die Schleife, wenn i gleich 5 ist
        break

# 23. Schleifendurchlauf überspringen
for i in range(5):  # Iteriert von 0 bis 4
    if i == 2:  # Überspringt die Iteration, wenn i gleich 2 ist
        continue
    print(i)

# 24. Klassen definieren
class Dog:  # Definiert eine Klasse "Dog"
    def __init__(self, name):  # Konstruktor der Klasse
        self.name = name  # Speichert den Namen des Hundes

# 25. Kontextmanager verwenden
with open("file.txt", "w") as file:  # Öffnet eine Datei im Schreibmodus
    file.write("Beispieltext")  # Schreibt "Beispieltext" in die Datei

# 26. Element zu einer Liste hinzufügen
lst = [1, 2, 3]
lst.append(4)  # Fügt die Zahl 4 ans Ende der Liste hinzu
print(lst)  # Gibt [1, 2, 3, 4] aus

# 27. Erstes Vorkommen eines Elements aus der Liste entfernen
lst.remove(3)  # Entfernt die Zahl 3 aus der Liste
print(lst)  # Gibt [1, 2, 4] aus

# 28. Element oder Variable löschen
del lst[1]  # Löscht das Element an Index 1 aus der Liste
print(lst)  # Gibt [1, 4] aus
y = 5
del y  # Löscht die Variable y
