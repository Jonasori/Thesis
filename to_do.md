## TO DO


- A Good Place, Orphan Black shows

- Write 04_Analysis
  - Make temperature/density structure plot (from Disk object, described in Kevin's guide.)
  - Find Sam's corner plot code, put it in mcmc.MCMCrun(). It looks great.

- Remake disk A optically thick thing (xmol by chi2)
  - For CO do it by disk mass, not xmol
  - Remove disk mass B from param_info
  - Increase disk size a bunch, choose based on HCO+ fit results

- Work on 02_Observations

- Work on 03_Results
  - Rewrite this whole thing.
  - Integrated Flux Measurements
  - Find max width of disks for each line by 3-sigma contour
  - use uvfit for elliptical guassian vis fits.


- Meredith's 49 Ceti (2008) paper, Luca Matra's recent papers (first Beta Pic paper?) for more info/context on the disk gas mass equation.



## MEREDITH QUESTIONS
- Should I really go all the way down into the weeds with the equations for the Gas Model? Cail didn't, but he only had a dust model to write about I guess.
- From email to M: How to progress with CO MCMC runs?


- How to get B0 in units of wavenumber?


## Current runs:

Other machines: varda, sonora, scout

Show Python Process: ps -fA | grep python
Show processor info (i.e. number of processors): lscpu



Multifig:
\begin{figure}[htp]
  % Maximum length
  % \subcaptionbox{1a\label{fig1:a}}{\includegraphics[width=1.6in]{example-image-a}}\hfill%
  % \subcaptionbox{1b\label{fig1:b}}{\includegraphics[width=1.6in]{example-image-a}}%
  % \bigskip
  % Equal length
  \hspace*{\fill}%
  \subcaptionbox{2a\label{fig2:a}}{\includegraphics[width=0.5\linewidth]{ALMA_universetoday.jpg}}\hfill%
  \subcaptionbox{2b\label{fig2:b}}{\includegraphics[width=0.3\linewidth]{Andrews2018_proplyds.png}}%
  \hspace*{\fill}%
\end{figure}

2x2 Panel Figures
\begin{figure}[htp]
  \hspace*{\fill}%
  \subcaptionbox{\label{fig:v2434ori_smith05}}{\includegraphics[width=0.47\linewidth]{V2434Ori_Smith05-2.png}}\hfill&
  \subcaptionbox{\label{fig:v2434ori_mann09}}{\includegraphics[width=0.47\linewidth]{V2434Ori_Mann09.png}}\hfill\\[2\tabcolsep]
  \hspace*{\fill}%
  \subcaptionbox{\label{fig:v2434ori_ricci11}}{\includegraphics[width=0.47\linewidth]{V2434Ori_Ricci11.png}}\hfill&
  \subcaptionbox{\label{fig:v2434ori_smith05}}{\includegraphics[width=0.47\linewidth]{m0-map_hco.pdf}}\hfill
  \hspace*{\fill}%
  \captionof{figure}{Images of V2434 Ori taken from Smith et al (2005) on HST (left panel), Mann et al (2009) with the SMA at 880 $\mu$m (center panel), and Ricci et al (2011) with the EVLA at 7mm (right panel). Not sure if I want just previous studies' images (3 panel) or to include mine and make it 4 panel.}
\end{figure}
