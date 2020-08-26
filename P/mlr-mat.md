---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-09 21:18:00

title: "Transformation matrices for ordinary least squares"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Estimation, projection and residual-forming matrix"

sources:
  - authors: "Stephan, Klaas Enno"
    year: 2010
    title: "The General Linear Model (GLM)"
    in: "Methods and models for fMRI data analysis in neuroeconomics"
    pages: "Lecture 3, Slide 10"
    url: "http://www.socialbehavior.uzh.ch/teaching/methodsspring10.html"

proof_id: "P75"
shortcut: "mlr-mat"
username: "JoramSoch"
---


**Theorem:** Assume a [linear regression model](/D/mlr) with independent observations

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)
$$

and consider estimation using [ordinary least squares](/P/mlr-ols). Then, the estimated parameters, fitted signal and residuals are given by

$$ \label{eq:mlr-est}
\begin{split}
\hat{\beta} &= E y \\
\hat{y} &= P y \\
\hat{\varepsilon} &= R y
\end{split}
$$

where 

$$ \label{eq:mlr-mat}
\begin{split}
E &= (X^\mathrm{T} X)^{-1} X^\mathrm{T} \\
P &= X (X^\mathrm{T} X)^{-1} X^\mathrm{T} \\
R &= I_n - X (X^\mathrm{T} X)^{-1} X^\mathrm{T}
\end{split}
$$

are the [estimation matrix](/D/emat), [projection matrix](/D/pmat) and [residual-forming matrix](/D/rfmat) and $n$ is the number of observations.


**Proof:**

1) Ordinary least squares parameter estimates of $\beta$ are defined as minimizing the [residual sum of squares](/D/rss)

$$ \label{eq:ols}
\hat{\beta} = \operatorname*{arg\,min}_{\beta} \left[ (y-X\beta)^\mathrm{T} (y-X\beta) \right]
$$

and the [solution to this](/P/mlr-ols) is given by

$$ \label{eq:b-est-qed}
\begin{split}
\hat{\beta} &= (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \\
&\overset{\eqref{eq:mlr-mat}}{=} E y \; .
\end{split}
$$

<br>
2) The fitted signal is given by multiplying the design matrix with the estimated regression coefficients

$$ \label{eq:y-est}
\hat{y} = X\hat{\beta}
$$

and using \eqref{eq:b-est-qed}, this becomes

$$ \label{eq:y-est-qed}
\begin{split}
\hat{y} &= X (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \\
&\overset{\eqref{eq:mlr-mat}}{=} P y \; .
\end{split}
$$

<br>
3) The residuals of the model are calculated by subtracting the fitted signal from the measured signal

$$ \label{eq:e-est}
\hat{\varepsilon} = y - \hat{y}
$$

and using \eqref{eq:y-est-qed}, this becomes

$$ \label{eq:e-est-qed}
\begin{split}
\hat{\varepsilon} &= y - X (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \\
&= (I_n - X (X^\mathrm{T} X)^{-1} X^\mathrm{T}) y \\
&\overset{\eqref{eq:mlr-mat}}{=} R y \; .
\end{split}
$$