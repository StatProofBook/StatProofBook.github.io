---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-09-11 15:14:06

title: "Log Bayes factor for $2 \times 2$ contigency table models"
chapter: "Statistical Models"
section: "Count data"
topic: "$2 \times 2$ contingency table"
theorem: "Log Bayes factor"

sources:

proof_id: "P551"
shortcut: "ct2x2-lbf"
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

Then, the [log Bayes factor](/D/lme) in favor of $m_1$ against $m_0$ is

$$ \label{eq:ct2x2-lbf}
\begin{split}
   \mathrm{LBF}_{10}
&= \log \Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right) - \log \Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right) + \sum_{j=1}^4 \log \Gamma(\alpha_{nj}) - \sum_{j=1}^4 \log \Gamma(\alpha_{0j}) \\
&+ \log B(\alpha_0,\beta_0) - \log B(\alpha_n,\beta_n) + \log B(\gamma_0,\delta_0) - \log B(\gamma_n,\delta_n)
\end{split}
$$

where $\Gamma(x)$ and $B(x,y)$ are the gamma and beta function, respectively; $\alpha_n$, $\beta_n$, $\gamma_n$ and $\delta_n$ are the [posterior hyperparameters of $m_0$](/P/ct2x2-lme); and $\alpha_{n1}, \ldots, \alpha_{n4}$ are the [posterior hyperparameters of $m_1$](/P/ct2x2-lme).


**Proof:** [The log Bayes factor is equal to the difference of two log model evidences](/P/lbf-lme):

$$ \label{eq:lbf-lme}
\mathrm{LBF}_{12} = \mathrm{LME}(m_1) - \mathrm{LME}(m_2) \; .
$$

The [log model evidence of $m_0$](/P/ct2x2-lme) is

$$ \label{eq:m0-lme}
\begin{split}
   \mathrm{LME}(m_0)
&= \log \Gamma(n+1) - \sum_{j=1}^4 \log \Gamma(y_j+1) \\
&+ \log B(\alpha_n,\beta_n)  - \log B(\alpha_0,\beta_0) \\
&+ \log B(\gamma_n,\delta_n) - \log B(\gamma_0,\delta_0)
\end{split}
$$

and the [log model evidence of $m_1$](/P/ct2x2-lme) is

$$ \label{eq:m1-lme}
\begin{split}
   \mathrm{LME}(m_1)
&= \log \Gamma(n+1) - \sum_{j=1}^4 \log \Gamma(y_j+1) \\
&+ \log \Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right) - \sum_{j=1}^4 \log \Gamma(\alpha_{0j}) \\
&- \log \Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right) + \sum_{j=1}^4 \log \Gamma(\alpha_{nj}) \; .
\end{split}
$$

Subtracting the two LMEs from each other, the LBF emerges as

$$ \label{eq:ct2x2-lbf-qed}
\begin{split}
   \mathrm{LBF}_{10}
&= \log \Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right) - \log \Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right) + \sum_{j=1}^4 \log \Gamma(\alpha_{nj}) - \sum_{j=1}^4 \log \Gamma(\alpha_{0j}) \\
&+ \log B(\alpha_0,\beta_0) - \log B(\alpha_n,\beta_n) + \log B(\gamma_0,\delta_0) - \log B(\gamma_n,\delta_n) \; .
\end{split}
$$