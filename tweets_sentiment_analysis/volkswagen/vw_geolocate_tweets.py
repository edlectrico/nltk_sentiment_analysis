import pandas as pd
import sys

# import language_detector as lang_detector

# Input DataFrames
vw_original = pd.read_csv('output/vw_clean_en_rechecked.csv')
locations = pd.read_csv('../data/cities_geo.csv')

vw = pd.DataFrame(data=vw_original)
cities = pd.DataFrame(data=locations)
# Output DataFrame
vw_geo = pd.DataFrame(columns=['id', 'latitude', 'longitude'])

for c_index, c_row in cities.iterrows():
  try:
    city = str(c_row['city']).lower().replace(" ", "") # cities may be written in a different way in each dataset
    print city
    for vw_index, vw_row in vw.iterrows():
      if city in str(vw_row['location']).lower().replace(" ", ""):
        print 'FOUND!\n'
	# Now we append a new line to the output DataFrame containing
	# the tweet id for future JOINS and the coordinates of the tweet
        vw_geo = vw_geo.append({'id':str(vw_row['id']), 
			'latitude':c_row['lat'], 
			'longitude':c_row['lon']}, 
			ignore_index=True)

  except KeyboardInterrupt:
    print 'KeyboradInterrupt exception raised: Generating out file...'
    # print 'Writing to file'
    vw_geo.to_csv('output/vw_clean_en_geo.csv')
    sys.exit()

print 'Writing to file'
vw_geo.to_csv('output/vw_clean_en_geo.csv')
