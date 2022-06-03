## Diplomado Python
#Nombre: Deison Tuiran Londoño
#Email:  deison.tuiran@upb.edu.co
#Codigo: 014810


from email.policy import default
import pandas as pd
import numpy as np

inf = pd.read_excel("inf.xlsx")

#exercise 1

imc = (inf["weight"]/(inf["height"])**2).round(0)
inf["imc"] = imc

#exercise 2

compound_interest = ((inf["money for investing"]*(1+(inf["annual interest rate"]/100))**inf["time for investing"])-inf["money for investing"]).round()
inf["compound interest"] = compound_interest

#exercise 3

condition_list = [
    (inf["time to buy the bread after baking"] <= 6),
    (inf["time to buy the bread after baking"] <= 12 ),
    (inf["time to buy the bread after baking"] <= 18 ),
    (inf["time to buy the bread after baking"] <= 24 )
]
choice_list = [10,20,30,40]
inf["discount percentage"] = np.select(condition_list,choice_list,default="not specified")

#exercise 4

condition_list_for_extension = [
    (inf["gender"] == "M"),
    (inf["gender"] == "F" )
]
choice_list_for_extension = [inf["phone number"] + "-11",inf["phone number"] + "-10"]
inf["number with extension"] = np.select(condition_list_for_extension,choice_list_for_extension,default="not specified")


print(inf)
