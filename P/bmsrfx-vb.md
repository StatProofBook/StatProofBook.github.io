---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-06-24 14:57:00

title: "Variational Bayesian estimation of random-effects Bayesian model selection using the mean-field approximation"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Random-effects Bayesian model selection"
theorem: "Variational Bayesian estimation"

sources:
  - authors: "Stephan KE, Penny WD, Daunizeau J, Moran RJ, Friston KJ"
    year: 2009
    title: "Bayesian model selection for group studies"
    in: "NeuroImage"
    pages: "vol. 46, pp. 1004–1017, eqs. 6-14"
    url: "https://www.sciencedirect.com/science/article/abs/pii/S1053811909002638"
    doi: "10.1016/j.neuroimage.2009.03.025"
  - authors: "Soch J, Allefeld C, Haynes JD"
    year: 2016
    title: "How to avoid mismodelling in GLM-based fMRI data analysis: cross-validated Bayesian model selection"
    in: "NeuroImage"
    pages: "vol. 141, pp. 469-489, eqs. D.1-D.2"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811916303615"
    doi: "10.1016/j.neuroimage.2016.07.047"

proof_id: "P545"
shortcut: "bmsrfx-vb"
username: "JoramSoch"
---


**Theorem:** Consider [model evidences](/D/ml) $p(y_i \vert m)$ from $K$ models describing $N$ data sets $y = \left\lbrace y_1, \ldots, y_N \right\rbrace$ and assume that those data follow the group-level model specified by [random-effects Bayesian model selection](/D/bms-rfx) (RFX BMS):

$$ \label{eq:bms-rfx}
\begin{split}
p(y_i|m_i = e_j)
\quad &\mathrm{for} \quad
i = 1,\ldots,N
\quad \mathrm{and} \quad
j = 1,\ldots,K \\
m_i \sim \mathrm{Cat}(r)
\quad &\mathrm{for} \quad
i = 1,\ldots,N \\
r \sim \mathrm{Dir}(\alpha_0)
\; . \quad &
\end{split}
$$

Then, using [variational Bayesian inference](/D/vb) with the [mean-field approximation](/D/mfa) leads to the following iterative scheme for the [posterior distribution](/D/post) over model frequencies $r$:

$$ \label{eq:bms-rfx-vb}
\begin{split}
& \alpha = \alpha_0 \\
& \text{until convergence} \\
& \quad \quad u_{ij}  = \exp \left[ \ln p(y_i|e_j) + \psi(\alpha_j) - \psi\left( \sum_{j=1}^K \alpha_j \right) \right] \\
& \quad \quad \beta_j = \sum_{i=1}^N \frac{u_{ij}}{u_i} \quad \text{where} \quad u_i = \sum_{j=1}^K u_{ij} \\
& \quad \quad \alpha  = \alpha_0 + \beta \\
& \text{end} \\
& \alpha_n = \alpha \\
& p(r|y)   = \mathrm{Dir}(r; \alpha_n) \; .
\end{split}
$$

Here, $\ln p(y_i \vert e_j)$ is the [log model evidence](/D/lme) of the $j$-model applied to the $i$-th data set, $\alpha_0$ and $\alpha_n$ are [prior](/D/prior) and [posterior](/D/post) concentration parameters, respectively, and $\psi(x)$ is the digamma function defined in terms of the gamma function $\Gamma(x)$:

$$ \label{eq:psi}
\psi(x) = \frac{\mathrm{d}}{\mathrm{d}x} \ln \Gamma(x) \; .
$$


**Proof:** Since data sets $y_i$ (and thus, models $m_i$) are considered [(conditionally) independent](/D/ind-cond), we have:

$$ \label{eq:p-y-m-p-m-r}
\begin{split}
p(y|m) &= \prod_{i=1}^N p(y_i|m_i) \\
p(m|r) &= \prod_{i=1}^N p(m_i|r) \; .
\end{split}
$$

