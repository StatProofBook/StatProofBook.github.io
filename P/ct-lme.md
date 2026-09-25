---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-09-18 11:29:18

title: "Log model evidences for $k \times l$ contigency table models"
chapter: "Statistical Models"
section: "Count data"
topic: "$k \times l$ contingency table"
theorem: "Log model evidences"

sources:

proof_id: "P553"
shortcut: "ct-lme"
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

Then, the [log model evidence](/D/lme) of $m_0$ is

$$ \label{eq:m0-lme}
\begin{split}
   \log p(y|m_0)
&= \log \Gamma(n+1) - \sum_{i=1}^k \sum_{j=1}^l \log \Gamma(y_{ij}+1) \\
&+ \log \Gamma\left( \sum_{i=1}^k \alpha_{0i} \right)
 - \log \Gamma\left( \sum_{i=1}^k \alpha_{ni} \right)
 + \sum_{i=1}^k \log \Gamma\left( \alpha_{ni} \right)
 - \sum_{i=1}^k \log \Gamma\left( \alpha_{0i} \right) \\
&+ \log \Gamma\left( \sum_{j=1}^l \beta_{0j}  \right)
 - \log \Gamma\left( \sum_{j=1}^l \beta_{nj}  \right)
 + \sum_{j=1}^l \log \Gamma\left( \beta_{nj}  \right)
 - \sum_{j=1}^l \log \Gamma\left( \beta_{0j}  \right)
\end{split}
$$

where

$$ \label{eq:m0-post-par}
\alpha_{ni} = \alpha_{0i} + \sum_{j=1}^l y_{ij}, \quad
\beta_{nj}  = \beta_{0j}  + \sum_{i=1}^k y_{ij}, \quad
i = 1,\ldots,k, \quad
j = 1,\ldots,l
$$

and the [log model evidence](/D/lme) of $m_1$ is

$$ \label{eq:m1-lme}
\begin{split}
   \log p(y|m_1)
&= \log \Gamma(n+1) - \sum_{i=1}^k \sum_{j=1}^l \log \Gamma(y_{ij}+1) \\
&+ \log \Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(0)} \right)
 - \log \Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(n)} \right) \\
&+ \sum_{i=1}^k \sum_{j=1}^l \log \Gamma\left( \gamma_{ij}^{(n)} \right)
 - \sum_{i=1}^k \sum_{j=1}^l \log \Gamma\left( \gamma_{ij}^{(0)} \right)
\end{split}
$$

where

$$ \label{eq:m1-post-par}
\gamma_{ij}^{(n)} = \gamma_{ij}^{(0)} + y_{ij}, \quad
i = 1,\ldots,k, \quad
j = 1,\ldots,l
$$

and $\Gamma(x)$ denotes the gamma function.


**Proof:** The [likelihood function](/D/lf) for observed counts $y$, given cell probabilities $p$ is given by the [probability mass function of the multinomial distribution](/P/mult-pmf):

$$ \label{eq:p-y-p}
\begin{split}
   \mahtrm{p}(y|p)
&= \mathrm{Mult}(n; \left[ p_{11}, \ldots, p_{kl} \right]) \\
&= {n \choose {y_{11}, \ldots, y_{kl}}} \prod_{i=1}^k \prod_{j=1}^l {p_{ij}}^{y_{ij}} \; .
\end{split}
$$

The null model has $(k-1) + (l-1)$ free parameters ($r_1,\ldots,r_{k-1}$ plus $s_1,\ldots,s_{l-1}$) while the alternative has $k \cdot l - 1$ free parameters ($r_1,\ldots,r_{k,l-1}$).

1) For the null model $m_0$, with \eqref{eq:m0-p}, the likelihood function \eqref{eq:p-y-p} becomes:

$$ \label{eq:m0-p-y-rs}
  p(y|r,s)
= {n \choose {y_{11}, \ldots, y_{kl}}} \prod_{i=1}^k \prod_{j=1}^l (r_i s_j)^{y_{ij}} \; .
$$

From \eqref{eq:m0-rs}, the prior densities for $r$ and $s$ are:

$$ \label{eq:m0-p-rs}
\begin{split}
   p(r)
&= \mathrm{Dir}(r; \alpha_0)
 = \frac{\Gamma\left( \sum_{i=1}^k \alpha_{0i} \right)}{\prod_{i=1}^k \Gamma(\alpha_{0i})} \prod_{i=1}^k {r_i}^{\alpha_{0i}-1} \\
   p(s)
&= \mathrm{Dir}(s; \beta_0)
 = \frac{\Gamma\left( \sum_{j=1}^l \beta_{0j} \right)}{\prod_{j=1}^l \Gamma(\beta_{0j})} \prod_{j=1}^l {s_j}^{\beta_{0j}-1} \; .
