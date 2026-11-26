---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-17 20:30:00

title: "Decision threshold for Bayes classification under asymmetric error costs"
chapter: "General Theorems"
section: "Machine learning"
topic: "Bayes classification"
theorem: "Decision threshold under asymmetric error costs"

sources:
  - authors: "George Casella, Roger L. Berger"
    year: 2002
    title: "Bayesian tests and loss function optimality"
    in: "Statistical Inference"
    pages: "Second edition, Sections 8.2.2 and 8.3.5, pp. 379-380 and 400-401"

proof_id: "P557"
shortcut: "bc-thr"
username: "kjpetrykowski"
---

**Theorem:** Let $H\in\lbrace0,1\rbrace$ be an unknown state. Let $X$ denote the data and $x$ their observed value. Suppose the model gives a [posterior probability](/D/post) for state 1 after observing $x$. Write this probability as

$$ \label{eq:posterior}
q=\mathrm{Pr}(H=1\mid X=x) \; .
$$

Choose an action $a\in\lbrace0,1\rbrace$ as the predicted state. Let $c\_{\mathrm{FP}}>0$ be the cost of a false positive, predicting 1 when $H=0$, and $c\_{\mathrm{FN}}>0$ the cost of a false negative, predicting 0 when $H=1$. The costs are measured in the same units. Write $h$ for the true value of $H$. With zero cost for a correct decision, the [loss](/D/loss-fct) for predicting $a$ when the state is $h$ is

$$ \label{eq:loss}
L(a,h)=
\begin{cases}
c_{\mathrm{FP}},&a=1,\ h=0,\\
c_{\mathrm{FN}},&a=0,\ h=1,\\
0,&a=h \; .
\end{cases}
$$

For each action $a$, average its cost over the two possible states using their posterior probabilities. Denote this [posterior expected loss](/D/post-loss) by $\rho(a\mid x)$. An action with the smallest average cost satisfies

$$ \label{eq:threshold}
a_{\mathrm{min}}=
\begin{cases}
1,&q>c_{\mathrm{FP}}/(c_{\mathrm{FP}}+c_{\mathrm{FN}}),\\
0,&q<c_{\mathrm{FP}}/(c_{\mathrm{FP}}+c_{\mathrm{FN}}),\\
0\text{ or }1,&q=c_{\mathrm{FP}}/(c_{\mathrm{FP}}+c_{\mathrm{FN}}) \; .
\end{cases}
$$


**Proof:** The two posterior state probabilities are $q$ and $1-q$. Average each action's loss over these two states:

$$ \label{eq:risks}
\begin{split}
\rho(1\mid x)
&=c_{\mathrm{FP}}(1-q)+0\cdot q
=c_{\mathrm{FP}}(1-q),\\
\rho(0\mid x)
&=0\cdot(1-q)+c_{\mathrm{FN}}q
=c_{\mathrm{FN}}q \; .
\end{split}
$$

Action 1 has the smaller expected loss precisely when

$$ \label{eq:compare}
\begin{split}
\rho(1\mid x)<\rho(0\mid x)
&\Leftrightarrow c_{\mathrm{FP}}(1-q)<c_{\mathrm{FN}}q\\
&\Leftrightarrow c_{\mathrm{FP}}<(c_{\mathrm{FP}}+c_{\mathrm{FN}})q\\
&\Leftrightarrow q>\frac{c_{\mathrm{FP}}}{c_{\mathrm{FP}}+c_{\mathrm{FN}}} \; .
\end{split}
$$

The last step divides by the positive number $c\_{\mathrm{FP}}+c\_{\mathrm{FN}}$. Reversing the inequalities gives the condition for action 0. At equality, the two actions have the same expected loss.

Choosing at random between the two actions gives a weighted average of their posterior expected losses. This average is at least as large as the smaller of the two losses. If action 1 is chosen with probability $r\in[0,1]$, independently of the unknown state after observing $x$, its posterior expected loss is

$$ \label{eq:randomized-loss}
r\rho(1\mid x)+(1-r)\rho(0\mid x)
\geq\min\lbrace\rho(1\mid x),\rho(0\mid x)\rbrace \; .
$$

At a tie every such randomization is also optimal. Thus \eqref{eq:threshold} gives the required rule. A larger false-negative cost lowers the threshold for choosing state 1.
