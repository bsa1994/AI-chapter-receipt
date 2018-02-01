# !/usr/bin/python3
# coding: utf-8

import os
import re
import time
from collections import defaultdict
from difflib import get_close_matches
import yaml
import vision
from objectview import ObjectView

THIS_FOLDER = os.getcwd()

# Expense receipt to be parsed
class Receipt(object):

    def __init__(self, config, raw):

        self.config = config # Set config file
        self.name = self.date = self.location = self.total = None # Initialize variables to be parsed
        self.tax = self.currency = self.type = None
        self.lines = raw # Set raw data
        self.parse()

# Launches all parsing functions
    def parse(self):

        self.name= self.parse_name()
        self.date = self.parse_date()
        self.location = self.parse_location()
        self.total = self.parse_total()
        self.tax = self.parse_tax()
        self.currency = self.parse_currency()
        self.type = self.parse_type()

# Returns the first line that contains a keyword
# Also runs a fuzzy match if accuracy < 1.0
    def fuzzy_find(self, keyword, accuracy=0.6):

        for line in self.lines:
            words = line.split()
            matches = get_close_matches(keyword, words, 1, accuracy)
            if matches:
                return line


# *************************** NAME ***************************
# Comment: Proposer la ligne 1 du reçu peut suffire pour l’instant, mais ça n’est probablement pas toujours le cas
    def parse_name(self):
        return None

# *************************** DATE ***************************
# Comment: Identifier un match rapproché avec un ensemble de regular expression (regex) prédéfinis dans un fichier de config
    def parse_date(self):
        return None

# *************************** LOCATION ***************************
# Comment: 1. Identifier un match avec une regex de type « int/int/int/int/int/space »
#          2. Faire ensuite un call à l’API Google Maps avec :
#               - Le code postal seul pour obtenir la ville
#               - La ligne contenant le code postal + la ligne précédente (adresse complète ?) pour obtenir le nom du bar (moins fiable mais à tester)
    def parse_location(self):
        return None

# *************************** TOTAL ***************************
# Comment: Identifier le plus grand nombre entier qui soit suivi d’un point
#          Identifier un match rapproché avec un ensemble de mots définis dans le fichier de config (« total », « somme », « tot », etc.) et retourner la ligne suivante
#          ATTENTION : chaque méthode n’est pas exclusive : nous pouvons implémenter les deux et checker si elles donnent le même résultat. Si ce n’est pas le cas ou si le degré de précision n’est pas atteint, notre futur bot rentrera en jeu pour confirmer auprès de l’utilisateur
    def parse_total(self):
        return None

# *************************** TAX ***************************
# Même principe que pour le Total, mais avec le nombre le plus grand qui soit dans l’intervalle 0-30% du Total
    def parse_tax(self):
        return None

# *************************** CURRENCY ***************************
# Identifier un match rapproché avec un ensemble de mots définis dans le fichier de config (« euro », « euros » , « eu », « usd », « $ »)
# Se baser sur le pays si l’adresse a été parsée (moins fiable)
    def parse_currency(self):
        return None

# *************************** TYPE ***************************
# Identifier un match rapproché avec un ensemble de mots définis dans le fichier de config ("restaurant", "bar", "taxi")
    def parse_type(self):
        return None


# Reads the config file
def read_config(file="config.yml"):

    stream = open(os.path.join(THIS_FOLDER, file), "r")
    docs = yaml.safe_load(stream)
    return ObjectView(docs)


def main():

    vision.launch()
    config = read_config()
    text = open('picture.txt','r')
    receipt = Receipt(config, text.readlines())

    #Prints the result - to modify in order to get an array of results
    print("Name:     "+str(receipt.total))
    print("Date:     "+str(receipt.total))
    print("Location: "+str(receipt.total))
    print("Total:    "+str(receipt.total))
    print("Tax:      "+str(receipt.total))
    print("Currency: "+str(receipt.total))
    print("Type:     "+str(receipt.total))


if __name__ == "__main__":
    main()
