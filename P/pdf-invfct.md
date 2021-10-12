---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-08-30 07:05:00

title: "Probability density function of an invertible function of a continuous random vector"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Probability density function of invertible function"

sources:
  - authors: "Taboga, Marco"
    year: 2017
    title: "Functions of random vectors and their distribution"
    in: "Lectures on probability and mathematical statistics"
    pages: "retrieved on 2021-08-30"
    url: "https://www.statlect.com/fundamentals-of-probability/functions-of-random-vectors"
  - authors: "Lebanon, Guy"
    year: 2017
    title: "Functions of a Random Vector"
    in: "Probability: The Analysis of Data, Vol. 1"
    pages: "retrieved on 2021-08-30"
    url: "http://theanalysisofdata.com/probability/4_4.html"
  - authors: "Poirier, Dale J."
    year: 1995
    title: "Distributions of Functions of Random Variables"
    in: "Intermediate Statistics and Econometrics: A Comparative Approach"
    pages: "ch. 4, pp. 149ff."
    url: "https://books.google.de/books?id=K52_YvD1YNwC&hl=de&source=gbs_navlinks_s"
  - authors: "Devore, Jay L.; Berk, Kennth N."
    year: 2011
    title: "Conditional Distributions"
    in: "Modern Mathematical Statistics with Applications"
    pages: "ch. 5.2, pp. 253ff."
    url: "https://books.google.de/books?id=5PRLUho-YYgC&hl=de&source=gbs_navlinks_s"
  - authors: "peek-a-boo"
    year: 2019
    title: "How to come up with the Jacobian in the change of variables formula"
    in: "StackExchange Mathematics"
    pages: "retrieved on 2021-08-30"
    url: "https://math.stackexchange.com/a/3239222"
  - authors: "Bazett, Trefor"
    year: 2019
    title: "Change of Variables & The Jacobian | Multi-variable Integration"
    in: "YouTube"
    pages: "retrieved on 2021-08-30"
    url: "https://www.youtube.com/watch?v=wUF-lyyWpUc"

proof_id: "P254"
shortcut: "pdf-invfct"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n \times 1$ [random vector](/D/rvec) of [continuous random variables](/D/rvar-disc) with possible outcomes $\mathcal{X} \subseteq \mathbb{R}^n$ and let $g: \; \mathbb{R}^n \rightarrow \mathbb{R}^n$ be an invertible and differentiable function on the support of $X$. Then, the [probability density function](/D/pdf) of $Y = g(X)$ is given by

$$ \label{eq:pdf-invfct}
f_Y(y) = \left\{
\begin{array}{rl}
f_X(g^{-1}(y)) \, \left| J_{g^{-1}}(y) \right| \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y \notin \mathcal{Y}
\end{array}
\right. \; ,
$$

if the Jacobian determinant satisfies

$$ \label{eq:jac-det}
\left| J_{g^{-1}}(y) \right| \neq 0 \quad \text{for all} \quad y \in \mathcal{Y}
$$

where $g^{-1}(y)$ is the inverse function of $g(x)$, $J_{g^{-1}}(y)$ is the Jacobian matrix of $g^{-1}(y)$

$$ \label{eq:jac}
J_{g^{-1}}(y) = \left[ \begin{matrix}
\frac{\mathrm{d}x_1}{\mathrm{d}y_1} & \ldots & \frac{\mathrm{d}x_1}{\mathrm{d}y_n} \\
\vdots & \ddots & \vdots \\
\frac{\mathrm{d}x_n}{\mathrm{d}y_1} & \ldots & \frac{\mathrm{d}x_n}{\mathrm{d}y_n}
\end{matrix} \right] \; ,
$$

$\lvert J \rvert$ is the determinant of $J$ and $\mathcal{Y}$ is the set of possible outcomes of $Y$:

$$ \label{eq:Y-range}
\mathcal{Y} = \left\lbrace y = g(x): x \in \mathcal{X} \right\rbrace \; .
$$


**Proof:**

1) First, we obtain the [cumulative distribution function](/D/cdf) of $Y = g(X)$. The [joint CDF](/D/cdf-joint) is given by

$$ \label{eq:Y-cdf-s1}
\begin{split}
F_Y(y) &= \mathrm{Pr}(Y_1 \leq y_1, \ldots, Y_n \leq y_n) \\
&= \mathrm{Pr}(g_1(X) \leq y_1, \ldots, g_n(X) \leq y_n) \\
&= \int_{A(y)} f_X(x) \, \mathrm{d}x
\end{split}
$$

where $A(y)$ is the following subset of the $n$-dimensional Euclidean space:

$$ \label{eq:A-y}
A(y) = \left\lbrace x \in \mathbb{R}^n: g_j(x) \leq y_j \; \text{for all} \; j = 1, \ldots, n \right\rbrace
$$

and $g_j(X)$ is the function which returns the $j$-th element of $Y$, given a vector $X$.

<br>
2) Next, we substitute $x = g^{-1}(y)$ into the integral which gives us

$$ \label{eq:Y-cdf-s2}
\begin{split}
F_Y(z) &= \int_{B(z)} f_X(g^{-1}(y)) \, \mathrm{d}g^{-1}(y) \\
&= \int_{-\infty}^{z_n} \ldots \int_{-\infty}^{z_1} f_X(g^{-1}(y)) \, \mathrm{d}g^{-1}(y) \; .
\end{split}
$$

where we have the modified the integration regime $B(z)$ which reads

$$ \label{eq:B-z}
B(z) = \left\lbrace y \in \mathbb{R}^n: y \leq z_j \; \text{for all} \; j = 1, \ldots, n \right\rbrace \; .
$$

<br>
3) The formula for change of variables in multivariable calculus states that

$$ \label{eq:cov-multi}
y = f(x) \quad \Rightarrow \quad \mathrm{d}y = \left| J_f(x) \right| \, \mathrm{d}x \; .
$$

Applied to equation \eqref{eq:Y-cdf-s2}, this yields

$$ \label{eq:Y-cdf-s3}
\begin{split}
F_Y(z) &= \int_{-\infty}^{z_n} \ldots \int_{-\infty}^{z_1} f_X(g^{-1}(y)) \, \left| J_{g^{-1}}(y) \right| \, \mathrm{d}y \\
&= \int_{-\infty}^{z_n} \ldots \int_{-\infty}^{z_1} f_X(g^{-1}(y)) \, \left| J_{g^{-1}}(y) \right| \, \mathrm{d}y_1 \ldots \mathrm{d}y_n \; .
\end{split}
$$

<br>
4) Finally, we obtain the [probability density function](/D/pdf) of $Y = g(X)$. Because [the PDF is the derivative of the CDF](/P/pdf-cdf), we can differentiate the joint CDF to get

$$ \label{eq:Y-cdf-s4}
\begin{split}
f_Y(z) &= \frac{\mathrm{d}^n}{\mathrm{d}z_1 \ldots \mathrm{d}z_n} \, F_Y(z) \\
&= \frac{\mathrm{d}^n}{\mathrm{d}z_1 \ldots \mathrm{d}z_n} \int_{-\infty}^{z_n} \ldots \int_{-\infty}^{z_1} f_X(g^{-1}(y)) \, \left| J_{g^{-1}}(y) \right| \, \mathrm{d}y_1 \ldots \mathrm{d}y_n \\
&= f_X(g^{-1}(z)) \, \left| J_{g^{-1}}(z) \right|
\end{split}
$$

which can also be written as

$$ \label{eq:pdf-invfct-qed}
f_Y(y) = f_X(g^{-1}(y)) \, \left| J_{g^{-1}}(y) \right| \; .
$$