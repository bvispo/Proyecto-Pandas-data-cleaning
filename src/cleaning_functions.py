import pandas as pd
import numpy as np
from numpy import nan
import re

#Cleaning Variable Activity:

def clean_activity(string):
    """
    This function cleans the variable Activity.
    Args:
        - Strings on variable Activity
    Returns:
    - Returns all the new categories in the variable Activity after implemented a regrex patron on them.

    """

    if(re.search(r'\bsurf|paddle|windsurf|body|boogie|skim',string, re.IGNORECASE) != None):
        return "Surf"
    elif(re.search(r'\bpulling|cleaning|spear|washing|crayfish|fish|lobster|hunting|catching',string, re.IGNORECASE) != None):
        return "Fishing"
    elif(re.search(r'\bwaist|knee-deep|bathing|swim|float|free|wading',string, re.IGNORECASE) != None):
        return "Free Swimming/Diving"
    elif(re.search(r'\bfreighter|boat|sank|overboard|wreck|ferry|sunk|sink|founde|submarine|adrift',string, re.IGNORECASE) != None):
        return "Sea Disaster"
    elif(re.search(r'\bskiing|kayak|rowing|canoe|play|board|photographing|snorkeling|filming|dive|diving|scuba|cage',string, re.IGNORECASE) != None):
        return "Water Sports"
    elif(re.search(r'\bsail|yacht|crew',string, re.IGNORECASE) != None):
        return "Sailing"
    elif(re.search(r'\bcrashed|air|plane',string, re.IGNORECASE) != None):
        return "Plane Crash"
    elif(re.search(r'\bshark|feeding|hand|touch|bitt',string, re.IGNORECASE) != None):
        return "Interaction with sharks"
    elif(re.search(r'\binto|fell',string, re.IGNORECASE) != None):
        return "Felt into the sea"
    else:
        return "Other"


