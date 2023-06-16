cd "D:\PU2022\ECON 490ADA\ADAData\"

//open data
import delimited "earnings\Koop-Tobias.csv", clear

//b
sort personid timetrnd
browse

//c
xtset personid timetrnd

//e
xtline logwage if personid <=10, overlay

//f
xtline educ if personid <=10, overlay

//g
xtline ability if personid <=10, overlay

//h
reg logwage educ, robust


 //j
 reg logwage educ ability, cluster(personid)
 
 //l
 reg logwage educ ability i.timetrnd, cluster(personid)
 
 //
ds personid timetrnd ability, not reshape wide `(varlist)', i(personid) j(timetrnd)

//
reg logwage10 edu10 ability, rob