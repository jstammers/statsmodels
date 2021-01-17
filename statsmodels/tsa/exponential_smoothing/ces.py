r"""
CES model for time series analysis
The Complex Exponential Smoothing (CES) model is an extension of simple exponential
smoothing that captures trends and seasonalities. In addition to the observed time
series :math:`y_{t}` this model has a non-observable component - the information
potential :math:`p_{t}` - that contains additional information about the time-series. The
inclusion of this additional term removes the need to distinguish between the level
and trend terms, as is the case in simple exponential smoothing.

A CES model substitutes the real-valued variable :math:`\hat{y}_{t}` in simple
exponential
smoothing with a complex-valued variable :math:`\hat{y}_{t} + i \hat{p}_{
t}`. The `smoothing_level` :math:`\alpha` is also replaced with a complex smoothing
paramter :math:`\alpha_0 + i \alpha_1`. In doing so, the CES model is written as

.. math::

    \hat{y}_{t+1} + i \hat{p}_{t+1} = (\alpha_{0} + i \alpha_1)(y_{t} + i
    p_{t}) + (1-\alpha_0+i - i\alpha_1)(\hat{y}_{t} + i \hat{
    p}_{t})

Following a derivation in [1]_, this model has a state-space form given by

.. math::
   \begin{cases}
   y_t &= l_{t-1} + e{t-1} \\
   l_t &= l_{t-1} - (1-\alpha_1)c_{t-1} - \alpha_1 p_{t} + \alpha_0 e_t \\
   c_t &= l_{t-1} + (1-\alpha_0)c_{t-1} + \alpha_0 p_{t} + \alpha_1 e_t
   \end{cases}

where :math:`l_t` is the level component, :math:`c_t` is the information component
and :math:`e_t \sim N(0, \sigma^2)`.
"""