---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-12-23 21:41:54

title: "Multinomial test"
chapter: "Statistical Models"
section: "Count data"
topic: "Multinomial observations"
theorem: "Multinomial test"

sources:
  - authors: "Wikipedia"
    year: 2023
    title: "Multinomial test"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2023-12-23"
    url: "https://en.wikipedia.org/wiki/Multinomial_test"

proof_id: "P430"
shortcut: "mult-test"
username: "JoramSoch"
---


**Theorem:** Let $y = [y_1, \ldots, y_k]$ be the number of observations in $k$ categories resulting from $n$ independent trials with unknown category probabilities $p = [p_1, \ldots, p_k]$, such that $y$ follows a [multinomial distribution](/D/mult):

$$ \label{eq:Mult}
y \sim \mathrm{Mult}(n,p) \; .
$$

Then, the [null hypothesis](/D/h0)

$$ \label{eq:mult-test-h0}
H_0: \; p = p_0 = [p_{01}, \ldots, p_{0k}]
$$

is [rejected](/D/test) at [significance level](/D/alpha) $\alpha$, if

$$ \label{eq:mult-test-rej}
\mathrm{Pr}_\mathrm{sig} = \sum_{x: \; \mathrm{Pr}_0(x) \leq \mathrm{Pr}_0(y)} \mathrm{Pr}_0(x) < \alpha
$$

where $\mathrm{Pr}_0(x)$ is the probability of observing the numbers of occurences $x = [x_1, \ldots, x_k]$ under the null hypothesis:

$$ \label{eq:mult-test-prob}
\mathrm{Pr}_0(x) = n! \prod_{j=1}^k \frac{p_{0j}^{x_j}}{x_j!} \; .
$$


**Proof:** The [alternative hypothesis](/D/h1) relative to $H_0$ is

$$ \label{eq:bin-test-h1}
H_1: \; p_j \neq p_{0j} \quad \text{for at least one} \quad j = 1, \ldots, k \; .
$$

We can use $y$ as a [test statistic](/D/tstat). Its [sampling distribution](/D/dist-samp) is given by \eqref{eq:Mult}. The [probability mass function](/D/pmf) (PMF) of the test statistic under the null hypothesis is thus equal to the [probability mass function of the multionomial distribution](/P/mult-pmf) with [category probabilities](/D/mult) $p_0$:

$$ \label{eq:y-pmf}
\mathrm{Pr}(y = x \vert H_0) = \mathrm{Mult}(x; n, p_0) = {n \choose {x_1, \ldots, x_k}} \, \prod_{j=1}^k {p_j}^{x_j} \; .
$$

The multinomial coefficient in this equation is equal to

$$ \label{eq:mult-coeff}
{n \choose {k_1, \ldots, k_m}} = \frac{n!}{k_1! \cdot \ldots \cdot k_m!} \; ,
$$

such that the probability of observing the counts $y$, given $H_0$, is

$$ \label{eq:Pr0-y}
\mathrm{Pr}(y \vert H_0) = n! \prod_{j=1}^k \frac{p_{0i}^{y_j}}{y_j!} \; .
$$

The probability of observing any other set of counts $x$, given $H_0$, is

$$ \label{eq:Pr0-x}
\mathrm{Pr}(x \vert H_0) = n! \prod_{j=1}^k \frac{p_{0i}^{x_j}}{x_j!} \; .
$$

The [p-value](/D/pval) is the probability of observing a value of the [test statistic](/D/tstat) that is as extreme or more extreme then the actually observed test statistic. Any set of counts $x$ might be considered as extreme or more extreme than the actually observed counts $y$, if the former is equally probable or less probably than the latter according to the PMF:

$$ \label{eq:mult-test-cond}
\mathrm{Pr}_0(x) \leq \mathrm{Pr}_0(y) \; .
$$

Thus, the [p-value](/D/pval) for the data in \eqref{eq:Mult} is equal to

$$ \label{eq:mult-test-p}
p = \sum_{x: \; \mathrm{Pr}_0(x) \leq \mathrm{Pr}_0(y)} \mathrm{Pr}_0(x)
$$

and the null hypothesis in \eqref{eq:mult-test-h0} is [rejected](/D/test), if

$$ \label{eq:mult-test-rej-qed}
p < \alpha \; .
$$