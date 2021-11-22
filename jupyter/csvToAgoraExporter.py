import pandas as pd
from bs4 import BeautifulSoup
from webbot import Browser
import sys
from pathlib import Path

def main(argv):
    print(argv)
    web = Browser()
    web.go_to("https://agora.univ-catholille.fr/isacademia/PORTAL3S.htm")
    if(len(argv)==2):
        web.type(argv[0],into="username")
        web.type(argv[1],into="password")
        web.click("SE CONNECTER",id="submit")
        print("Rendez-vous sur la plateforme de saisie de notes et selectionnez la classe voulue.")
    else :
        print("Connectez-vous a Agora puis rendez-vous sur la plateforme de saisie de notes et selectionnez la classe voulue.")

    print("Voici un exemple de fichier csv au format attendu :\nid;notes\nREYNAERT Vincent;17.00\nESTEVES Aurelien;17.00\nNOM prenom;note")
    csvFilePath = input("Veuillez entrer le chemin vers le fichier csv que vous voulez saisir automatiquement \n\
        (ATTENTION veillez a avoir une premiere ligne pour les indices des colonnes qui devront correspondre a : \n\
        id (NOM prenom) et notes (les notes avec des points pour les nombres a virgules) ): ")
    csvSep = input("Merci de preciser le caractere separateur utilise dans votre CSV (generalement ; ou ,) : ")
    while not(csvFilePath and csvSep and Path(csvFilePath).is_file()):  
        print("Mauvais chemin ou saisie invalide.")      
        csvFilePath = input("Veuillez entrer le chemin vers le fichier csv que vous voulez saisir automatiquement \n\
            (ATTENTION veillez a avoir une premiere ligne pour les indices des colonnes qui devront correspondre a : \n\
            id (NOM prenom) et notes (les notes avec des points pour les nombres a virgules) ): ")
        csvSep = input("Merci de preciser le caractere separateur utilise dans votre CSV (generalement ; ou ,) : ")
    
    if (csvFilePath and csvSep and Path(csvFilePath).is_file()):
        pass
        df = pd.read_csv(csvFilePath,sep=csvSep,index_col='id')
        notes = df.to_dict()["notes"]
        source = web.get_page_source()
        soup = BeautifulSoup(source)
        htmlTable = soup.find("table",id="laTable").find("tbody")
        for element in htmlTable.find_all("tr",style="background:"):
            print(element.get("id"))
            name = str(element.find("td")).replace("<td>","").replace("</td>","")
            print(str.lower(name).split(" "))
            namenote = notes[name]
            print(namenote)#.get("name")
            for i in element.find_all('input',type="text"):
                elementid = i.get("id")
                print(elementid)
                web.type(str(namenote),id=elementid)
                break
            print()
    else:
        print("Wrong path")
        quit()


if __name__ == "__main__":
    main(sys.argv[1:])

