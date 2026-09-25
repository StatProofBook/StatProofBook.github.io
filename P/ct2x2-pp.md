---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-09-11 16:22:32

title: "Posterior probability of the alternative model for the $2 \times 2$ contigency table"
chapter: "Statistical Models"
section: "Count data"
topic: "$2 \times 2$ contingency table"
theorem: "Posterior probability"

sources:

proof_id: "P552"
shortcut: "ct2x2-pp"
username: "JoramSoch"
---


**Theorem:** Consider a [2 $\times$ 2 contingency table](/D/ct2x2), denote observed counts as

$$ \label{eq:y}
\left\lbrace y_1, y_2, y_3, y_4 \right\rbrace
$$

and assume that these counts come a [multinomial distribution](/D/mult) with unknown cell probabilities:

$$ \label{eq:y-p}
y = \left[ y_1, y_2, y_3, y_4 \right] \sim \mathrm{Mult}(n; \left[ p_1, p_2, p_3, p_4 \right]) \; .
$$

Let $m_0$ be a [null model](/D/h0) which assumes [statistical independence](/D/ind) of $A$ and $B$, i.e. cell probabilities

$$ \label{eq:m0-p}
m_0: \quad
p_1 = p q, \quad
p_2 = p (1-q), \quad
p_3 = (1-p) q, \quad
p_4 = (1-p) (1-q) \; ,
$$

and [beta](/D/beta) [prior distributions](/D/prior) over the model parameters $p$ and $q$:

$$ \label{eq:m0-pq}
\begin{split}
p &\sim \mathrm{Bet}(\alpha_0, \beta_0) \\
q &\sim \mathrm{Bet}(\gamma_0, \delta_0) \; .
\end{split}
$$

Let $m_1$ be an [alternative model](/D/h1) which allows for arbitrary parametrization of cell probabilities

$$ \label{eq:m1-p}
m_1: \quad
p_1 = r_1, \quad
p_2 = r_2, \quad
p_3 = r_3, \quad
p_4 = r_4
$$

and has a [Dirichlet](/D/dir) [prior distribution](/D/prior) over the model parameters $r$:

$$ \label{eq:m1-r}
r \sim \mathrm{Dir}\left(\left[ \alpha_{01}, \alpha_{02}, \alpha_{03}, \alpha_{04} \right]\right) \; .
$$

Then, the [posterior probability](/D/pmp) of the [alternative model](/D/h1) is given by

$$ \label{eq:ct2x2-pp}
  p(m_1|y)
= \left( 1 +
  \frac{\Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right)}{\Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right)} \cdot
  \frac{\prod_{j=1}^4 \Gamma(\alpha_{0j})}{\prod_{j=1}^4 \Gamma(\alpha_{nj})} \cdot
  \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)} \cdot
  \frac{B(\gamma_n,\delta_n)}{B(\gamma_0,\delta_0)}
  \right)^{-1}
$$

where $\Gamma(x)$ and $B(x,y)$ are the gamma and beta function, respectively; $\alpha_n$, $\beta_n$, $\gamma_n$ and $\delta_n$ are the [posterior hyperparameters of $m_0$](/P/ct2x2-lme); and $\alpha_{n1}, \ldots, \alpha_{n4}$ are the [posterior hyperparameters of $m_1$](/P/ct2x2-lme).


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

The [LBF in favor of the alternative for the $2 \times 2$ contingency table](/P/ct2x2-lbf) is given by

$$ \label{eq:ct2x2-lbf}
\begin{split}
   \mathrm{LBF}_{10}
&= \log \Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right) - \log \Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right) + \sum_{j=1}^4 \log \Gamma(\alpha_{nj}) - \sum_{j=1}^4 \log \Gamma(\alpha_{0j}) \\
&+ \log B(\alpha_0,\beta_0) - \log B(\alpha_n,\beta_n) + \log B(\gamma_0,\delta_0) - \log B(\gamma_n,\delta_n) \; .
\end{split}
$$

Multiplying \eqref{eq:ct2x2-lbf} with $-1$ and exponentiating, we get

$$ \label{eq:exp-lbf}
\begin{split}
  \exp(-\mathrm{LBF}_{10})
= \frac{\Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right)}{\Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right)} \cdot
  \frac{\prod_{j=1}^4 \Gamma(\alpha_{0j})}{\prod_{j=1}^4 \Gamma(\alpha_{nj})} \cdot
  \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)} \cdot
  \frac{B(\gamma_n,\delta_n)}{B(\gamma_0,\delta_0)} \; .
\end{split}
$$

Substituting this expression into \eqref{eq:pmp-m1}, we finally obtain:

$$ \label{eq:ct2x2-pp-qed}
  p(m_1|y)
= \left( 1 +
  \frac{\Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right)}{\Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right)} \cdot
  \frac{\prod_{j=1}^4 \Gamma(\alpha_{0j})}{\prod_{j=1}^4 \Gamma(\alpha_{nj})} \cdot
  \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)} \cdot
  \frac{B(\gamma_n,\delta_n)}{B(\gamma_0,\delta_0)}
  \right)^{-1} \; .
$$