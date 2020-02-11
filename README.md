# COSMOlogical Parmeterization And Scalar fields Solver - COSMOPASS

COSMOPASS can be used to calculate the different Cosmological models, which includes different Dark Energy Parameterisation , scalar fields such as minimally coupled quintessence, tachyon and galileon fields. It can be easily integrated with emcee and pymultinest.

## Installing
```
pip install cosmopass
```

## Getting Started

The package cosmopass has organised as the tree shown below. Here the submodule equations is the mirror of publicaly available package ScalPy.
```
cosmopass
   |
   |-----> __init__.py
   |-----> equations
   |           |
   |           |----> __init__.py
   |           |----> fluids.py
   |           |----> scalar_all_eqn.py
   |           |----> transfer_func.py
   |
   |
   |-----> likelihoods
               |
               |----> __init__.py
               |----> chisquares.py
               |----> dataimport.py
               |----> Data/
```
Cosmopass contains a wide cosmological model definitions which includes,
         **Paramerisations: LCDM, wCDM, w0waCDM, BA, JBP, SCPL, GCG***
         **EDEs: Exponential Scalar, Power Scalar, Exponential Tachyon, Power Tachyon, Exponential Galelion, Power Galelion.**
The available likelihoods are,
         **H0, H,  BAO, Pantheon, JLA, Masers, Time delay in strong lensing, CMB prior, Quasar.**
         
## How to Use ?
Few examples are given in Example.ipynb. Also you can run it here [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gl/antolonappan%2Fcosmopass/e2649a9ef34790e98ac9d0368450073325897485?filepath=Example.ipynb)



## Keywords
Available Models:
```
LCDM, wCDM, w0waCDM, BA, JBP, SCPL, GCG, 
scalarpow,scalarexp, tachyonpow, tachyonexp, galelionpow, galelionexp
```

Available Chi Sq:
```
h,qso,panth,bao,masers,fs8,cmb,td,jla
```
### Acknowledgments
* scalpy
