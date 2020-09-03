---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-09-03 08:37:00

title: "Posterior distribution for multivariate Bayesian linear regression"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Multivariate Bayesian linear regression"
theorem: "Posterior distribution"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Bayesian multivariate linear regression"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-09-03"
    url: "https://en.wikipedia.org/wiki/Bayesian_multivariate_linear_regression#Posterior_distribution"

proof_id: "P160"
shortcut: "mblr-post"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:GLM}
Y = X B + E, \; E \sim \mathcal{MN}(0, V, \Sigma)
$$

be a [general linear model](/D/glm) with measured $n \times v$ data matrix $Y$, known $n \times p$ design matrix $X$, known $n \times n$ [covariance structure](/D/matn) $V$ as well as unknown $p \times v$ regression coefficients $B$ and unknown $v \times v$ [noise covariance](/D/matn) $\Sigma$. Moreover, assume a [normal-Wishart prior distribution](/P/mblr-prior) over the model parameters $B$ and $T = \Sigma^{-1}$:

$$ \label{eq:GLM-NW-prior}
p(B,T) = \mathcal{MN}(B; M_0, \Lambda_0^{-1}, T^{-1}) \cdot \mathcal{W}(T; \Omega_0^{-1}, \nu_0) \; .
$$

Then, the [posterior distribution](/D/post) is also a [normal-Wishart distribution](/D/nw)

$$ \label{eq:GLM-NW-post}
p(B,T|Y) = \mathcal{MN}(B; M_n, \Lambda_n^{-1}, T^{-1}) \cdot \mathcal{W}(T; \Omega_n^{-1}, \nu_n)
$$

and the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:GLM-NW-post-par}
\begin{split}
M_n &= \Lambda_n^{-1} (X^\mathrm{T} P Y + \Lambda_0 M_0) \\
\Lambda_n &= X^\mathrm{T} P X + \Lambda_0 \\
\Omega_n &= \Omega_0 + Y^\mathrm{T} P Y + M_0^\mathrm{T} \Lambda_0 M_0 - M_n^\mathrm{T} \Lambda_n M_n \\
\nu_n &= \nu_0 + n \; .
\end{split}
$$


**Proof:** According to [Bayes' theorem](/P/bayes-th), the [posterior distribution](/D/post) is given by

$$ \label{eq:GLM-NG-BT}
p(B,T|Y) = \frac{p(Y|B,T) \, p(B,T)}{p(Y)} \; .
$$

Since $p(Y)$ is just a normalization factor, the [posterior is proportional](/P/post-jl) to the numerator:

$$ \label{eq:GLM-NG-post-JL}
p(B,T|Y) \propto p(Y|B,T) \, p(B,T) = p(Y,B,T) \; .
$$

Equation \eqref{eq:GLM} implies the following [likelihood function](/D/lf)

$$ \label{eq:GLM-LF-Class}
p(Y|B,\Sigma) = \mathcal{MN}(Y; X B, V, \Sigma) = \sqrt{\frac{1}{(2 \pi)^{nv} |\Sigma|^n |V|^v}} \, \exp\left[ -\frac{1}{2} \mathrm{tr}\left( \Sigma^{-1} (Y-XB)^\mathrm{T} V^{-1} (Y-XB) \right) \right]
$$

which, for mathematical convenience, can also be parametrized as

$$ \label{eq:GLM-LF-Bayes}
p(Y|B,T) = \mathcal{MN}(Y; X B, P, T^{-1}) = \sqrt{\frac{|T|^n |P|^v}{(2 \pi)^{nv}}} \, \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T (Y-XB)^\mathrm{T} P (Y-XB) \right) \right]
$$

using the $v \times v$ [precision matrix](/D/precmat) $T = \Sigma^{-1}$ and the $n \times n$ [precision matrix](/D/precmat) $P = V^{-1}$.

<br>
Combining the [likelihood function](/D/lf) \eqref{eq:GLM-LF-Bayes} with the [prior distribution](/D/prior) \eqref{eq:GLM-NW-prior}, the [joint likelihood](/D/jl) of the model is given by

$$ \label{eq:GLM-NW-JL-s1}
\begin{split}
p(Y,B,T) = \; & p(Y|B,T) \, p(B,T) \\
= \; & \sqrt{\frac{|T|^n |P|^v}{(2 \pi)^{nv}}} \, \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T (Y-XB)^\mathrm{T} P (Y-XB) \right) \right] \cdot \\
& \sqrt{\frac{|T|^p |\Lambda_0|^v}{(2 \pi)^{pv}}} \, \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T (B-M_0)^\mathrm{T} \Lambda_0 (B-M_0) \right) \right] \cdot \\
& \frac{1}{\Gamma_v \left( \frac{\nu_0}{2} \right)} \sqrt{\frac{|\Omega_0|^{\nu_0}}{2^{\nu_0 v}}} |T|^{(\nu_0-v-1)/2} \exp\left[ -\frac{1}{2} \mathrm{tr}\left( \Omega_0 T \right) \right] \; .
\end{split}
$$

Collecting identical variables gives:

