# MHWTracking
Welcome to our spatio-temporal MHW tracking procedure !


This free package is organized by :

1.Detect MHWs using previous definition by Hobday et al., 2016 (detect.m and main.m);

2.Tranfer the MHWs to masks (mask.m);

3.Make KNN labels and the KNN algorithm (knn_mask.m and knn_test.py);

4.Remove the land, discard the small regions and find the connectivity (conn.m);

5.The tracking procedure (mhw_overlap_tracks.m).

# Reference
Sun, D., Jing, Z., Li, F., & Wu, L. (2023). Characterizing global marine heatwaves under a spatio-temporal framework. Progress in Oceanography, 211, 102947.