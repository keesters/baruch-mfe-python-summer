# CrunchBase API
CrunchBase API is a library to allow downloading and presenting organization and people data from Crunchbase.

## Quick Start
There are two main functions to be used in the CrunchBase API.
These functions allow you to pull people and organization data directly from CrunchBase fitting a given set of inputs.
```python
import cbapi

cbapi.people(name='Steve',locations='California') # returns people data based on the given inputs
cbapi.companies(name='word',locations='',socials='',types='') # returns company data based on the given inputs
```





## Installation

