# Importing random
import random

# Geohazard function

def Geohazard(word):
    dic = [
        "ACID RAIN",
        "ASTEROID CRASHING",
        "AVALANCHE",
        "BLIZZARD",
        "COLD WAVE",
        "CONTINENTAL DRIFT",
        "CYCLONE",
        "DISEASE EPIDERMIC",
        "DUST STORM",
        "DROUGHT",
        "EARTHQUAKE",
        "FLOOD",
        "GLOBAL WARMING",
        "GLACIER MELTING",
        "HAILSTORM",
        "HEAT WAVE",
        "HURRICANE",
        "ICE STORM",
        "ICEBERG MELTING",
        "IMPACT EVENT",
        "LANDSLIDE",
        "LIGHTNING",
        "LIMNIC ERUPTION",
        "METEORITE CRASHING",
        "MUDSLIDE",
        "PLAGUE",
        "QUICKSAND",
        "SAND STORM",
        "SINKHOLE",
        "THUNDER",
        "TORNADO",
        "TSUNAMI",
        "TYPHOON",
        "VOLCANIC ERUPTION",
        "WILDFIRE"
    ]

    word = random.choice(dic)

    return word