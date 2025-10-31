---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2024-06-28 14:38:09

title: "Equivalence of log-likelihood ratios for regular and inverse general linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Inverse general linear model"
theorem: "Equivalence of log-likelihood ratios"

sources:
  - authors: "Friston K, Chu C, Mourão-Miranda J, Hulme O, Rees G, Penny W, Ashburner J"
    year: 2008
    title: "Bayesian decoding of brain images"
    in: "NeuroImage"
    pages: "vol. 39, pp. 181-205, p. 183"
    url: "https://www.sciencedirect.com/science/article/abs/pii/S1053811907007203"
    doi: "10.1016/j.neuroimage.2007.08.013"
  - authors: "Wikipedia"
    year: 2024
    title: "Weinstein–Aronszajn identity"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-06-28"
    url: "https://en.wikipedia.org/wiki/Weinstein%E2%80%93Aronszajn_identity"

proof_id: "P459"
shortcut: "iglm-llrs"
username: "JoramSoch"
---


**Theorem:** Consider two [general linear models](/D/glm)

$$ \label{eq:glms}
\begin{split}
m_1^{(Y)}: \; & Y = X B + E_1, \; E_1 \sim \mathcal{MN}(0, I_n, \Sigma_1^{(Y)}) \\
m_0^{(Y)}: \; & Y =       E_0, \; E_0 \sim \mathcal{MN}(0, I_n, \Sigma_0^{(Y)})
\end{split}
$$

and two [inverse general linear models](/D/iglm)

$$ \label{eq:iglms}
\begin{split}
m_1^{(X)}: \; & X = Y W + N_1, \; N_1 \sim \mathcal{MN}(0, I_n, \Sigma_1^{(X)}) \\
m_0^{(X)}: \; & X =       N_0, \; N_0 \sim \mathcal{MN}(0, I_n, \Sigma_0^{(X)})
\end{split}
$$

where $Y \in \mathbb{R}^{n \times v}$ and $X \in \mathbb{R}^{n \times p}$ are data matrices, such that $n > v$ and $n > p$. Then, the [log-likelihood ratio](/D/llr) comparing the [forward models](/D/glm) is equivalent to the [log-likelihood ratio](/D/llr) comparing the [backward models](/D/iglm):

$$ \label{eq:iglm-llreq}
\ln \Lambda_{10}^{(Y)} = \ln \Lambda_{10}^{(X)} \; .
$$


**Proof:** The [maximum likelihood estimates for the general linear models](/P/glm-mle) are

$$ \label{eq:glms-mle}
\begin{split}
\hat{\Sigma}_1^{(Y)} &= \frac{1}{n} (Y - X\hat{B})^\mathrm{T} (Y - X\hat{B}) \quad \text{with} \quad
\hat{B}               = (X^\mathrm{T} X)^{-1} X^\mathrm{T} Y \quad \text{and} \quad \\
\hat{\Sigma}_0^{(Y)} &= \frac{1}{n} Y^\mathrm{T} Y
\end{split}
$$

as well as

$$ \label{eq:iglms-mle}
\begin{split}
\hat{\Sigma}_1^{(X)} &= \frac{1}{n} (X - Y\hat{W})^\mathrm{T} (X - Y\hat{W}) \quad \text{with} \quad
\hat{W}               = (Y^\mathrm{T} Y)^{-1} Y^\mathrm{T} X \quad \text{and} \quad \\
\hat{\Sigma}_0^{(X)} &= \frac{1}{n} X^\mathrm{T} X \; .
\end{split}
$$

The [likelihood ratio for two general linear models](/P/glm-llr) $m_1$ and $m_2$ is:

$$ \label{eq:glm-llr}
\begin{split}
\ln \Lambda_{12}
&= - \frac{n}{2} \ln \frac{|\hat{\Sigma}_1|}{|\hat{\Sigma}_2|} \\
&= - \frac{n}{2} \ln \left( |\hat{\Sigma}_2^{-1}| |\hat{\Sigma}_1| \right) \\
&= - \frac{n}{2} \ln |\hat{\Sigma}_2^{-1} \hat{\Sigma}_1| \; .
\end{split}
$$

Thus, with \eqref{eq:glms-mle}, the [log-likelihood ratio](/D/llr) of $m_1^{(Y)}$ vs. $m_0^{(Y)}$ is given as

