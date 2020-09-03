---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2019-12-06 10:40:00

title: "Maximum likelihood estimation for the general linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "General linear model"
theorem: "Maximum likelihood estimation"

sources:

proof_id: "P7"
shortcut: "glm-mle"
username: "JoramSoch"
---


**Theorem:** Given a [general linear model](/D/glm) with [matrix-normally distributed](/D/matn) errors

$$ \label{eq:GLM}
Y = X B + E, \; E \sim \mathcal{MN}(0, V, \Sigma) \; ,
$$

[maximum likelihood estimates](/D/mle) for the unknown parameters $B$ and $\Sigma$ are given by

$$ \label{eq:GLM-MLE}
\begin{split}
\hat{B} &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} Y \\
\hat{\Sigma} &= \frac{1}{n} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \; . \\
\end{split}
$$


**Proof:** In \eqref{eq:GLM}, $Y$ is an $n \times v$ matrix of measurements ($n$ observations, $v$ dependent variables), $X$ is an $n \times p$ design matrix ($n$ observations, $p$ independent variables) and $V$ is an $n \times n$ covariance matrix across observations. This multivariate GLM implies the following [likelihood function](/D/lf)

$$ \label{eq:GLM-LF}
\begin{split}
p(Y|B,\Sigma) &= \mathcal{MN}(Y; XB, V, \Sigma) \\
&= \sqrt{\frac{1}{(2\pi)^{nv} |\Sigma|^n |V|^v}} \cdot \exp\left[ -\frac{1}{2} \, \mathrm{tr}\left( \Sigma^{-1} (Y - XB)^\mathrm{T} V^{-1} (Y - XB) \right)  \right] \\
\end{split}
$$

and the [log-likelihood function](/D/llf)

$$ \label{eq:GLM-LL1}
\begin{split}
\mathrm{LL}(B,\Sigma) = &\log p(Y|B,\Sigma) \\
= &- \frac{nv}{2} \log(2\pi) - \frac{n}{2} \log |\Sigma| - \frac{v}{2} \log |V| \\
&- \frac{1}{2} \, \mathrm{tr}\left[ \Sigma^{-1} (Y - XB)^\mathrm{T} V^{-1} (Y - XB) \right] \; .\\
\end{split}
$$

Substituting $V^{-1}$ by the precision matrix $P$ to ease notation, we have:

$$ \label{eq:GLM-LL2}
\begin{split}
\mathrm{LL}(B,\Sigma) = &- \frac{nv}{2} \log(2\pi) - \frac{n}{2} \log(|\Sigma|) - \frac{v}{2} \log(|V|) \\
&- \frac{1}{2} \, \mathrm{tr}\left[ \Sigma^{-1} \left( Y^\mathrm{T} P Y - Y^\mathrm{T} P X B - B^\mathrm{T} X^\mathrm{T} P Y + B^\mathrm{T} X^\mathrm{T} P X B \right) \right] \; .\\
\end{split}
$$

<br>
The derivative of the log-likelihood function \eqref{eq:GLM-LL2} with respect to $B$ is

$$ \label{eq:dLL-dB}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(B,\Sigma)}{\mathrm{d}B} &= \frac{\mathrm{d}}{\mathrm{d}B} \left( - \frac{1}{2} \, \mathrm{tr}\left[ \Sigma^{-1} \left( Y^\mathrm{T} P Y - Y^\mathrm{T} P X B - B^\mathrm{T} X^\mathrm{T} P Y + B^\mathrm{T} X^\mathrm{T} P X B \right) \right] \right) \\
&= \frac{\mathrm{d}}{\mathrm{d}B} \left( -\frac{1}{2} \, \mathrm{tr}\left[ -2 \Sigma^{-1} Y^\mathrm{T} P X B \right] \right) + \frac{\mathrm{d}}{\mathrm{d}B} \left( -\frac{1}{2} \, \mathrm{tr}\left[ \Sigma^{-1} B^\mathrm{T} X^\mathrm{T} P X B \right] \right) \\
&= - \frac{1}{2} \left( -2 X^\mathrm{T} P Y \Sigma^{-1} \right) - \frac{1}{2} \left( X^\mathrm{T} P X B \Sigma^{-1} + (X^\mathrm{T} P X)^\mathrm{T} B (\Sigma^{-1})^\mathrm{T} \right) \\
&= X^\mathrm{T} P Y \Sigma^{-1} - X^\mathrm{T} P X B \Sigma^{-1} \\
\end{split}
$$

and setting this derivative to zero gives the MLE for $B$:

$$ \label{eq:B-MLE}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{B},\Sigma)}{\mathrm{d}B} &= 0 \\
0 &= X^\mathrm{T} P Y \Sigma^{-1} - X^\mathrm{T} P X \hat{B} \Sigma^{-1} \\
0 &= X^\mathrm{T} P Y - X^\mathrm{T} P X \hat{B} \\
X^\mathrm{T} P X \hat{B} &= X^\mathrm{T} P Y \\
\hat{B} &= \left( X^\mathrm{T} P X \right)^{-1} X^\mathrm{T} P Y \\
\end{split}
$$

<br>
The derivative of the log-likelihood function \eqref{eq:GLM-LL1} at $\hat{B}$ with respect to $\Sigma$ is

$$ \label{eq:dLL-dS}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{B},\Sigma)}{\mathrm{d}\Sigma} &= \frac{\mathrm{d}}{\mathrm{d}\Sigma} \left( - \frac{n}{2} \log |\Sigma| - \frac{1}{2} \, \mathrm{tr}\left[ \Sigma^{-1} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \right] \right) \\
&= - \frac{n}{2} \left( \Sigma^{-1} \right)^\mathrm{T} + \frac{1}{2} \left( \Sigma^{-1} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \, \Sigma^{-1} \right)^\mathrm{T} \\
&= - \frac{n}{2} \, \Sigma^{-1} + \frac{1}{2} \, \Sigma^{-1} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \, \Sigma^{-1} \\
\end{split}
$$

and setting this derivative to zero gives the MLE for $\Sigma$:

$$ \label{eq:S-MLE}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{B},\hat{\Sigma})}{\mathrm{d}\Sigma} &= 0 \\
0 &= - \frac{n}{2} \, \hat{\Sigma}^{-1} + \frac{1}{2} \, \hat{\Sigma}^{-1} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \, \hat{\Sigma}^{-1} \\
\frac{n}{2} \, \hat{\Sigma}^{-1} &= \frac{1}{2} \, \hat{\Sigma}^{-1} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \, \hat{\Sigma}^{-1} \\
\hat{\Sigma}^{-1} &= \frac{1}{n} \, \hat{\Sigma}^{-1} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \, \hat{\Sigma}^{-1} \\
I_v &= \frac{1}{n} \, (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \, \hat{\Sigma}^{-1} \\
\hat{\Sigma} &= \frac{1}{n} \, (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \\
\end{split}
$$

<br>
Together, \eqref{eq:B-MLE} and \eqref{eq:S-MLE} constitute the MLE for the GLM.