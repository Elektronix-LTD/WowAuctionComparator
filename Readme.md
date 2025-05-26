Wow Auction Comprator Tool

# INTRODUCTION

This World Of Warcraft specific tool allows to compare prices of the given item among many realms.


# USAGE

Syntax for running this amazing magic command:

    python .\WowAuctionComparator.py "Green Lumberjack Shirt" 5

Where 5 is OPTIONAL and it can be any number to limit number of realms to check (if You are impatient and You don't want to wait ages till script will finish checking all 267 realms ;-)


# EXAMPLE OUTPUT

Here is example output and usage:

    PS C:\Users\lukas\Desktop\WowAuctionComparator> python .\WowAuctionComparator.py "Green Lumberjack Shirt" 5
    Comparing prices for: Green Lumberjack Shirt
    Limiting number of realms to: 5
    Checking prices in following 'eu' realms:
    ['aegwynn', 'aerie-peak', 'agamaggan', 'aggra-portugues', 'aggramar']
    Checking prices of the item in realm aegwynn...
    Checking prices of the item in realm aerie-peak...
    Checking prices of the item in realm agamaggan...
    Checking prices of the item in realm aggra-portugues...
    Checking prices of the item in realm aggramar...
    Finished checking prices of the item in realm aegwynn...
    Finished checking prices of the item in realm aggramar...
    Finished checking prices of the item in realm agamaggan...
    Finished checking prices of the item in realm aerie-peak...
    Finished checking prices of the item in realm aggra-portugues...
    ----------------------------------------------------------------------------

          _____                 _ _
         |  __ \               | | |
         | |__) |___  ___ _   _| | |_ ___
         |  _  // _ \/ __| | | | | __/ __|
         | | \ \  __/\__ \ |_| | | |_\____
         |_|  \_\___||___/\__,_|_|\__|___/


    Lowest prices found for the item 'Green%20Lumberjack%20Shirt' among all (5) requested realms:
    {
      "Green Lumberjack Shirt": {
        "item_name": "Green Lumberjack Shirt",
        "link": "http://www.wowhead.com/item=41250",
        "realm": "aerie-peak",
        "item_price": {
          "gold": 1221,
          "silver": 87,
          "copper": 0
        }
      },
      "Pattern: Green Lumberjack Shirt": {
        "item_name": "Pattern: Green Lumberjack Shirt",
        "link": "http://www.wowhead.com/item=42175",
        "realm": "aggra-portugu\u00eas",
        "item_price": {
          "gold": 60000,
          "silver": 0,
          "copper": 0
        }
      }
    }