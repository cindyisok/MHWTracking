# MHWTracking
This is for three-dimension MHW tracking procedure.

The flow of this free package is organized by :
①Detect MHWs using previous definition by Hobday et al., 2016 (detect.m and main.m);
②Tranfer the results MHWs to masks (mask.m);
③Make KNN labels (knn_mask.m);
④The KNN algorithm (knn_test.py);
⑤Find the connectivity (conn.m);
⑥The tracking procedure (mhw_overlap_tracks.m).
