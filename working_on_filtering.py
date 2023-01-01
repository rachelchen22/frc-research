
# dict1= "Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, District of Columbia, Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina, South Dakota, Tennessee, Utah, Vermont, Virginia, Washington, West Virginia, Wisconsin, Wyoming"
dict1 = "Michigan"
# num_lines = sum(1 for line in open('state.txt'))
filteredTeams = open('filteredTeams.txt', 'w', encoding='utf-8')
filteredNums = open('filteredNums.txt', 'w', encoding='utf-8')
filteredCity = open('filteredcity.txt', 'w', encoding='utf-8')
filteredState = open('filteredstate.txt', 'w', encoding='utf-8')
teams = open("nameandnum.txt", "r", encoding='utf-8')
city = open("city.txt", "r", encoding='utf-8')
num = open("num.txt", "r", encoding='utf-8')
state = open("state.txt", "r", encoding='utf-8') # change names file to the location file eventually, r means read only
# make sure locations match up to the names/numbers

for (line, line2, line3, line4) in zip(state, city, teams, num):
   bark = line.strip()
   bark2 = line2.strip()
   bark3 = line3.strip()
   bark4 = line4.strip()
   # print(bark)

   if bark in dict1:
     # for line2 in city:
         filteredState.write(bark + "\n")
         filteredCity.write(bark2 + "\n")
         filteredTeams.write(bark3 + "\n")
         filteredNums.write(bark4 + "\n")

state.close()
city.close()
teams.close()
filteredState.close()
filteredCity.close()
filteredTeams.close()
filteredNums.close()