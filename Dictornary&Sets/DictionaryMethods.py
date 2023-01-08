myDic={"Fast":"fastest",
"harry":"person"
,"marks":[1,2,4,5,6],
"luluDic":{"image":"photo","bottle":"paani"},
1:2
}

print(type(myDic.keys())) # by default the type of dictionary is dict

print(list(myDic.keys())) #it converts the type of the dictionary
 
print(myDic.values()) #it prints the values of all keys

print(myDic.items()) #it prints the key as well as their value 

print(myDic)

update={"samsung":"phone","Apple":"phone","oneplus":"phone","a":[123,123,234,34,213],"Fast":"superFast"} # this will also update the old key value to the new value for the same key
myDic.update(update) #update the dictionary by adding key value pairs from update
print(myDic)


# this will both return the value for their corresponding value but if the key is not present in the dictionary then square bracket will give error but .get method doesn't show any error it return null because if we use sqaure bracket for finding the value of the key then its our responsibilty that particular key is present in the dictionary 
print(myDic.get("Fast2"))
# print(myDic["Fast2"])
