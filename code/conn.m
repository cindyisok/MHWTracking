%% mask to MHWs
MHWs = struct('day',{}, 'xloc',{},'yloc',{}); 

mask_daily = mask;
for i = 1:length(mask_daily(1,1,:))
    count = 0;
    mask = mask_daily(:,:,i);
    D = bwconncomp(mask,8); 
    for j = 1:D.NumObjects

    [x,y] = ind2sub([1440,720],D.PixelIdxList{j});
        if length(x)>=21*21
            count = count + 1;
            MHWs(i).yloc{count,1} = single(y);
            MHWs(i).xloc{count,1} = single(x);
            MHWs(i).day = i;
        end
    end
    disp(i)
end
           
           
           
           