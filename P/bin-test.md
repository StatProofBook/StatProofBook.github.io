---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-12-16 20:01:14

title: "Binomial test"
chapter: "Statistical Models"
section: "Count data"
topic: "Binomial observations"
theorem: "Binomial test"

sources:
  - authors: "Wikipedia"
    year: 2023
    title: "Binomial test"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2023-12-16"
    url: "https://en.wikipedia.org/wiki/Binomial_test#Usage"
  - authors: "Wikipedia"
    year: 2023
    title: "Binomialtest"
    in: "Wikipedia – Die freie Enzyklopädie"
    pages: "retrieved on 2023-12-16"
    url: "https://de.wikipedia.org/wiki/Binomialtest#Signifikanzniveau_und_kritische_Werte"

proof_id: "P429"
shortcut: "bin-test"
username: "JoramSoch"
---


**Theorem:** Let $y$ be the number of successes resulting from $n$ independent trials with unknown success probability $p$, such that $y$ follows a [binomial distribution](/D/bin):

$$ \label{eq:Bin}
y \sim \mathrm{Bin}(n,p) \; .
$$

Then, the [null hypothesis](/D/h0)

$$ \label{eq:bin-test-h0}
H_0: \; p = p_0
$$

is [rejected](/D/test) at [significance level](/D/alpha) $\alpha$, if

$$ \label{eq:bin-test-rej}
y \leq c_1 \quad \text{or} \quad y \geq c_2
$$

where $c_1$ is the largest integer value, such that

$$ \label{eq:bin-test-c1}
\sum_{x=0}^{c_1} \mathrm{Bin}(x; n, p_0) \leq \frac{\alpha}{2} \; ,
$$

and $c_2$ is the smallest integer value, such that

$$ \label{eq:bin-test-c2}
\sum_{x=c_2}^{n} \mathrm{Bin}(x; n, p_0) \leq \frac{\alpha}{2} \; ,
$$

where $\mathrm{Bin}(x; n, p)$ is the [probability mass function of the binomial distribution](/P/bin-pmf):

$$ \label{eq:bin-pmf}
\mathrm{Bin}(x; n, p) = {n \choose x} \, p^x \, (1-p)^{n-x} \; .
$$


**Proof:** The [alternative hypothesis](/D/h1) relative to $H_0$ for a [two-sided test](/D/test-tail) is

$$ \label{eq:bin-test-h1}
H_1: \; p \neq p_0 \; .
$$

We can use $y$ as a [test statistic](/D/tstat). Its [sampling distribution](/D/dist-samp) is given by \eqref{eq:Bin}. The [cumulative distribution function](/D/cdf) (CDF) of the test statistic under the null hypothesis is thus equal to the [cumulative distribution function of a binomial distribution](/P/bin-cdf) with [success probability](/D/bin) $p_0$:

$$ \label{eq:y-cdf}
\mathrm{Pr}(y \leq z \vert H_0) = \sum_{x=0}^{z} \mathrm{Bin}(x; n, p_0) = \sum_{x=0}^{z} {n \choose x} \, p_0^x \, (1-p_0)^{n-x} \; .
$$

The [critical value](/D/cval) is the value of $y$, such that the probability of observing this or more extreme values of the test statistic is equal to or smaller than $\alpha$. Since $H_0$ and $H_1$ define a two-tailed test, we need two critical values $y_1$ and $y_2$ that satisfy

$$ \label{eq:y-cvals}
\begin{split}
\alpha &\geq \mathrm{Pr}(y \in \left\lbrace 0, \ldots, y_1 \right\rbrace \cup \left\lbrace y_2, \ldots, n \right\rbrace \vert H_0) \\
&= \mathrm{Pr}(y \leq y_1 \vert H_0) + \mathrm{Pr}(y \geq y_2 \vert H_0) \\
&= \mathrm{Pr}(y \leq y_1 \vert H_0) + (1-\mathrm{Pr}(y \leq (y_2-1) \vert H_0) \; .
\end{split}
$$

Given the test statistic's CDF in \eqref{eq:y-cdf}, this is fulfilled by the values $c_1$ and $c_2$ defined in \eqref{eq:bin-test-c1} and \eqref{eq:bin-test-c2}. Thus, the null hypothesis $H_0$ [can be rejected](/D/cval), if the [observed test statistic](/D/test) is inside the rejection region:

$$ \label{eq:bin-test-rej-qed}
y \in \left\lbrace 0, \ldots, c_1 \right\rbrace \cup \left\lbrace c_2, \ldots, n \right\rbrace \; .
$$

This is equivalent to \eqref{eq:bin-test-rej} and thus completes the proof.