---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-06-14 14:46:09

title: "Maximum log-likelihood for general linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "General linear model"
theorem: "Maximum log-likelihood"

sources:

proof_id: "P456"
shortcut: "glm-mll"
username: "JoramSoch"
---


**Theorem:** Consider a [general linear model](/D/glm) $m$ with $n \times v$ data matrix $Y$, $n \times p$ design matrix $X$ and $n \times n$ [covariance across rows](/D/glm) $V$

$$ \label{eq:glm}
m: \; Y = X B + E, \; E \sim \mathcal{MN}(0, V, \Sigma) \; .
$$

Then, the [maximum log-likelihood](/D/mll) for this model is

$$ \label{eq:glm-mll-v1}
\mathrm{MLL}(m) = - \frac{nv}{2} \ln(2\pi) - \frac{n}{2} \ln |\hat{\Sigma}| - \frac{nv}{2}
$$

under [uncorrelated observations](/D/glm), i.e. if $V = I_n$, and

$$ \label{eq:glm-mll-v2}
\mathrm{MLL}(m) = - \frac{nv}{2} \ln(2\pi) - \frac{n}{2} \ln |\hat{\Sigma}| - \frac{v}{2} \ln |V| - \frac{nv}{2} \; ,
$$

in the general case, i.e. if $V \neq I_n$, where $\hat{\Sigma}$ is the [maximum likelihood estimate](/D/mle) of the $v \times v$ [covariance across columns](/D/glm).


**Proof:** The [likelihood function](/D/lf) for the general linear model [is given by](/P/glm-mle)

$$ \label{eq:glm-lf}
\begin{split}
p(Y|B,\Sigma) &= \mathcal{MN}(Y; XB, V, \Sigma) \\
&= \sqrt{\frac{1}{(2\pi)^{nv} |\Sigma|^n |V|^v}} \cdot \exp\left[ -\frac{1}{2} \, \mathrm{tr}\left( \Sigma^{-1} (Y - XB)^\mathrm{T} V^{-1} (Y - XB) \right) \right] \; ,
\end{split}
$$

such that the [log-likelihood function](/D/llf) for this model [becomes](/P/glm-mle)

$$ \label{eq:glm-llf}
\begin{split}
\mathrm{LL}(B,\Sigma) = - \frac{nv}{2} \log(2\pi) - \frac{n}{2} \log |\Sigma| - \frac{v}{2} \log |V| - \frac{1}{2} \, \mathrm{tr}\left[ \Sigma^{-1} (Y - XB)^\mathrm{T} V^{-1} (Y - XB) \right] \; .
\end{split}
$$

The [maximum likelihood estimate for the noise covariance](/P/glm-mle) is

$$ \label{eq:glm-mle-Si}
\hat{\Sigma} = \frac{1}{n} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B})
$$

Plugging \eqref{eq:glm-mle-Si} into \eqref{eq:glm-llf}, we obtain the [maximum log-likelihood](/D/mll) as

$$ \label{eq:glm-mll-v2-qed}
\begin{split}
\mathrm{MLL}(m) = &\;\mathrm{LL}(\hat{B},\hat{\Sigma}) \\
= &- \frac{nv}{2} \log(2\pi) - \frac{n}{2} \log |\hat{\Sigma}| - \frac{v}{2} \log |V| - \frac{1}{2} \, \mathrm{tr}\left[ \hat{\Sigma}^{-1} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \right] \\
= &- \frac{nv}{2} \log(2\pi) - \frac{n}{2} \log |\hat{\Sigma}| - \frac{v}{2} \log |V| \\
&- \frac{1}{2} \, \mathrm{tr}\left[ \left( \frac{1}{n} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \right)^{-1} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \right] \\
= &- \frac{nv}{2} \log(2\pi) - \frac{n}{2} \log |\hat{\Sigma}| - \frac{v}{2} \log |V| - \frac{n}{2} \, \mathrm{tr}\left[ I_v \right] \\
= &- \frac{nv}{2} \log(2\pi) - \frac{n}{2} \log |\hat{\Sigma}| - \frac{v}{2} \log |V| - \frac{nv}{2}
\end{split}
$$

which proves the result in \eqref{eq:glm-mll-v2}. Assuming $V = I_n$, we have

$$ \label{eq:glm-mle-Si-iid}
\hat{\Sigma} = \frac{1}{n} (Y - X\hat{B})^\mathrm{T} (Y - X\hat{B})
$$

and

$$ \label{eq:glm-logdet-V-iid}
\frac{v}{2} \log|V| = \frac{v}{2} \log|I_n| = \frac{v}{2} \log 1 = 0 \; ,
$$

such that

$$ \label{eq:glm-mll-v1-qed}
\mathrm{MLL}(m) = - \frac{nv}{2} \ln(2\pi) - \frac{n}{2} \ln |\hat{\Sigma}| - \frac{nv}{2}
$$

which proves the result in \eqref{eq:glm-mll-v1}. This completes the proof.