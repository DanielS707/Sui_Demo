cd "D:\PU2022\ECON 490ADA\ADAData\"


//open data
use "gpa/gpa.dta", clear

//Q1
su sat

//q2
reg colgpa athlete, rob

//q3

//q4: on pg5

//5: No, athlete & error term is correlated

//6
ge satsq = sat^2
ge satcub = sat^3
ge verbmathsq = verbmath^2
ge verbmathcub = verbmath^3

local x "hsize hsrank sat satsq satcub female verbmath verbmathsq verbmathcub i.tothrs"
reg colgpa athlete `x', rob 

//7 default option: do not use quotation mark
set seed 1234
local x hsize hsrank sat satsq satcub female verbmath verbmathsq verbmathcub i.tothrs
lasso linear colgpa athlete `x'

//8
//9
//10
lassoselect lambda=0.0072617 
lassoinfo
//11
lassoselect lambda=0.0072617 
lassocoef

//12
//13
coefpath, xunit(lnlambda) minmax

//14

//15 double selection
set seed 1234
dsregress colgpa athlete, controls(hsize hsrank sat satsq satcub female verbmath verbmathsq verbmathcub i.tothrs) select(cv)
//or
ds colgpa athlete, not
set seed 1234
local x hsize hsrank sat satsq satcub female verbmath verbmathsq verbmathcub i.tothrs
local controls `x'
dsregress colgpa athlete, controls(`x') select(cv)

//16

//17
