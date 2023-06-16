. cd "C:\490data\ADAData"
 use "crime/crime.dta" ,clear
 //keep '87
 keep if year ==87
 hist crmrte
 //drop if year !=87
 
 //histogram of crime rate
 ge HiCrime = crmrte>0.04
 su HiCrime
 
 //probit model
 probit HiCrime density
 
 //predict p1
 predict p1, pr
 
 //d s shape of the graph: probability
 twoway line p1 density, sort
 
 //average marginal effects
 margins, dydx(density)
 margins, dydx(density) at(density=2)
 margins, dydx(density) at(density=5)

 //extend probit model
 probit HiCrime density polpc
 test density==polpc==0