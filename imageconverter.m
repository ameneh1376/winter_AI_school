ds = datastore('voice.csv','TreatAsMissing','NA');
m=zeros(1,20);
ds.ReadSize =1;
ext = '.png';
 format long
for i=1586:3168
  T = read(ds);
  m=T(:,1:20);    
  n=table2array(m);
   s=num2str(i-1585);
   filename = [s,ext];
   l=mat2gray(n,[0  max(n)]);
   imwrite(l,filename);
end   


    