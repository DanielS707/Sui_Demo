. cd "C:\490data\ADAData"
 use "401k/401k.dta" ,clear
 
 regress nettfa inc incsq
 
 //xb is what we use to gen yhat, which is our new gen variable
 predict yhat, xb
 // yhat's euqation made by beta0+beta1hat*x1+... anyway it is predicted nettfa
 // draw the graph
 twoway line yhat inc, sort
 //nale==1
 reg nettfa inc incsq if male==1
 predict yhatm1, xb
 twoway line yhatm1 inc, sort
 //male==0
 reg nettfa inc incsq if male==0
 predict yhatm0, xb
 twoway line yhatm0 inc, sort
 
 //comparison use xx xx as y & x, legend xxx for x-axis label.
 twoway line yhatm1 yhatm0 inc, sort legend(label(1 "Male=1") label(2 "Male=0"))
 graph close
 
 ge incmale = inc*male
 ge incnotmale = inc*(1-male)
 
 ge incsqmale = incsq*male
 ge incsqnotmale = incsq*(1-male)
 
 reg nettfa male incmale incsqmale incnotmale incsqnotmale
 
 lincom _cons + male + incmale + incmale*50+incsqmale*(2500)
 lincom _cons + male + incnotmale + incnotmale*50+incsqnotmale*(2500)
 
 //control for family size
 
 ta fsize, gen(F)
 reg nettfa inc incsq
 est sto es1
 
 // reg and gen all of dummy variables
 reg nettfa inc incsq F*
 reg nettfa inc incsq F1-F12
 //est store the estimates into es1
 est sto es2
 
 est table es1 es2, keep(inc incsq)
 
 