---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-13 10:16:00

title: "t-test for multiple linear regression using contrast-based inference"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Contrast-based t-test"

sources:
  - authors: "Stephan, Klaas Enno"
    year: 2010
    title: "Classical (frequentist) inference"
    in: "Methods and models for fMRI data analysis in neuroeconomics"
    pages: "Lecture 4, Slides 7/9"
    url: "http://www.socialbehavior.uzh.ch/teaching/methodsspring10.html"
  - authors: "Walter, Henrik (ed.)"
    year: 2005
    title: "Datenanalyse für funktionell bildgebende Verfahren"
    in: "Funktionelle Bildgebung in Psychiatrie und Psychotherapie"
    pages: "Schattauer, Stuttgart/New York, 2005, p. 40"
    url: "https://books.google.de/books?id=edWzKAHi7jQC&source=gbs_navlinks_s"
  - authors: "jld"
    year: 2018
    title: "Understanding t-test for linear regression"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2022-12-13"
    url: "https://stats.stackexchange.com/a/344008"
  - authors: "Soch, Joram"
    year: 2020
    title: "Distributional Transformation Improves Decoding Accuracy When Predicting Chronological Age From Structural MRI"
    in: "Frontiers in Psychiatry"
    pages: "vol. 11, art. 604268, eqs. 8/9"
    url: "https://www.frontiersin.org/articles/10.3389/fpsyt.2020.604268/full"
    doi: "10.3389/fpsyt.2020.604268"

proof_id: "P391"
shortcut: "mlr-t"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr)

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

and a [t-contrast](/D/tcon) on the model parameters

$$ \label{eq:tcon}
\gamma = c^\mathrm{T} \beta \quad \text{where} \quad c \in \mathbb{R}^{p \times 1} \; .
$$

Then, the [test statistic](/D/tstat)

$$ \label{eq:mlr-t}
t = \frac{c^\mathrm{T} \hat{\beta}}{\sqrt{\hat{\sigma}^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}}
$$

with the [parameter estimates](/P/mlr-mle)

$$ \label{eq:mlr-est}
\begin{split}
\hat{\beta} &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \\
\hat{\sigma}^2 &= \frac{1}{n-p} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta})
\end{split}
$$

follows a [t-distribution](/D/t)

$$ \label{eq:mlr-t-dist}
t \sim \mathrm{t}(n-p)
$$

under the [null hypothesis](/D/h0)

$$ \label{eq:mlr-t-h0}
\begin{split}
H_0: &\; c^\mathrm{T} \beta = 0 \\
H_1: &\; c^\mathrm{T} \beta > 0 \; .
\end{split}
$$


**Proof:**

1) We know that [the estimated regression coefficients in linear regression follow a multivariate normal distribution](/P/mlr-wlsdist):

$$ \label{eq:b-est-dist}
\hat{\beta} \sim \mathcal{N}\left( \beta, \, \sigma^2 (X^\mathrm{T} V^{-1} X)^{-1} \right) \; .
$$

Thus, the [estimated contrast value](/D/tcon) $\hat{\gamma} = c^\mathrm{T} \hat{\beta}$ is [distributed according to a univariate normal distribution](/P/mvn-ltt):

$$ \label{eq:g-est-dist}
\hat{\gamma} \sim \mathcal{N}\left( c^\mathrm{T} \beta, \, \sigma^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c \right) \; .
$$

Now, define the random variable $z$ by dividing $\hat{\gamma}$ by its standard deviation:

$$ \label{eq:z}
z = \frac{c^\mathrm{T} \hat{\beta}}{\sqrt{\sigma^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}} \; .
$$

Again applying the [linear transformation theorem](/P/mvn-ltt), this is distributed as

$$ \label{eq:z-dist}
z \sim \mathcal{N}\left( \frac{c^\mathrm{T} \beta}{\sqrt{\sigma^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}}, \, 1 \right)
$$

and thus follows a [standard normal distribution](/D/snorm) under the [null hypothesis](/D/h0):

$$ \label{eq:z-dist-h0}
z \sim \mathcal{N}(0, 1), \quad \text{if} \; H_0 \; .
$$

2) We also know that the [residual sum of squares](/D/rss), divided the [true error variance](/D/mlr)

$$ \label{eq:mlr-rss}
v = \frac{1}{\sigma^2} \sum_{i=1}^{n} \hat{\varepsilon}_i^2 = \frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{\sigma^2} = \frac{1}{\sigma^2} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta})
$$

[is following a chi-squared distribution](/P/mlr-rssdist):

$$ \label{eq:mlr-rss-dist}
v \sim \chi^2(n-p) \; .
$$

3) Because [the estimated regression coefficients and the vector of residuals are independent from each other](/P/mlr-ind)

$$ \label{eq:mlr-ind-v1}
\hat{\beta} \quad \text{and} \quad \hat{\varepsilon} \quad \text{ind.}
$$

and thus, the estimated contrast values are also independent from the function of the residual sum of squares

$$ \label{eq:mlr-ind-v2}
z = \frac{c^\mathrm{T} \hat{\beta}}{\sqrt{\sigma^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}} \quad \text{and} \quad v = \frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{\sigma^2} \quad \text{ind.} \; ,
$$

the following quantity [is, by definition, t-distributed](/D/t)

$$ \label{eq:mlr-t-s1}
t = \frac{z}{\sqrt{v/(n-p)}} \sim \mathrm{t}(n-p), \quad \text{if} \; H_0
$$

and the quantity can be evaluated as:

$$ \label{eq:mlr-t-s2}
\begin{split}
t &\overset{\eqref{eq:mlr-t-s1}}{=} \frac{z}{\sqrt{v/(n-p)}} \\
&\overset{\eqref{eq:mlr-ind-v2}}{=} \frac{c^\mathrm{T} \hat{\beta}}{\sqrt{\sigma^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}} \cdot \sqrt{\frac{n-p}{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon} / \sigma^2}} \\
&= \frac{c^\mathrm{T} \hat{\beta}}{\sqrt{\frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{n-p} \cdot c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}} \\
&\overset{\eqref{eq:mlr-rss}}{=} \frac{c^\mathrm{T} \hat{\beta}}{\sqrt{\frac{(y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta})}{n-p} \cdot c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}} \\
&\overset{\eqref{eq:mlr-est}}{=} \frac{c^\mathrm{T} \hat{\beta}}{\sqrt{\hat{\sigma}^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}} \; .
\end{split}
$$

This means that the [null hypothesis](/D/h0) in \eqref{eq:mlr-t-h0} can be rejected when $t$ from \eqref{eq:mlr-t-s2} is as extreme or more extreme than the [critical value](/D/cval) obtained from [Student's t-distribution](/D/t) with $n-p$ [degrees of freedom](/D/dof) using a [significance level](/D/alpha) $\alpha$.