$$ \label{eq:glms-llr}
\begin{split}
\ln \Lambda_Y = \ln \Lambda_{10}^{(Y)}
&\overset{\eqref{eq:glm-llr}}{=} - \frac{n}{2} \ln \left| \left( \hat{\Sigma}_0^{(Y)} \right)^{-1} \hat{\Sigma}_1^{(Y)} \right| \\
&\overset{\eqref{eq:glms-mle}}{=} - \frac{n}{2} \ln \left| \left( \frac{1}{n} Y^\mathrm{T} Y \right)^{-1} \frac{1}{n} (Y - X \hat{B})^\mathrm{T} (Y - X \hat{B}) \right| \\
&= - \frac{n}{2} \ln \left| \left( Y^\mathrm{T} Y \right)^{-1} \left( Y^\mathrm{T} Y - 2 Y^\mathrm{T} X \hat{B} + \hat{B}^\mathrm{T} X^\mathrm{T} X \hat{B} \right) \right| \\
&= - \frac{n}{2} \ln \left| \left( (Y^\mathrm{T} Y)^{-1} Y^\mathrm{T} Y - 2 (Y^\mathrm{T} Y)^{-1} Y^\mathrm{T} X \hat{B} + (Y^\mathrm{T} Y)^{-1} \hat{B}^\mathrm{T} X^\mathrm{T} X \hat{B} \right) \right| \\
&\overset{\eqref{eq:glms-mle}}{=} - \frac{n}{2} \ln \left| I_v - 2 \hat{W} \hat{B} + (Y^\mathrm{T} Y)^{-1} Y^\mathrm{T} X (X^\mathrm{T} X)^{-1} X^\mathrm{T} X (X^\mathrm{T} X)^{-1} X^\mathrm{T} Y \right| \\
&= - \frac{n}{2} \ln \left| I_v - 2 \hat{W} \hat{B} + (Y^\mathrm{T} Y)^{-1} Y^\mathrm{T} X (X^\mathrm{T} X)^{-1} X^\mathrm{T} Y \right| \\
&= - \frac{n}{2} \ln \left| I_v - 2 \hat{W} \hat{B} + \hat{W} \hat{B} \right| \\
&= - \frac{n}{2} \ln \left| I_v - \hat{W} \hat{B} \right| \; .
\end{split}
$$

Similarly, with \eqref{eq:iglms-mle}, the [log-likelihood ratio](/D/llr) of $m_1^{(X)}$ vs. $m_0^{(X)}$ becomes

$$ \label{eq:iglms-llr}
\begin{split}
\ln \Lambda_X = \ln \Lambda_{10}^{(X)}
&\overset{\eqref{eq:glm-llr}}{=} - \frac{n}{2} \ln \left| \left( \hat{\Sigma}_0^{(X)} \right)^{-1} \hat{\Sigma}_1^{(X)} \right| \\
&\overset{\eqref{eq:iglms-mle}}{=} - \frac{n}{2} \ln \left| \left( \frac{1}{n} X^\mathrm{T} X \right)^{-1} \frac{1}{n} (X - Y \hat{W})^\mathrm{T} (X - Y \hat{W}) \right| \\
&= - \frac{n}{2} \ln \left| \left( X^\mathrm{T} X \right)^{-1} \left( X^\mathrm{T} X - 2 X^\mathrm{T} Y \hat{W} + \hat{W}^\mathrm{T} Y^\mathrm{T} Y \hat{W} \right) \right| \\
&= - \frac{n}{2} \ln \left| \left( (X^\mathrm{T} X)^{-1} X^\mathrm{T} X - 2 (X^\mathrm{T} X)^{-1} X^\mathrm{T} Y \hat{W} + (X^\mathrm{T} X)^{-1} \hat{W}^\mathrm{T} Y^\mathrm{T} Y \hat{W} \right) \right| \\
&\overset{\eqref{eq:iglms-mle}}{=} - \frac{n}{2} \ln \left| I_p - 2 \hat{B} \hat{W} + (X^\mathrm{T} X)^{-1} X^\mathrm{T} Y (Y^\mathrm{T} Y)^{-1} Y^\mathrm{T} Y (Y^\mathrm{T} Y)^{-1} Y^\mathrm{T} X \right| \\
&= - \frac{n}{2} \ln \left| I_p - 2 \hat{B} \hat{W} + (X^\mathrm{T} X)^{-1} X^\mathrm{T} Y (Y^\mathrm{T} Y)^{-1} Y^\mathrm{T} X \right| \\
&= - \frac{n}{2} \ln \left| I_p - 2 \hat{B} \hat{W} + \hat{B} \hat{W} \right| \\
&= - \frac{n}{2} \ln \left| I_p - \hat{B} \hat{W} \right| \; .
\end{split}
$$

Sylvester's determinant theorem (also known as the "Weinstein–Aronszajn identity") states that, for two matrices $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times m}$, the following identity holds:

$$ \label{eq:sdt}
\left| I_m + AB \right| = \left| I_n + BA \right| \; .
$$

Since $\hat{B} \in \mathbb{R}^{p \times v}$ and $(-\hat{W}) \in \mathbb{R}^{v \times p}$, it follows that

$$ \label{eq:sdt-BW}
\left| I_p - \hat{B} \hat{W} \right| = \left| I_v - \hat{W} \hat{B} \right|
$$

and thus, we finally have:

$$ \label{eq:iglm-llreq-qed}
  \ln \Lambda_Y
= - \frac{n}{2} \ln \left| I_v - \hat{W} \hat{B} \right|
= - \frac{n}{2} \ln \left| I_p - \hat{B} \hat{W} \right|
= \ln \Lambda_X \; .
$$