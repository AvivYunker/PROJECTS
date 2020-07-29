import pymongo
import pygame
from pymongo import MongoClient
RED = (255,0,0)
screen = pygame.display.set_mode((1300,700))

# IN-GAME VARIABLES
#no_players = int(input("User, how many players?"))
#lim = no_players
#for cnt in range(0, lim, 1):
    #print("User, enter color for player" + str(cnt + 1) + ":\n")


cluster = MongoClient("mongodb+srv://pyrisk_user:6310297799@cluster0-udhog.gcp.mongodb.net/test?retryWrites=true&w=majority")

#pygame.draw.lines(screen, RED, False, alaska_outlines, THICKNESS)

db = cluster["pyrisk_db"]
collection_layouts = db["pyrisk_outlines"]
collection_resolutions = db["pyrisk_resolutions"]
collection_colors = db["pyrisk_colors"]

# FOR LAYOUTS
# 0 - 41 ==> countries
# 42 - 97 ==> hexagons
# 98 - 161 ==> pyramids
# 162 - 165 ==> quick-triangles
# 166 - 197 ==> serious-triangles
# 198 - 233 ==> squares
# 234 - 265 ==> stadium
# 266 - 370 ==> keyboard

# FOR RESOLUTIONS
# 0 ==> Countries
# 1 ==> Hexagons
# 2 ==> Pyramids
# 3 ==> Quick-Triangles
# 4 ==> Serious-Triangles
# 5 ==> Squares
# 6 ==> Stadium
# 7 ==> Keyboard

# FOR COLORS
# 0 ==> Green
# 1 ==> Blue
# 2 ==> Yellow
# 3 ==> Red
# 4 ==> Orange
# 5 ==> Purple

for cnt in range(198, 234, 1):
    results = collection_layouts.find_one({"_id":cnt})
    x  = results["outlines"]
    pygame.draw.lines(screen, RED, False, x, 1)
pygame.display.update()

for cnt in range(0, 6, 1):
    results = collection_colors.find_one({"_id":cnt})
    x = results["rgb_data"]
    print("The " + str(cnt + 1) + " color is:")
    lim = len(x)
    for cnt1 in range(0, lim, 1):
        print(str(cnt1), end=",")