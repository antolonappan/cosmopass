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
Here are some examples of Cosmopass.
```python
#for finding hubble(z) in LCDM

from cosmopass.equations.fluids import LCDM

h0 = LCDM(Om0=.3,rd=147,h=.7,Or0=5,sigma8=.8).hubble_z(0)
```
```python
#How to get likelihoods?
from cosmopass.likelihoods.chisquares import model

lcdm = model('LCDM')

#Now if you want to know what are the parameters of 'LCDM' you can get info by,
print(lcdm.Params)

#For computing specific chi_sq like BAO,
lcdm.chi_bao(.3,147,.7,5,.8)

#For computing combination of different chi_sq like h+bao+jla
lcdm.chi_list = ["h","bao","jla"]
lcdm.chi_sq(.3,147,.7,5,.8)

#If you want to use quasar you need to add to parameters 'm' and 'delta' specified in Risaliti.et al
lcdm.chi_qso(.3, 147, .7, 5, .8, 0, 1.3)

#Or if the combination has qso
lcdm.chi_list = ["h","bao","qso"]
lcdm.chi_sq(.3, 147, .7, 5, .8, 0, 1.3) # since the combination has 'qso', you have to provide 'm' and 'delta'

# VERY IMPORTANT THING TO REMEMBER
# The flexibility of likelihoods is achived using *args
# What does it means?
# Likelihood does't care of the order of parameters it silently passes to parent definitions.
# Which means; (0.3,147,.7,5,.8) is not equal to (0.3,.7,147,5,.8) ORDER MATTERS. 
# For confirming the order you can always check the 'Params' as shown in the above lines
# Since it is not using **kwargs passing the arguments by assignment(Om0=.3,rd=147) won't work


```



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
