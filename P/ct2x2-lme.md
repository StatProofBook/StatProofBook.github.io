---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-09-11 13:59:30

title: "Log model evidences for $2 \times 2$ contigency table models"
chapter: "Statistical Models"
section: "Count data"
topic: "$2 \times 2$ contingency table"
theorem: "Log model evidences"

sources:

proof_id: "P550"
shortcut: "ct2x2-lme"
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

Then, the [log model evidence](/D/lme) of $m_0$ is

$$ \label{eq:m0-lme}
\begin{split}
   \log \mathrm{p}(y|m_0)
&= \log \Gamma(n+1) - \sum_{j=1}^4 \log \Gamma(y_j+1) \\
&+ \log B(\alpha_n,\beta_n)  - \log B(\alpha_0,\beta_0) \\
&+ \log B(\gamma_n,\delta_n) - \log B(\gamma_0,\delta_0)
\end{split}
$$

where

$$ \label{eq:m0-post-par}
\alpha_n = \alpha_0 + y_1 + y_2, \quad
\beta_n  = \beta_0  + y_3 + y_4, \quad
\gamma_n = \gamma_0 + y_1 + y_3, \quad
\delta_n = \delta_0 + y_2 + y_4
$$

and the [log model evidence](/D/lme) of $m_1$ is

$$ \label{eq:m1-lme}
\begin{split}
   \log \mathrm{p}(y|m_1)
&= \log \Gamma(n+1) - \sum_{j=1}^4 \log \Gamma(y_j+1) \\
&+ \log \Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right) - \sum_{j=1}^4 \log \Gamma(\alpha_{0j}) \\
&- \log \Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right) + \sum_{j=1}^4 \log \Gamma(\alpha_{nj})
\end{split}
$$

where

$$ \label{eq:m1-post-par}
\alpha_{nj} = \alpha_{0j} + y_j
\quad \mathrm{for} \quad
j = 1,\ldots,4
$$

with $\Gamma(x)$ and $B(x,y)$ denoting the gamma and beta function, respectively.


**Proof:** The [likelihood function](/D/lf) for observed counts $y$, given cell probabilities $p$ is given by the [probability mass function of the multinomial distribution](/P/mult-pmf):

$$ \label{eq:p-y-p}
\begin{split}
   \mathrm{p}(y|p)
&= \mathrm{Mult}(n; \left[ p_1, p_2, p_3, p_4 \right]) \\
&= {n \choose {y_1, y_2, y_3, y_4}} \prod_{j=1}^4 {p_j}^{y_j} \; .
\end{split}
$$

The null model has two free parameters ($p$ and $q$) while the alternative has three free parameters ($r_1$, $r_2$ and $r_3$, since $r_4 = 1 - r_1 - r_2 - r_3$).

1) For the null model $m_0$, with \eqref{eq:m0-p}, the likelihood function \eqref{eq:p-y-p} becomes:

$$ \label{eq:m0-p-y-pq}
  \mathrm{p}(y|p,q)
= {n \choose {y_1, y_2, y_3, y_4}} \cdot (pq)^{y_1} \cdot (p(1-q))^{y_2} \cdot ((p-1)q)^{y_3} \cdot ((p-1)(q-1))^{y_4} \; .
$$

From \eqref{eq:m0-pq}, the prior densities for $p$ and $q$ are:

$$ \label{eq:m0-p-pq}
\begin{split}
   \mathrm{p}(p)
&= \mathrm{Bet}(p; \alpha_0, \beta_0)
 = \frac{1}{B(\alpha_0,\beta_0)} \, p^{\alpha_0-1} \, (1-p)^{\beta_0-1} \\
   \mathrm{p}(q)
&= \mathrm{Bet}(q; \gamma_0, \delta_0)
 = \frac{1}{B(\gamma_0,\delta_0)} \, p^{\gamma_0-1} \, (1-p)^{\delta_0-1} \; .
\end{split}
$$

Thus, combining \eqref{eq:m0-p-y-pq} and \eqref{eq:m0-p-pq}, the [joint likelihood function](/D/jl) is:

$$ \label{eq:m0-p-ypq-s1}
\begin{split}
   \mathrm{p}(y,p,q)
