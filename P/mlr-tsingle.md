---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-05-03 14:37:33

title: "Specific t-test for single regressor in multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "t-test for single regressor"

sources:
  - authors: "Ostwald, Dirk"
    year: 2023
    title: "T-Statistiken"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (7), Folien 20, 27"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2023/Allgemeines+Lineares+Modell/7_T_Statistiken-p-9968.pdf"

proof_id: "P450"
shortcut: "mlr-tsingle"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr)

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

using the $n \times p$ design matrix $X$ and the [parameter estimates](/P/mlr-mle)

$$ \label{eq:mlr-est}
\begin{split}
\hat{\beta} &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \\
\hat{\sigma}^2 &= \frac{1}{n-p} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) \; .
\end{split}
$$

Then, the [test statistic](/D/tstat)

$$ \label{eq:mlr-t-single}
t_j = \frac{\hat{\beta}_j}{\sqrt{\left( \hat{\varepsilon}^\mathrm{T} V^{-1} \hat{\varepsilon} \right)/(n-p) \; \sigma_{jj}}}
$$

with the $n \times 1$ [vector of residuals](/P/mlr-mat)

$$ \label{eq:mlr-eps-est}
\hat{\varepsilon} = y - X\hat{\beta}
$$

and $\sigma_{jj}$ equal to the $j$-th diagonal element of the [parameter covariance matrix](/P/mlr-wlsdist)

$$ \label{eq:mlr-t-single-sig}
\sigma_{jj} = \left[ \left( X^\mathrm{T} V^{-1} X \right)^{-1} \right]_{jj}
$$

follows a [t-distribution](/D/t)

$$ \label{eq:mlr-t-single-dist}
t_j \sim \mathrm{t}(n-p)
$$

under the [null hypothesis](/D/h0) that the $j$-th [regression coefficient](/D/mlr) is zero:

$$ \label{eq:mlr-t-single-h0}
H_0: \; \beta_j = 0 \; .
$$


**Proof:** This is a special case of the [contrast-based t-test for multiple linear regression](/P/mlr-t) based on the following [t-statistic](/D/t):

$$ \label{eq:mlr-t}
t = \frac{c^\mathrm{T} \hat{\beta}}{\sqrt{\hat{\sigma}^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}} \sim \mathrm{t}(n-p) \; .
$$

In this special case, the [contrast vector](/D/tcon) is equal to the $j$-th elementary vector $e_j$ (a $p \times 1$ vector of zeros, with a single $1$ in the $j$-th entry)

$$ \label{eq:mlr-t-single-con}
c = e_j = \left[ 0, \ldots, 0, 1, 0, \ldots, 0 \right]^\mathrm{T} \; ,
$$

such that the null hypothesis is given by

$$ \label{eq:mlr-t-single-h0-qed}
H_0: \; c^\mathrm{T} \beta = e_j^\mathrm{T} \beta = \beta_j = 0
$$

and the test statistic becomes

$$ \label{eq:mlr-t-single-qed}
\begin{split}
t_j &= \frac{e_j^\mathrm{T} \hat{\beta}}{\sqrt{\hat{\sigma}^2 e_j^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} e_j}} \\
&= \frac{\left[ 0, \ldots, 0, 1, 0, \ldots, 0 \right] \left[ \hat{\beta}_1, \ldots, \beta_{j-1}, \beta_j, \beta_{j+1}, \ldots, \hat{\beta}_p \right]^\mathrm{T}}{\sqrt{\frac{1}{n-p} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) \left[ 0, \ldots, 1, \ldots, 0 \right] (X^\mathrm{T} V^{-1} X)^{-1} \left[ 0, \ldots, 1, \ldots, 0 \right]^\mathrm{T}}} \\
&= \frac{\hat{\beta}_j}{\sqrt{\frac{1}{n-p} \left( \hat{\varepsilon}^\mathrm{T} V^{-1} \hat{\varepsilon} \right) \left[ \left( X^\mathrm{T} V^{-1} X \right)^{-1} \right]_{jj}}} \\
&= \frac{\hat{\beta}_j}{\sqrt{\left( \hat{\varepsilon}^\mathrm{T} V^{-1} \hat{\varepsilon} \right)/(n-p) \; \sigma_{jj}}} \; .
\end{split}
$$