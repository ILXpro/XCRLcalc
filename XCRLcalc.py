import periodictable as pt
import periodictable.xsf as ptx
import numpy as np
import foo
import time

tstart_cpu = time.clock()   # start the CPU timer


E = 12			# Energy in keV

M = 'Be'		# Material 
R = 50			# CRL radius of curvature 
N = 40			# number of refractive lens 


M = getattr(pt, '%s'%M)							# I dont know how, but 'eval' - not good idea!)
name = getattr(pt.elements, '%s'%M).name		# name of element
density = M.density								# density
mass = M.mass									# mass of element

lyamda = ptx.xray_energy(E)
n = ptx.index_of_refraction(M, energy=E)		# index of refraction
delta = 1-n.real								# Delta
beta = -n.imag									# Beta
u = 4*np.pi*beta/(lyamda*1e-10)					# Linear attenuation coefficient
Lpi = 1e-10*lyamda/(2*delta)


F = (R*1e-6)/(2*N*delta)							# CRL focus distance (thin lens)
e1 = (2*np.log(2)/np.pi)**.5					# V.Kohn coefficient
Aeff = e1*(F*lyamda*1e-10*delta/beta)**.5		# CRL effective aperture (V.Kohn)
Aeff_1m = e1*(1*lyamda*1e-10*delta/beta)**.5	# CRL effective aperture @ 1m focus distance

print ('Material	%s (%s)'%(M, name))
print ('Density		%s g/cm^3'%density)

print ('\nEnergy		%s keV'%E)
print ('Wavelength	%s A'%lyamda)
print ('Delta		%s '%delta)
print ('Beta		%s '%beta)
print ('u at.coef.	%s um^-1'%u)
print ('Pi shift	%s um'%(Lpi*1e6))

print ('\nCRL properties:')
print ('Focus		%s m'%F)
print ('Aeff		%s um'%(Aeff*1e6))
print ('Aeff @ 1m	%s um'%(Aeff_1m*1e6))


t_cpu = time.clock() - tstart_cpu
print ("\n\n\nCPU time:%12.6f seconds\n"%t_cpu)
