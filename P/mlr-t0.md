---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-08-28 12:30:59

title: "Contrast-based t-test with null hypothesis parameter for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "t-test with null parameter"

sources:
  - authors: "Ostwald D, Soch J"
    year: 2026
    title: "T-Statistiken"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (7), Folien 20-22"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre/Sommersemester+2026/Allgemeines+Lineares+Modell/07_T_Statistiken-p-13981.pdf"

proof_id: "P549"
shortcut: "mlr-t0"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr)

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; ,
$$

a [t-contrast](/D/tcon) on the model parameters

$$ \label{eq:tcon}
\gamma = c^\mathrm{T} \beta \quad \text{where} \quad c \in \mathbb{R}^p
$$

and the [parameter estimates](/P/mlr-mle)

$$ \label{eq:mlr-est}
\begin{split}
\hat{\beta} &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \\
\hat{\sigma}^2 &= \frac{1}{n-p} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) \; .
\end{split}
$$

Then, the [test statistic](/D/tstat)

$$ \label{eq:mlr-t0}
t = \frac{c^\mathrm{T} \hat{\beta} - \mu_0}{\sqrt{\hat{\sigma}^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}}
$$

follows a [t-distribution](/D/t)

$$ \label{eq:mlr-t0-dist}
t \sim \mathrm{t}(n-p)
$$

under the [null hypothesis](/D/h0)

$$ \label{eq:mlr-t0-h0}
H_0: \; c^\mathrm{T} \beta = \mu_0
\quad \Leftrightarrow \quad
c^\mathrm{T} \beta - \mu_0 = 0 \; .
$$


**Proof:**

1) We know that [the estimated regression coefficients in linear regression follow a multivariate normal distribution](/P/mlr-wlsdist):

$$ \label{eq:b-est-dist}
\hat{\beta} \sim \mathcal{N}\left( \beta, \, \sigma^2 (X^\mathrm{T} V^{-1} X)^{-1} \right) \; .
$$

Thus, the quantity $\hat{\delta} = \hat{\gamma} - \mu_0 = c^\mathrm{T} \hat{\beta} - \mu_0$ is [distributed according to a univariate normal distribution](/P/mvn-ltt):

$$ \label{eq:g-est-dist}
\hat{\delta} \sim \mathcal{N}\left( c^\mathrm{T} \beta - \mu_0, \, \sigma^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c \right) \; .
$$

Now, define the random variable $z$ by dividing $\hat{\delta}$ by its standard deviation:

$$ \label{eq:z}
z = \frac{c^\mathrm{T} \hat{\beta} - \mu_0}{\sqrt{\sigma^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}} \; .
$$

Again applying the [linear transformation theorem](/P/mvn-ltt), this is distributed as

$$ \label{eq:z-dist}
z \sim \mathcal{N}\left( \frac{c^\mathrm{T} \beta - \mu_0}{\sqrt{\sigma^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}}, \, 1 \right)
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

3) Because [the estimated regression coefficients and the residuals are independent from each other](/P/mlr-ind)

$$ \label{eq:mlr-ind-v1}
\hat{\beta} \quad \text{and} \quad \hat{\varepsilon} \quad \text{ind.}
$$

and thus, the [random variables](/D/rvar) $z$ and $v$ are also [independent](/D/ind)

$$ \label{eq:mlr-ind-v2}
z = \frac{c^\mathrm{T} \hat{\beta}}{\sqrt{\sigma^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}} \quad \text{and} \quad v = \frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{\sigma^2} \quad \text{ind.} \; ,
$$

the following quantity [is, by definition, t-distributed](/D/t)

$$ \label{eq:mlr-t0-s1}
t = \frac{z}{\sqrt{v/(n-p)}} \sim \mathrm{t}(n-p), \quad \text{if} \; H_0
$$

and the quantity can be evaluated as:

$$ \label{eq:mlr-t0-s2}
\begin{split}
t &\overset{\eqref{eq:mlr-t0-s1}}{=} \frac{z}{\sqrt{v/(n-p)}} \\
&\overset{\eqref{eq:mlr-ind-v2}}{=} \frac{c^\mathrm{T} \hat{\beta} - \mu_0}{\sqrt{\sigma^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}} \cdot \sqrt{\frac{n-p}{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon} / \sigma^2}} \\
&= \frac{c^\mathrm{T} \hat{\beta} - \mu_0}{\sqrt{\frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{n-p} \cdot c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}} \\
&\overset{\eqref{eq:mlr-rss}}{=} \frac{c^\mathrm{T} \hat{\beta} - \mu_0}{\sqrt{\frac{(y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta})}{n-p} \cdot c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}} \\
&\overset{\eqref{eq:mlr-est}}{=} \frac{c^\mathrm{T} \hat{\beta} - \mu_0}{\sqrt{\hat{\sigma}^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}} \; .
\end{split}
$$

This means that the [null hypothesis](/D/h0) in \eqref{eq:mlr-t0-h0} can be rejected when $t$ from \eqref{eq:mlr-t0-s2} is as extreme or more extreme than the [critical value](/D/cval) obtained from [Student's t-distribution](/D/t) with $n-p$ [degrees of freedom](/D/dof) using a [significance level](/D/alpha) $\alpha$.