import numpy as np

def q (x): #onde x é o ângulo de fase solar
  x = float(input("Digite o valor do ângulo de fase solar: "))
	q = 2*((funcao_de_x*np.pi*(-1))*(fucao_de_x*np.pi))
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