\end{split}
$$

Thus, combining \eqref{eq:m0-p-y-rs} and \eqref{eq:m0-p-rs}, the [joint likelihood function](/D/jl) is:

$$ \label{eq:m0-p-yrs-s1}
\begin{split}
   p(y,r,s)
&= p(y|r,s) \cdot p(r) \cdot p(s) \\
&= {n \choose {y_{11}, \ldots, y_{kl}}} \prod_{i=1}^k \prod_{j=1}^l (r_i s_j)^{y_{ij}} \cdot \\
&\hphantom{=} \frac{\Gamma\left( \sum_{i=1}^k \alpha_{0i} \right)}{\prod_{i=1}^k \Gamma(\alpha_{0i})} \prod_{i=1}^k {r_i}^{\alpha_{0i}-1} \cdot \frac{\Gamma\left( \sum_{j=1}^l \beta_{0j} \right)}{\prod_{j=1}^l \Gamma(\beta_{0j})} \prod_{j=1}^l {s_j}^{\beta_{0j}-1} \; .
\end{split}
$$

Collecting identical variables, we obtain:

$$ \label{eq:m0-p-yrs-s2}
\begin{split}
   p(y,r,s)
&= {n \choose {y_{11}, \ldots, y_{kl}}} \, \frac{\Gamma\left( \sum_{i=1}^k \alpha_{0i} \right)}{\prod_{i=1}^k \Gamma(\alpha_{0i})} \, \frac{\Gamma\left( \sum_{j=1}^l \beta_{0j} \right)}{\prod_{j=1}^l \Gamma(\beta_{0j})} \cdot \\
&\phantom{=} \prod_{i=1}^k {r_i}^{\alpha_{0i} + \sum_{j=1}^l y_{ij} - 1} \cdot \prod_{j=1}^l {s_j}^{\beta_{0j} + \sum_{i=1}^k y_{ij} - 1} \\
&\overset{\eqref{eq:m0-post-par}}{=} {n \choose {y_{11}, \ldots, y_{kl}}} \, \frac{\Gamma\left( \sum_{i=1}^k \alpha_{0i} \right)}{\Gamma\left( \sum_{i=1}^k \alpha_{ni} \right)} \, \frac{\prod_{i=1}^k \Gamma(\alpha_{ni})}{\prod_{i=1}^k \Gamma(\alpha_{0i})} \, \frac{\Gamma\left( \sum_{j=1}^l \beta_{0j} \right)}{\Gamma\left( \sum_{j=1}^l \beta_{nj} \right)} \, \frac{\prod_{j=1}^l \Gamma(\beta_{nj})}{\prod_{j=1}^l \Gamma(\beta_{0j})} \cdot \\
&\phantom{=} \frac{\Gamma\left( \sum_{i=1}^k \alpha_{ni} \right)}{\prod_{i=1}^k \Gamma(\alpha_{ni})} \prod_{i=1}^k {r_i}^{\alpha_{ni}-1} \cdot \frac{\Gamma\left( \sum_{j=1}^l \beta_{nj} \right)}{\prod_{j=1}^l \Gamma(\beta_{nj})} \prod_{j=1}^l {s_j}^{\beta_{nj}-1} \\
&= {n \choose {y_{11}, \ldots, y_{kl}}} \, \frac{\Gamma\left( \sum_{i=1}^k \alpha_{0i} \right)}{\Gamma\left( \sum_{i=1}^k \alpha_{ni} \right)} \, \frac{\prod_{i=1}^k \Gamma(\alpha_{ni})}{\prod_{i=1}^k \Gamma(\alpha_{0i})} \, \frac{\Gamma\left( \sum_{j=1}^l \beta_{0j} \right)}{\Gamma\left( \sum_{j=1}^l \beta_{nj} \right)} \, \frac{\prod_{j=1}^l \Gamma(\beta_{nj})}{\prod_{j=1}^l \Gamma(\beta_{0j})} \cdot \\
&\phantom{=} \mathrm{Dir}(r; \alpha_0) \cdot \mathrm{Dir}(s; \beta_0) \; .
\end{split}
$$

With that, we can integrate out $r$ and $s$:

$$ \label{eq:m0-p-y-m}
\begin{split}
   p(y|m_0)