&= \mathrm{p}(y|p,q) \cdot \mathrm{p}(p) \cdot \mathrm{p}(q) \\
&= {n \choose {y_1, y_2, y_3, y_4}} \cdot (pq)^{y_1} \cdot (p(1-q))^{y_2} \cdot ((p-1)q)^{y_3} \cdot ((p-1)(q-1))^{y_4} \cdot \\
&\hphantom{=} \frac{1}{B(\alpha_0,\beta_0)}  \, p^{\alpha_0-1} \, (1-p)^{\beta_0-1} \cdot \frac{1}{B(\gamma_0,\delta_0)} \, p^{\gamma_0-1} \, (1-p)^{\delta_0-1} \; .
\end{split}
$$

Collecting identical variables, we obtain:

$$ \label{eq:m0-p-ypq-s2}
\begin{split}
   \mathrm{p}(y,p,q)
&= {n \choose {y_1, y_2, y_3, y_4}} \, \frac{1}{B(\alpha_0,\beta_0)} \, \frac{1}{B(\gamma_0,\delta_0)} \cdot \\
&\phantom{=} p^{\alpha_0 + y_1 + y_2 - 1} \, (1-p)^{\beta_0 + y_3 + y_4 - 1} \, p^{\gamma_0 + y_1 + y_3 - 1} \, (1-p)^{\delta_0 + y_2 + y_4 - 1} \\
&\overset{\eqref{eq:m0-post-par}}{=} {n \choose {y_1, y_2, y_3, y_4}} \, \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)} \, \frac{B(\gamma_n,\delta_n)}{B(\gamma_0,\delta_0)} \cdot \\
&\phantom{=} \frac{1}{B(\alpha_n,\beta_n)} \, p^{\alpha_n-1} \, (1-p)^{\beta_n-1} \cdot \frac{1}{B(\gamma_n,\delta_n)} \, p^{\gamma_n-1} \, (1-p)^{\delta_n-1} \\
&= {n \choose {y_1, y_2, y_3, y_4}} \, \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)} \, \frac{B(\gamma_n,\delta_n)}{B(\gamma_0,\delta_0)} \cdot \mathrm{Bet}(p; \alpha_n, \beta_n) \cdot \mathrm{Bet}(q; \gamma_n, \delta_n) \; .
\end{split}
$$

With that, we can integrate out $p$ and $q$:

$$ \label{eq:m0-p-y-m}
\begin{split}
   \mathrm{p}(y|m_0)
&= \iint \mathrm{p}(y,p,q) \, \mathrm{d}p \, \mathrm{d}q \\
&= {n \choose {y_1, y_2, y_3, y_4}} \, \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)} \, \frac{B(\gamma_n,\delta_n)}{B(\gamma_0,\delta_0)} \iint \mathrm{Bet}(p; \alpha_n, \beta_n) \cdot \mathrm{Bet}(q; \gamma_n, \delta_n) \, \mathrm{d}p \, \mathrm{d}q \\
&= {n \choose {y_1, y_2, y_3, y_4}} \, \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)} \, \frac{B(\gamma_n,\delta_n)}{B(\gamma_0,\delta_0)} \\
&= \frac{n!}{\prod_{j=1}^4 y_j!} \, \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)} \, \frac{B(\gamma_n,\delta_n)}{B(\gamma_0,\delta_0)} \; .
\end{split}
$$

Finally, logarithmizing both sides and applying the relation $n! = \Gamma(n+1)$, we obtain:

$$ \label{eq:m0-lme-qed}
\begin{split}
   \log \mathrm{p}(y|m_0)
&= \log \Gamma(n+1) - \sum_{j=1}^4 \log \Gamma(y_j+1) \\
&+ \log B(\alpha_n,\beta_n)  - \log B(\alpha_0,\beta_0) \\
&+ \log B(\gamma_n,\delta_n) - \log B(\gamma_0,\delta_0) \ .
\end{split}
$$

2) For the alternative $m_1$, with \eqref{eq:m1-p}, the likelihood function \eqref{eq:p-y-p} becomes:

$$ \label{eq:m1-p-y-r}
  \mathrm{p}(y|r)
= {n \choose {y_1, y_2, y_3, y_4}} \cdot \prod_{j=1}^4 {r_j}^{y_j} \; .
$$

From \eqref{eq:m1-r}, the prior density for $r$ ps:

$$ \label{eq:m1-p-r}
  \mathrm{p}(r)
