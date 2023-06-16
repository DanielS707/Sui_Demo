//open data 
cd "D:\PU2022\ECON 490ADA\ADAData"
use gpa/gpa.dta, clear

su colgpa
ge HiColGPA = colgpa>r(mean)

su HiColGPA
ta HiColGPA

ge p1 = exp(1-0.1*hsperc)/(1+exp(1-0.1*hsperc))
su p1
su HiColGPA

//p(Y|X)
ge p_obs = p1^HiColGPA*(1-p1)^(1-HiColGPA)
su p_obs

ge log_p_obs = log(p_obs)

egen ll = sum(log_p_obs)
su ll

logit HiColGPA hsperc

//q2 same dataset
logit HiColGPA tothrs athlete hsize

predict phat, pr
su phat

test athlete==hsize==0