1) First, we need to establish the [joint likelihood](/D/jl). Using the [probability mass function of the categorical distribution](/P/cat-pmf) and the [probability density function of the Dirichlet distribution](/P/dir-pdf), we obtain:

$$ \label{eq:p-y-m-r}
\begin{split}
   p(y,m,r)
&= p(y|m) \, p(m|r) \, p(r|\alpha) \\
&= \left[ \prod_{i=1}^N p(y_i|m_i) \right] \cdot
   \left[ \prod_{i=1}^N p(m_i|r) \right] \cdot
   p(r|\alpha) \\
&= \left[ \prod_{i=1}^N \prod_{j=1}^K p(y_i|e_j)^{m_{ij}} \right] \cdot
   \left[ \prod_{i=1}^N \prod_{j=1}^K r_j^{m_{ij}} \right] \cdot
   \left[ \frac{1}{Z(\alpha)} \prod_{j=1}^K {r_i}^{\alpha_j-1} \right] \\
&= \frac{1}{Z(\alpha)} \cdot
   \left[ \prod_{j=1}^K {r_i}^{\alpha_j-1} \right] \cdot
   \left[ \prod_{i=1}^N \prod_{j=1}^K \left( p(y_i|e_j) \cdot r_j \right)^{m_{ij}} \right] \\
\mathrm{where} \quad Z(\alpha) &= \frac{\prod_{i=1}^k \Gamma(\alpha_i)}{\Gamma\left( \sum_{i=1}^k \alpha_i \right)} \; .
\end{split}
$$

Thus, the [joint log-likelihood function](/D/jl) is given by

$$ \label{eq:ln-p-y-m-r}
   \ln p(y,m,r)
= -\ln Z(\alpha) + \sum_{j=1}^K (\alpha_j-1) \ln r_j + \sum_{i=1}^N \sum_{j=1}^K m_{ij} \left[ \ln p(y_i|e_j) + \ln r_j \right] \; .
$$

The [mean-field approximation](/D/mfa) is based on assuming that the [approximate posterior distribution](/D/vb) factorizes with respect to [model parameters](/D/para)

$$ \label{eq:q-m-r}
p(m,r|y) \approx q(m,r) = q(m) \cdot q(r)
$$

which [implies that each posterior distribution is propertional to an exponentiated variational energy](/P/vb-mfa)

$$ \label{eq:q-m-q-r}
\begin{split}
q(m) &\propto \exp \left[ I(r) \right] \\
q(r) &\propto \exp \left[ I(m) \right]
\end{split}
$$

where the [variational energies are expectations over the joint log-likelihood with respect to the other model parameters](/P/vb-mfa):

$$ \label{eq:I-m-I-r}
\begin{split}
I(m) &= \left\langle \ln p(y,m,r) \right\rangle_{q(r)} \\
I(r) &= \left\langle \ln p(y,m,r) \right\rangle_{q(m)} \; .
\end{split}
$$

2) Inferring on $q(m) \approx p(m \vert y)$ gives the following result:

$$ \label{eq:I-m}
\begin{split}
   I(m)
&= \left\langle \ln p(y,m,r) \right\rangle_{q(r)} \\
&= \sum_{i=1}^N \sum_{j=1}^K m_{ij} \left[ \ln p(y_i|e_j) + \left\langle \ln r_j \right\rangle_{q(r)} \right] \\
&= \sum_{i=1}^N \sum_{j=1}^K m_{ij} \left[ \ln p(y_i|e_j) + \psi(\alpha_j) - \psi\left( \sum_{j=1}^K \alpha_j \right) \right] + \mathrm{const.}
\end{split}
$$

where we have used the [Dirichlet distribution property](/P/dir-logmean)

$$ \label{eq:dir-logmean}
X \sim \mathrm{Dir}(\alpha)
\quad \Rightarrow \quad
\left\langle \ln X_j \right\rangle = \psi(\alpha_j) - \psi\left( \sum_{j=1}^K \alpha_j \right)
\quad \mathrm{for} \quad
j = 1,\ldots,K \; .
$$

