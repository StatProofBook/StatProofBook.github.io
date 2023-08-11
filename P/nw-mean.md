---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-07-14 07:17:00

title: "Mean of the normal-Wishart distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Normal-Wishart distribution"
theorem: "Mean"

sources:

proof_id: "P327"
shortcut: "nw-mean"
username: "JoramSoch"
---


**Theorem:** Let $X \in \mathbb{R}^{n \times p}$ and $Y \in \mathbb{R}^{p \times p}$ follow a [normal-Wishart distribution](/D/nw):

$$ \label{eq:nw}
X,Y \sim \mathrm{NW}(M, U, V, \nu) \; .
$$

Then, the [expected value](/D/mean) of $X$ and $Y$ is

$$ \label{eq:nw-mean}
\mathrm{E}[(X,Y)] = \left( M, \nu V \right) \; .
$$


**Proof:** Consider the [random matrix](/D/rmat)

$$ \label{eq:rmat}
\left[ \begin{array}{c} X \\ Y \end{array} \right] = \left[ \begin{array}{ccc} x_{11} & \ldots & x_{1p} \\ \vdots & \ddots & \vdots \\ x_{n1} & \ldots & x_{np} \\ y_{11} & \ldots & y_{1p} \\ \vdots & \ddots & \vdots \\ y_{p1} & \ldots & y_{pp} \end{array} \right] \; .
$$

According to the [expected value of a random matrix](/D/mean-rmat), its expected value is

$$ \label{eq:mean-rmat}
\mathrm{E}\left( \left[ \begin{array}{c} X \\ Y \end{array} \right] \right) = \left[ \begin{array}{ccc} \mathrm{E}(x_{11}) & \ldots & \mathrm{E}(x_{1p}) \\ \vdots & \ddots & \vdots \\ \mathrm{E}(x_{n1}) & \ldots & \mathrm{E}(x_{np}) \\ \mathrm{E}(y_{11}) & \ldots & \mathrm{E}(y_{1p}) \\ \vdots & \ddots & \vdots \\ \mathrm{E}(y_{p1}) & \ldots & \mathrm{E}(y_{pp}) \end{array} \right] = \left[ \begin{array}{c} \mathrm{E}(X) \\ \mathrm{E}(Y) \end{array} \right] \; .
$$

When $X$ and $Y$ are [jointly normal-Wishart distributed, then](/D/nw) by definition $X$ follows a [matrix-normal distribution](/D/matn) conditional on $Y$ and $Y$ follows a [Wishart distribution](/D/wish):

$$ \label{eq:nw-def}
X,Y \sim \mathrm{NW}(M, U, V, \nu) \quad \Leftrightarrow \quad X \vert Y \sim \mathcal{MN}(M, U, Y^{-1}) \quad \wedge \quad Y \sim \mathcal{W}(V, \nu) \; .
$$

Thus, with the [expected value of the matrix-variate normal distribution](/P/matn-mean) and the [law of conditional probability](/D/prob-cond), $\mathrm{E}(X)$ becomes

$$ \label{eq:mean-X}
\begin{split}
\mathrm{E}(X) &= \iint X \cdot p(X,Y) \, \mathrm{d}X \, \mathrm{d}Y \\
&= \iint X \cdot p(X|Y) \cdot p(Y) \, \mathrm{d}X \, \mathrm{d}Y \\
&= \int p(Y) \int X \cdot p(X|Y) \, \mathrm{d}X \, \mathrm{d}Y \\
&= \int p(Y) \left\langle X \right\rangle_{\mathcal{MN}(M, U, Y^{-1})} \, \mathrm{d}Y \\
&= \int p(Y) \cdot M \, \mathrm{d}Y \\
&= M \int p(Y) \, \mathrm{d}Y \\
&= M \; ,
\end{split}
$$

and with the [expected value of the Wishart distribution](/P/wish-mean), $\mathrm{E}(Y)$ becomes

$$ \label{eq:mean-Y}
\begin{split}
\mathrm{E}(Y) &= \int Y \cdot p(Y) \, \mathrm{d}Y \\
&= \left\langle Y \right\rangle_{\mathcal{W}(V,\nu)} \\
&= \nu V \; .
\end{split}
$$

Thus, the expectation of the random matrix in equations \eqref{eq:rmat} and \eqref{eq:mean-rmat} is

$$ \label{eq:nw-mean-qed}
\mathrm{E}\left( \left[ \begin{array}{c} X \\ Y \end{array} \right] \right) = \left[ \begin{array}{c} M \\ \nu V \end{array} \right] \; ,
$$

as indicated by equation \eqref{eq:nw-mean}.