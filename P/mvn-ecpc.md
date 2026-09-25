---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-08-28 11:35:56

title: "Equivalence of conditional and partial correlation for the multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Conditional and partial correlation"

sources:

proof_id: "P547"
shortcut: "mvn-ecpc"
username: "JoramSoch"
---


**Theorem:** Let $X$, $Y$ and $Z$ be [random variables](/D/rvar) jointly following a [multivariate normal distribution](/D/mvn):

$$ \label{eq:V}
V =    \left[ \begin{matrix} X \\ Y \\ Z \end{matrix} \right]
  \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, the [conditional correlation](/D/corr-cond) of $X$ and $Y$ given $Z$  is equal to the [partial correlation](/D/corr-part) of $X$ and $Y$ controlling for $Z$:

$$ \label{eq:mvn-ecpc}
\mathrm{Corr}(X,Y|Z) = \mathrm{Corr}(X,Y \backslash Z) \; .
$$


**Proof:** For a three-dimensional [multivariate normal random vector](/D/mvn)

$$ \label{eq:XYZ}
\left[ \begin{matrix} X \\ Y \\ Z \end{matrix} \right] \sim \mathcal{N}(\mu, \Sigma) \; ,
$$

the [conditional correlation of $X$ and $Y$ given $Z$ is](/P/mvn-corrcond)

$$ \label{eq:mvn-corr-cond}
\mathrm{Corr}(X,Y|Z) = \frac{\rho_{XY} - \rho_{XZ} \rho_{YZ}}{\sqrt{1-\rho_{XZ}^2} \sqrt{1-\rho_{YZ}^2}}
$$

and the [partial correlation of $X$ and $Y$ controlling for $Z$ is](/D/mvn-corrpart)

$$ \label{eq:mvn-corr-part}
\mathrm{Corr}(X,Y \backslash Z) = \frac{\rho_{XY} - \rho_{XZ} \rho_{YZ}}{\sqrt{1-\rho_{XZ}^2} \sqrt{1-\rho_{YZ}^2}}
$$

where $\rho_{XY}$, $\rho_{XZ}$ and $\rho_{YZ}$ are the [pairwise correlations](/D/corr) of the random variables $X$, $Y$ and $Z$. Thus, conditional and partial correlation are equivalent for the multivariate normal distribution:

$$ \label{eq:mvn-ecpc-qed}
\mathrm{Corr}(X,Y|Z) = \mathrm{Corr}(X,Y \backslash Z) \; .
$$