Exponentiating and normalizing, we obtain:

$$ \label{eq:q-m}
\begin{split}
   q(m)
&\approx \exp \left[ I(m) \right] \\
&= \prod_{i=1}^N \prod_{j=1}^K \left( \exp \left[ \ln p(y_i|e_j) + \psi(\alpha_j) - \psi\left( \sum_{j=1}^K \alpha_j \right) \right] \right)^{m_{ij}} \cdot \mathrm{const.} \\
&= \prod_{i=1}^N \prod_{j=1}^K \left( \frac{u_{ij}}{u_i} \right)^{m_{ij}} \\
\mathrm{where} \quad u_{ij} &= \exp \left[ \ln p(y_i|e_j) + \psi(\alpha_j) - \psi\left( \sum_{j=1}^K \alpha_j \right) \right] \\
\mathrm{and}   \quad u_i    &= \sum_{j=1}^K u_{ij} \; .
\end{split}
$$

This corresponds to a [categorical distribution](/D/cat) over $m_i$:

$$ \label{eq:p-m-y}
p(m_i|y) = \mathrm{Cat}\left( m_i; \frac{u_{ij}}{u_i} \right) \; .
$$

3) Inferring on $q(r) \approx p(r \vert y)$ gives the following result:

$$ \label{eq:I-r}
\begin{split}
   I(r)
&= \left\langle \ln p(y,m,r) \right\rangle_{q(m)} \\
&= \sum_{j=1}^K (\alpha_j-1) \ln r_j + \sum_{i=1}^N \sum_{j=1}^K \left\langle m_{ij} \right\rangle_{q(m)} \ln r_j + \mathrm{const.} \\
&= \sum_{j=1}^K (\alpha_j-1) \ln r_j + \sum_{i=1}^N \sum_{j=1}^K \left( \frac{u_{ij}}{u_i} \right) \ln r_j + \mathrm{const.} \\
&= \sum_{j=1}^K \left( \alpha_j + \sum_{i=1}^N \frac{u_{ij}}{u_i} - 1 \right) \ln r_j + \mathrm{const.}
\end{split}
$$

where we have used the [categorical distribution property](/P/cat-mean)

$$ \label{eq:cat-mean}
X \sim \mathrm{Cat}(p)
\quad \Rightarrow \quad
\left\langle X_j \right\rangle = p_j
\quad \mathrm{for} \quad
j = 1,\ldots,K \; .
$$

Exponentiating and normalizing, we obtain:

$$ \label{eq:q-r}
\begin{split}
   q(r)
&\approx \exp \left[ I(r) \right] \\
&= \prod_{j=1}^K r_j^{\alpha_j + \beta_j - 1} \cdot \mathrm{const.} \\
\mathrm{where} \quad \beta_j &= \sum_{i=1}^N \frac{u_{ij}}{u_i} \; .
\end{split}
$$

This corresponds to a [Dirichlet distribution](/D/dir) over $r$:

$$ \label{eq:p-r-y}
p(r|y) = \mathrm{Dir}(r; \alpha + \beta) \; .
$$

4) Taken together, \eqref{eq:q-m} and \eqref{eq:q-r} imply the following iterative scheme for the posterior distribution in [random-effects Bayesian model selection](/D/bms-rfx):

$$ \label{eq:bms-rfx-vb-qed}
\begin{split}
& \alpha = \alpha_0 \\
& \text{until convergence} \\
& \quad \quad u_{ij}  = \exp \left[ \ln p(y_i|e_j) + \psi(\alpha_j) - \psi\left( \sum_{j=1}^K \alpha_j \right) \right] \\
& \quad \quad \beta_j = \sum_{i=1}^N \frac{u_{ij}}{u_i} \quad \text{where} \quad u_i = \sum_{j=1}^K u_{ij} \\
& \quad \quad \alpha  = \alpha_0 + \beta \\
& \text{end}
\end{split}
$$