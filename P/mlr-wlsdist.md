---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-13 05:13:00

title: "Distributions of estimated parameters, fitted signal and residuals in multiple linear regression upon weighted least squares"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Distribution of estimated parameters, signal and residuals"

sources:
  - authors: "Koch, Karl-Rudolf"
    year: 2007
    title: "Linear Model"
    in: "Introduction to Bayesian Statistics"
    pages: "Springer, Berlin/Heidelberg, 2007, ch. 4, eqs. 4.2, 4.30"
    url: "https://www.springer.com/de/book/9783540727231"
    doi: "10.1007/978-3-540-72726-2"
  - authors: "Penny, William"
    year: 2006
    title: "Multiple Regression"
    in: "Mathematics for Brain Imaging"
    pages: "ch. 1.5, pp. 39-41, eqs. 1.106-1.110"
    url: "https://ueapsylabs.co.uk/sites/wpenny/mbi/mbi_course.pdf"
  - authors: "Soch J, Allefeld C, Haynes JD"
    year: 2020
    title: "Inverse transformed encoding models – a solution to the problem of correlated trial-by-trial parameter estimates in fMRI decoding"
    in: "NeuroImage"
    pages: "vol. 209, art. 116449, eq. A.10"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811919310407"
    doi: "10.1016/j.neuroimage.2019.116449"
  - authors: "Soch J, Meyer AP, Allefeld C, Haynes JD"
    year: 2017
    title: "How to improve parameter estimates in GLM-based fMRI data analysis: cross-validated Bayesian model averaging"
    in: "NeuroImage"
    pages: "vol. 158, pp. 186-195, eq. A.2"
    url: "https://www.sciencedirect.com/science/article/pii/S105381191730527X"
    doi: "10.1016/j.neuroimage.2017.06.056"

proof_id: "P389"
shortcut: "mlr-wlsdist"
username: "JoramSoch"
---


**Theorem:** Assume a [linear regression model](/D/mlr) with correlated observations

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

and consider estimation using [weighted least squares](/P/mlr-wls). Then, the estimated parameters, fitted signal and residuals are distributed as

$$ \label{eq:mlr-dist}
\begin{split}
\hat{\beta} &\sim \mathcal{N}\left( \beta, \sigma^2 (X^\mathrm{T} V^{-1} X)^{-1} \right) \\
\hat{y} &\sim \mathcal{N}\left( X \beta, \sigma^2 (PV) \right) \\
\hat{\varepsilon} &\sim \mathcal{N}\left( 0, \sigma^2 (I_n - P) V \right)
\end{split}
$$

where $P$ is the [projection matrix](/D/pmat) for [weighted least squares](/P/mlr-wls)

$$ \label{eq:mlr-pmat}
P = X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} \; .
$$


**Proof:** We will use the [linear transformation theorem for the multivariate normal distribution](/P/mvn-ltt):

$$ \label{eq:mvn-ltt}
x \sim \mathcal{N}(\mu, \Sigma) \quad \Rightarrow \quad y = Ax + b \sim \mathcal{N}(A\mu + b, A \Sigma A^\mathrm{T}) \; .
$$

Applying \eqref{eq:mvn-ltt} to \eqref{eq:mlr}, the measured data are distributed as

$$ \label{eq:y-dist}
y \sim \mathcal{N}\left( X \beta, \sigma^2 V \right) \; .
$$

1) The [parameter estimates from weighted least sqaures](/P/mlr-wls) are given by

$$ \label{eq:b-est}
\hat{\beta} = (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y
$$

and thus, by applying \eqref{eq:mvn-ltt} to \eqref{eq:b-est}, they are distributed as

$$ \label{eq:b-est-dist}
\begin{split}
\hat{\beta} &\sim \mathcal{N}\left( \left[ (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} \right] X \beta, \, \sigma^2 \left[ (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} \right] V \left[ V^{-1} X (X^\mathrm{T} V^{-1} X)^{-1} \right] \right) \\
&\sim \mathcal{N}\left( \beta, \, \sigma^2 (X^\mathrm{T} V^{-1} X)^{-1} \right) \; .
\end{split}
$$

2) The [fitted signal in multiple linear regression](/P/mlr-mat) is given by

$$ \label{eq:y-est}
\hat{y} = X \hat{\beta} = X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y = P y
$$

and thus, by applying \eqref{eq:mvn-ltt} to \eqref{eq:y-est}, they are distributed as

$$ \label{eq:y-est-dist}
\begin{split}
\hat{y} &\sim \mathcal{N}\left( X \beta, \, \sigma^2 X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} \right) \\
&\sim \mathcal{N}\left( X \beta, \, \sigma^2 (PV) \right) \; .
\end{split}
$$

3) The [residuals of the linear regression model](/P/mlr-mat) are given by

$$ \label{eq:e-est}
\hat{\varepsilon} = y - X \hat{\beta} = \left( I_n - X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} \right) y = \left( I_n - P \right) y
$$

and thus, by applying \eqref{eq:mvn-ltt} to \eqref{eq:e-est}, they are distributed as

$$ \label{eq:e-est-dist}
\begin{split}
\hat{\varepsilon} &\sim \mathcal{N}\left( \left[ I_n - X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} \right] X \beta, \, \sigma^2 \left[ I_n - P \right] V \left[ I_n - P \right]^\mathrm{T} \right) \\
&\sim \mathcal{N}\left( X \beta - X \beta, \, \sigma^2 \left[ V - V P^\mathrm{T} - P V + P V P^\mathrm{T} \right] \right) \\
&\sim \mathcal{N}\left( 0, \, \sigma^2 \left[ V - V V^{-1} X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} - X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} V + P V P^\mathrm{T} \right] \right) \\
&\sim \mathcal{N}\left( 0, \, \sigma^2 \left[ V - 2 P + X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} V V^{-1} X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} \right] \right) \\
&\sim \mathcal{N}\left( 0, \, \sigma^2 \left[ V - 2 P + P \right] \right) \\
&\sim \mathcal{N}\left( 0, \, \sigma^2 \left[ V - X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} \right] \right) \\
&\sim \mathcal{N}\left( 0, \, \sigma^2 \left[ I_n - P \right] V \right) \; .
\end{split}
$$