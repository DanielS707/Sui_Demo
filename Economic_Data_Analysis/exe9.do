//Q1
cd "D:\PU2022\ECON 490ADA\ADAData\"
//open data
 use "loanapp/loanapp.dta", clear
 
 //a
 su loanamt
 
 //b
 centile loanamt, centile(25 50 75)
 return list
 
 //c
 ge HighLoan = loanamt > `r(c_2)'
 ta HighLoan
 
 //d
 probit HighLoan appinc
 
//iv
 disp normal(-0.2996208)
 
 //e
 predict preHigh, pr
 twoway line preHigh appinc, sort
 
 //f
 margins, predict(pr) dydx(appinc)
 
 //g
 margins, predict(pr) dydx(appinc) at(appinc=(100 400 800))
 
 //2
 probit HighLoan appinc
 margins, predict(pr) dydx(appinc)
 
 //a
  probit HighLoan appinc netw
 margins, predict(pr) dydx(appinc)
 
  //b
 probit HighLoan appinc i.dep
 margins, predict(pr) dydx(appinc)
 
 //c
 reg HighLoan appinc, rob
 
 //d
 logit HighLoan appinc
 margins, predict(pr) dydx(appinc)