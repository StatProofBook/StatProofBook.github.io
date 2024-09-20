---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-23 16:36:00

title: "Distributions of estimated parameters, fitted signal and residuals in multiple linear regression upon ordinary least squares"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Distribution of OLS estimates, signal and residuals"

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
  - authors: "Ostwald, Dirk"
    year: 2023
    title: "Modellformulierung"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (5), Folie 14"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2023/Allgemeines+Lineares+Modell/5_Modellformulierung.pdf"
  - authors: "Ostwald, Dirk"
    year: 2023
    title: "Parameterschätzung"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (6), Folien 10-12"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2023/Allgemeines+Lineares+Modell/6_Parametersch%C3%A4tzung.pdf"

proof_id: "P400"
shortcut: "mlr-olsdist"
username: "JoramSoch"
---


**Theorem:** Assume a [linear regression model](/D/mlr) with independent observations

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)
$$

and consider estimation using [ordinary least squares](/P/mlr-ols). Then, the estimated parameters, fitted signal and residuals are distributed as

$$ \label{eq:mlr-dist}
\begin{split}
\hat{\beta} &\sim \mathcal{N}\left( \beta, \sigma^2 (X^\mathrm{T} X)^{-1} \right) \\
\hat{y} &\sim \mathcal{N}\left( X \beta, \sigma^2 P \right) \\
\hat{\varepsilon} &\sim \mathcal{N}\left( 0, \sigma^2 (I_n - P) \right)
\end{split}
$$

where $P$ is the [projection matrix](/D/pmat) for [ordinary least squares](/P/mlr-ols)

$$ \label{eq:mlr-pmat}
P = X (X^\mathrm{T} X)^{-1} X^\mathrm{T} \; .
$$


**Proof:** We will use the [linear transformation theorem for the multivariate normal distribution](/P/mvn-ltt):

$$ \label{eq:mvn-ltt}
x \sim \mathcal{N}(\mu, \Sigma) \quad \Rightarrow \quad y = Ax + b \sim \mathcal{N}(A\mu + b, A \Sigma A^\mathrm{T}) \; .
$$

The distributional assumption in \eqref{eq:mlr} [is equivalent to](/P/mvn-ind):

$$ \label{eq:mlr-vect}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 I_n) \; .
$$

Applying \eqref{eq:mvn-ltt} to \eqref{eq:mlr-vect}, the measured data are distributed as

$$ \label{eq:y-dist}
y \sim \mathcal{N}\left( X \beta, \sigma^2 I_n \right) \; .
$$

1) The [parameter estimates from ordinary least sqaures](/P/mlr-ols) are given by

$$ \label{eq:b-est}
\hat{\beta} = (X^\mathrm{T} X)^{-1} X^\mathrm{T} y
$$

and thus, by applying \eqref{eq:mvn-ltt} to \eqref{eq:b-est}, they are distributed as

$$ \label{eq:b-est-dist}
\begin{split}
\hat{\beta} &\sim \mathcal{N}\left( \left[ (X^\mathrm{T} X)^{-1} X^\mathrm{T} \right] X \beta, \, \sigma^2 \left[ (X^\mathrm{T} X)^{-1} X^\mathrm{T} \right] I_n \left[ X (X^\mathrm{T} X)^{-1} \right] \right) \\
&\sim \mathcal{N}\left( \beta, \, \sigma^2 (X^\mathrm{T} X)^{-1} \right) \; .
\end{split}
$$

2) The [fitted signal in multiple linear regression](/P/mlr-mat) is given by

$$ \label{eq:y-est}
\hat{y} = X \hat{\beta} = X (X^\mathrm{T} X)^{-1} X^\mathrm{T} y = P y
$$

and thus, by applying \eqref{eq:mvn-ltt} to \eqref{eq:y-est}, they are distributed as

$$ \label{eq:y-est-dist}
\begin{split}
\hat{y} &\sim \mathcal{N}\left( X \beta, \, \sigma^2 X (X^\mathrm{T} X)^{-1} X^\mathrm{T} \right) \\
&\sim \mathcal{N}\left( X \beta, \, \sigma^2 P \right) \; .
\end{split}
$$

3) The [residuals of the linear regression model](/P/mlr-mat) are given by

$$ \label{eq:e-est}
\hat{\varepsilon} = y - X \hat{\beta} = \left( I_n - X (X^\mathrm{T} X)^{-1} X^\mathrm{T} \right) y = \left( I_n - P \right) y
$$

and thus, by applying \eqref{eq:mvn-ltt} to \eqref{eq:e-est}, they are distributed as

$$ \label{eq:e-est-dist-s1}
\begin{split}
\hat{\varepsilon} &\sim \mathcal{N}\left( \left[ I_n - X (X^\mathrm{T} X)^{-1} X^\mathrm{T} \right] X \beta, \, \sigma^2 \left[ I_n - P \right] I_n \left[ I_n - P \right]^\mathrm{T} \right) \\
&\sim \mathcal{N}\left( X \beta - X \beta, \, \sigma^2 \left[ I_n - P \right] \left[ I_n - P \right]^\mathrm{T} \right) \; .
\end{split}
$$

Because the [residual-forming matrix](/D/rfmat) is [symmetric](/P/mlr-symm) and [idempotent](/P/mlr-idem), this becomes:

$$ \label{eq:e-est-dist-s2}
\hat{\varepsilon} \sim \mathcal{N}\left( 0, \sigma^2 (I_n - P) \right) \; .
$$