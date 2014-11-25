#!/usr/bin/python3
from math import *
from decimal import *

import nbt

# setup 
TIME_INTERVAL = 18000  # 20 ticks * 60 seconds * 15 minutes
timeDict = {}
scoreDict = {}
totalDict = {}

def main():
    nfile = nbt.nbt.NBTFile("lan/data/scoreboard.dat", "rb")

    # Iterate through all stats records
    # Creates dictionaries with all needed keys.
    #print("DEBUG: Initializing keys")
    for i in range(nfile["data"]["PlayerScores"].__len__()):
        # Explicitly cast NBT data as string to avoid dictionary duplicates
        # caused by pass-by-reference issues.
        name = str(nfile["data"]["PlayerScores"][i]["Name"])
        obj  = str(nfile["data"]["PlayerScores"][i]["Objective"])
        if obj == "playOneMinute":
            timeDict[name] = Decimal(nfile["data"]["PlayerScores"][i]["Score"].value)
        scoreDict[name] = 0
        totalDict[name] = 0
    #print("DEBUG: printing Dicts")
    #print("TimeDict: ", timeDict)
    #print("ScoreDict: ", scoreDict)
    #print("TotalDict: ", totalDict)

    # Re-iterate through, this time looking for
    # player objectives values.
    for i in range(nfile["data"]["PlayerScores"].__len__()):
        # pull name, objective, and score out
        # Again, explicitly cast type to avoid key duplication issues
        name  = str(nfile["data"]["PlayerScores"][i]["Name"])
        obj   = str(nfile["data"]["PlayerScores"][i]["Objective"])
        score = nfile["data"]["PlayerScores"][i]["Score"]
        # Calculate and put in dictionary structure.
        #scoreDict[name] = (scoreDict[name])+calcScore(name, obj, score.value)
        calcScore(name, obj, score.value)

    for i in totalDict:
        scoreDict[i] = totalDict[i] / ceil(timeDict[i]/TIME_INTERVAL)

    # Sort scores high to low. Put them in ordered list with values
    finList = []
    for i in sorted(scoreDict, key=scoreDict.get, reverse=True):
        finList += [[i, scoreDict[i]]]

    # Display ranks and scores
    count = 0
    print("Rank\tName\t\tAvg.Score\tTotal Score\t\tPlay Time")
    print("-"*80)
    for i in finList:
        count+=1
        print("{}.\t{}\t\t{}\t\t{}\t\t\t{}".format(
                                               count,
                                               i[0], # Name
                                               #float(floor(i[1]*1000)/1000), # Avg Score
                                               #i[1],
                                               int(totalDict[str(i[0])] /ceil(timeDict[i[0]]/ TIME_INTERVAL)),
                                               #float(floor(totalDict[str(i[0])]*1000)/1000),
                                               int(totalDict[str(i[0])]),
                                               floor((timeDict[str(i[0])]/1200)*100)/100
                                               #timeDict[i[0]]/TIME_INTERVAL/15
                                              ))


