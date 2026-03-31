---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-03-26 15:43:00

title: "Conditional correlation of random variables which are jointly multivariate normally distributed"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Conditional correlation"

sources:
  - authors: "Ostwald D, Soch J"
    year: 2025
    title: "Partielle Korrelation"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (12), Folien 13-14"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2025/Allgemeines+Lineares+Modell/12_Partielle_Korrelation.pdf"

proof_id: "P529"
shortcut: "mvn-corrcond"
username: "JoramSoch"
---


**Theorem:** Let $X$, $Y$ and $Z$ be [random variables](/D/rvar) jointly following a [multivariate normal distribution](/D/mvn):

$$ \label{eq:V}
V =    \left[ \begin{matrix} X \\ Y \\ Z \end{matrix} \right]
  \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, the [conditional correlation](/D/corr-cond) of $X$ and $Y$ given $Z$ can be computed as

$$ \label{eq:mvn-corr-cond}
\mathrm{Corr}(X,Y|Z) = \frac{\rho_{XY} - \rho_{XZ} \rho_{YZ}}{\sqrt{1-\rho_{XZ}^2} \sqrt{1-\rho_{YZ}^2}}
$$

where $\rho_{XY}$, $\rho_{XZ}$ and $\rho_{YZ}$ are the [pairwise correlations](/D/corr) of the random variables $X$, $Y$ and $Z$.


**Proof:** In the first part of the proof, we will justify that we can work with a simplified form for $\Sigma$. In the second part of the proof, we will compute the conditional correlation, as implied by its definition, from $\Sigma$.

1) We will denote the entries of $\Sigma$ as follows:

$$ \label{eq:Sigma}
\Sigma = \left[ \begin{matrix} \sigma_X^2 & \sigma_{XY} & \sigma_{XZ} \\ \sigma_{YX} & \sigma_Y^2 & \sigma_{YZ} \\ \sigma_{ZX} & \sigma_{ZY} & \sigma_Z^2 \end{matrix} \right]
$$

where $\sigma_X^2$, $\sigma_Y^2$ and $\sigma_Z^2$ are the [variances](/D/var) and $\sigma_{XY}$, $\sigma_{XZ}$ and $\sigma_{YZ}$ are the [covariances](/D/cov) of [the entries of the random vector](/P/mvn-cov) $V$. Define the following matrix:

$$ \label{eq:A}
A = \left[ \begin{matrix} \frac{1}{\sigma_X} & 0 & 0 \\ 0 & \frac{1}{\sigma_Y} & 0 \\ 0 & 0 & \frac{1}{\sigma_Z} \end{matrix} \right] \; .
$$

With the [linear transformation theorem for the multivariate normal distribution](/P/mvn-ltt), the distribution of $W = AV$ is

$$ \label{eq:W}
W = AV = \left[ \begin{matrix} X/\sigma_X \\ Y/\sigma_Y \\ Z/\sigma_Z \end{matrix} \right]
  \sim \mathcal{N}(A \mu, A \Sigma A^\mathrm{T})
$$

with

$$ \label{eq:A-Sigma-A}
  A \Sigma A^\mathrm{T}
= \left[ \begin{matrix} \frac{\sigma_X^2}{\sigma_X \sigma_X} & \frac{\sigma_{XY}}{\sigma_X \sigma_Y} & \frac{\sigma_{XZ}}{\sigma_X \sigma_Z} \\ \frac{\sigma_{YX}}{\sigma_Y \sigma_X} & \frac{\sigma_Y^2}{\sigma_Y \sigma_Y} & \frac{\sigma_{YZ}}{\sigma_Y \sigma_Z} \\ \frac{\sigma_{ZX}}{\sigma_Z \sigma_X} & \frac{\sigma_{ZY}}{\sigma_Z \sigma_Y} & \frac{\sigma_Z^2}{\sigma_Z \sigma_Z} \end{matrix} \right]
= \left[ \begin{matrix} 1 & \rho_{XY} & \rho_{XZ} \\ \rho_{YX} & 1 & \rho_{YZ} \\ \rho_{ZX} & \rho_{ZY} & 1 \end{matrix} \right] \; .
$$

