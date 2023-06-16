clear
// Question 1


// a
set seed 123456789 
set obs 1000

ge x_1=rnormal()
su x_1

// b
forvalues k=2/100{
 local j=`k'-1
 ge x_`k'=rnormal()-0.99*x_`j'
}


//c
ge y=1+0.5*x_1+0.5*x_3+rnormal()

reg y x_1 x_3

//d

// Split sample in two
splitsample, generate(sample) nsplit(2)
label define svalues 1 "Training" 2 "Testing"
label values sample svalues

lasso linear y x* if sample==1, grid(5, min(.001))
local l=e(lambda_sel)

//f
lassoselect lambda=.001
lassogof, over(sample)

//g
lassoselect lambda=`l'
lassoinfo  
lassocoef  
lassogof, over(sample)

