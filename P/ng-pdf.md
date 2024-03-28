---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-07 20:44:00

title: "Probability density function of the normal-gamma distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Normal-gamma distribution"
theorem: "Probability density function"

sources:
  - authors: "Koch KR"
    year: 2007
    title: "Normal-Gamma Distribution"
    in: "Introduction to Bayesian Statistics"
    pages: "ch. 2.5.3, pp. 55-56, eq. 2.212"
    url: "https://www.springer.com/gp/book/9783540727231"
    doi: "10.1007/978-3-540-72726-2"

proof_id: "P44"
shortcut: "ng-pdf"
username: "JoramSoch"
---


**Theorem:** Let $x$ and $y$ follow a [normal-gamma distribution](/D/ng):

$$ \label{eq:ng}
x,y \sim \mathrm{NG}(\mu, \Lambda, a, b) \; .
$$

Then, the [joint probability](/D/prob-joint) [density function](/D/pdf) of $x$ and $y$ is

$$ \label{eq:ng-pdf}
p(x,y) = \sqrt{\frac{|\Lambda|}{(2 \pi)^n}} \frac{b^a}{\Gamma(a)} \cdot y^{a+\frac{n}{2}-1} \exp \left[ -\frac{y}{2} \left( (x-\mu)^\mathrm{T} \Lambda (x-\mu) + 2b \right) \right] \; .
$$


**Proof:** The [normal-gamma distribution](/D/ng) is defined as $X$ conditional on $Y$ following a [multivariate distribution](/D/mvn) and $Y$ following a [gamma distribution](/D/gam):

$$ \label{eq:mvn-gam}
\begin{split}
X \vert Y &\sim \mathcal{N}(\mu, (Y \Lambda)^{-1}) \\
Y &\sim \mathrm{Gam}(a, b) \; .
\end{split}
$$

Thus, using the [probability density function of the multivariate normal distribution](/P/mvn-pdf) and the [probability density function of the gamma distribution](/P/gam-pdf), we have the following probabilities:

$$ \label{eq:mvn-gam-pdf}
\begin{split}
p(x \vert y) &= \mathcal{N}(x; \mu, (y \Lambda)^{-1}) \\
&= \sqrt{\frac{|y \Lambda|}{(2 \pi)^n}} \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} (y \Lambda) (x-\mu) \right] \\
p(y) &= \mathrm{Gam}(y; a, b) \\
&= \frac{b^a}{\Gamma(a)} y^{a-1} \exp\left[-by\right] \; .
\end{split}
$$

The [law of conditional probability](/D/prob-cond) implies that

$$ \label{eq:prob-cond}
p(x,y) = p(x \vert y) \, p(y) \; ,
$$

such that the normal-gamma density function becomes:

$$ \label{eq:ng-pdf-prod}
p(x,y) = \sqrt{\frac{|y \Lambda|}{(2 \pi)^n}} \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} (y \Lambda) (x-\mu) \right] \cdot \frac{b^a}{\Gamma(a)} y^{a-1} \exp\left[-by\right] \; .
$$

Using the relation $\lvert y A \rvert = y^n \lvert A \rvert$ for an $n \times n$ matrix $A$ and rearranging the terms, we have:

$$ \label{eq:ng-pdf-qed}
p(x,y) = \sqrt{\frac{|\Lambda|}{(2 \pi)^n}} \frac{b^a}{\Gamma(a)} \cdot y^{a+\frac{n}{2}-1} \exp \left[ -\frac{y}{2} \left( (x-\mu)^\mathrm{T} \Lambda (x-\mu) + 2b \right) \right] \; .
$$