def calcScore(name, obj, val):
    # Scoring ruleset. Bunch of ifs.
    if obj == "jump":
        totalDict[name] = totalDict[name] + (val*.001)
        scoreDict[name] = scoreDict[name] + (val*.001) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "earnOnce template":
        totalDict[name] = totalDict[name] + 10
        scoreDict[name] = scoreDict[name] + 10
    elif obj == "junkFished": 
        totalDict[name] = totalDict[name] + (val*3)
        scoreDict[name] = scoreDict[name] + (val*3) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "animalsBred":
        totalDict[name] = totalDict[name] + (val*6)
        scoreDict[name] = scoreDict[name] + (val*6) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "climbOneCm":
        totalDict[name] = totalDict[name] + (val*.001)
        scoreDict[name] = scoreDict[name] + (val*.001) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "crouchOneCm":
        totalDict[name] = totalDict[name] + (val*.001)
        scoreDict[name] = scoreDict[name] + (val*.001) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "damageDealt":
        totalDict[name] = totalDict[name] + (val*.15)
        scoreDict[name] = scoreDict[name] + (val*.15) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "damageTaken":
        totalDict[name] = totalDict[name] - (val*.1)
        scoreDict[name] = scoreDict[name] - (val*.1) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "deaths":
        totalDict[name] = totalDict[name] - (val*5)
        scoreDict[name] = scoreDict[name] - (val*5) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "diveOneCm":
        totalDict[name] = totalDict[name] + (val*.001)
        scoreDict[name] = totalDict[name] + (val*.001) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "drop":
        pass
    elif obj == "fallOneCm":
        pass
    elif obj == "fishCaught":
        totalDict[name] = totalDict[name] + (val*2.5)
        scoreDict[name] = scoreDict[name] + (val*2.5) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "horseOneCm":
        totalDict[name] = totalDict[name] + (val*.0055)
        scoreDict[name] = scoreDict[name] + (val*.0055) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "leaveGame":
        pass
    elif obj == "minecartOneCm":
        totalDict[name] = totalDict[name] + (val*.0055)
        scoreDict[name] = scoreDict[name] + (val*.0055) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mobKills":
        pass
    elif obj == "pigOneCm":
        totalDict[name] = totalDict[name] + (val*.0055)
        scoreDict[name] = scoreDict[name] + (val*.0055) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "playerKills":
        pass
    elif obj == "sprintOneCm":
        totalDict[name] += (val*.004)
        scoreDict[name] += (val*.004) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "swimOneCm":
        totalDict[name] += (val*.004)
        scoreDict[name] += (val*.004) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "talkedToVillager":
        pass
    elif obj == "tradedWVillager":
        totalDict[name] += (val*5)
        scoreDict[name] += (val*5) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "treasureFished":
        totalDict[name] += (val*6)
        scoreDict[name] += (val*6) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "walkOneCm":
        totalDict[name] += (val*.001)
        scoreDict[name] += (val*.001) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "craftAnvil":
        totalDict[name] += (val*7)
        scoreDict[name] += (val*7) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "craftBeacon":
        totalDict[name] += (val*15)
        scoreDict[name] += (val*15) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "craftBrewStand":
        totalDict[name] += (val*5)
        scoreDict[name] += (val*5) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "craftCake":
        totalDict[name] += (val*10)
        scoreDict[name] += (val*10) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "craftJukebox":
        totalDict[name] += (val*4)
        scoreDict[name] += (val*4) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "useActivRail":
        totalDict[name] += (val*.2)
        scoreDict[name] += (val*.2) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "useComparator":
        totalDict[name] += (val*.2)
        scoreDict[name] += (val*.2) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "useDetector_Rail":
        totalDict[name] += (val*.2)
        scoreDict[name] += (val*.2) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "useDispenser":
        totalDict[name] += (val*.2)
        scoreDict[name] += (val*.2) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "useDropper":
        totalDict[name] += (val*.2)
        scoreDict[name] += (val*.2) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "useLever":
        totalDict[name] += (val*.2)
        scoreDict[name] += (val*.2) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "useNoteblock":
        totalDict[name] += (val*.2)
        scoreDict[name] += (val*.2) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "usePiston":
        totalDict[name] += (val*.2)
        scoreDict[name] += (val*.2) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "useRepeater":
        totalDict[name] += (val*.2)
        scoreDict[name] += (val*.2) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "useStone_PP":
        totalDict[name] += (val*.2)
        scoreDict[name] += (val*.2) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "useWooden_PP":
        totalDict[name] += (val*.2)
        scoreDict[name] += (val*.2) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineNetherrack":
        totalDict[name] += (val*1)
        scoreDict[name] += (val*1) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineDirt":
        totalDict[name] += (val*1)
        scoreDict[name] += (val*1) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineSand":
        totalDict[name] += (val*2)
        scoreDict[name] += (val*2) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineNether_Brick":
        totalDict[name] += (val*2)
        scoreDict[name] += (val*2) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineSandstone":
        totalDict[name] += (val*3)
        scoreDict[name] += (val*3) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineCobblestone":
        totalDict[name] += (val*3)
        scoreDict[name] += (val*3) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineStone":
        totalDict[name] += (val*4)
        scoreDict[name] += (val*4) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineMossCob":
        totalDict[name] += (val*4)
        scoreDict[name] += (val*4) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineQuartz_Ore":
        totalDict[name] += (val*5)
        scoreDict[name] += (val*5) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineIron_Ore":
        totalDict[name] += (val*6)
        scoreDict[name] += (val*6) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineGold_Ore":
        totalDict[name] += (val*7)
        scoreDict[name] += (val*7) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineRedstone_Ore":
        totalDict[name] += (val*8)
        scoreDict[name] += (val*8) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineLapis_Ore":
        totalDict[name] += (val*9)
        scoreDict[name] += (val*9) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineDiamond_Ore":
        totalDict[name] += (val*10)
        scoreDict[name] += (val*10) /ceil(timeDict[name]/TIME_INTERVAL)
    elif obj == "mineObsidian":
        totalDict[name] += (val*11)
        scoreDict[name] += (val*11) /ceil(timeDict[name]/TIME_INTERVAL)
    else:
        return 0

if __name__ == "__main__":
    main()
