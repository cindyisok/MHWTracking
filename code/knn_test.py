import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.colors import LinearSegmentedColormap
import scipy.io as io
from sklearn.neighbors import KNeighborsClassifier
#from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid
#from sklearn.metrics import classification_report

for i in range(11991,11992):
    
    x = io.loadmat('./OI_SST/data/knn_train/features_train' + str(i) + '.mat')
    x = x['features_train']
    x_train = x / 4 - 0.125
    x_train[:, 0] = x_train[:, 0] - 90
    x_train = x_train / 180 * 3.14159
    
    y_train = io.loadmat('./OI_SST/data/knn_train/labels_train' + str(i) + '.mat')
    y_train = y_train['labels_train']
    # x_test = io.loadmat('F:/study/heatwave/data/knn/features_test.mat')
    # x_test = x_test['features_test']


    knn = KNeighborsClassifier(n_neighbors=9*9,metric='haversine')
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_train)

    # maxa = sum(y_pred)
    y_pred = np.array(y_pred)
    mask_new = y_pred.reshape(1440,720)
    #mask_new = np.where(mask_new,mask_new,np.nan)
    io.savemat('./OI_SST/data/knn_sensitivity/mask' + str(i) + '.mat', {'mask_new':mask_new})
    print(i)
    
'''
plt.figure(figsize=(10, 10))
# m=Basemap(llcrnrlat=-90, urcrnrlat=90,llcrnrlon=0,urcrnrlon=360,resolution='c')
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
# io.savemat('F:/study/heatwave/data/knn/labels_test140110.mat', {'labels_test':y_pred})
'''


