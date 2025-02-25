### TO DO

- velocity axis on PVD diagram. Maybe change cmap to 0 -> positive, rather than negative -> positive

- Physical units to baseline cuts plot. Maybe just plot all four individually

- Check that all MIRIADs and miriads are \textsc{miriad}


- Check corrections:
    - i.e. -> i.e.,
    - e.g. -> e.g.,
    - T$_ -> $T_
    - M$_ -> $M_
    - R$_ -> $R_






### MEREDITH TALKING POINTS

* Spell detex filename.tex is a linux spellchecker


- Sig fig rules
  * Only report one digit of uncertainty in, rounding extras, then report on that one
  * If uncertainty starts with 1: then include one extra digit (i.e. 1.81 - > 1.8, report value out to tenths)
  * In case of 95.8 -> 100.0, 166 -> 170 (bc ones)


### Meredith Notes:

- Check Cleeves2015 for line strength ratios

- Dartois on vertical

- Andrews, Tripathi, maybe someone else on mass/radius dust ratios


### PLOTTING STUFF

- Make DMR not look bad

- Cornerplot looks mediocre at best right now
  - At least fix axis labels
  - Maybe add best-fit crosshairs



### TEX STUFF

- all arcsecs to \farcs i.e. 0."5 -> 0\farcs5

- AU -> au

- All .tex files: $^o$ -> \degree (works in Table 4.3)

- Zeroth or zeroeth?


# Far future/never:
- The whole Hanning smoothing business. From meredith: "Random thought as I’m reading this: can you please check whether or not Hanning smoothing is implemented in the MIRIAD commands that Kevin’s code uses?  Before uvmodel, there should be a “hanning” command in MIRIAD… let me know.  (If not, we should add it.) "


- Integrate DMR chanmaps and DMR m0/m1 together: each row has chanmaps on left, m0 on right -> column of chanmaps, column of m0s.

- On grid search results diagram, plot a 1-row heatmap of each value sampled (instead of the circled number line)

- For moment maps, make two-figure "zoom-ins", e.g. Fig. 2 in https://arxiv.org/pdf/1804.09190.pdf

- All the Hanning smoothing stuff: Meredith's comments, FN8 on p3 of Williams2014, Kevin's code, etc.

- Gaia has a bunch of different sources listed at V2434's location? http://aladin.u-strasbg.fr/AladinLite/?target=V*%20V2434%20Ori&fov=0.033334&survey=P%2fDSS2%2fcolor
