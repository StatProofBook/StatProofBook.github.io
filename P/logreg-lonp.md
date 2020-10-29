---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-03 12:01:00

title: "Log-odds and probability in logistic regression"
chapter: "Statistical Models"
section: "Categorical data"
topic: "Logistic regression"
theorem: "Log-odds and probability"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Logistic regression"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-03"
    url: "https://en.wikipedia.org/wiki/Logistic_regression#Logistic_model"

proof_id: "P72"
shortcut: "logreg-lonp"
username: "JoramSoch"
---


**Theorem:** Assume a [logistic regression model](/D/logreg)

$$ \label{eq:logreg}
l_i = x_i \beta + \varepsilon_i, \; i = 1,\ldots,n
$$

where $x_i$ are the predictors corresponding to the $i$-th observation $y_i$ and $l_i$ are the log-odds that $y_i = 1$.

Then, the probability that $y_i = 1$ is given by

$$ \label{eq:prob}
\mathrm{Pr}(y_i = 1) = \frac{1}{1 + b^{-(x_i \beta + \varepsilon_i)}}
$$

where $b$ is the base used to form the log-odds $l_i$.


**Proof:** Let us denote $\mathrm{Pr}(y_i = 1)$ as $p_i$. Then, the log-odds are

$$ \label{eq:lodds}
l_i = \log_b \frac{p_i}{1-p_i}
$$

and using \eqref{eq:logreg}, we have

$$ \label{eq:prob-qed}
\begin{split}
\log_b \frac{p_i}{1-p_i} &= x_i \beta + \varepsilon_i \\
\frac{p_i}{1-p_i} &= b^{x_i \beta + \varepsilon_i} \\
p_i &= \left( b^{x_i \beta + \varepsilon_i} \right) (1-p_i) \\
p_i \left( 1 + b^{x_i \beta + \varepsilon_i} \right) &= b^{x_i \beta + \varepsilon_i} \\
p_i &= \frac{b^{x_i \beta + \varepsilon_i}}{1 + b^{x_i \beta + \varepsilon_i}} \\
p_i &= \frac{b^{x_i \beta + \varepsilon_i}}{b^{x_i \beta + \varepsilon_i} \left( 1 + b^{-(x_i \beta + \varepsilon_i)} \right)} \\
p_i &= \frac{1}{1 + b^{-(x_i \beta + \varepsilon_i)}}
\end{split}
$$

which proves the identity given by \eqref{eq:prob}.