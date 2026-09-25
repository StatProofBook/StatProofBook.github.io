---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-09-18 11:57:19

title: "Log Bayes factor for general contigency table models"
chapter: "Statistical Models"
section: "Count data"
topic: "General contingency table"
theorem: "Log Bayes factor"

sources:

proof_id: "P554"
shortcut: "ct-lbf"
username: "JoramSoch"
---


**Theorem:** Consider a [$k \times l$ contingency table](/D/ct), denote observed counts as

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

Then, the [log Bayes factor](/D/lme) in favor of $m_1$ against $m_0$ is

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

where $\Gamma(x)$ is the gamma function; $\alpha_n$ and $\beta_n$ are the [posterior hyperparameters of $m_0$](/P/ct-lme); and $\gamma_{ij}^{(n)}$ are the [posterior hyperparameters of $m_1$](/P/ct-lme).


**Proof:** [The log Bayes factor is equal to the difference of two log model evidences](/P/lbf-lme):

$$ \label{eq:lbf-lme}
\mathrm{LBF}_{12} = \mathrm{LME}(m_1) - \mathrm{LME}(m_2) \; .
$$

The [log model evidence of $m_0$](/P/ct-lme) is

$$ \label{eq:m0-lme}
\begin{split}
   \mathrm{LME}(m_0)
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

and the [log model evidence of $m_1$](/P/ct-lme) is

$$ \label{eq:m1-lme}
\begin{split}
   \mathrm{LME}(m_1)
&= \log \Gamma(n+1) - \sum_{i=1}^k \sum_{j=1}^l \log \Gamma(y_{ij}+1) \\
&+ \log \Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(0)} \right)
 - \log \Gamma\left( \sum_{i=1}^k \sum_{j=1}^l \gamma_{ij}^{(n)} \right) \\
&+ \sum_{i=1}^k \sum_{j=1}^l \log \Gamma\left( \gamma_{ij}^{(n)} \right)
 - \sum_{i=1}^k \sum_{j=1}^l \log \Gamma\left( \gamma_{ij}^{(0)} \right) \; .
\end{split}
$$

Subtracting the two LMEs from each other, the LBF emerges as

$$ \label{eq:ct-lbf-qed}
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