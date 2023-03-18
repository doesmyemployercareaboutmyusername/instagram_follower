import pathlib
import json

# Open and read .json file with people that follow me
print(str(pathlib.Path().resolve()))
with open(str(pathlib.Path().resolve()) + "\\followers_1.json","r", encoding='utf-8') as followers:
# Decode .json file into python object (https://realpython.com/python-json)
    followers_json = json.load(followers)
    length_followers_json = len(followers_json)
    count_1 = 0
    followers_list = []
    while(count_1 < length_followers_json):
        tmp = followers_json[count_1]['string_list_data'][0]['value']
        followers_list.append(tmp)
        count_1 += 1
#print(followers_list)
    
# Open, read and decode .json file with people that I follow
with open(str(pathlib.Path().resolve()) + "\\following.json","r", encoding='utf-8') as following:
    following_json = json.load(following)
    length_following_json = len(following_json['relationships_following'])
    count_2 = 0
    following_list = []
    while(count_2 < length_following_json):
        tmp = following_json['relationships_following'][count_2]['string_list_data'][0]['value']
        following_list.append(tmp)
        count_2 += 1
#print(following_list)

# Compare 'values' of 'followers' and 'following' and print the people that do now follow you back
new_list = list(set(following_list).difference(followers_list))
print(new_list)
