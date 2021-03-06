import numpy as np

def q (G): #onde G é o parâmetro de inclinação, às vezes adotado como 0.15
	q = 0.29 + 0.684 * G
	return q

##############################################################

def pv (A, q): #onde A é o albedo bolométrico de Bond e q é uma integral de fase
	pv = A/q
	return pv

##############################################################

def H (D, pv): #onde H é a magnitude absoluta, D é o diâmetro, dado em km e pv é o albedo geométrico
	x = (D*np.sqrt(pv))/1329
	H = -5*np.log(x)
	return H
