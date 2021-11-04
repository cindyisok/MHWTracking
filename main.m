% Load NOAA OI SST V2 data
sst_full=NaN(90*4,30*4,datenum(2020,12,31)-datenum(1982,1,1)+1);
for i=1982:2020
    file_here=['./OI_SST/data/sst/sst.day.mean.' num2str(i) '.nc' ];
    data_here=ncread(file_here,'sst');
    data_here=data_here(1:360,1:120,:);
    sst_full(:,:,(datenum(i,1,1):datenum(i,12,31))-datenum(1982,1,1)+1)=data_here;
    disp(i)
end
sst_full(sst_full<-10000)=nan;

[MHW,mclim,m90,mhw_ts]=detect(sst_full,datenum(1982,1,1):datenum(2020,12,31),datenum(1982,1,1),datenum(2011,12,31),datenum(1982,1,1),datenum(2020,12,31));
disp('saving')
save('./OI_SST/code/logs/logs1/mclim.mat','mclim');
save('./OI_SST/code/logs/logs1/MHW.mat','MHW');
