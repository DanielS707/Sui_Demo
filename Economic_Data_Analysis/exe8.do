clear

//question1

//b
set obs 2000

//c
ge x=uniform()
su x

//d
hist x
hist x, bin(100)
//e
ge u=rnormal()
su u

//f
hist u

//g
ge ystar=-2+3*x+u
ge y=ystar>0

//h
probit y x

//i
reg ystar x

//question2
//a
probit y x
est store es_probit

//b
logit y x
est store es_logit

//c
estimates table es_probit es_logit

//d
est restore es_probit
margins, predict(pr) dydx(x)

est restore es_logit
margins, predict(pr) dydx(x)

//e
reg y x

//f
est restore es_probit
margins, predict(pr) dydx(x) at(x=2)

est restore es_logit
margins, predict(pr) dydx(x) at(x=2)

reg y x
