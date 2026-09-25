---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-09-18 13:29:41

title: "Posterior probability of the alternative model for the $2 \times 2$ contigency table"
chapter: "Statistical Models"
section: "Count data"
topic: "$k \times l$ contingency table"
theorem: "Posterior probability"

sources:

proof_id: "P555"
shortcut: "ct-pp"
username: "JoramSoch"
---


**Theorem:** Consider a [k $\times$ l contingency table](/D/ct), denote observed counts as

$$ \label{eq:y}
\left\lbrace y_{ij} \, | \, i \in \left\lbrace 1,\ldots,k \right\rbrace, \, j \in \left\lbrace 1,\ldots,l \right\rbrace \right\rbrace
$$

and assume that these counts come a [multinomial distribution](/D/mult) with unknown cell probabilities:

$$ \label{eq:y-p}
y = \left[ y_{11}, \ldots, y_{kl} \right] \sim \mathrm{Mult}(n; \left[ p_{11}, \ldots, p_{kl} \right]) \; .
$$

Let $m_0$ be a [null model](/D/h0) which assumes [statistical independence](/D/ind) of $A$ and $B$, i.e. cell probabilities

$$ \label{eq:m0-p}
m_0: \quad
p_{ij} = r_i s_j, \quad
i = 1,\ldots,k, \quad
j = 1,\ldots,l
$$

and [Dirichlet](/D/dir) [prior distributions](/D/prior) over the model parameters $r$ and $s$:

$$ \label{eq:m0-rs}
\begin{split}
r &\sim \mathrm{Dir}(\alpha_0) \\
s &\sim \mathrm{Dir}(\beta_0)  \; .
\end{split}
$$

Let $m_1$ be an [alternative model](/D/h1) which allows for arbitrary parametrization of cell probabilities

$$ \label{eq:m1-p}
m_1: \quad
p_{ij} = r_{ij}, \quad
i = 1,\ldots,k, \quad
j = 1,\ldots,l
$$

and [Dirichlet](/D/dir) [prior distributions](/D/prior) over the model parameters $r$:

$$ \label{eq:m1-r}
\mathrm{vec}(r) \sim \mathrm{Dir}\left( \mathrm{vec}\left(\gamma^{(0)}\right) \right) \; .
$$

Then, the [posterior probability](/D/pmp) of the [alternative model](/D/h1) is given by

$$ \label{eq:ct-pp}
  p(m_1|y)
= \left( 1 +
  \frac{Z\left( \mathrm{vec}(\gamma^{(0)}) \right)}{Z\left( \mathrm{vec}(\gamma^{(n)}) \right)} \, \frac{Z\left( \alpha_n \right)}{Z\left( \alpha_0 \right)} \, \frac{Z\left( \beta_n \right)}{Z\left( \beta_0 \right)}
  \right)^{-1} \; .
$$

where $\alpha_n$ and $\beta_n$ are the [posterior hyperparameters of $m_0$](/P/ct-lme); $\gamma_{ij}^{(n)}$ are the [posterior hyperparameters of $m_1$](/P/ct-lme); and $Z(\alpha)$ is defined as

$$ \label{eq:Z-alpha}
  Z(\alpha)
= \frac{\prod_{i=1}^n \Gamma(\alpha_i)}{\Gamma\left( \sum_{i=1}^n \alpha_i \right)}
$$

for an $n$-dimensional vector $\alpha$, with $\Gamma(x)$ being the gamma function.


**Proof:** [The posterior probability for one of two models is a function of the log Bayes factor in favor of this model](/P/pmp-lbf):

$$ \label{eq:pmp-lbf}
p(m_1|y) = \frac{\exp(\mathrm{LBF}_{12})}{\exp(\mathrm{LBF}_{12}) + 1} \; .
$$

Applied to the present model comparison case, this is equal to

$$ \label{eq:pmp-m1}
\begin{split}
   p(m_1|y)
&= \frac{\exp(\mathrm{LBF}_{10})}{\exp(\mathrm{LBF}_{10}) + 1} \\
&= \frac{\frac{1}{\exp(\mathrm{LBF}_{10})}}{\frac{1}{\exp(\mathrm{LBF}_{10})}} \cdot \frac{\exp(\mathrm{LBF}_{10})}{\exp(\mathrm{LBF}_{10}) + 1} \\
&= \frac{1}{1 + \frac{1}{\exp(\mathrm{LBF}_{10})}} \\
&= \frac{1}{1 + \exp(-\mathrm{LBF}_{10})} \\
&= \frac{1}{1 + \exp(\mathrm{LBF}_{01})} \; .
\end{split}
$$

The [LBF in favor of the alternative for the $k \times l$ contingency table](/P/ct-lbf) is given by

$$ \label{eq:ct-lbf}
\begin{split}
   \mathrm{LBF}_{10}
&= \log \Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(0)} \right)
 - \log \Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(n)} \right) \\
&+ \sum_{i=1}^k \sum_{j=1}^l \log \Gamma\left( \gamma_{ij}^{(n)} \right)
 - \sum_{i=1}^k \sum_{j=1}^l \log \Gamma\left( \gamma_{ij}^{(0)} \right) \\
&- \log \Gamma\left( \sum_{i=1}^k \alpha_{0i} \right)
 + \log \Gamma\left( \sum_{i=1}^k \alpha_{ni} \right)
 - \sum_{i=1}^k \log \Gamma\left( \alpha_{ni} \right)
 + \sum_{i=1}^k \log \Gamma\left( \alpha_{0i} \right) \\
&- \log \Gamma\left( \sum_{j=1}^l \beta_{0j}  \right)
 + \log \Gamma\left( \sum_{j=1}^l \beta_{nj}  \right)
 - \sum_{j=1}^l \log \Gamma\left( \beta_{nj}  \right)
 + \sum_{j=1}^l \log \Gamma\left( \beta_{0j}  \right) \; .
\end{split}
$$

With definition \eqref{eq:Z-alpha}, this is equal to:

$$ \label{eq:ct-lbf-Z}
\begin{split}
   \mathrm{LBF}_{10}
&= \log \left[ \frac{Z\left( \mathrm{vec}(\gamma^{(n)}) \right)}{Z\left( \mathrm{vec}(\gamma^{(0)}) \right)} \, \frac{Z\left( \alpha_0 \right)}{Z\left( \alpha_n \right)} \, \frac{Z\left( \beta_0 \right)}{Z\left( \beta_n \right)} \right] \; .
\end{split}
$$

Multiplying \eqref{eq:ct-lbf-Z} with $-1$ and exponentiating, we get

$$ \label{eq:exp-lbf}
\begin{split}
  \exp(-\mathrm{LBF}_{10})
= \frac{Z\left( \mathrm{vec}(\gamma^{(0)}) \right)}{Z\left( \mathrm{vec}(\gamma^{(n)}) \right)} \, \frac{Z\left( \alpha_n \right)}{Z\left( \alpha_0 \right)} \, \frac{Z\left( \beta_n \right)}{Z\left( \beta_0 \right)} \; .
\end{split}
$$

Substituting this expression into \eqref{eq:pmp-m1}, we finally obtain:

$$ \label{eq:ct-pp-qed}
  p(m_1|y)
= \left( 1 +
  \frac{Z\left( \mathrm{vec}(\gamma^{(0)}) \right)}{Z\left( \mathrm{vec}(\gamma^{(n)}) \right)} \, \frac{Z\left( \alpha_n \right)}{Z\left( \alpha_0 \right)} \, \frac{Z\left( \beta_n \right)}{Z\left( \beta_0 \right)}
  \right)^{-1} \; .
$$