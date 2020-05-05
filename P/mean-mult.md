---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-17 21:51:00

title: "(Non-)Multiplicativity of the expected value"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "(Non-)Multiplicativity"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Expected value"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-17"
    url: "https://en.wikipedia.org/wiki/Expected_value#Basic_properties"

proof_id: "P55"
shortcut: "mean-mult"
username: "JoramSoch"
---


**Theorem:**

1) If two [random variables](/D/rvar) $X$ and $Y$ are [independent](/D/ind), the [expected value](/D/mean) is multiplicative, i.e.

$$ \label{eq:mean-mult}
\mathrm{E}(X\,Y) = \mathrm{E}(X) \, \mathrm{E}(Y) \; .
$$

2) If two [random variables](/D/rvar) $X$ and $Y$ are [dependent](/D/ind), the [expected value](/D/mean) is not necessarily multiplicative, i.e. there exist $X$ and $Y$ such that

$$ \label{eq:mean-nonmult}
\mathrm{E}(X\,Y) \neq \mathrm{E}(X) \, \mathrm{E}(Y) \; .
$$


**Proof:**

1) If $X$ and $Y$ are [independent](/D/ind), it holds that

$$ \label{eq:ind}
p(x,y) = p(x) \, p(y) \quad \text{for all} \quad x \in \mathcal{X}, y \in \mathcal{Y} \; .
$$

Applying this to the [expected value for discrete random variables](/D/mean), we have

$$ \label{eq:mean-mult-disc}
\begin{split}
\mathrm{E}(X\,Y) &= \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} (x \cdot y) \cdot f_{X,Y}(x,y) \\
&\overset{\eqref{eq:ind}}{=} \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} (x \cdot y) \cdot \left( f_X(x) \cdot f_Y(y) \right) \\
&= \sum_{x \in \mathcal{X}} x \cdot f_X(x) \, \sum_{y \in \mathcal{Y}} y \cdot f_Y(y) \\
&= \sum_{x \in \mathcal{X}} x \cdot f_X(x) \cdot \mathrm{E}(Y) \\
&= \mathrm{E}(X) \, \mathrm{E}(Y) \; . \\
\end{split}
$$

And applying it to the [expected value for continuous random variables](/D/mean), we have

$$ \label{eq:mean-mult-cont}
\begin{split}
\mathrm{E}(X\,Y) &= \int_{\mathcal{X}} \int_{\mathcal{Y}} (x \cdot y) \cdot f_{X,Y}(x,y) \, \mathrm{d}y \, \mathrm{d}x \\
&\overset{\eqref{eq:ind}}{=} \int_{\mathcal{X}} \int_{\mathcal{Y}} (x \cdot y) \cdot \left( f_X(x) \cdot f_Y(y) \right) \, \mathrm{d}y \, \mathrm{d}x \\
&= \int_{\mathcal{X}} x \cdot f_X(x) \, \int_{\mathcal{Y}} y \cdot f_Y(y)  \, \mathrm{d}y \, \mathrm{d}x \\
&= \int_{\mathcal{X}} x \cdot f_X(x) \cdot \mathrm{E}(Y) \, \mathrm{d}x \\
&= \mathrm{E}(X) \, \mathrm{E}(Y) \; . \\
\end{split}
$$

<br>
2) Let $X$ and $Y$ be [Bernoulli random variables](/D/bern) with the following [joint probability](/D/prob-joint) [mass function](/D/pmf)

$$ \label{eq:joint}
\begin{split}
p(X=0, Y=0) &= 1/2 \\
p(X=0, Y=1) &= 0 \\
p(X=1, Y=0) &= 0 \\
p(X=1, Y=1) &= 1/2
\end{split}
$$

and thus, the following marginal probabilities:

$$ \label{eq:marg}
\begin{split}
p(X=0) = p(X=1) &= 1/2 \\
p(Y=0) = p(Y=1) &= 1/2 \; .
\end{split}
$$

Then, $X$ and $Y$ are dependent, because

$$ \label{eq:dep}
p(X=0, Y=1) \overset{\eqref{eq:joint}}{=} 0 \neq \frac{1}{2} \cdot \frac{1}{2} \overset{\eqref{eq:marg}}{=} p(X=0) \, p(Y=1) \; ,
$$

and the expected value of their product is

$$ \label{eq:mean-prod}
\begin{split}
\mathrm{E}(X\,Y) &= \sum_{x \in \left\lbrace 0,1 \right\rbrace} \sum_{y \in \left\lbrace 0,1 \right\rbrace} (x \cdot y) \cdot p(x,y) \\
&= (1 \cdot 1) \cdot p(X=1, Y=1) \\
&\overset{\eqref{eq:joint}}{=} \frac{1}{2}
\end{split}
$$

while the product of their expected values is

$$ \label{eq:prod-mean}
\begin{split}
\mathrm{E}(X) \, \mathrm{E}(Y) &= \left( \sum_{x \in \left\lbrace 0,1 \right\rbrace} x \cdot p(x) \right) \cdot \left( \sum_{y \in \left\lbrace 0,1 \right\rbrace} y \cdot p(y) \right) \\
&= \left( 1 \cdot p(X=1) \right) \cdot \left( 1 \cdot p(Y=1) \right) \\
&\overset{\eqref{eq:marg}}{=} \frac{1}{4}
\end{split}
$$

and thus,

$$ \label{eq:mean-nonmult-qed}
\mathrm{E}(X\,Y) \neq \mathrm{E}(X) \, \mathrm{E}(Y) \; .
$$