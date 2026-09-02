team_data={

"team1": {"name": "adi", "job": "cricketer", "passion": "cricket,art"},

"team2": {"name": "kush", "job": "footballer", "passion": "cricket, fortnite"},

"team3": {"name": "azaan", "job": "basketballer", "passion": "sports,arabic"}, 

"team4": {"name": "kush", "job": "footballer", "passion": "cricket, fortnite"},
}
result={}
seen_keys=[]
for team ,details in team_data.items():
    unique_key=(details["name"],details["job"],details["passion"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[team]=details
for k,v in result.items():
    print(k,":",v)