$$ \label{eq:GLM-NW-JL-s2}
\begin{split}
p(Y,B,T) = \; & \sqrt{\frac{|T|^n |P|^v}{(2 \pi)^{nv}}} \sqrt{\frac{|T|^p |\Lambda_0|^v}{(2 \pi)^{pv}}} \sqrt{\frac{|\Omega_0|^{\nu_0}}{2^{\nu_0 v}}} \frac{1}{\Gamma_v \left( \frac{\nu_0}{2} \right)} \cdot |T|^{(\nu_0-v-1)/2} \exp\left[ -\frac{1}{2} \mathrm{tr}\left( \Omega_0 T \right) \right] \cdot \\
& \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T \left[ (Y-XB)^\mathrm{T} P (Y-XB) + (B-M_0)^\mathrm{T} \Lambda_0 (B-M_0) \right] \right) \right] \; .
\end{split}
$$

Expanding the products in the exponent gives:

$$ \label{eq:GLM-NW-JL-s3}
\begin{split}
p(Y,B,T) = \; & \sqrt{\frac{|T|^n |P|^v}{(2 \pi)^{nv}}} \sqrt{\frac{|T|^p |\Lambda_0|^v}{(2 \pi)^{pv}}} \sqrt{\frac{|\Omega_0|^{\nu_0}}{2^{\nu_0 v}}} \frac{1}{\Gamma_v \left( \frac{\nu_0}{2} \right)} \cdot |T|^{(\nu_0-v-1)/2} \exp\left[ -\frac{1}{2} \mathrm{tr}\left( \Omega_0 T \right) \right] \cdot \\
& \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T \left[ Y^\mathrm{T} P Y - Y^\mathrm{T} P X B - B^\mathrm{T} X^\mathrm{T} P Y + B^\mathrm{T} X^\mathrm{T} P X B + \right. \right. \right. \\
& \hphantom{\exp\left[ -\frac{1}{2} \mathrm{tr}\left( T \left[ \right. \right. \right. \!\!\!} \; \left. \left. \left. B^\mathrm{T} \Lambda_0 B - B^\mathrm{T} \Lambda_0 M_0 - M_0^\mathrm{T} \Lambda_0 B + M_0^\mathrm{T} \Lambda_0 \mu_0 \right] \right) \right] \; .
\end{split}
$$

Completing the square over $B$, we finally have

$$ \label{eq:GLM-NW-JL-s4}
\begin{split}
p(Y,B,T) = \; & \sqrt{\frac{|T|^n |P|^v}{(2 \pi)^{nv}}} \sqrt{\frac{|T|^p |\Lambda_0|^v}{(2 \pi)^{pv}}} \sqrt{\frac{|\Omega_0|^{\nu_0}}{2^{\nu_0 v}}} \frac{1}{\Gamma_v \left( \frac{\nu_0}{2} \right)} \cdot |T|^{(\nu_0-v-1)/2} \exp\left[ -\frac{1}{2} \mathrm{tr}\left( \Omega_0 T \right) \right] \cdot \\
& \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T \left[ (B-M_n)^\mathrm{T} \Lambda_n (B-M_n) + (Y^\mathrm{T} P Y + M_0^\mathrm{T} \Lambda_0 M_0 - M_n^\mathrm{T} \Lambda_n M_n) \right] \right) \right] \; .
\end{split}
$$

with the [posterior hyperparameters](/D/post)

$$ \label{eq:GLM-NW-post-B-par}
\begin{split}
M_n &= \Lambda_n^{-1} (X^\mathrm{T} P Y + \Lambda_0 M_0) \\
\Lambda_n &= X^\mathrm{T} P X + \Lambda_0 \; .
\end{split}
$$

Ergo, the joint likelihood is proportional to

$$ \label{eq:GLM-NW-JL-s5}
p(Y,B,T) \propto |T|^{p/2} \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T \left[ (B-M_n)^\mathrm{T} \Lambda_n (B-M_n) \right] \right) \right] \cdot |T|^{(\nu_n-v-1)/2} \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( \Omega_n T \right) \right]
$$

with the [posterior hyperparameters](/D/post)

$$ \label{eq:GLM-NW-post-T-par}
\begin{split}
\Omega_n &= \Omega_0 + Y^\mathrm{T} P Y + M_0^\mathrm{T} \Lambda_0 M_0 - M_n^\mathrm{T} \Lambda_n M_n \\
\nu_n &= \nu_0 + n \; .
\end{split}
$$

From the term in \eqref{eq:GLM-NW-JL-s5}, we can isolate the posterior distribution over $B$ given $T$:

$$ \label{eq:GLM-NW-post-B}
p(B|T,Y) = \mathcal{MN}(B; M_n, \Lambda_n^{-1}, T^{-1}) \; .
$$

From the remaining term, we can isolate the posterior distribution over $T$:

$$ \label{eq:GLM-NW-post-T}
p(T|Y) = \mathcal{W}(T; \Omega_n^{-1}, \nu_n) \; .
$$

Together, \eqref{eq:GLM-NW-post-B} and \eqref{eq:GLM-NW-post-T} constitute the [joint](/D/prob-joint) [posterior distribution](/D/post) of $B$ and $T$.