import numpy as np
import scipy.io as io
from sklearn.neighbors import KNeighborsClassifier

for i in range(1,12785):
    
    x = io.loadmat('./features_train' + str(i) + '.mat')
    x = x['features_train']
    x_train = x / 4 - 0.125
    x_train[:, 0] = x_train[:, 0] - 90
    x_train = x_train / 180 * 3.14159
    
    y_train = io.loadmat('./labels_train' + str(i) + '.mat')
    y_train = y_train['labels_train']

    knn = KNeighborsClassifier(n_neighbors=21*21,metric='haversine')
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_train)

    y_pred = np.array(y_pred)
    mask_new = y_pred.reshape(1440,720)
    io.savemat('./mask' + str(i) + '.mat', {'mask_new':mask_new})
    print(i)
    
'''
plt.figure(figsize=(10, 10))
m = Basemap(projection='robin',lon_0=-180)
m.drawparallels(np.arange(-90.,120.,30.), labels = [1, 0, 0, 0],fontsize=14,linewidth='0.2',color='black')
m.drawmeridians(np.arange(0.,360.,60.), labels = [0, 0, 0, 1],fontsize=14,linewidth='0.2',color='black')
m.drawcoastlines()
m.drawmapboundary()
m.fillcontinents(color='k')
lon = np.linspace(0.125, 359.875, 1440)
lat = np.linspace(-89.875, 89.875, 720)
lons, lats = np.meshgrid(lon, lat)
x, y = m(lons, lats)
datamap = m.pcolormesh(x, y, mask_new.T, vmin = 0, vmax = 1, cmap='bwr')
m.colorbar(datamap)
plt.title('2014-01-13',fontsize=20)
plt.show()
'''


