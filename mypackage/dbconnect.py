import pymongo
import os
from dotenv import *

load_dotenv()
Username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


myclinet = pymongo.MongoClient(f"mongodb+srv://{Username}:{password}@cluster0.ncdyd.mongodb.net")

mydb = myclinet["CSEC"]

def addPresedent(names):
    global mydb
    
    mycol = mydb["President"]
    nominee = []
    
    for name in names :
        nominee.append({"name": name })
    mycol.insert_many(nominee)

def addCPD(names):
    global mydb
    
    mycol = mydb["CPD"]
    nominee = []
    
    for name in names :
        nominee.append({"name": name })
    mycol.insert_many(nominee)

def addCapacityB(names):
    global mydb
    
    mycol = mydb["Capacity Building"]
    nominee = []
    
    for name in names :
        nominee.append({"name": name })
    mycol.insert_many(nominee)

def addDevelopment(names):
    global mydb
    
    mycol = mydb["Development"]
    nominee = []
    
    for name in names :
        nominee.append({"name": name })
    mycol.insert_many(nominee)

def addVPresident (names):
    global mydb
    
    mycol = mydb["Vice President "]
    nominee = []
    
    for name in names :
        nominee.append({"name": name })
    mycol.insert_many(nominee)


    