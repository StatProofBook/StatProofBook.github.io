---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-19 05:08:00

title: "Probability and log-odds in logistic regression"
chapter: "Statistical Models"
section: "Categorical data"
topic: "Logistic regression"
theorem: "Probability and log-odds"

sources:
  - authors: "Bishop, Christopher M."
    year: 2006
    title: "Linear Models for Classification"
    in: "Pattern Recognition for Machine Learning"
    pages: "ch. 4, p. 197, eq. 4.58"
    url: "http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf"

proof_id: "P105"
shortcut: "logreg-pnlo"
username: "JoramSoch"
---


**Theorem:** Assume a [logistic regression model](/D/logreg)

$$ \label{eq:logreg}
l_i = x_i \beta + \varepsilon_i, \; i = 1,\ldots,n
$$

where $x_i$ are the predictors corresponding to the $i$-th observation $y_i$ and $l_i$ are the log-odds that $y_i = 1$.

Then, the log-odds in favor of $y_i = 1$ against $y_i = 0$ can also be expressed as

$$ \label{eq:lodds}
l_i = \log_b \frac{p(x_i|y_i=1) \, p(y_i=1)}{p(x_i|y_i=0) \, p(y_i=0)}
$$

where $p(x_i \vert y_i)$ is a [likelihood function](/D/lf) consistent with \eqref{eq:logreg}, $p(y_i)$ are [prior probabilities](/D/prior) for $y_i = 1$ and $y_i = 0$ and where $b$ is the base used to form the log-odds $l_i$.


**Proof:** Using [Bayes' theorem](/P/bayes-th) and the [law of marginal probability](/D/prob-marg), the [posterior probabilities](/D/post) for $y_i = 1$ and $y_i = 0$ are given by

$$ \label{eq:prob}
\begin{split}
p(y_i=1|x_i) &= \frac{p(x_i|y_i=1) \, p(y_i=1)}{p(x_i|y_i=1) \, p(y_i=1) + p(x_i|y_i=0) \, p(y_i=0)} \\
p(y_i=0|x_i) &= \frac{p(x_i|y_i=0) \, p(y_i=0)}{p(x_i|y_i=1) \, p(y_i=1) + p(x_i|y_i=0) \, p(y_i=0)} \; .
\end{split}
$$

Calculating the log-odds from the posterior probabilties, we have

$$ \label{eq:lodds-qed}
\begin{split}
l_i &= \log_b \frac{p(y_i=1|x_i)}{p(y_i=0|x_i)} \\
&= \log_b \frac{p(x_i|y_i=1) \, p(y_i=1)}{p(x_i|y_i=0) \, p(y_i=0)} \; .
\end{split}
$$