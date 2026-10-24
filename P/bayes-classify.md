---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-17 20:30:00

title: "Bayes classification threshold under asymmetric error costs"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Bayesian inference"
theorem: "Bayes classification threshold"

sources:
  - authors: "George Casella, Roger L. Berger"
    year: 2002
    title: "Bayesian tests and loss function optimality"
    in: "Statistical Inference"
    pages: "Second edition, Sections 8.2.2 and 8.3.5, pp. 379-380 and 400-401"

proof_id: "P557"
shortcut: "bayes-classify"
username: "kjpetrykowski"
---


**Theorem:** Let $H \in \lbrace 0,1 \rbrace$ be a [binary state](/D/reve), and let $X$ be the [data](/D/data). Choose a version of the [posterior probability](/D/post) $q(x)=\mathrm{Pr}(H=1 \mid X=x)$ taking values in $[0,1]$. The rule below applies almost surely under the marginal law of $X$. The model does not uniquely determine posterior probabilities at impossible observations. An action $a \in \lbrace 0,1 \rbrace$ announces the chosen state. Let $c_{\mathrm{FP}}>0$ be the cost of choosing 1 when $H=0$, and let $c_{\mathrm{FN}}>0$ be the cost of choosing 0 when $H=1$. Correct decisions have zero cost, so

$$ \label{eq:bayes-classify-loss}
L(a,h)=
\begin{cases}
c_{\mathrm{FP}}, & a=1,\ h=0, \\
c_{\mathrm{FN}}, & a=0,\ h=1, \\
0,               & a=h \; .
\end{cases}
$$

A version is a chosen function representing the [conditional probability](/D/prob-cond). Different choices on a set of data values with [marginal probability](/D/prob-marg) zero do not change the averaged risk. The two costs must use the same units. The posterior expected loss is $\rho(a \mid x)=\mathrm{E}[L(a,H) \mid X=x]$. Its minimizing action satisfies

$$ \label{eq:bayes-classify-threshold}
a_{\mathrm{min}} = 
\begin{cases}
1,                   & q(x)>c_{\mathrm{FP}}/(c_{\mathrm{FP}}+c_{\mathrm{FN}}), \\
0,                   & q(x)<c_{\mathrm{FP}}/(c_{\mathrm{FP}}+c_{\mathrm{FN}}), \\
0 \; \text{or} \; 1, & q(x)=c_{\mathrm{FP}}/(c_{\mathrm{FP}}+c_{\mathrm{FN}}) \; .
\end{cases}
$$


**Proof:** For action 1, a loss occurs, only if $H=0$. For action 0, a loss occurs, only if $H=1$. Therefore:

$$ \label{eq:bayes-classify-risks}
\rho(1\mid x)=c_{\mathrm{FP}}[1-q(x)], \qquad
\rho(0\mid x)=c_{\mathrm{FN}}q(x) \; .
$$

Action 1 is strictly better, exactly when its expected loss is smaller:

$$ \label{eq:bayes-classify-compare}
\begin{split}
\rho(1\mid x)<\rho(0\mid x)
&\Leftrightarrow c_{\mathrm{FP}}[1-q(x)]<c_{\mathrm{FN}}q(x) \\
&\Leftrightarrow c_{\mathrm{FP}}<(c_{\mathrm{FP}}+c_{\mathrm{FN}})q(x) \\
&\Leftrightarrow q(x)>\frac{c_{\mathrm{FP}}}{c_{\mathrm{FP}}+c_{\mathrm{FN}}} \; .
\end{split}
$$

Division preserves the inequality, because both costs are positive. Reversing the strict inequality gives action 0. At equality, the risks are identical. A randomized choice with probability $r\in[0,1]$ of action 1 has posterior risk $r\rho(1 \mid x)+(1-r)\rho(0 \mid x)$, so randomization cannot improve the smaller risk and is also optimal at a tie. This proves the threshold rule.

The optimal decision depends on the relative costs of the two errors. A higher false-negative cost lowers the posterior-probability threshold for choosing state 1.