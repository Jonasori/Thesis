"""Observations Scratch"""


from astropy.io import fits
from pathlib2 import Path
c = 3e8     # m/s

Path.cwd()


def get_baseline_in_klam(nu_ghz, baseline_m):
    # Convert a baseline from meters to klam

    nu_hz = nu_ghz * 1e9            # GHz -> Hz
    lam_m = (c/nu_hz)               # m/s/Hz
    baseline_klam = baseline_m / (1e3 * lam_m) # m klam/

    return baseline_klam

def get_las(self, d_min, d_min_units='klam', lam=None):
    """Get the largest angular scale of an observation.
    Args:
        d_min: minimum baseline length, in units of either distance or klamda
        lam: wavelength of observation (mm). If None, assumes d_min is in units of klam.
             Otherwise assumes d_min in meters.
    """
    if d_min_units == 'klam':
        las = 1/(d_min)
    else:
        # Make sure these units match.
        las = lam/(d_min)

    las *= 206265 # rads to arcsec
    return las

hco_dict = {'path': '/Volumes/disks/jonas/modeling/data/hco/hco',
            'line_name': 'hco', 'restfreq': 356.734, 'baseline_cut': 110}
hcn_dict = {'path': '/Volumes/disks/jonas/modeling/data/hcn/hcn',
            'line_name': 'hcn', 'restfreq': 354.505, 'baseline_cut': 80}
co_dict = {'path': '/Volumes/disks/jonas/modeling/data/co/co',
           'line_name': 'co', 'restfreq': 345.796, 'baseline_cut': 60}
cs_dict = {'path': '/Volumes/disks/jonas/modeling/data/cs/cs',
           'line_name': 'cs', 'restfreq': 342.883, 'baseline_cut': 0}


get_baseline_in_klam(hco_dict['restfreq'], 21.2)



class Obs():
    def __init__(self, mol_dict):
        self.path = mol_dict['path']
        self.line_name = mol_dict['line_name'].upper()
        self.restfreq = mol_dict['restfreq']
        self.headers = (fits.getheader(self.path + '.fits'),
                        fits.getheader(self.path + '-short{}.fits'.format(mol_dict['baseline_cut'])))

        self.beam_info_full = [self.headers[0]['bmaj'] * 3600,
                               self.headers[0]['bmin'] * 3600,
                               self.headers[0]['bpa']]

        self.beam_info_cut = [self.headers[1]['bmaj'] * 3600,
                              self.headers[1]['bmin'] * 3600,
                              self.headers[1]['bpa']]

        # Min baseline length (klambda)
        # This stuff is a little funky
        self.baseline_cut = mol_dict['baseline_cut']
        self.d_min_cut = max([21.2, self.baseline_cut])
        self.d_min_full = get_baseline_in_klam(mol_dict['restfreq'], 21.2)
        self.d_max = get_baseline_in_klam(mol_dict['restfreq'], 384.2)

        self.cut_las = 206265 / (1e3 * self.d_min_cut)          # arcsec conversion/lam
        self.full_las = 206265 / (1e3 * self.d_min_full)          # arcsec conversion/lam
        self.ang_res = 206265 / (1e3 * self.d_max)


for d in [hco_dict, hcn_dict, co_dict, cs_dict]:
    line = Obs(d)
    print ("Molecular Line: ", line.line_name)
    print ("LAS (Cut): ", line.cut_las)
    print ("LAS (Full): ", line.full_las)
    print ("Angular Resolution: ", line.ang_res)
    # print ("Beam Info (All Baselines): ", line.beam_info_full)
    # print ("Beam Info (Cut Baselines): ", line.beam_info_cut)
    print("\n")



v = None



def calc_sigma(vector=None):
    import numpy as np
    if vector:
        val1, sig1, val2, sig2 = vector
    else:
        val1 = input('Value of Param 1:\n')
        sig1 = input('Value of sigma 1:\n')
        val2 = input('Value of Param 2:\n')
        sig2 = input('Value of sigma 2:\n')

    diff =  abs(val1 - val2)/(np.sqrt(sig1**2 + sig2**2))
    print (diff)
    return diff




mass_jonasA_sam = calc_sigma([78.66, 0.42, 45.84, 0.77])
radii_jonasA_ritaA = calc_sigma([268, 26.8, 340.77, 8])
radii_sam_rita = calc_sigma([525, 52.5, 530, 10])


'''
V2434 Ori: 05 35 25.23 -05 15 35.69
Distance to Theta Ori C
Theta Ori C: 05 35 31.43 -05 25 16.36
sqrt(6.2^2 + (10*60 -9)^2)
Nu Ori: 05 35 31.36	-05 16 02.58
sqrt(6.1^2 + (1*60 -32)^2) = 11147au = 0.05pc
'''



# The End