&= \iint p(y,r,s) \, \mathrm{d}r \, \mathrm{d}s \\
&= {n \choose {y_{11}, \ldots, y_{kl}}} \, \frac{\Gamma\left( \sum_{i=1}^k \alpha_{0i} \right)}{\Gamma\left( \sum_{i=1}^k \alpha_{ni} \right)} \, \frac{\prod_{i=1}^k \Gamma(\alpha_{ni})}{\prod_{i=1}^k \Gamma(\alpha_{0i})} \, \frac{\Gamma\left( \sum_{j=1}^l \beta_{0j} \right)}{\Gamma\left( \sum_{j=1}^l \beta_{nj} \right)} \, \frac{\prod_{j=1}^l \Gamma(\beta_{nj})}{\prod_{j=1}^l \Gamma(\beta_{0j})} \cdot \\
&\phantom{=} \iint \mathrm{Dir}(r; \alpha_0) \cdot \mathrm{Dir}(s; \beta_0) \, \mathrm{d}r \, \mathrm{d}s \\
&= {n \choose {y_{11}, \ldots, y_{kl}}} \, \frac{\Gamma\left( \sum_{i=1}^k \alpha_{0i} \right)}{\Gamma\left( \sum_{i=1}^k \alpha_{ni} \right)} \, \frac{\prod_{i=1}^k \Gamma(\alpha_{ni})}{\prod_{i=1}^k \Gamma(\alpha_{0i})} \, \frac{\Gamma\left( \sum_{j=1}^l \beta_{0j} \right)}{\Gamma\left( \sum_{j=1}^l \beta_{nj} \right)} \, \frac{\prod_{j=1}^l \Gamma(\beta_{nj})}{\prod_{j=1}^l \Gamma(\beta_{0j})} \\
&= \frac{n!}{\prod_{i=1}^k \prod_{j=1}^l y_{ij}!} \, \frac{\Gamma\left( \sum_{i=1}^k \alpha_{0i} \right)}{\Gamma\left( \sum_{i=1}^k \alpha_{ni} \right)} \, \frac{\prod_{i=1}^k \Gamma(\alpha_{ni})}{\prod_{i=1}^k \Gamma(\alpha_{0i})} \, \frac{\Gamma\left( \sum_{j=1}^l \beta_{0j} \right)}{\Gamma\left( \sum_{j=1}^l \beta_{nj} \right)} \, \frac{\prod_{j=1}^l \Gamma(\beta_{nj})}{\prod_{j=1}^l \Gamma(\beta_{0j})} \; .
\end{split}
$$

Finally, logarithmizing both sides and applying the relation $n! = \Gamma(n+1)$, we obtain:

$$ \label{eq:m0-lme-qed}
\begin{split}
   \log p(y|m_0)
&= \log \Gamma(n+1) - \sum_{i=1}^k \sum_{j=1}^l \log \Gamma(y_{ij}+1) \\
&+ \log \Gamma\left( \sum_{i=1}^k \alpha_{0i} \right)
 - \log \Gamma\left( \sum_{i=1}^k \alpha_{ni} \right)
 + \sum_{i=1}^k \log \Gamma\left( \alpha_{ni} \right)
 - \sum_{i=1}^k \log \Gamma\left( \alpha_{0i} \right) \\
&+ \log \Gamma\left( \sum_{j=1}^l \beta_{0j}  \right)
 - \log \Gamma\left( \sum_{j=1}^l \beta_{nj}  \right)
 + \sum_{j=1}^l \log \Gamma\left( \beta_{nj}  \right)
 - \sum_{j=1}^l \log \Gamma\left( \beta_{0j}  \right) \; .
\end{split}
$$

2) For the alternative $m_1$, with \eqref{eq:m1-p}, the likelihood function \eqref{eq:p-y-p} becomes:

$$ \label{eq:m1-p-y-r}
  p(y|r)
= {n \choose {y_{11}, \ldots, y_{kl}}} \prod_{i=1}^k \prod_{j=1}^l {r_{ij}}^{y_{ij}} \; .
$$

From \eqref{eq:m1-r}, the prior density for $r$ ps:

$$ \label{eq:m1-p-r}
  p(\mathrm{vec}(r))
= \mathrm{Dir}\left(\mathrm{vec}(r); \mathrm{vec}\left(\gamma^{(0)}\right)\right)
= \frac{\Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(0)} \right)}{\prod_{i=1}^k \prod_{j=1}^l \Gamma\left(\gamma_{ij}^{(0)}\right)} \prod_{i=1}^k \prod_{j=1}^l {r_{ij}}^{\gamma_{ij}^{(0)}-1} \; .
$$

Thus, combining \eqref{eq:m1-p-r} and \eqref{eq:m1-p-r}, the [joint likelihood function](/D/jl) is:

$$ \label{eq:m1-p-yr-s1}
\begin{split}
   p(y,r)
