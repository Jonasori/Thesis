"""Scratch code for Section 3"""

import os
import numpy as np
import subprocess as sp
import astropy.units as u
import astropy.constants as const
from pathlib2 import Path


# All MKS
h = const.h.value
c = const.c.value
k = const.k_B.value
hbar = const.hbar.value


Path.cwd()




def get_fluxed():
    os.chdir('/Volumes/disks/jonas/modeling')
    from tools import imstat_single

    im = 'data/hco/hco-short110_moment0'
    rms = imstat_single(im)[1]
    call_str = "cgcurs in={},{} device=/xs type=both slev=a,{} levs=2,7,15 options=stats".format(im + '.cm', im + '.cm', rms)
    def miriad_caller(call_str):
        call_list = call_str.split(' ')
        l = sp.check_output(call_list)
        # l2 = list(filter(None, l.decode("utf-8").split('\n')))
        l2 = filter(None, l.split('\n'))
        stats = []
        for row in l2:
            if list(filter(None, row.split(' ')))[0] == 'Sum':
                stats.append(list(filter(None, row.split(' '))))

        # nums = []
        # for stat in stats:
        #     try:
        #         nums.append(int(stat))
        #     except ValueError:
        #         pass

        return stats


get_fluxed()

h = const.h.decompose()
c = const.c.decompose()
k = const.k_B.decompose()
hbar = const.hbar.decompose()


# Einstein A (FCO+(4-3) come from: https://home.strw.leidenuniv.nl/~moldata/datafiles/hco+@xpol.dat
# Using the value listed as the 5-4 trans since the indexing is bad.
A_43 =  3.6269e-03 * (1/u.s) # s-1.
# F = float(miriad_caller(call_str)[0][2])


J_hco = 4.
E_43 = 29.7491 * u.cm.decompose()      #cm-1, from https://home.strw.leidenuniv.nl/~moldata/datafiles/hco+@xpol.dat

E0_hco = 2.975e-2 * (1/u.cm).decompose()    # cm-1, taken from first non-zero energy in hcoplus.dat, converted to m-1
B0_hco = 2*np.pi*E0_hco

E43_hco = E0_hco/(J_hco * (J_hco+1))
B_hco43 = 2*np.pi*E43_hco # From wiki: k = E/(hbar c = hc/2pi) -> k (hc) = 2pi E

d = 389 * u.pc.decompose()  # pc -> m
nu0 = 356.734288 * u.GHz.decompose()
mol_mass_hco = 29.0 # Molecular weight - should this have units?
T_ex_hco = 17 * u.K # From Sam

F_hco_jy = 4.15 * u.Jy * u.km * u.s**(-1)  #Jy km/s
F_hco = (F_hco_jy * nu0/c * 1e5).decompose()

F_hco.decompose()


# params = [J_u, B0 (wavenumber), T_ex (K), nu0 (GHz), F (J/beam km/s), m (molecular mass), d (parsecs), A_ul (Hz)]
params = [J_hco, B0_hco.value, T_ex_hco.value, nu0.value, F_hco.value, mol_mass_hco, d.value, A_43.value]
params = [J_hco, B0_hco, T_ex_hco, nu0, F_hco, mol_mass_hco, d, A_43]

def get_gas_mass(params):
    """
    Calculate a value for Eqn 3.1 in Factor et al 2017.

    Args (unpacked):
        J_u (int): Upper level's quantum number.
        B0 (int): Rotational constant (units of wavenumber)
        T_ex (float): Excitational temperature (K)
        nu0 (float): restfreq (GHz)
        F (float): integrated line flux (get from cgcurs)
        m (float): mass of emitting molecule (units?)
        d (float): distance to source
        A_ul (float): Einstein coefficient of u-l transition (Hz)
    """
    J_u, B0, T_ex, nu0, F, m, d, A_ul = params
    # Straighten out the units (other -> MKS)


    # This is cheating - the units aren't dead yet.
    Xu_exp = ((-B0 * J_u * (J_u + 1) * h * c) /(k * T_ex))
    Xu_coeff = ((2 * J_u + 1) / (k * T_ex/(h * c * B0)))

    Xu_exp

    Xu_coeff

    Xu = Xu_coeff * np.exp(Xu_exp)

    m_gas = (4 * np.pi/(h.decompose().value * nu0.decompose().value) ) * (F.decompose().value * m * d.decompose().value**2 / (A_ul.decompose().value * Xu))
    m_gas /= 1.9891e30 # Put it in solar masses.
    return m_gas

m = get_gas_mass(params)
print m

m_gas




def get_stellar_mass():
    spt_A = 'G2'
    spt_B = 'M2'

    T_eff_A = 5770 # From hw2 data












# The End
