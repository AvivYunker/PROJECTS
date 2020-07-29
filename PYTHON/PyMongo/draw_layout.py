import pymongo
import pygame
from pymongo import MongoClient
RED = (255,0,0)
screen = pygame.display.set_mode((1300,700))

cluster = MongoClient("mongodb+srv://PyRiskUser:123123321@cluster0-udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

#pygame.draw.lines(screen, RED, False, alaska_outlines, THICKNESS)

db = cluster["pyrisk_db"]
collection = db["pyrisk_outlines"]

# 0 - 41 ==> countries
# 42 - 97 ==> hexagons
# 98 - 161 ==> pyramids
# 162 - 165 ==> quick-triangles
# 166 - 197 ==> serious-triangles
# 198 - 233 ==> squares
# 234 - 265 ==> stadium
# 266 - 370 ==> keyboard

for cnt in range(0, 42, 1):
    results = collection.find_one({"_id":cnt})
    x  = results["outlines"]
    pygame.draw.lines(screen, RED, False, x, 1)
pygame.display.update()


input("\nDONE!\n")