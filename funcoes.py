import numpy as np

def q (G): #onde G é o parâmetro de inclinação, às vezes adotado como 0.15
  G = float(input("Digite o valor do parâmetro de inclinação: "))
	q = 0.29 + 0.684 * G
	return q

##############################################################

def pv (A, q): #onde A é o albedo bolométrico de Bond e q é uma integral de fase
	A = float(input("Digite o valor do albedo bolométrico: "))
	pv = A/q
	return pv

##############################################################

def H (D, pv): #onde H é a magnitude absoluta, D é o diâmetro e pv é o albedo geométrico
	D = float(input("Digite o valor do diâmetro em km: "))
	H = (-5*math.log(D)) - ((5/2)*math.log(pv)) + 15.62
	return H
