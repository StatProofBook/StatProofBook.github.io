---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-06-21 10:27:06

title: "Equivalence of log-likelihood ratio and mutual information for the general linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "General linear model"
theorem: "Equivalence of log-likelihood ratio and mutual information"

sources:
  - authors: "Friston K, Chu C, Mourão-Miranda J, Hulme O, Rees G, Penny W, Ashburner J"
    year: 2008
    title: "Bayesian decoding of brain images"
    in: "NeuroImage"
    pages: "vol. 39, pp. 181-205, eq. 6"
    url: "https://www.sciencedirect.com/science/article/abs/pii/S1053811907007203"
    doi: "10.1016/j.neuroimage.2007.08.013"

proof_id: "P458"
shortcut: "glm-llrmi"
username: "JoramSoch"
---


**Theorem:** Consider a [general linear model](/D/glm) $m_1$ with $n \times v$ data matrix $Y$, $n \times p$ design matrix $X$ and [uncorrelated observations](/D/glm), i.e. $V = I_n$,

$$ \label{eq:m1}
m_1: \; Y = X B + E_1, \; E_1 \sim \mathcal{MN}(0, I_n, \Sigma_1) \; ,
$$

as well as another model $m_0$ in which $X$ has no influence on $Y$:

$$ \label{eq:m0}
m_0: \; Y = E_0, \; E_0 \sim \mathcal{MN}(0, I_n, \Sigma_0) \; .
$$

Then, the [log-likelihood ratio](/D/llr) of $m_1$ vs. $m_0$ is equal to the estimated [mutual information](/D/mi) of $X$ and $Y$:

$$ \label{eq:glm-llrmi}
\ln \Lambda_{10} = I(X,Y) \; .
$$


**Proof:** The [maximum likelihood estimates for a general linear model](/P/glm-mle) are

$$ \label{eq:glm-mle}
\begin{split}
\hat{B} &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} Y \\
\hat{\Sigma} &= \frac{1}{n} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \; ,
\end{split}
$$

such that, for the two models, the [maximum likelihood estimates](/D/mle) are:

$$ \label{eq:m1-m0-mle}
\begin{split}
\hat{\Sigma}_1 &= \frac{1}{n} (Y - X\hat{B})^\mathrm{T} (Y - X\hat{B}) \quad \text{with} \quad
\hat{B} = (X^\mathrm{T} X)^{-1} X^\mathrm{T} Y \quad \text{and} \quad \\
\hat{\Sigma}_0 &= \frac{1}{n} Y^\mathrm{T} Y \; .
\end{split}
$$

The [log-likelihood ratio for two general linear models](/P/glm-llr) is

$$ \label{eq:glm-llr}
\ln \Lambda_{12} = - \frac{n}{2} \ln \frac{|\hat{\Sigma}_1|}{|\hat{\Sigma}_2|} \; ,
$$

such that in the present case, we have:

$$ \label{eq:m1-m0-llr}
\ln \Lambda_{10} = - \frac{n}{2} \ln \frac{|\hat{\Sigma}_1|}{|\hat{\Sigma}_0|} \; .
$$

The [mutual information for the general linear model](/P/glm-mi) is

$$ \label{eq:glm-mi}
I(X,Y) = - \frac{n}{2} \ln \frac{|\Sigma_1|}{|\Sigma_0|} \; ,
$$

such that with \eqref{eq:m1-m0-mle}, the estimated mutual information is:

$$ \label{eq:Y-X-mi}
I(X,Y) = - \frac{n}{2} \ln \frac{|\hat{\Sigma}_1|}{|\hat{\Sigma}_0|} \; ,
$$

Together, \eqref{eq:m1-m0-llr} and \eqref{eq:Y-X-mi} show that

$$ \label{eq:glm-llrmi-qed}
\ln \Lambda_{10} = I(X,Y) \; .
$$