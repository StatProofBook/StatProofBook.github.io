---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-07-25 13:41:38

title: "Log-likelihood ratio for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Log-likelihood ratio"

sources:
  - authors: "Ostwald, Dirk"
    year: 2024
    title: "F-Statistiken"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (8), Folien 20-22"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2023/Allgemeines+Lineares+Modell/8_F_Statistiken-p-9972.pdf"

proof_id: "P463"
shortcut: "mlr-llr"
username: "JoramSoch"
---


**Theorem:** Let $y = \left[ y_1, \ldots, y_n \right]^\mathrm{T}$ be an $n \times 1$ [data vector](/D/data) and consider a [linear regression model](/D/mlr) $m_1$ with [design matrix](/D/mlr) $X = \left[ X_0, X_1 \right] \in \mathbb{R}^{n \times p}$ as well as a reduced [linear regression model](/D/mlr) $m_0$ with [design matrix](/D/mlr) $X_0 \in \mathbb{R}^{n \times p_0}$:

$$ \label{eq:m1-m0}
\begin{split}
m_1: \; y &= X \beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \\
m_0: \; y &= X_0 \beta_0 + \varepsilon_0, \; \varepsilon_0 \sim \mathcal{N}(0, \sigma_0^2 V) \; .
\end{split}
$$

Both models use the same [covariance matrix](/D/mlr) $V \in \mathbb{R}^{n \times n}$, but entail potentially different [regression coefficients](/D/mlr) $\beta, \beta_0$ and [noise variances](/D/mlr) $\sigma^2, \sigma_0^2$. Then, the [log-likelihood ratio](/D/llr) for comparing $m_0$ vs. $m_1$ is given by

$$ \label{eq:mlr-llr}
\ln \Lambda_{01} = \frac{n}{2} \ln \left( \frac{\hat{\sigma}^2}{\hat{\sigma}_0^2} \right)
$$

where $\hat{\sigma}^2$ and $\hat{\sigma}_0^2$ are the [maximum likelihood estimates](/D/mle) of the [noise variance](/D/mlr) based on the full model $m_1$ and the reduced model $m_0$, respectively.


**Proof:** The [likelihood ratio](/D/lr) between two models $m_1$ and $m_2$ with model parameters $\theta_1$ and $\theta_2$ and parameter spaces $\Theta_1$ and $\Theta_2$ is defined as the quotient of their [maximized](/D/mle) [likelihood functions](/D/lf):

$$ \label{eq:lr}
\Lambda_{12} = \frac{\operatorname*{max}_{\theta_1 \in \Theta_1} p(y|\theta_1,m_1)}{\operatorname*{max}_{\theta_2 \in \Theta_2} p(y|\theta_2,m_2)} \; .
$$

The [likelihood function](/D/lf) of [multiple linear regression](/D/mlr) is a [multivariate normal probability density function](/P/mvn-pdf):

$$ \label{eq:mlr-lf}
\begin{split}
p(y|\beta,\sigma^2)
&= \mathcal{N}(y; X \beta, \sigma^2 V) \\
&= \sqrt{\frac{1}{(2\pi)^n |\sigma^2 V|}} \cdot \exp\left[ -\frac{1}{2} (y-X\beta)^\mathrm{T} (\sigma^2 V)^{-1} (y-X\beta) \right] \\
&= \sqrt{\frac{1}{(2 \pi \sigma^2)^n |V|}} \cdot \exp\left[ -\frac{1}{2 \sigma^2} (y-X\beta)^\mathrm{T} V^{-1} (y-X\beta) \right]
\end{split}
$$

and the [maximum likelihood estimates for multiple linear regression](/P/mlr-mle) are given by

$$ \label{eq:mlr-mle}
\begin{split}
\hat{\beta}    &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \\
\hat{\sigma}^2 &= \frac{1}{n} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) \; .
\end{split}
$$

Thus, the likelihood ratio comparing $m_0$ vs. $m_1$ is equal to

$$ \label{eq:mlr-lr}
\begin{split}
\Lambda_{01}
&= \frac{p(y|\hat{\beta}_0,\hat{\sigma}_0^2,m_0)}{p(y|\hat{\beta},\hat{\sigma}^2,m_1)} \\
&= \frac{\sqrt{\frac{1}{(2 \pi \hat{\sigma}_0^2)^n |V|}} \cdot \exp\left[ -\frac{1}{2 \hat{\sigma}_0^2} (y - X_0 \hat{\beta}_0)^\mathrm{T} V^{-1} (y - X_0 \hat{\beta}_0) \right]}{\sqrt{\frac{1}{(2 \pi \hat{\sigma}^2)^n |V|}} \cdot \exp\left[ -\frac{1}{2 \hat{\sigma}^2} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) \right]} \\
&= \frac{(2\pi)^{-n/2} (\hat{\sigma}_0^2)^{-n/2} |V|^{-n/2} \cdot \exp\left[ -\frac{1}{2 \hat{\sigma}_0^2} (y - X_0 \hat{\beta}_0)^\mathrm{T} V^{-1} (y - X_0 \hat{\beta}_0) \right]}{(2\pi)^{-n/2} (\hat{\sigma}^2)^{-n/2} |V|^{-n/2} \cdot \exp\left[ -\frac{1}{2 \hat{\sigma}^2} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) \right]} \\
&= \left( \frac{\hat{\sigma}_0^2}{\hat{\sigma}^2} \right)^{-n/2} \cdot \frac{\exp\left[ -\frac{n}{2} \frac{(y - X_0 \hat{\beta}_0)^\mathrm{T} V^{-1} (y - X_0 \hat{\beta}_0)}{(y - X_0 \hat{\beta}_0)^\mathrm{T} V^{-1} (y - X_0 \hat{\beta}_0)} \right]}{\exp\left[ -\frac{n}{2} \frac{(y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta})}{(y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta})} \right]} \\
&= \left( \frac{\hat{\sigma}_0^2}{\hat{\sigma}^2} \right)^{-n/2} \cdot \frac{\exp\left[ -\frac{n}{2} \right]}{\exp\left[ -\frac{n}{2} \right]} \\
&= \left( \frac{\hat{\sigma}_0^2}{\hat{\sigma}^2} \right)^{-n/2} \; .
\end{split}
$$

Logarithmizing both sides, the log-likelihood ratio is obtained as

$$ \label{eq:mlr-llr-qed}
\ln \Lambda_{01}
= \ln \left( \frac{\hat{\sigma}_0^2}{\hat{\sigma}^2} \right)^{-n/2}
=-\frac{n}{2} \ln \left( \frac{\hat{\sigma}_0^2}{\hat{\sigma}^2} \right)
= \frac{n}{2} \ln \left( \frac{\hat{\sigma}^2}{\hat{\sigma}_0^2} \right) \; .
$$