. cd "D:\PU2022\ECON 490ADA\ADAData\"
 //open data

use "401k\401k.dta", clear

//q1
reg p401k male, rob

//b 
test male==0

//d
ds p401k male, not
local controls `r(varlist)'

reg p401k male `controls', rob

test male==0

//e

ds p401k, not

local controls `r(varlist)'

lasso linear p401k male `controls'

lassocoef

//f

ds p401k male, not

local controls `r(varlist)'

dsregress p401k male, controls(`controls') select(cv)