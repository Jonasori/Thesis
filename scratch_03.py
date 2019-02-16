"""Scratch code for Section 3"""

import os
import numpy as np
import subprocess as sp
import astropy.units as u
import astropy.constants as const
from pathlib2 import Path

from tools import imstat_single

# All MKS
h = const.h.value
c = const.c.value
k = const.k_B.value


os.chdir('/Volumes/disks/jonas/modeling')
Path.cwd()





im = 'hco_moment0'
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



F = float(miriad_caller(call_str)[0][2])
J = 1
E0_hco = 2.975 * 1e-2         # cm/s, taken from first non-zero energy in hcoplus.dat
B0 = E0_hco/(J * (J+1))       # Need this in units of wavenumber?!
# params = [J_u, B0 (wavenumber), T_ex (K), nu0 (GHz), F (J/beam km/s), m (molecular mass), d (parsecs), A_ul (Hz)]
params_hco = [4, B0, 17, 356.734288, F, 29.0, 389, 3.6269e-3]

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
    nu0 *= 1e9              # GHz -> Hz
    B0 *= 1e-2              # cm/s -> m/s in the E0 term.
    d *= 3.08e16            # parsecs -> m


    X_u = (2 * J_u + 1) * np.exp(-B0 * J_u * (J_u + 1) * h * c /(k * T_ex))/(k * T_ex/(h * c * B0))
    m_gas = (4 * np.pi/(h * nu0) ) * (F * m * d**2 / (A_ul * X_u))
    return m_gas

m = get_gas_mass(params_hco)
print m








# The End
