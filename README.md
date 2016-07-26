# StEVE - A Static Data Access API for EVE Online

StEVE is intended to ease the development for EVE Online and it's Static Data 
Export (SDE). StEVE provides a high-level API to access the SDE data without 
having to know much about the data is structured internally.

## Installation

1- Install the dependencies:

    appdirs
    sqlite3

Additional dependencies:

    ...    

2- Download the source code: 

    git clone https://github.com/PageArkanis/StEVE

3- build and install:

    cd StEVE
    python setup.py install


## Running StEVE

First time StEVE is imported it will fetch the SDE from https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite. 
Afterwards it will only fetch a new version once its available but will check 
for it every time a program is started. Without an Internet connection it will
throw a warning but will continue to work.

## Examples


    from steve import Assets, Universe
    
    # print Tritanium ID
    print Assets.type['Tritanium'].uid

    # print Name for ID 34
    print Assets.type[34].name

    # print Jita ID
    print Universe.system['Jita'].uid

    # print System Name for ID 
    print Universe.system[30000142].name



Happy hacking!

## License

See [COPYING](https://github.com/PageArkanis/StEVE/COPYING) for licensing info.
