def clean_year(years):
    for i in year:
        if i< 1543:
            i == "nan"
    return years















def limpiar_activity(list):  
    
    for string in list:

        if(re.search(r'\b(surf|paddle)',string, re.IGNORECASE) != None):
            return "surf"
        elif(re.search(r'\bpulling|cleaning|spear|washing|crayfish|fishing',string, re.IGNORECASE) != None):
            return "fishing"
        elif(re.search(r'\bphotographing|snorkeling|filming|dive|diving|scuba|diving|feeding',string, re.IGNORECASE) != None):
            return "diving"
        elif(re.search(r'\bwaist|knee-deep|bathing|swim',string, re.IGNORECASE) != None):
            return "swimming"
        elif(re.search(r'\bfreighter|boat|sank|overboard|wreck',string, re.IGNORECASE) != None):
            return "boat accident"
        elif(re.search(r'\bskiing|kayak|rowing|canoe',string, re.IGNORECASE) != None):
            return "water sports"
        elif(re.search(r'\bsailing|yacht',string, re.IGNORECASE) != None):
            return "sailing"
        elif(re.search(r'\bcrashed|aircraft',string, re.IGNORECASE) != None):
            return "plane crash"
        else:
            return "Other"