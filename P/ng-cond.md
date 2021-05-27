---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-05 06:54:00

title: "Conditional distributions of the normal-gamma distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Normal-gamma distribution"
theorem: "Conditional distributions"

sources:

proof_id: "P146"
shortcut: "ng-cond"
username: "JoramSoch"
---


**Theorem:** Let $x$ and $y$ follow a [normal-gamma distribution](/D/ng):

$$ \label{eq:ng}
x,y \sim \mathrm{NG}(\mu, \Lambda, a, b) \; .
$$

Then,

1) the [conditional distribution](/D/dist-cond) of $x$ given $y$ is a [multivariate normal distribution](/D/mvn)

$$ \label{eq:ng-cond-x-y}
x|y \sim \mathcal{N}(\mu, (y \Lambda)^{-1}) \; ;
$$

2) the [conditional distribution](/D/dist-cond) of a subset vector $x_1$, given the complement vector $x_2$ and $y$, is also a [multivariate normal distribution](/D/mvn)

$$ \label{eq:ng-cond-x1-x2-y}
x_1|x_2,y \sim \mathcal{N}(\mu_{1|2}(y), \Sigma_{1|2}(y))
$$

with the conditional [mean](/D/mean) and [covariance](/D/cov)

$$ \label{eq:ng-cond-x1-x2-y-hyp}
\begin{split}
\mu_{1|2}(y) &= \mu_1 + \Sigma_{12} \Sigma_{22}^{-1} (x_2 - \mu_2) \\
\Sigma_{1|2}(y) &= \Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{12}
\end{split}
$$

where $\mu_1$, $\mu_2$ and $\Sigma_{11}$, $\Sigma_{12}$, $\Sigma_{22}$, $\Sigma_{21}$ are [block-wise components](/P/mvn-cond) of $\mu$ and $\Sigma(y) = (y \Lambda)^{-1}$;

3) the [conditional distribution](/D/dist-cond) of $y$ given $x$ is a [gamma distribution](/D/gam)

$$ \label{eq:ng-cond-y-x}
y|x \sim \mathrm{Gam}\left( a + \frac{n}{2}, b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right)
$$

where $n$ is the dimensionality of $x$.


**Proof:**

1) This follows from the [definition of the normal-gamma distribution](/D/ng):

$$ \label{eq:ng-pdf}
\begin{split}
p(x,y) &= p(x|y) \cdot p(y) \\
&= \mathcal{N}(x; \mu, (y \Lambda)^{-1}) \cdot \mathrm{Gam}(y; a, b) \; .
\end{split}
$$

2) This follows from \eqref{eq:ng-cond-x-y} and the [conditional distributions of the multivariate normal distribution](/P/mvn-cond):

$$ \label{eq:mvn-cond}
\begin{split}
x &\sim \mathcal{N}(\mu, \Sigma) \\
\Rightarrow x_1|x_2 &\sim \mathcal{N}(\mu_{1|2}, \Sigma_{1|2}) \\
\mu_{1|2} &= \mu_1 + \Sigma_{12} \Sigma_{22}^{-1} (x_2 - \mu_2) \\
\Sigma_{1|2} &= \Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} \; .
\end{split}
$$

3) The conditional density of $y$ given $x$ follows from [Bayes' theorem](/P/bayes-th) as

$$ \label{eq:ng-cond-y-x-s1}
p(y|x) = \frac{p(x|y) \cdot p(y)}{p(x)} \; .
$$

The [conditional distribution](/D/dist-cond) of $x$ given $y$ [is a multivariate normal distribution](/P/ng-pdf)

$$ \label{eq:ng-x-y-pdf}
p(x|y) = \mathcal{N}(x; \mu, (y \Lambda)^{-1}) = \sqrt{\frac{|y \Lambda|}{(2 \pi)^n}} \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} (y \Lambda) (x-\mu) \right] \; ,
$$

the [marginal distribution](/D/dist-marg) of $y$ [is a gamma distribution](/P/ng-marg)

$$ \label{eq:ng-y-pdf}
p(y) = \mathrm{Gam}(y; a, b) = \frac{b^a}{\Gamma(a)} y^{a-1} \exp\left[ -by \right]
$$

and the [marginal distribution](/D/dist-marg) of $x$ [is a multivariate t-distribution](/P/ng-marg)

$$ \label{eq:ng-x-pdf}
\begin{split}
p(x) &= t\left( x; \mu, \left(\frac{a}{b} \Lambda \right)^{-1}, 2a \right) \\
&= \sqrt{\frac{\left| \frac{a}{b}\,\Lambda \right|}{(2a\,\pi)^n}} \cdot \frac{\Gamma\left( \frac{2a+n}{2} \right)}{\Gamma\left( \frac{2a}{2} \right)} \cdot \left( 1 + \frac{1}{2a} (x-\mu)^\mathrm{T} \left( \frac{a}{b}\Lambda \right) (x-\mu) \right)^{-\frac{2a+n}{2}} \\
&= \sqrt{\frac{|\Lambda|}{(2 \pi)^n}} \cdot \frac{\Gamma\left( a+\frac{n}{2} \right)}{\Gamma(a)} \cdot b^a \cdot \left( b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right)^{-\left( a+\frac{n}{2} \right)} \; .
\end{split}
$$

Plugging \eqref{eq:ng-x-y-pdf}, \eqref{eq:ng-y-pdf} and \eqref{eq:ng-x-pdf} into \eqref{eq:ng-cond-y-x-s1}, we obtain

$$ \label{eq:ng-cond-y-x-s2}
\begin{split}
p(y|x) &= \frac{\sqrt{\frac{|y \Lambda|}{(2 \pi)^n}} \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} (y \Lambda) (x-\mu) \right] \cdot \frac{b^a}{\Gamma(a)} y^{a-1} \exp\left[ -by \right]}{\sqrt{\frac{|\Lambda|}{(2 \pi)^n}} \cdot \frac{\Gamma\left( a+\frac{n}{2} \right)}{\Gamma(a)} \cdot b^a \cdot \left( b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right)^{-\left( a+\frac{n}{2} \right)}} \\
&= y^{\frac{n}{2}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} (y \Lambda) (x-\mu) \right] \cdot y^{a-1} \cdot \exp\left[ -by \right] \cdot \frac{1}{\Gamma\left( a+\frac{n}{2} \right)} \cdot \left( b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right)^{a+\frac{n}{2}} \\
&= \frac{\left( b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right)^{a+\frac{n}{2}}}{\Gamma\left( a+\frac{n}{2} \right)} \cdot y^{a+\frac{n}{2}-1} \cdot \exp \left[ -\left( b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right) \right]
\end{split}
$$

which is the [probability density function of a gamma distribution](/P/gam-pdf) with shape and rate parameters

$$ \label{eq:ng-cond-y-x-hyp}
a + \frac{n}{2} \quad \text{and} \quad b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \; ,
$$

such that

$$ \label{eq:ng-cond-y-x-qed}
p(y|x) = \mathrm{Gam}\left( y; a + \frac{n}{2}, b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right) \; .
$$