---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-09-03 09:23:00

title: "Log model evidence for multivariate Bayesian linear regression"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Multivariate Bayesian linear regression"
theorem: "Log model evidence"

sources:

proof_id: "P161"
shortcut: "mblr-lme"
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

Then, the [log model evidence](/D/lme) for this model is

$$ \label{eq:GLM-NW-LME}
\begin{split}
\log p(y|m) = & \frac{v}{2} \log |P| - \frac{nv}{2} \log (2 \pi)  + \frac{v}{2} \log |\Lambda_0| - \frac{v}{2} \log |\Lambda_n| + \\
& \frac{\nu_0}{2} \log\left| \frac{1}{2} \Omega_0 \right| - \frac{\nu_n}{2} \log\left| \frac{1}{2} \Omega_n \right| + \log \Gamma_v \left( \frac{\nu_n}{2} \right) - \log \Gamma_v \left( \frac{\nu_0}{2} \right)
\end{split}
$$

where the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:GLM-NW-post-par}
\begin{split}
M_n &= \Lambda_n^{-1} (X^\mathrm{T} P Y + \Lambda_0 M_0) \\
\Lambda_n &= X^\mathrm{T} P X + \Lambda_0 \\
\Omega_n &= \Omega_0 + Y^\mathrm{T} P Y + M_0^\mathrm{T} \Lambda_0 M_0 - M_n^\mathrm{T} \Lambda_n M_n \\
\nu_n &= \nu_0 + n \; .
\end{split}
$$


**Proof:** According to the [law of marginal probability](/D/prob-marg), the [model evidence](/D/ml) for this model is:

$$ \label{eq:GLM-NW-ME-s1}
p(Y|m) = \iint p(Y|B,T) \, p(B,T) \, \mathrm{d}B \, \mathrm{d}T \; .
$$

According to the [law of conditional probability](/D/prob-cond), the integrand is equivalent to the [joint likelihood](/D/jl):

$$ \label{eq:GLM-NW-ME-s2}
p(Y|m) = \iint p(Y,B,T) \, \mathrm{d}B \, \mathrm{d}T \; .
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
When [deriving the posterior distribution](/P/mblr-post) $p(B,T|Y)$, the joint likelihood $p(Y,B,T)$ is obtained as

$$ \label{eq:GLM-NW-LME-s1}
\begin{split}
p(Y,B,T) = \; & \sqrt{\frac{|T|^n |P|^v}{(2 \pi)^{nv}}} \sqrt{\frac{|T|^p |\Lambda_0|^v}{(2 \pi)^{pv}}} \sqrt{\frac{|\Omega_0|^{\nu_0}}{2^{\nu_0 v}}} \frac{1}{\Gamma_v \left( \frac{\nu_0}{2} \right)} \cdot |T|^{(\nu_0-v-1)/2} \exp\left[ -\frac{1}{2} \mathrm{tr}\left( \Omega_0 T \right) \right] \cdot \\
& \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T \left[ (B-M_n)^\mathrm{T} \Lambda_n (B-M_n) + (Y^\mathrm{T} P Y + M_0^\mathrm{T} \Lambda_0 M_0 - M_n^\mathrm{T} \Lambda_n M_n) \right] \right) \right] \; .
\end{split}
$$

Using the [probability density function of the matrix-normal distribution](/P/matn-pdf), we can rewrite this as

$$ \label{eq:GLM-NW-LME-s2}
\begin{split}
p(Y,B,T) = \; & \sqrt{\frac{|T|^n |P|^v}{(2 \pi)^{nv}}} \sqrt{\frac{|T|^p |\Lambda_0|^v}{(2 \pi)^{pv}}} \sqrt{\frac{(2 \pi)^{pv}}{|T|^p |\Lambda_n|^v}} \sqrt{\frac{|\Omega_0|^{\nu_0}}{2^{\nu_0 v}}} \frac{1}{\Gamma_v \left( \frac{\nu_0}{2} \right)} \cdot |T|^{(\nu_0-v-1)/2} \exp\left[ -\frac{1}{2} \mathrm{tr}\left( \Omega_0 T \right) \right] \cdot \\
& \mathcal{MN}(B; M_n, \Lambda_n^{-1}, T^{-1}) \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T \left[ Y^\mathrm{T} P Y + M_0^\mathrm{T} \Lambda_0 M_0 - M_n^\mathrm{T} \Lambda_n M_n \right] \right) \right] \; .
\end{split}
$$

Now, $B$ can be integrated out easily:

$$ \label{eq:GLM-NW-LME-s3}
\begin{split}
\int p(Y,B,T) \, \mathrm{d}B = \; & \sqrt{\frac{|T|^n |P|^v}{(2 \pi)^{nv}}} \sqrt{\frac{|\Lambda_0|^v}{|\Lambda_n|^v}} \sqrt{\frac{|\Omega_0|^{\nu_0}}{2^{\nu_0 v}}} \frac{1}{\Gamma_v \left( \frac{\nu_0}{2} \right)} \cdot |T|^{(\nu_0-v-1)/2} \cdot \\
& \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T \left[ \Omega_0 + Y^\mathrm{T} P Y + M_0^\mathrm{T} \Lambda_0 M_0 - M_n^\mathrm{T} \Lambda_n M_n \right] \right) \right] \; .
\end{split}
$$

Using the [probability density function of the Wishart distribution](/P/wish-pdf), we can rewrite this as

$$ \label{eq:GLM-NW-LME-s4}
\int p(Y,B,T) \, \mathrm{d}B = \sqrt{\frac{|P|^v}{(2 \pi)^{nv}}} \sqrt{\frac{|\Lambda_0|^v}{|\Lambda_n|^v}} \sqrt{\frac{|\Omega_0|^{\nu_0}}{2^{\nu_0 v}}} \sqrt{\frac{2^{\nu_n v}}{|\Omega_n|^{\nu_n}}} \, \frac{\Gamma_v \left( \frac{\nu_n}{2} \right)}{\Gamma_v \left( \frac{\nu_0}{2} \right)} \cdot \mathcal{W}(T; \Omega_n^{-1}, \nu_n) \; .
$$

Finally, $T$ can also be integrated out:

$$ \label{eq:GLM-NW-LME-s5}
\iint p(Y,B,T) \, \mathrm{d}B \, \mathrm{d}T = \sqrt{\frac{|P|^v}{(2 \pi)^{nv}}} \sqrt{\frac{|\Lambda_0|^v}{|\Lambda_n|^v}} \sqrt{\frac{\left| \frac{1}{2} \Omega_0 \right|^{\nu_0}}{\left| \frac{1}{2} \Omega_n \right|^{\nu_n}}} \, \frac{\Gamma_v \left( \frac{\nu_n}{2} \right)}{\Gamma_v \left( \frac{\nu_0}{2} \right)} = p(y|m) \; .
$$

Thus, the [log model evidence](/D/lme) of this model is given by

$$ \label{eq:GLM-NW-LME-s6}
\begin{split}
\log p(y|m) = & \frac{v}{2} \log |P| - \frac{nv}{2} \log (2 \pi)  + \frac{v}{2} \log |\Lambda_0| - \frac{v}{2} \log |\Lambda_n| + \\
& \frac{\nu_0}{2} \log\left| \frac{1}{2} \Omega_0 \right| - \frac{\nu_n}{2} \log\left| \frac{1}{2} \Omega_n \right| + \log \Gamma_v \left( \frac{\nu_n}{2} \right) - \log \Gamma_v \left( \frac{\nu_0}{2} \right) \; .
\end{split}
$$