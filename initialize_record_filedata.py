import tbapy
# the blue alliance requires an auth key to access the api, even though this library
key = 'U3Kav5lMFPMZRvMP5HLYxcqoXxu0NOJtAxSSMyy4ulOqXKjLisw58CqMuxcurw2e'
tba = tbapy.TBA(key)

# simple is just for "simplified" data
# simple = True

# opening files
indTeamNums = open('indiana nums.txt')
indPostal = open('indPostal.txt', 'w', encoding='utf-8')

for line in indTeamNums:
    bark = line.strip()
    x= tba.team(int(bark))
    indPostal.write((x.postal_code) + "\n")

indTeamNums.close()
indPostal.close()