Since [correlation is invariant under linear transformation](/P/corr-inv), the entries of $V$ and $W$ have the same pairwise correlations and conditional correlations. Thus, for the above theorem, we can assume without loss of generality that

$$ \label{eq:Sigma-wlog}
\Sigma = \left[ \begin{matrix} 1 & \rho_{XY} & \rho_{XZ} \\ \rho_{YX} & 1 & \rho_{YZ} \\ \rho_{ZX} & \rho_{ZY} & 1 \end{matrix} \right] \; .
$$

2) The theorem about [conditional distributions of the multivariate normal distribution](/P/mvn-cond) states that

$$ \label{eq:mvn-cond}
X \sim \mathcal{N}(\mu, \Sigma)
\quad \Rightarrow \quad
X_1|X_2 \sim \mathcal{N}(\mu_{1|2}, \Sigma_{1|2})
$$

with

$$ \label{eq:mvn-cond-para}
\begin{split}
\mu_{1|2}    &= \mu_1 + \Sigma_{12} \Sigma_{22}^{-1} (X_2 - \mu_2) \\
\Sigma_{1|2} &= \Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21}
\end{split}
$$

where

$$ \label{eq:mvn-joint-para}
\mu    = \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right]
\quad \text{and} \quad
\Sigma = \left[ \begin{matrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{matrix} \right] \; .
$$

With that, we can derive the [conditional distribution](/D/dist-cond) of $X$ and $Y$ given $Z$. Specifically, the conditional [covariance matrix](/D/covmat) can be computed as follows:

$$ \label{eq:Sigma-cond}
\begin{split}
   \Sigma_{X,Y|Z}
&= \Sigma_{XY} - \Sigma_{XY,Z} \Sigma_{Z}^{-1} \Sigma_{Z,XY} \\
&= \left[ \begin{matrix} 1 & \rho_{XY} \\ \rho_{YX} & 1 \end{matrix} \right]
 - \left[ \begin{matrix} \rho_{XZ} \\ \rho_{YZ} \end{matrix} \right]
   \left[ \begin{matrix} 1 \end{matrix} \right]^{-1}
   \left[ \begin{matrix} \rho_{ZX} & \rho_{ZY} \end{matrix} \right] \\
&= \left[ \begin{matrix} 1 & \rho_{XY} \\ \rho_{YX} & 1 \end{matrix} \right]
 - \left[ \begin{matrix} \rho_{XZ} \rho_{ZX} & \rho_{XZ} \rho_{ZY} \\ \rho_{YZ} \rho_{ZX} & \rho_{YZ} \rho_{ZY} \end{matrix} \right] \\
&= \left[ \begin{matrix} 1 - \rho_{XZ}^2 & \rho_{XY} - \rho_{XZ} \rho_{YZ} \\ \rho_{XY} - \rho_{XZ} \rho_{YZ} & 1 - \rho_{YZ}^2 \end{matrix} \right]
 = \left[ \begin{matrix} \sigma_{X|Z}^2 & \sigma_{X,Y|Z} \\ \sigma_{X,Y|Z} & \sigma_{Y|Z}^2 \end{matrix} \right]
\end{split}
$$

With that, we can derive the [conditional correlation](/D/corr-cond) of $X$ and $Y$ given $Z$. Specifically, dividing the covariance of the conditional distribution by the product of its standard deviations, we get:

$$ \label{eq:mvn-corr-cond-qed}
\begin{split}
   \mathrm{Corr}(X,Y|Z)
&= \frac{\mathrm{Cov}(X,Y|Z)}{\sqrt{\mathrm{Var}(X|Z)} \sqrt{\mathrm{Var}(Y|Z)}} \\
&= \frac{\sigma_{X,Y|Z}}{\sigma_{X|Z} \sigma_{Y|Z}} \\
&= \frac{\rho_{XY} - \rho_{XZ} \rho_{YZ}}{\sqrt{1-\rho_{XZ}^2} \sqrt{1-\rho_{YZ}^2}} \; .
\end{split}
$$