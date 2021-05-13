from functools import reduce
import operator
import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd
import scr.foursquare as f
load_dotenv()

def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)