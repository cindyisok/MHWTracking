load('./OI_SST/code/logs/logs1/MHW.mat')
%MHWs_tmp = struct('day',{},'xloc',{},'yloc',{});
MHWs = struct('order',{},'day',{}, 'xloc',{},'yloc',{}); 

%count = 0; 
mask_daily = zeros(360,120,2921+1);
d = 0;

mhw = table2array(MHW);
mhw(:,1) = datenum(num2str(mhw(:,1)),'yyyymmdd');
mhw(:,2) = datenum(num2str(mhw(:,2)),'yyyymmdd');

for day_i = datenum(1982,1,1):datenum(1989,12,31)
    d = d+1;
    search_day = day_i;
    mask = zeros(360,120);
    
    for i = 1:length(mhw)
        start_day = mhw(i,1);
        end_day = mhw(i,2);
        
        [in,loc] = ismember(search_day,start_day:end_day); 

        if in==1
 %           count = count + 1;

%            MHWs_tmp(count).day = str2num(datestr(search_day,'YYYYmmdd'));
%            MHWs_tmp(count).xloc = mhw(i,8);
%            MHWs_tmp(count).yloc = mhw(i,9);
            mask(mhw(i,8),mhw(i,9)) = 1; % 
        end
    end
    mask_daily(:,:,d) = mask;
    disp(d)
end

save('./OI_SST/code/masks/mask1_1.mat','mask_daily','-v7.3')
