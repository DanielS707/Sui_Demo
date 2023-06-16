 cd	"D:\PU2022\ECON 490ADA\ADAData"
 
 //q1
 
 use "401k/401k.dta", clear	
 
 ta p401k
 ta fsize
 
 ge cfsize = min(fsize,5)
 
 ta cfsize
 
 corr p401k cfsize
 
 bys p401k cfsize: ge NN=_N
 //every varible in this dataset, repeated testing
 ta NN
 
 //ta NN if p401k==1 & cfsize==5
 //ta NN if p401k==1 & cfsize==4
 
 twoway scatter p401k  cfsize [w=NN]
 //mysymbol(circle_hollow)
 
 reg p401k cfsize, rob
 
 predict phat1, xb
 
 su phat1
 
 reg p401k cfsize nettfa age, rob
 predict phat2, xb
 // | means or.
 ge I=(phat2<0|phat2>1)
 su I
 
 Q2
 
 use "401k/401k.dta", clear
 
 reg p401k age, rob
 predict yhat
 
 //var(u|x)=p(y=1)*(p(y=0))
 
 ge sdu=(yhat*(1-yhat))^0.5
 
 su sdu
 
 //weight by inverse of variance
 reg p401k age [aw=1/sdu^2]
 

 