# Cleaning Variable Country:
"""
    This function cleans the variable Country:
    Arggs:
    - Strings in variable Year.
    Returns:
        a) List of continents where the countries in the string given where found.
        b) Unknown if the country is not found in any continen list given.
"""
def clean_country(string):
    
    
    Africa = ["AFRICA","ALGERIA","ANGOLA","BENIN","BOTSWANA","BURKINA FASO", "BURUNDI","CAPE VERDE",
          "CAMEROON", "CENTRAL AFRICAN REPUBLIC","CHAD","COMOROS","CONGO",
          "DEMOCRATIC REPUBLIC OF THE","CONGO, REPUBLIC OF THE","COTE D'IVOIRE",
          "DJIBOUTI","EGYPT","EQUATORIAL GUINEA","ERITREA","ESWATINI","ETHIOPIA",
          "GABON","GAMBIA","GHANA","GUINEA","GUINEA-BISSAU","KENYA","LESOTHO","LIBERIA",
          "LIBYA","MADAGASCAR","MALAWI","MALI","MAURITANIA","MAURITIUS","MOROCCO","MOZAMBIQUE",
          "NAMIBIA","NIGER","NIGERIA","RWANDA","SAO TOME AND PRINCIPE","SENEGAL","SEYCHELLES",
          "SIERRA LEONE","SOMALIA", "SOUTH AFRICA","SOUTH SUDAN","SUDAN","TANZANIA","TOGO",
          "TUNISIA","UGANDA","ZAMBIA","ZIMBABWE",]

    Asia = ["ASIA","AFGHANISTAN","ARMENIA","AZERBAIJAN","BAHRAIN","BANGLADESH","BHUTAN","BRUNEI",
            "CAMBODIA","CHINA","CYPRUS","EAST TIMOR","EGYPT","GEORGIA","INDIA","INDONESIA","IRAN",
            "IRAQ","ISRAEL","JAPAN","JORDAN","KAZAKHSTAN","KUWAIT","KYRGYZSTAN","LAOS","LEBANON",
            "MALAYSIA","MALDIVES","MONGOLIA","MYANMAR","NEPAL","NORTH KOREA","OMAN","PAKISTAN",
            "PALESTINE","PHILIPPINES","QATAR","RUSSIA","SAUDI ARABIA","SINGAPORE","SOUTH KOREA",
            "SRI LANKA","SYRIA","TAIWAN","TAJIKISTAN","THAILAND","TURKEY","TURKMENISTAN",
            "UNITED ARAB EMIRATES","UZBEKISTAN","VIETNAM","YEMEN"]

    Oceania = ["OCEANIA","AUSTRALIA", "FIJI", "KIRIBATI", "MARSHALL ISLANDS","MICRONESIA","NAURU",
               "NEW ZEALAND", "PALAU","PAPUA NEW GUINEA","SAMOA","SOLOMON ISLANDS",
               "TONGA","TUVALU","VANUATU"]

    Europe = ["EUROPE","ALBANIA","ANDORRA","ARMENIA","AUSTRIA","AZERBAIJAN","BELARUS","BELGIUM",
              "BOSNIA AND HERZEGOVINA", "BULGARIA","CROATIA","CYPRUS","CZECHIA","DENMARK",
              "ESTONIA","FINLAND","FRANCE","GEORGIA","GERMANY","GREECE","HUNGARY","ICELAND",
              "IRELAND","ITALY","KAZAKHSTAN","KOSOVO","LATVIA","LIECHTENSTEIN","LITHUANIA",
              "LUXEMBOURG","MALTA","MOLDOVA","MONACO","MONTENEGRO","NETHERLANDS","NORTH MACEDONIA",
              "NORWAY","POLAND","PORTUGAL","ROMANIA","RUSSIA","SAN MARINO","SERBIA","SLOVAKIA",
              "SLOVENIA","SPAIN","SWEDEN","SWITZERLAND","TURKEY","UKRAINE","UNITED KINGDOM",
              "VATICAN CITY"]

    North_America = ["NORTH AMERICA","ANTIGUA AND BARBUDA", "BAHAMAS", "BARBADOS", "BELIZE", "CANADA", 
                     "COSTA RICA","CUBA", "DOMINICA", "DOMINICAN REPUBLIC", "EL SALVADOR",
                     "GRENADA", "GUATEMALA", "HAITI", "HONDURAS", "JAMAICA", "MEXICO",
                     "NICARAGUA", "PANAMA", "SAINT KITTS AND NEVIS","SAINT LUCIA",
                     "SAINT VINCENT AND THE GRENADINES", "TRINIDAD AND TOBAGO",
                     "USA"]

    South_America = ["SOUTH AMERICA","ARGENTINA","BOLIVIA","BRAZIL","CHILE","COLOMBIA","ECUADOR","GUYANA"
                     ,"PARAGUAY","PERU","SURINAME","URUGUAY","VENEZUELA"]
    
    string = string.upper().strip()

    if string in Africa:
        return "Africa"
    elif string in Asia:
        return "Asia"
    elif string in Europe:
        return "Europe"
    elif string in Oceania:
        return "Oceania"
    elif string in North_America:
        return "North America"
    elif string in South_America:
        return "South America"
    elif re.search(r'\bsea|ocean|isl', string, re.IGNORECASE) is not None:
        return "Unknown"
    else:
        return "Unknown"


#Cleaning Variable Age:

def clean_age(string):
    """
    This function cleans the variable Age:
    Arggs:
    - Strings in variable Year.
    Returns:
        a) Unknown for all the strings starting by teen, middle, etc., or specific values.
        b) Only those existing digits with two values in the strings.
    """
    try:
        string = string.split(" ")[0]
        if(re.search(r'\bteen|middle|adult|elderly|make|young|mid ',string, re.IGNORECASE) != None):
            return "Unknown"
        elif(re.search(r'\bBoth|F|A.M.|Ca.|X|\W\w+|\W',string, re.IGNORECASE) != None):
            return "Unknown"    
        else:
            age = re.search(r'\d{1,2}', string)
            return age.group()
    except: 
        return string


#Cleaning Variable Year:

def clean_year(x):
    """
    This function transforms floar types in the variable Year, to integrers:
    Arggs:
    - Float year in variable Year
    Returns:
        a)If year is nan, then return "Unknown"
        b)If year is not nan, and it is samaller than year 1543, then return the integrer of the year.
    """

    if np.isnan(x) == True:
        return "Unknown"
    else:
        if int(x) <=1543:
            return "Unknown"
        else:
            return int(x)
