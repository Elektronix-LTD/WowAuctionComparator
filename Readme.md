# Wow Auction Comprator Tool

## Introduction

This World Of Warcraft specific tool allows to compare prices of the given item among many realms.

## Preparation to run

Script uses PlayWright library to fetch the data.
To install all needed requirements please go to the directory with the WowAuctionComparator.py tool and run following command:

    python -m pip install -r requirements.txt

After that PlayWright library needs also to install its dependences, so please run this command to install all necessary components needed by PlayWright

    playwright install
    

## Command usage

> [!IMPORTANT]  
> Please run it from Windows PowerShell. GitBash terminal has some difficulties which are currently not resolved.

Syntax for running this amazing magic command:

    python WowAuctionComparator.py "Green Lumberjack Shirt" 5

Where 5 is OPTIONAL and it can be any number to limit number of realms to check (if You are impatient and You don't want to wait ages till script will finish checking all 267 realms ;-)


## Example output

Here is example output and usage:

    PS C:\WowAuctionComparator> python .\WowAuctionComparator.py "Green Lumberjack Shirt" 15
    Comparing prices for: Green Lumberjack Shirt
    Limiting number of realms to: 15
    Checking prices in following 'eu' realms:
    ['aegwynn', 'aerie-peak', 'agamaggan', 'aggra-português', 'aggramar', 'ahnqiraj', 'alakir', 'alexstrasza', 'alleria', 'alonsus', 'amanthul', 'ambossar', 'anachronos', 'anetheron', 'antonidas']
    Checking prices of the item in realm aegwynn...
    Checking prices of the item in realm aerie-peak...
    Checking prices of the item in realm agamaggan...
    Checking prices of the item in realm aggra-português...
    Checking prices of the item in realm aggramar...
    Checking prices of the item in realm ahnqiraj...
    Checking prices of the item in realm alakir...
    Checking prices of the item in realm alexstrasza...
    Checking prices of the item in realm alleria...
    Checking prices of the item in realm alonsus...
    Finished checking prices of the item in realm aegwynn...
    Finished checking prices of the item in realm agamaggan...
    Checking prices of the item in realm amanthul...
    Checking prices of the item in realm ambossar...
    Finished checking prices of the item in realm ahnqiraj...
    Finished checking prices of the item in realm alleria...
    Checking prices of the item in realm anachronos...
    Checking prices of the item in realm anetheron...
    Finished checking prices of the item in realm alakir...
    Finished checking prices of the item in realm alonsus...
    Finished checking prices of the item in realm alexstrasza...
    Finished checking prices of the item in realm aggramar...
    Checking prices of the item in realm antonidas...
    Finished checking prices of the item in realm aggra-português...
    Finished checking prices of the item in realm aerie-peak...
    Finished checking prices of the item in realm amanthul...
    Finished checking prices of the item in realm ambossar...
    Finished checking prices of the item in realm anetheron...
    Finished checking prices of the item in realm anachronos...
    Finished checking prices of the item in realm antonidas...
    ----------------------------------------------------------------------------
    
          _____                 _ _
         |  __ \               | | |
         | |__) |___  ___ _   _| | |_ ___
         |  _  // _ \/ __| | | | | __/ __|
         | | \ \  __/\__ \ |_| | | |_\____
         |_|  \_\___||___/\__,_|_|\__|___/
    
    
    Lowest prices found for the item 'Green%20Lumberjack%20Shirt' among all (15) requested realms:
    {
      "Green Lumberjack Shirt": {
        "item_name": "Green Lumberjack Shirt",
        "link": "http://www.wowhead.com/item=41250",
        "realm": "alakir",
        "item_price": {
          "gold": 390,
          "silver": 89,
          "copper": 0
        }
      },
      "Pattern: Green Lumberjack Shirt": {
        "item_name": "Pattern: Green Lumberjack Shirt",
        "link": "http://www.wowhead.com/item=42175",
        "realm": "antonidas",
        "item_price": {
          "gold": 15600,
          "silver": 75,
          "copper": 0
        }
      }
    }