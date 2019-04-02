"""A place to make 'leftover' plots for the thesis."""


import numpy as np
import seaborn as sns
import astropy.units as u
import matplotlib.pyplot as plt
sns.set_style('white')

from astropy.constants import c, h, k_B
c, h, k_B = c.value, h.value, k_B.value




def plot_SED():
    # These l's are just the exponent for the wavelength
    d = 3.315 * 10**18                         # distance to hd157587, in m
    r_star, r_disk = 6.957 * 10**8, 10**12     # Solar radius and 100 AU, in m
    t_star, t_disk = 6000, 50


    def planck_nu(l, temp):
        # l is wavelength in m
        nu = c/l
        top = 2. * h * nu**3 * c**-2
        bot_exp = h*nu/ (k_B * temp)
        B_nu = top / ((np.exp(bot_exp) - 1.))
        return B_nu


    nfn_star, nfn_disk, nfn_total = [], [], []
    l_range = np.logspace(-8, -2, 1000)

    nfn_star = planck_nu(l_range, t_star) * (c/l_range * 1e26 * np.pi * (r_star/d)**2)
    nfn_disk = planck_nu(l_range, t_disk) * (c/l_range * 1e26 * np.pi * (r_disk/d)**2)
    nfn_total = nfn_disk + nfn_star

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.loglog(l_range, nfn_total, '-k', lw=4, label='Observed SED')
    ax.loglog(l_range, nfn_disk, linestyle=":", color='red', lw=2, label='Disk Contribution')
    ax.loglog(l_range, nfn_star, linestyle=":", color='orange', lw=2, label='Stellar Contribution')

    ax.set_ylim(1e10, 6e14)
    ax.set_xlim(10**(-7.1), 10**(-2.5))

    def format_func(value, tick_number):
        N = value * 1e3
        if N < 1:
            i = 1
            while round(N, i) == 0:
                i += 1
            N = round(N, i)
        else:
            N = int(N)
        return N

    ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
    ax.set_yticklabels([])

    ax.set_ylabel(r"$\nu F_{\nu}$ (Jy Hz)", weight='bold')
    ax.set_xlabel("Wavelength (mm)", weight='bold')

    plt.legend(loc='best')
    sns.despine()
    plt.savefig('/Volumes/disks/jonas/Thesis/Figures/example_SED.pdf')
    plt.show()


plot_SED()












# The End
