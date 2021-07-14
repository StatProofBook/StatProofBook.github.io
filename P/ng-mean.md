---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-08 09:40:00

title: "Mean of the normal-gamma distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Normal-gamma distribution"
theorem: "Mean"

sources:

proof_id: "P237"
shortcut: "ng-mean"
username: "JoramSoch"
---


**Theorem:** Let $x \in \mathbb{R}^n$ and $y > 0$ follow a [normal-gamma distribution](/D/ng):

$$ \label{eq:ng}
x,y \sim \mathrm{NG}(\mu, \Lambda, a, b) \; .
$$

Then, the [expected value](/D/mean) of $x$ and $y$ is

$$ \label{eq:ng-mean}
\mathrm{E}[(x,y)] = \left[ \left( \mu, \frac{a}{b} \right) \right] \; .
$$


**Proof:** Consider the [random vector](/D/rvec)

$$ \label{eq:rvec}
\left[ \begin{array}{c} x \\ y \end{array} \right] = \left[ \begin{array}{c} x_1 \\ \vdots \\ x_n \\ y \end{array} \right] \; .
$$

According to the [expected value of a random vector](/D/mean-rvec), its expected value is

$$ \label{eq:mean-rvec}
\mathrm{E}\left( \left[ \begin{array}{c} x \\ y \end{array} \right] \right) = \left[ \begin{array}{c} \mathrm{E}(x_1) \\ \vdots \\ \mathrm{E}(x_n) \\ \mathrm{E}(y) \end{array} \right] = \left[ \begin{array}{c} \mathrm{E}(x) \\ \mathrm{E}(y) \end{array} \right] \; .
$$

When $x$ and $y$ are [jointly normal-gamma distributed, then](/D/ng) by definition $x$ follows a [multivariate normal distribution](/D/mvn) conditional on $y$ and $y$ follows a [univariate gamma distribution](/D/gam):

$$ \label{eq:ng-def}
x,y \sim \mathrm{NG}(\mu, \Lambda, a, b) \quad \Leftrightarrow \quad x \vert y \sim \mathcal{N}(\mu, (y \Lambda)^{-1}) \quad \wedge \quad y \sim \mathrm{Gam}(a,b) \; .
$$

Thus, with the [expected value of the multivariate normal distribution](/P/mvn-mean) and the [law of conditional probability](/D/prob-cond), $\mathrm{E}(x)$ becomes

$$ \label{eq:mean-x}
\begin{split}
\mathrm{E}(x) &= \iint x \cdot p(x,y) \, \mathrm{d}x \, \mathrm{d}y \\
&= \iint x \cdot p(x|y) \cdot p(y) \, \mathrm{d}x \, \mathrm{d}y \\
&= \int p(y) \int x \cdot p(x|y) \, \mathrm{d}x \, \mathrm{d}y \\
&= \int p(y) \left\langle x \right\rangle_{\mathcal{N}(\mu, (y \Lambda)^{-1})} \, \mathrm{d}y \\
&= \int p(y) \cdot \mu \, \mathrm{d}y \\
&= \mu \int p(y) \, \mathrm{d}y \\
&= \mu \; ,
\end{split}
$$

and with the [expected value of the gamma distribution](/P/gam-mean), $\mathrm{E}(y)$ becomes

$$ \label{eq:mean-y}
\begin{split}
\mathrm{E}(y) &= \int y \cdot p(y) \, \mathrm{d}y \\
&= \left\langle y \right\rangle_{\mathrm{Gam}(a,b)} \\
&= \frac{a}{b} \; .
\end{split}
$$

Thus, the expectation of the random vector in equations \eqref{eq:rvec} and \eqref{eq:mean-rvec} is

$$ \label{eq:ng-mean-qed}
\mathrm{E}\left( \left[ \begin{array}{c} x \\ y \end{array} \right] \right) = \left[ \begin{array}{c} \mu \\ a/b \end{array} \right] \; ,
$$

as indicated by equation \eqref{eq:ng-mean}.