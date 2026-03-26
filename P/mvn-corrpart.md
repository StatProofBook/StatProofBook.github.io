---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-03-26 17:37:00

title: "Partial correlation of random variables which are jointly multivariate normal distributed"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Partial correlation"

sources:
  - authors: "Ostwald D, Soch J"
    year: 2025
    title: "Partielle Korrelation"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (12), Folien 19-22"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2025/Allgemeines+Lineares+Modell/12_Partielle_Korrelation.pdf"

proof_id: "P530"
shortcut: "mvn-corrpart"
username: "JoramSoch"
---


**Theorem:** Let $X$, $Y$ and $Z$ be [random variables](/D/rvar) jointly following a [multivariate normal distribution](/D/mvn):

$$ \label{eq:V}
V =    \left[ \begin{matrix} X \\ Y \\ Z \end{matrix} \right]
  \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, the [partial correlation](/D/corr-part) of $X$ and $Y$ controlling for $Z$ can be computed as

$$ \label{eq:mvn-corr-part}
\mathrm{Corr}(X,Y \backslash Z) = \frac{\rho_{XY} - \rho_{XZ} \rho_{YZ}}{\sqrt{1-\rho_{XZ}^2} \sqrt{1-\rho_{YZ}^2}}
$$

where $\rho_{XY}$, $\rho_{XZ}$ and $\rho_{YZ}$ are the [pairwise correlations](/D/corr) of the random variables $X$, $Y$ and $Z$.


**Proof:** In the first part of the proof, we will justify that we can work with a simplified form for $\Sigma$. In the second part of the proof, we will compute the partial correlation, as implied by its definition, from $\Sigma$.

1) We will denote the entries of $\Sigma$ as follows:

$$ \label{eq:Sigma}
\Sigma = \left[ \begin{matrix} \sigma_X^2 & \sigma_{XY} & \sigma_{XZ} \\ \sigma_{YX} & \sigma_Y^2 & \sigma_{YZ} \\ \sigma_{ZX} & \sigma_{ZY} & \sigma_Z^2 \end{matrix} \right]
$$

where $\sigma_X^2$, $\sigma_Y^2$ and $\sigma_Z^2$ are the [variances](/D/var) and $\sigma_{XY}$, $\sigma_{XZ}$ and $\sigma_{YZ}$ are the [covariances](/D/cov) of [the entries of the random vector](/P/mvn-cov) $V$. Define the following matrix:

$$ \label{eq:C}
C = \left[ \begin{matrix} \frac{1}{\sigma_X} & 0 & 0 \\ 0 & \frac{1}{\sigma_Y} & 0 \\ 0 & 0 & \frac{1}{\sigma_Z} \end{matrix} \right] \; .
$$

With the [linear transformation theorem for the multivariate normal distribution](/P/mvn-ltt), the distribution of $W = CV$ is

$$ \label{eq:W}
W = CV = \left[ \begin{matrix} X/\sigma_X \\ Y/\sigma_Y \\ Z/\sigma_Z \end{matrix} \right]
  \sim \mathcal{N}(C \mu, C \Sigma C^\mathrm{T})
$$

with

$$ \label{eq:C-Sigma-C}
  C \Sigma C^\mathrm{T}
= \left[ \begin{matrix} \frac{\sigma_X^2}{\sigma_X \sigma_X} & \frac{\sigma_{XY}}{\sigma_X \sigma_Y} & \frac{\sigma_{XZ}}{\sigma_X \sigma_Z} \\ \frac{\sigma_{YX}}{\sigma_Y \sigma_X} & \frac{\sigma_Y^2}{\sigma_Y \sigma_Y} & \frac{\sigma_{YZ}}{\sigma_Y \sigma_Z} \\ \frac{\sigma_{ZX}}{\sigma_Z \sigma_X} & \frac{\sigma_{ZY}}{\sigma_Z \sigma_Y} & \frac{\sigma_Z^2}{\sigma_Z \sigma_Z} \end{matrix} \right]
= \left[ \begin{matrix} 1 & \rho_{XY} & \rho_{XZ} \\ \rho_{YX} & 1 & \rho_{YZ} \\ \rho_{ZX} & \rho_{ZY} & 1 \end{matrix} \right] \; .
$$

Since [correlation is invariant under linear transformation](/P/corr-inv), the entries of $V$ and $W$ have the same pairwise correlations and partial correlations. Thus, for the above theorem, we can assume without loss of generality that

$$ \label{eq:Sigma-wlog}
\Sigma = \left[ \begin{matrix} 1 & \rho_{XY} & \rho_{XZ} \\ \rho_{YX} & 1 & \rho_{YZ} \\ \rho_{ZX} & \rho_{ZY} & 1 \end{matrix} \right] \; .
$$

2) For deriving [partial correlation](/D/corr-part), we define the [residual variables](/D/corr-part)

$$ \label{eq:E-XY}
\begin{split}
E^{(X)} &= X - \beta_0^{(X)} - \beta_1^{(X)} Z \\
E^{(Y)} &= Y - \beta_0^{(Y)} - \beta_1^{(Y)} Z \; .
\end{split}
$$

Note that $E^{(X)}$ and $E^{(Y)}$ can be written as

$$ \label{eq:E-A-b}
  E
