---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-22 09:17:00

title: "Covariance and variance of the normal-gamma distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Normal-gamma distribution"
theorem: "Covariance"

sources:

proof_id: "P345"
shortcut: "ng-cov"
username: "JoramSoch"
---


**Theorem:** Let $x \in \mathbb{R}^n$ and $y > 0$ follow a [normal-gamma distribution](/D/ng):

$$ \label{eq:ng}
x,y \sim \mathrm{NG}(\mu, \Lambda, a, b) \; .
$$

Then,

1) the [covariance](/D/cov) of $x$, [conditional](/D/dist-cond) on $y$ is

$$ \label{eq:ng-cov-cond}
\mathrm{Cov}(x \vert y) = \frac{1}{y} \Lambda^{-1} \; ;
$$

2) the [covariance](/D/cov) of $x$, [unconditional](/D/dist-marg) on $y$ is

$$ \label{eq:ng-cov-x}
\mathrm{Cov}(x) = \frac{b}{a-1} \Lambda^{-1} \; ;
$$

3) the [variance](/D/var) of $y$ is

$$ \label{eq:ng-var-y}
\mathrm{Var}(y) = \frac{a}{b^2} \; .
$$


**Proof:** 

1) According to the [definition of the normal-gamma distribution](/D/ng), the distribution of $x$ given $y$ is a [multivariate normal distribution](/D/mvn):

$$ \label{eq:ng-mvn}
x \vert y \sim \mathcal{N}(\mu, (y \Lambda)^{-1}) \; .
$$

The [covariance of the multivariate normal distribution](/P/mvn-cov) is

$$ \label{eq:mvn-cov}
x \sim \mathcal{N}(\mu, \Sigma) \quad \Rightarrow \quad \mathrm{Cov}(x) = \Sigma \; ,
$$

such that we have:

$$ \label{eq:ng-cov-cond-qed}
\mathrm{Cov}(x \vert y) = (y \Lambda)^{-1} = \frac{1}{y} \Lambda^{-1} \; .
$$

2) The [marginal distribution of the normal-gamma distribution](/P/ng-marg) with respect to $x$ is a [multivariate t-distribution](/D/mvt):

$$ \label{eq:ng-marg-x}
x \sim t\left( \mu, \left(\frac{a}{b} \Lambda \right)^{-1}, 2a \right) \; .
$$

The [covariance of the multivariate t-distribution](/P/mvt-cov) is

$$ \label{eq:mvt-cov}
x \sim t(\mu, \Sigma, \nu) \quad \Rightarrow \quad \mathrm{Cov}(x) = \frac{\nu}{\nu-2} \Sigma \; ,
$$

such that we have:

$$ \label{eq:ng-cov-x-qed}
\mathrm{Cov}(x) = \frac{2a}{2a-2} \left(\frac{a}{b} \Lambda \right)^{-1} = \frac{a}{a-1} \, \frac{b}{a} \, \Lambda^{-1} = \frac{b}{a-1} \Lambda^{-1} \; .
$$

3) The [marginal distribution of the normal-gamma distribution](/P/ng-marg) with respect to $y$ is a [univariate gamma distribution](/D/gam):

$$ \label{eq:ng-marg-y}
y \sim \mathrm{Gam}(a, b) \; .
$$

The [variance of the gamma distribution](/P/gam-var) is

$$ \label{eq:gam-var}
x \sim \mathrm{Gam}(a, b) \quad \Rightarrow \quad \mathrm{Var}(x) = \frac{a}{b^2} \; ,
$$

such that we have:

$$ \label{eq:ng-var-y-qed}
\mathrm{Var}(y) = \frac{a}{b^2} \; .
$$