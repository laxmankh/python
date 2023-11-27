import math
#create one list 
x=[23,33,45,64,76,11,45]
y=[22,17,41,63,16,21,45]
count=0
total=0
for i in x:
	total=total+i
	count=count+1
#print mean of the following 
mean=total/count
print("the mean of the given data:",mean)

#find the median of gien data
x.sort()
print(x)
mid=int(count/2)
if(count%2==0):
	median=float((x[mid]/2+ x[mid-1]/2))
	
else:
	median=x[mid]	
print("the Median of given data:",median)

#variance of gievn data
var=0
for i in x:
	ans=pow((mean-i),2)
	var=var+ans;
print("variance:",var)

#standarad deviatrion of data
sd=math.sqrt(var)
print("Standard D:",sd)

#corelation of data
c1=0
c2=0
sqx=0
sqy=0
xy=0
for i in x:
	c1=c1+i
	sqx=sqx+pow(i,2)
for i in y:
	c2=c2+i
	sqy=sqy+pow(i,2)
	
for i in range(0,count):
	xy=xy+(x[i]*y[i])
	
upper=count*(xy)-(c1*c2)
lower=((count*sqx-pow(c1,2))*(count*sqy-pow(c2,2)))
sqlower=math.sqrt(lower)

r=float(upper/sqlower)
print("co-relation:",r)