&= p(y|r) \cdot p(r) \\
&= {n \choose {y_{11}, \ldots, y_{kl}}} \prod_{i=1}^k \prod_{j=1}^l {r_{ij}}^{y_{ij}} \cdot \frac{\Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(0)} \right)}{\prod_{i=1}^k \prod_{j=1}^l \Gamma\left(\gamma_{ij}^{(0)}\right)} \prod_{i=1}^k \prod_{j=1}^l {r_{ij}}^{\gamma_{ij}^{(0)}-1} \; .
\end{split}
$$

Collecting identical variables, we obtain:

$$ \label{eq:m1-p-yr-s2}
\begin{split}
   p(y,r)
&= {n \choose {y_{11}, \ldots, y_{kl}}} \, \frac{\Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(0)} \right)}{\prod_{i=1}^k \prod_{j=1}^l \Gamma\left(\gamma_{ij}^{(0)}\right)} \cdot \prod_{i=1}^k \prod_{j=1}^l {r_{ij}}^{\gamma_{ij}^{(0)}+y_{ij}-1} \\
&\overset{\eqref{eq:m1-post-par}}{=} {n \choose {y_{11}, \ldots, y_{kl}}} \, \frac{\Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(0)} \right)}{\Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(n)} \right)} \, \frac{\prod_{i=1}^k \prod_{j=1}^l \Gamma\left(\gamma_{ij}^{(n)}\right)}{\prod_{i=1}^k \prod_{j=1}^l \Gamma\left(\gamma_{ij}^{(0)}\right)} \cdot \\
&\hphantom{=} \frac{\Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(n)} \right)}{\prod_{i=1}^k \prod_{j=1}^l \Gamma\left(\gamma_{ij}^{(n)}\right)} \prod_{i=1}^k \prod_{j=1}^l {r_{ij}}^{\gamma_{ij}^{(n)}-1} \\
&= {n \choose {y_{11}, \ldots, y_{kl}}} \, \frac{\Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(0)} \right)}{\Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(n)} \right)} \, \frac{\prod_{i=1}^k \prod_{j=1}^l \Gamma\left(\gamma_{ij}^{(n)}\right)}{\prod_{i=1}^k \prod_{j=1}^l \Gamma\left(\gamma_{ij}^{(0)}\right)} \cdot \\
&\hphantom{=} \mathrm{Dir}\left(\mathrm{vec}(r); \mathrm{vec}\left(\gamma^{(n)}\right)\right) \; .
\end{split}
$$

With that, we can integrate out $r$:

$$ \label{eq:m1-p-y-m}
\begin{split}
   p(y|m_1)
&= \int p(y,r) \, \mathrm{d}r \\
&= {n \choose {y_{11}, \ldots, y_{kl}}} \, \frac{\Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(0)} \right)}{\Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(n)} \right)} \, \frac{\prod_{i=1}^k \prod_{j=1}^l \Gamma\left(\gamma_{ij}^{(n)}\right)}{\prod_{i=1}^k \prod_{j=1}^l \Gamma\left(\gamma_{ij}^{(0)}\right)} \cdot \\
&\hphantom{=} \int \mathrm{Dir}\left(\mathrm{vec}(r); \mathrm{vec}\left(\gamma^{(n)}\right)\right) \, \mathrm{d}r \\
&= {n \choose {y_{11}, \ldots, y_{kl}}} \, \frac{\Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(0)} \right)}{\Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(n)} \right)} \, \frac{\prod_{i=1}^k \prod_{j=1}^l \Gamma\left(\gamma_{ij}^{(n)}\right)}{\prod_{i=1}^k \prod_{j=1}^l \Gamma\left(\gamma_{ij}^{(0)}\right)} \\
&= \frac{n!}{\prod_{i=1}^k \prod_{j=1}^l y_{ij}!} \, \frac{\Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(0)} \right)}{\Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(n)} \right)} \, \frac{\prod_{i=1}^k \prod_{j=1}^l \Gamma\left(\gamma_{ij}^{(n)}\right)}{\prod_{i=1}^k \prod_{j=1}^l \Gamma\left(\gamma_{ij}^{(0)}\right)} \; .
\end{split}
$$

Finally, logarithmizing both sides and applying the relation $n! = \Gamma(n+1)$, we obtain:

$$ \label{eq:m1-lme-qed}
\begin{split}
   \log p(y|m_1)
&= \log \Gamma(n+1) - \sum_{i=1}^k \sum_{j=1}^l \log \Gamma(y_{ij}+1) \\
&+ \log \Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(0)} \right)
 - \log \Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(n)} \right) \\
&+ \sum_{i=1}^k \sum_{j=1}^l \log \Gamma\left( \gamma_{ij}^{(n)} \right)
 - \sum_{i=1}^k \sum_{j=1}^l \log \Gamma\left( \gamma_{ij}^{(0)} \right) \; .
\end{split}
$$

This completes the proof.