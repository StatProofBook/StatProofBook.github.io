---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-29 07:51:00

title: "Method-of-moments estimation"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Likelihood theory"
definition: "Method of moments"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Method of moments (statistics)"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-04-29"
    url: "https://en.wikipedia.org/wiki/Method_of_moments_(statistics)#Method"

def_id: "D151"
shortcut: "mome"
username: "JoramSoch"
---


**Definition:** Let measured data $y$ follow a [probability distribution](/D/dist) with [probability mass](/D/pmf) or [probability density](/D/pdf) $p(y \vert \theta)$ governed by unknown parameters $\theta_1, \ldots, \theta_k$. Then, method-of-moments estimation, also referred to as "method of moments" or "matching the moments", consists in

<br>
1) expressing the first $k$ [moments](/D/mom) of $y$ in terms of $\theta$

$$ \label{eq:mom}
\begin{split}
\mu_1 &= f_1(\theta_1, \ldots, \theta_k) \\
&\vdots \\
\mu_k &= f_k(\theta_1, \ldots, \theta_k) \; ,
\end{split}
$$

<br>
2) calculating the first $k$ sample [moments](/D/mom) from $y$

$$ \label{eq:mom-samp}
\hat{\mu}_1(y), \ldots, \hat{\mu}_k(y)
$$

<br>
3) and solving the system of $k$ equations

$$ \label{eq:mome}
\begin{split}
\hat{\mu}_1(y) &= f_1(\hat{\theta}_1, \ldots, \hat{\theta}_k) \\
&\vdots \\
\hat{\mu}_k(y) &= f_k(\hat{\theta}_1, \ldots, \hat{\theta}_k)
\end{split}
$$

for $\hat{\theta}_1, \ldots, \hat{\theta}_k$, which are subsequently refered to as "method-of-moments estimates".