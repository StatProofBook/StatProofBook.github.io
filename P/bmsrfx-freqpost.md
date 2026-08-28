---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-06-29 17:36:00

title: "Posterior frequencies for random-effects Bayesian model selection using Dirichlet posterior distribution"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Random-effects Bayesian model selection"
theorem: "Posterior frequencies"

sources:
  - authors: "Stephan KE, Penny WD, Daunizeau J, Moran RJ, Friston KJ"
    year: 2009
    title: "Bayesian model selection for group studies"
    in: "NeuroImage"
    pages: "vol. 46, pp. 1004–1017, eqs. 15-17"
    url: "https://www.sciencedirect.com/science/article/abs/pii/S1053811909002638"
    doi: "10.1016/j.neuroimage.2009.03.025"

proof_id: "P545"
shortcut: "bmsrfx-freqpost"
username: "JoramSoch"
---


**Theorem:** Consider [model evidences](/D/ml) $p(y_i \vert m)$ from $K$ models describing $N$ data sets $y = \left\lbrace y_1, \ldots, y_N \right\rbrace$ and assume that those data follow the group-level [model](/D/fpm) specified by [random-effects Bayesian model selection](/D/bms-rfx) (RFX BMS):

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
r \sim \mathrm{Dir}(\alpha)
\; . \quad &
\end{split}
$$

Furthermore, let $p(r \vert y)$ be a [Dirichlet](/D/dir) [posterior density](/D/post) over [model frequencies](/D/bms-rfx), e.g. obtained via [variational Bayes for RFX BMS](/P/bmsrfx-vb), parametrized by [concentration parameters](/D/dir) $\alpha_n$:

$$ \label{eq:bms-rfx-post}
p(r|y) = \mathrm{Dir}(r; \alpha_n) \; .
$$

Then, the posterior [expected frequency](/D/expfreq), [likeliest frequency](/D/likfreq) and [exceedance probability](/D/excprob) of the $j$-th model are given by:

$$ \label{eq:bms-rfx-freq-post}
\begin{split}
\mathrm{EF}_j &= \frac{\alpha_{nj}}{\sum_{k=1}^K \alpha_{nk}} \\
\mathrm{LF}_j &= \frac{\alpha_{nj} - 1}{\sum_{k=1}^K \alpha_{nk} - K} \\
\mathrm{EP}_j &= \int_0^\infty \prod_{i \neq j} \left( \frac{\gamma(\alpha_{ni},q_j)}{\Gamma(\alpha_{ni})} \right) \, \frac{q_j^{\alpha_{nj}-1} \exp[-q_j]}{\Gamma(\alpha_{nj})} \, \mathrm{d}q_j \; .
\end{split}
$$


**Proof:** Let $\alpha_n$ be [posterior](/D/post) [concentration parameters](/D/dir) specifying a [Dirichlet](/D/dir) [probability distribution](/D/dist) over possible combinations of model frequencies $r$:

$$ \label{eq:bms-rfx-post-dir}
r|y \sim \mathrm{Dir}(\alpha_n)
\quad \mathrm{where} \quad
0 \leq r_j \leq 1
\quad \mathrm{for} \quad
j = 1,\ldots,K
\quad \mathrm{and} \quad
\sum_{j=1}^K r_j = 1 \; .
$$

1) The [mean of the Dirichlet distribution](/P/dir-mean) is:

$$ \label{eq:dir-mean}
X \sim \mathrm{Dir}(\alpha)
\quad \Rightarrow \quad
\mathrm{E}(X_j) = \frac{\alpha_j}{\sum_{k=1}^K \alpha_k} \; .
$$

Thus, the expected frequency according to the posterior distribution is:

$$ \label{eq:bms-rfx-freq-exp}
\mathrm{EF}_j = \frac{\alpha_{nj}}{\sum_{k=1}^K \alpha_{nk}}
\quad \mathrm{for} \quad
j = 1,\ldots,K \; .
$$

2) The [mode of the Dirichlet distribution](/P/dir-mode) is:

$$ \label{eq:dir-mode}
X \sim \mathrm{Dir}(\alpha)
\quad \Rightarrow \quad
\mathrm{mode}(X_j) = \frac{\alpha_j - 1}{\sum_{k=1}^K \alpha_k - K} \; .
$$

Thus, the likeliest frequency according to posterior distribution is:

$$ \label{eq:bms-rfx-freq-lik}
\mathrm{LF}_j = \frac{\alpha_{nj} - 1}{\sum_{k=1}^K \alpha_{nk} - K}
\quad \mathrm{for} \quad
j = 1,\ldots,K \; .
$$

3) The [exceedance probabilities for the Dirichlet distribution](/P/dir-probexc) are given by

$$ \label{eq:dir-prob-exc}
\begin{split}
X  \sim \mathrm{Dir}(\alpha)
   \quad \Rightarrow \quad
   \varphi(X_j)
&= \mathrm{Pr}\left( \forall i \in \left\lbrace 1, \ldots, n | i \neq j \right\rbrace: \, X_j > X_i \right) \\
&= \int_0^\infty \prod_{i \neq j} \left( \frac{\gamma(\alpha_i,q_j)}{\Gamma(\alpha_i)} \right) \, \frac{q_j^{\alpha_j-1} \exp[-q_j]}{\Gamma(\alpha_j)} \, \mathrm{d}q_j
\end{split}
$$

where $\Gamma(x)$ is the gamma function and $\gamma(s,x)$ is the lower incomplete gamma function. Thus, the probability that, according to the posterior distribution, $r_j$ is higher than all other model frequencies $r_i$, $i \neq j$, is equal to:

$$ \label{eq:bms-rfx-prob-exc}
\mathrm{EP}_j = \int_0^\infty \prod_{i \neq j} \left( \frac{\gamma(\alpha_{ni},q_j)}{\Gamma(\alpha_{ni})} \right) \, \frac{q_j^{\alpha_{nj}-1} \exp[-q_j]}{\Gamma(\alpha_{nj})} \, \mathrm{d}q_j
\quad \mathrm{for} \quad
j = 1,\ldots,K \; .
$$