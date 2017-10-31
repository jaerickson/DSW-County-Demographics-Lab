import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))
    print(your_interesting_demographic_function(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first = counties[0]["County"]
    for c in counties:
        if c["County"] < first:
            first = c["County"]
    return first
def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    s = counties[0]["State"]
    d = counties[0]["County"]
    most_under_18 = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > most_under_18:
            most_under_18 = c["Age"]["Percent Under 18 Years"]
            s = c["State"]
            d = c["County"]
    return d +" "+ s
    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    most_under_18 = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > most_under_18:
            most_under_18 = c["Age"]["Percent Under 18 Years"]
    return most_under_18
    
def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    s = counties[0]["State"]
    d = counties[0]["County"]
    most_under_18 = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > most_under_18:
            most_under_18 = c["Age"]["Percent Under 18 Years"]
            s = c["State"]
            d = c["County"]
    return d +" "+ s +" "+ str(most_under_18)
    
def state_with_most_counties(counties):    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    state = {}
    for c in counties:
        if c["State"] in state:
            state[c["State"]]+=1
        else:
            state[c["State"]]=1
    #print(state)    
    #Find the state in the dictionary with the most counties
    most_counties = state["AK"]
    d = 'AK'
    for s in state:
        if state[s] > most_counties:
            most_counties= state[s]
            d = s
    return d
     
        
    #Return the state with the most counties
    
    
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    s = counties[0]["State"]
    d = counties[0]["County"]
    most_women_owned = counties[0]["Employment"]["Firms"]["Women-Owned"]
    for c in counties:
        if c["Employment"]["Firms"]["Women-Owned"] > most_women_owned:
            most_women_owned = c["Employment"]["Firms"]["Women-Owned"]
            s = c["State"]
            d = c["County"]
    return s +" "+ d +" "+ str(most_women_owned) +"% women owned"
   
if __name__ == '__main__':
    main()
