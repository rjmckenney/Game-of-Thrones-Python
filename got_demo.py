from pprint import pprint
from characters import characters



#count = 0
#for character in characters:
#    if character['name'].startswith('A') == True:
#        pprint(character['name'])
#        count +=1
#pprint(count)        

#count = 0
#for character in characters:
#    if character['name'].startswith('Z') == True:
#        pprint(character['name'])
#        count +=1
#pprint(count)        

# this counts how many people died
count = 0 
for character in characters:
    if character['died'] == "":
        count +=1
print (count)
 
#who has the most titles
count = 0
for character in characters:
    if character["titles"] ==  [""]:
        count +=1
print (count)     


#how many people are Valyrian
#"culture" ""
count = 0
for character in characters:
    if character ["culture"] ==  "Valyrian":
        count += 1
print(count)        



# print(len(characters))

# # print out the key names individually
# for k in jon_snow:
#    print(k)

# # print out just the values
# for key in jon_snow:
#    print(jon_snow[key])

# # print both the key and the value
# for k in characters.jon_snow:
#    print("%s: %s" % (k, jon_snow[k]))