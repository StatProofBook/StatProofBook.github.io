---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-26 10:37:00

title: "Relationship between signal-to-noise ratio and R²"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "Signal-to-noise ratio"
theorem: "Relationship with R²"

sources:

proof_id: "P63"
shortcut: "snr-rsq"
username: "JoramSoch"
---


**Theorem:** Let there be a [linear regression model](/D/mlr) with [independent](/D/ind) observations

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)
$$

and [parameter estimates](/D/est) obtained with [ordinary least squares](/P/mlr-ols)

$$ \label{eq:OLS}
\hat{\beta} = (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \; .
$$

Then, the [signal-to noise ratio](/D/snr) can be expressed in terms of the [coefficient of determination](/D/rsq)

$$ \label{eq:SNR-R2}
\mathrm{SNR} = \frac{R^2}{\mathrm{1-R^2}}
$$

and vice versa

$$ \label{eq:R2-SNR}
R^2 = \frac{\mathrm{SNR}}{\mathrm{1+\mathrm{SNR}}} \; ,
$$

if the predicted signal mean is equal to the actual signal mean.


**Proof:** The signal-to-noise ratio (SNR) [is defined as](/D/snr)

$$ \label{eq:SNR}
\mathrm{SNR} = \frac{\mathrm{Var}(X\hat{\beta})}{\hat{\sigma}^2} = \frac{\mathrm{Var}(\hat{y})}{\hat{\sigma}^2} \; .
$$

Writing out the variances, we have

$$ \label{eq:SNR-s1}
\mathrm{SNR} = \frac{\frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - \bar{\hat{y}})^2}{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2} = \frac{\sum_{i=1}^{n} (\hat{y}_i - \bar{\hat{y}})^2}{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2} \; .
$$

Note that it is irrelevant whether we use the [biased estimator of the variance](/P/resvar-bias) (dividing by $n$) or the [unbiased estimator fo the variance](/P/resvar-unb) (dividing by $n-1$), because the relevant terms cancel out.

If the predicted signal mean is equal to the actual signal mean -- which is the case when variable regressors in $X$ have mean zero, such that they are orthogonal to a constant regressor in $X$ --, this means that $\bar{\hat{y}} = \bar{y}$, such that

$$ \label{eq:SNR-s2}
\mathrm{SNR} = \frac{\sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2}{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2} \; .
$$

Then, the SNR can be written in terms of the [explained](/D/ess), [residual](/D/rss) and [total sum of squares](/D/tss):

$$ \label{eq:SNR-s3}
\mathrm{SNR} = \frac{\mathrm{ESS}}{\mathrm{RSS}} = \frac{\mathrm{ESS}/\mathrm{TSS}}{\mathrm{RSS}/\mathrm{TSS}} \; .
$$

With the [derivation of the coefficient of determination](/P/rsq-der), this becomes

$$ \label{eq:SNR-R2-qed}
\mathrm{SNR} = \frac{R^2}{1-R^2} \; .
$$

Rearranging this equation for the [coefficient of determination](/D/rsq), we have

$$ \label{eq:R2-SNR-qed}
R^2 = \frac{\mathrm{SNR}}{\mathrm{1+\mathrm{SNR}}} \; ,
$$