= \mathrm{Dir}(r; \left[ \alpha_{01}, \alpha_{02}, \alpha_{03}, \alpha_{04} \right])
= \frac{\Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right)}{\prod_{j=1}^4 \Gamma(\alpha_{0j})} \prod_{j=1}^4 {r_j}^{\alpha_{0j}-1} \; .
$$

Thus, combining \eqref{eq:m1-p-r} and \eqref{eq:m1-p-r}, the [joint likelihood function](/D/jl) is:

$$ \label{eq:m1-p-yr-s1}
\begin{split}
   \mathrm{p}(y,r)
&= \mathrm{p}(y|r) \cdot \mathrm{p}(r) \\
&= {n \choose {y_1, y_2, y_3, y_4}} \prod_{j=1}^4 {r_j}^{y_j} \cdot \frac{\Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right)}{\prod_{j=1}^4 \Gamma(\alpha_{0j})} \prod_{j=1}^4 {r_j}^{\alpha_{0j}-1} \; .
\end{split}
$$

Collecting identical variables, we obtain:

$$ \label{eq:m1-p-yr-s2}
\begin{split}
   \mathrm{p}(y,r)
&= {n \choose {y_1, y_2, y_3, y_4}} \, \frac{\Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right)}{\prod_{j=1}^4 \Gamma(\alpha_{0j})} \cdot \prod_{j=1}^4 {r_j}^{\alpha_{0j} + y_j - 1} \\
&\overset{\eqref{eq:m1-post-par}}{=} {n \choose {y_1, y_2, y_3, y_4}} \, \frac{\Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right)}{\prod_{j=1}^4 \Gamma(\alpha_{0j})} \, \frac{\prod_{j=1}^4 \Gamma(\alpha_{nj})}{\Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right)} \cdot \frac{\Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right)}{\prod_{j=1}^4 \Gamma(\alpha_{nj})} \prod_{j=1}^4 {r_j}^{\alpha_{nj}-1} \\
&= {n \choose {y_1, y_2, y_3, y_4}} \, \frac{\Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right)}{\prod_{j=1}^4 \Gamma(\alpha_{0j})} \, \frac{\prod_{j=1}^4 \Gamma(\alpha_{nj})}{\Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right)} \cdot \mathrm{Dir}(r; \left[ \alpha_{n1}, \alpha_{n2}, \alpha_{n3}, \alpha_{n4} \right]) \; .
\end{split}
$$

With that, we can integrate out $r$:

$$ \label{eq:m1-p-y-m}
\begin{split}
   \mathrm{p}(y|m_1)
&= \int \mathrm{p}(y,r) \, \mathrm{d}r \\
&= {n \choose {y_1, y_2, y_3, y_4}} \, \frac{\Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right)}{\prod_{j=1}^4 \Gamma(\alpha_{0j})} \, \frac{\prod_{j=1}^4 \Gamma(\alpha_{nj})}{\Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right)} \int \mathrm{Dir}(r; \left[ \alpha_{n1}, \alpha_{n2}, \alpha_{n3}, \alpha_{n4} \right]) \, \mathrm{d}r \\
&= {n \choose {y_1, y_2, y_3, y_4}} \, \frac{\Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right)}{\prod_{j=1}^4 \Gamma(\alpha_{0j})} \, \frac{\prod_{j=1}^4 \Gamma(\alpha_{nj})}{\Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right)} \\
&= \frac{n!}{\prod_{j=1}^4 y_j!} \, \frac{\Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right)}{\prod_{j=1}^4 \Gamma(\alpha_{0j})} \, \frac{\prod_{j=1}^4 \Gamma(\alpha_{nj})}{\Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right)} \; .
\end{split}
$$

Finally, logarithmizing both sides and applying the relation $n! = \Gamma(n+1)$, we obtain:

$$ \label{eq:m1-lme-qed}
\begin{split}
   \log \mathrm{p}(y|m_1)
&= \log \Gamma(n+1) - \sum_{j=1}^4 \log \Gamma(y_j+1) \\
&+ \log \Gamma\left( \sum_{j=1}^4 \alpha_{0j} \right) - \sum_{j=1}^4 \log \Gamma(\alpha_{0j}) \\
&- \log \Gamma\left( \sum_{j=1}^4 \alpha_{nj} \right) + \sum_{j=1}^4 \log \Gamma(\alpha_{nj}) \; .
\end{split}
$$

This completes the proof.