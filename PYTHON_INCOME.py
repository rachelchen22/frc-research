from uszipcode import SearchEngine, SimpleZipcode, ComprehensiveZipcode

# open files

postal = open('testingpostal.txt', 'r')
income = open('testingAGAIN.txt', 'w', encoding='utf-8')

search = SearchEngine()
for line in postal:
    bark = line.strip()
    z = search.by_zipcode(int(bark))
    income.write(str(z.median_household_income) + "\n")






postal.close()
income.close()