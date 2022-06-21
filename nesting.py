capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
#print(travel_log)
'''for country, cities_list in travel_log.items():
	print(country)
	for cities in cities_list:
		print(cities)'''
#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

'''for key, value in travel_log.items():
	print(f'{key}: ')
	for key,val in value.items():
		print(key,val)'''
#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]
'''for index, item in enumerate(travel_log):
	#print(index,item)
	for key,value in travel_log[index].items():
		print(key,value)'''
order = {
	"starter": {1:"Salad", 2:"Soup"},
	"main": {1:['Burger', 'Fries'], 2: ["Steak"]},
	"dessert": {1:['Ice Cream'], 2:[]},
}

print(order["main"][2][0])
