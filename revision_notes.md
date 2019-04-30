### MEREDITH TALKING POINTS


- Questions about B0 in scratch_03.py/get_mass.
  - M(E0 = 0.029) = 7.4e-6 Msol
  - M(E43 = 29) = 2e129 M_sol
  - Did I do/interpret mol mass right?

* Spell detex filename.tex is a linux spellchecker


- Getting rid of the DFM corner plots anyways. Useful to have 0? 1?
  * One set of corner plots (probably HCO)

- Should every instance of HCO/HCN etc have transition? i.e. HCO(4-3) always.
  * put it in "where it matters" i.e. ratios etc
  * only don't include if it doesn't matter

- Forgetting spaces after HCO+: because of set command
  * See line 74 in Thesis.tex

- Sig fig rules
  * Only report one digit of uncertainty in, rounding extras, then report on that one
  * If uncertainty starts with 1: then include one extra digit (i.e. 1.81 - > 1.8, report value out to tenths)
  * In case of 95.8 -> 100.0, 166 -> 170 (bc ones)


### Meredith Notes:

- Check Cleeves2015 for line strength ratios

- Dartois on vertical

- Andrews, Tripathi, maybe someone else on mass/radius dust ratios


### PLOTTING STUFF

- LOTS TO DO ON PVD: Make Fig. 3.7 a diptych to show where the slice is coming from. Also fix the PVDs axes. Also make the cbar scale go dark to light, rather than dark light dark, since 0 doesn't really have meaning here.
- Increase label sizes on structure plots.


- Fig 4.4: Take off disk A's fit (maybe?); at least change its color.


### TO DO
- Acknowledgements!
- Conclusion!
- Discussion!

- Disk structure plots
- Sort out units on PVD
- Get rid of DFM corner plot right before 4.3 Fitting Procedure



### TEX STUFF

- all arcsecs to \farcs i.e. 0."5 -> 0\farcs5

- AU -> au

- All .tex files: $^o$ -> \degree (works in Table 4.3)

- Zeroth or zeroeth?


# Far future/never:

- Integrate DMR chanmaps and DMR m0/m1 together: each row has chanmaps on left, m0 on right -> column of chanmaps, column of m0s.

- On grid search results diagram, plot a 1-row heatmap of each value sampled (instead of the circled number line)

- For moment maps, make two-figure "zoom-ins", e.g. Fig. 2 in https://arxiv.org/pdf/1804.09190.pdf

- All the Hanning smoothing stuff: Meredith's comments, FN8 on p3 of Williams2014, Kevin's code, etc.

- Gaia has a bunch of different sources listed at V2434's location? http://aladin.u-strasbg.fr/AladinLite/?target=V*%20V2434%20Ori&fov=0.033334&survey=P%2fDSS2%2fcolor
