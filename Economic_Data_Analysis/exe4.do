cd "D:\PU2022\ECON 490ADA/ADAData"

//open data
use "production/dairy.dta", clear

* regular SEs
reg milk land labor cows feed
estimates store es1

*robust SEs without clustering
//The vce() option causes Stata to change the way standard error is calculated.
//super small sample cannot use robust because it is homoskedastic.
reg milk land labor cows feed, vce(robust)
estimates store es2

//coef & s.e.
// modelwidth = more space, %7.3f 3decimal places, 
estimates table es1 es2, modelwidth(15) b(%7.3f) se(%7.3f)

*robust SEs with clustering
reg milk land labor cows feed, vce(cluster farm)
estimates store es3

//q2

//a
*from reg table

//b
*equal coefficients on land plus labor?
//linear combination
lincom land+labor

//c
*zero coefficients on labor and land
test labor==land==0

*zero coefficients on labor and land and cows
test labor==land==cows==0

//equal*zero coefficients on labor and land and cows
test labor==land==0
test cows==3000, acc