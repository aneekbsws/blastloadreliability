import pyre
from pyre import *


limit_state = LimitState(lambda fy, s, w, l,t: (fy * s) - ((2 * w * l) - (w * 8)+ t))
stochastic_model = StochasticModel()
stochastic_model.addVariable(Normal('s', 6.9368, 0.3468))
stochastic_model.addVariable(Normal('fy', 44497000, 4449700))
stochastic_model.addVariable(Normal('w', 628000, 209333))
stochastic_model.addVariable(Normal('l', 20, 2))
stochastic_model.addVariable(Normal('t', 345083, 46500))

options = AnalysisOptions()
Analysis = Form(analysis_options=options, stochastic_model=stochastic_model, limit_state=limit_state)