= \left[ \begin{matrix} E^{(X)} \\ E^{(Y)} \end{matrix} \right]
= \left[ \begin{matrix} 1 & 0 & -\beta_1^{(X)} \\ 0 & 1 & -\beta_1^{(Y)} \end{matrix} \right]
  \left[ \begin{matrix} X \\ Y \\ Z \end{matrix} \right]
+ \left[ \begin{matrix} -\beta_0^{(X)} \\ -\beta_0^{(Y)} \end{matrix} \right]
= A V + b
$$

with

$$ \label{eq:A-b}
A = \left[ \begin{matrix} 1 & 0 & -\beta_1^{(X)} \\ 0 & 1 & -\beta_1^{(Y)} \end{matrix} \right]
\quad \text{and} \quad
b = \left[ \begin{matrix} -\beta_0^{(X)} \\ -\beta_0^{(Y)} \end{matrix} \right] \; .
$$

When two random variables are in a linear relationship of the form $Y = \beta_0 + \beta_1 X + E$, then [the correlation is related to the slope parameter via the standard deviations](/P/corr-slope):

$$ \label{eq:corr-slope}
\begin{split}
\rho_{XY} = \frac{\sigma_X}{\sigma_Y} \beta_1
\quad \Leftrightarrow \quad
\beta_1 = \frac{\sigma_Y}{\sigma_X} \rho_{XY} \; .
\end{split}
$$

This [also holds in the finite-sample case](/P/slr-corr). Thus, in the present case defined by \eqref{eq:Sigma-wlog}, we have

$$ \label{eq:b1-XY}
\beta_1^{(X)} = \frac{1}{1} \rho_{XZ}
\quad \text{and} \quad
\beta_1^{(Y)} = \frac{1}{1} \rho_{YZ} \; ,
$$

such that

$$ \label{eq:A-rev}
A = \left[ \begin{matrix} 1 & 0 & -\rho_{XZ} \\ 0 & 1 & -\rho_{YZ} \end{matrix} \right] \; .
$$

With that, we can obtain the [distribution of the residual variables](/D/corr-part). Specifically, the [linear transformation theorem for the multivariate normal distribution](/P/mvn-ltt) implies that the distribution of $E$ is

$$ \label{eq:E}
E = AV + b
  \sim \mathcal{N}(A \mu + b, A \Sigma A^\mathrm{T}) \; .
$$

where

$$ \label{eq:A-Sigma-A}
\begin{split}
   A \Sigma A^\mathrm{T}
&= \left[ \begin{matrix} 1 & 0 & -\rho_{XZ} \\ 0 & 1 & -\rho_{YZ} \end{matrix} \right]
   \left[ \begin{matrix} 1 & \rho_{XY} & \rho_{XZ} \\ \rho_{YX} & 1 & \rho_{YZ} \\ \rho_{ZX} & \rho_{ZY} & 1 \end{matrix} \right]
   \left[ \begin{matrix} 1 & 0 \\ 0 & 1 \\ -\rho_{XZ} & -\rho_{YZ} \end{matrix} \right] \\
&= \left[ \begin{matrix} 1 - \rho_{XZ} \rho_{ZX} & \rho_{XY} - \rho_{XZ} \rho_{ZY} & \rho_{XZ} - \rho_{XZ} \\ \rho_{YX} - \rho_{YZ} \rho_{ZX} & 1 - \rho_{YZ} \rho_{ZY} & \rho_{YZ} - \rho_{YZ} \end{matrix} \right]
   \left[ \begin{matrix} 1 & 0 \\ 0 & 1 \\ -\rho_{XZ} & -\rho_{YZ} \end{matrix} \right] \\
&= \left[ \begin{matrix} 1 - \rho_{XZ}^2 & \rho_{XY} - \rho_{XZ} \rho_{YZ} & 0 \\ \rho_{XY} - \rho_{XZ} \rho_{YZ} & 1 - \rho_{YZ}^2 & 0 \end{matrix} \right]
   \left[ \begin{matrix} 1 & 0 \\ 0 & 1 \\ -\rho_{XZ} & -\rho_{YZ} \end{matrix} \right] \\
&= \left[ \begin{matrix} 1 - \rho_{XZ}^2 & \rho_{XY} - \rho_{XZ} \rho_{YZ} \\ \rho_{XY} - \rho_{XZ} \rho_{YZ} & 1 - \rho_{YZ}^2 \end{matrix} \right]
 = \left[ \begin{matrix} \sigma_{X \backslash Z}^2 & \sigma_{X,Y \backslash Z} \\ \sigma_{X,Y \backslash Z} & \sigma_{Y \backslash Z}^2 \end{matrix} \right] \; .
\end{split}
$$

With that, we can derive the [partial correlation](/D/corr-part) of $X$ and $Y$ controlling for $Z$. Specifically, dividing the covariance of the residual variable distribution by the product of its standard deviations, we get:

$$ \label{eq:mvn-corr-part-qed}
\begin{split}
   \mathrm{Corr}(X,Y|Z)
&= \mathrm{Corr}\left( E^{(X)}, E^{(Y)} \right) \\
&= \frac{\sigma_{X,Y \backslash Z}}{\sigma_{X \backslash Z} \sigma_{Y \backslash Z}} \\
&= \frac{\rho_{XY} - \rho_{XZ} \rho_{YZ}}{\sqrt{1-\rho_{XZ}^2} \sqrt{1-\rho_{YZ}^2}} \; .
\end{split}
$$