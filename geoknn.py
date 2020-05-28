import numpy as np
from sklearn.neighbors import NearestNeighbors
      
lat= 42.86792753758858
lng= -84.59592787480472
#here we can trend own model with all Location
allLocation=np.array([item.Latitude,item.Longitude] for item in traffic)
#n_neighbors give the number of output locations
knn = NearestNeighbors(n_neighbors=5)
knn.fit(allLocation)
distances, indices = knn.kneighbors([[float(lat),float(lng)]])

import numpy as np
from sklearn.neighbors import NearestNeighbors
from Traffics.models import*
traffic=TrafficAnalysis.objects.filter(state_code='MI')
allLocation=np.array([[float(item.Latitude),float(item.Longitude)] for item in traffic])
knn=NearestNeighbors(n_neighbors=5)
allLocation=np.array([[float(item.Latitude),float(item.Longitude)] for item in traffic])
knn.fit(allLocation)


      
    
