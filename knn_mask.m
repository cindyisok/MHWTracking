load('./OI_SST/data/mask_yr/mask_00_09.mat')
path = './OI_SST/data/knn_train/';
%ppl = parpool(4);
for k = 1:3653
    features_train = zeros(1440*720,2);
    for i = 1:1440
        for j = 1:720
            features_train(720*(i-1)+1:720*i,1) = i;
            features_train(720*(i-1)+j,2) = j;
        end
    end
    mask_trans = mask_00_09(:,:,k)';
    labels_train = mask_trans(:);
    save([path,'features_train',num2str(k+6574),'.mat'],'features_train');
    save([path,'labels_train',num2str(k+6574),'.mat'],'labels_train');
    disp(k)
end
%delete(ppl);



