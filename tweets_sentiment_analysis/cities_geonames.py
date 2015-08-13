class City:
	def __init__(self, geonameid, name, latitude, longitude, country_code, population, elevation, timezone):
		self.geonameid=geonameid
		self.name=name
		self.latitude=latitude
		self.longitude=longitude
		self.country_code=country_code
		self.population=population
		self.elevation=elevation
		self.timezone=timezone
		
cities_file = open('data/cities1000.txt', 'r')
cities_out = open('output/cities_formatted.csv', 'a')

for c in cities_file:
	city = c.rsplit('\t', 19) #19 colums (see http://download.geonames.org/export/dump/)
	new_city = City(city[0], city[1], city[4], city[5], city[8], city[14], city[15], city[17])
	cities_out.write(new_city.geonameid + ',' + new_city.name + ',' + new_city.latitude + ',' + new_city.longitude + ',' + new_city.country_code + ',' + new_city.population + ',' + new_city.elevation + ',' + new_city.timezone + '\n')

cities_file.close()
cities_out.close()
