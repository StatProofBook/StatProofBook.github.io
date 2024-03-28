---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-13 16:18:00

title: "Independence of estimated parameters and residuals in multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Independence of estimated parameters and residuals"

sources:
  - authors: "jld"
    year: 2018
    title: "Understanding t-test for linear regression"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2022-12-13"
    url: "https://stats.stackexchange.com/a/344008"

proof_id: "P393"
shortcut: "mlr-ind"
username: "JoramSoch"
---


**Theorem:** Assume a [linear regression model](/D/mlr) with correlated observations

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

and consider estimation using [weighted least squares](/P/mlr-wls). Then, the [estimated parameters and the vector of residuals](/P/mlr-wlsdist) are independent from each other:

$$ \label{eq:mlr-ind}
\begin{split}
\hat{\beta} &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \quad \text{and} \\ \hat{\varepsilon} &= y - X \hat{\beta} \quad \text{ind.}
\end{split}
$$


**Proof:** Equation \eqref{eq:mlr} [implies the following distribution](/P/mlr-wlsdist) for the [random vector](/D/rvec) $y$:

$$ \label{eq:y-dist}
\begin{split}
y &\sim \mathcal{N}\left( X \beta, \sigma^2 V \right) \\
&\sim \mathcal{N}\left( X \beta, \Sigma \right) \\
\text{with} \quad \Sigma &= \sigma^2 V \; .
\end{split}
$$

Note that the [estimated parameters and residuals can be written as projections from the same random vector](/P/mlr-mat) $y$:

$$ \label{eq:b-proj}
\begin{split}
\hat{\beta} &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \\
&= A y \\
\text{with} \quad A &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1}
\end{split}
$$

$$ \label{eq:e-proj}
\begin{split}
\hat{\varepsilon} &= y - X \hat{\beta} \\
&= (I_n - X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1}) y \\
&= B y \\
\text{with} \quad B &= (I_n - X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1}) \; .
\end{split}
$$

Two projections $AZ$ and $BZ$ from the same [multivariate normal](/D/mvn) [random vector](/D/rvec) $Z \sim \mathcal{N}(\mu, \Sigma)$ [are independent, if and only if the following condition holds](/P/mvn-ind):

$$ \label{eq:mvn-ind}
A \Sigma B^\mathrm{T} = 0 \; .
$$

Combining \eqref{eq:y-dist}, \eqref{eq:b-proj} and \eqref{eq:e-proj}, we check whether this is fulfilled in the present case:

$$ \label{eq:mlr-ind-qed}
\begin{split}
A \Sigma B^\mathrm{T} &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} (\sigma^2 V) (I_n - X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1})^\mathrm{T} \\
&= \sigma^2 \left[ (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} V - (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} V V^{-1} X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} \right] \\
&= \sigma^2 \left[ (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} - (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} \right] \\
&= \sigma^2 \cdot 0_{pn} \\
&= 0 \; .
\end{split}
$$

This demonstrates that $\hat{\beta}$ and $\hat{\varepsilon}$ -- and likewise, all [pairs of terms separately derived](/P/mlr-t) from $\hat{\beta}$ and $\hat{\varepsilon}$ -- are [statistically independent](/D/ind).