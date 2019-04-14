## TO DO


- Adapt Intro edits

- Get PVD diagram sorted out (Meredith PVD in 49 Ceti paper from CASA)


- Work on 03_Results
  - Rewrite this whole thing.
  - Integrated Flux Measurements
  - Find max width of disks for each line by 3-sigma contour
  - use uvfit for elliptical guassian vis fits.
  - Meredith's 49 Ceti (2008) paper, Luca Matra's recent papers (first Beta Pic paper?) for more info/context on the disk gas mass equation.

- Work on 02_Observations



## Meredith Questions:
- Go (partially?) through email questions
- Thoughts on new SED
-




## Current Runs:
- Iorek: march20-co: Completed, ended up kinda weird.
- Iorek: march26-hco: np=10. Maybe overloaded iorek.
- Sirius: march30-hcn: has updated pos_angle and r_out_B priors.


## Next Runs:
- CS: fixed incl, PA,


## Run Notes:
- As of 3/15/19ish, all code is in Py3
- As of 3/16/19, all runs have inclB = 45
- As of 3/26/19, all runs have max priors of r_out_A=700, r_out_B=400, pos_angle_*=180
- As of 3/30/19, lnprob is defaulting to setting Gaussian position angle priors on both disks, using values from Williams et al 2014.


## Other Notes for Thesis'ing
- System name on all figures (V2434...)
- For CS, use 3*RMS for Flux in disk mass calculation to get upper limit.

- For multiline fit:
  - Fix PA, incl, temp str, t atms,
  - Vary radius, abundances, mass,










## LINUX BOXES
- Iorek: 24 CPUs, 2 sockets, 6 cores/socket, 2 threads/core; 256GB Mem
- Sirius: 4 CPUs, 1 sockets, 4 cores/socket, 1 thread/core; 64GB
- Scout: 12 CPUs, 1 sockets, 6 cores/socket, 2 threads/core; 24GB (too little memory to handle my needs)
- Sonora: 8 CPUs, 1 sockets, 4 cores/socket, 2 threads/core; 64GB (currently down)
- Varda: 8 CPUs, 1 sockets, 4 cores/socket, 2 threads/core; 64GB (currently hangs on login)




## EQUATION STUFF
- How to get B0 in units of wavenumber?




## Useful Terminal Commands
Show Python Process: ps -fA | grep python
Show processor info (i.e. number of processors): lscpu
ls -d



- A Good Place, Orphan Black shows
