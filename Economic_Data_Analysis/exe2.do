cd "D:\PU2022\ECON 490ADA\ADAData"

use "gpa/gpa.dta" , clear

tabstat sat-hsizesq, by(female) stat(mean) nototal

su hsrank, detail
return list

ge rhsrank=.
replace rhsrank=1 if hsrank<r(p25)
replace rhsrank=2 if hsrank>=r(p25) & hsrank<r(p50)
replace rhsrank=3 if hsrank>=r(p50) & hsrank<r(p75)
replace rhsrank=4 if hsrank>r(p75)

ta rhsrank

forvalues i=1/4{
	ge D`i'=rhsrank==`i'
}

su D2, detail

ge hsrankbysize=hsrank/hsize

corr hsrankbysize hsperc

