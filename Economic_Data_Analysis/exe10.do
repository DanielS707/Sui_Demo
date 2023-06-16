cd "D:\PU2022\ECON 490ADA\ADAData\"

//Q1
//open data
use "gpa/gpa.dta", clear

//b
reg colgpa athlete
est sto estb

//c
ge sat2=sat^2
reg colgpa athlete tothrs sat sat2
est sto estc

//d
reg colgpa athlete tothrs##c.sat tothrs##c.sat2
est sto estd

//e
est table estb estc estd, keep(athlete) stats(r2 rmse df_m N)

//f RMSE = (sum u_ihat^2/N)^0.5

//g 
set seed 123456789
ge S=uniform()
su S

//h
ge G=1
replace G=2 if S>=0.2
replace G=3 if S>=0.4
replace G=4 if S>=0.6
replace G=5 if S>=0.8
ta G

//i 
*Model 1
ge u2_M1=.
forvalues g=1/5{
	reg colgpa athlete if G!=`g'
	
	//predict residuals
	predict u_M1_`g', resid
	
	//squared residuals for out-of-sample obs
	replace u2_M1=u_M1_`g'^2 if G==`g'
	drop u_M1_`g'
}

//i 
*Model 2
ge u2_M2=.
forvalues g=1/5{
	//qui = run without showing result, since we prove model is correct in the first time.
	qui reg colgpa athlete tothrs sat sat2 if G!=`g'
	
	//predict residuals
	predict u_M2_`g', resid
	
	//squared residuals for out-of-sample obs
	replace u2_M2=u_M2_`g'^2 if G==`g'
	drop u_M2_`g'
}

*Model 3
ge u2_M3=.
forvalues g=1/5{
	//qui = run without showing result, since we prove model is correct in the first time.
	qui reg colgpa athlete tothrs##c.sat tothrs##c.sat2 if G!=`g'
	
	//predict residuals
	predict u_M3_`g', resid
	
	//squared residuals for out-of-sample obs
	replace u2_M3=u_M3_`g'^2 if G==`g'
	drop u_M3_`g'
}

//average out of same RMSE
su u2_M1
disp r(mean)^0.5
su u2_M2
disp r(mean)^0.5
su u2_M3
disp r(mean)^0.5

