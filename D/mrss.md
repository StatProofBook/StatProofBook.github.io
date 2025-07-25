---
layout: definition
mathjax: true

author: "Alexander D. Bolton"
affiliation: "The Book of Statistical Proofs"
e_mail: "StatProofBook@gmail.com"
date: 2025-07-15 00:00:00

title: "Minimum detectable effect"
chapter: "General Theorems"
section: "Probability theory"
topic: "Random experiments"
definition: "Minimum detectable effect"

sources:
  - authors: "Sylvain Chabé-Ferret"
    year: 2025
    title: Power Analysis
    in: Statistical Tools for Causal Inference
    pages: "Retrieved on 2025-07-05"
    url: "https://chabefer.github.io/STCI/Power.html"

def_id: "D225"
shortcut: "mrss"
username: "alexanderdbolton"
---


**Definition:**
We'll start with a formal definition that covers all cases, and then give an example of the typical use case. Consider a [hypothesis test](/D/test) concerning parameter $\theta$. We have $H_0: \theta \in \Theta_0$ versus $H_1: \theta \in \Theta_1$, where $\{\Theta_0, \Theta_1\}$ is a partition of $\Theta$. Let the probability of rejecting the null hypothesis for the test with $n$ observations be $\kappa_n(\theta)$.

Given a pre-specified [significance level](/D/alpha) $\alpha \in (0, 1)$ and a desired [power](/D/power) $1 - \beta \in (0, 1)$, the test must satisfy two conditions:

1.  *Significance Constraint:* The probability of a Type I error must not exceed $\alpha$.
$$
\label{eq:type1error}
\sup_{\theta \in \Theta_0} \kappa_n(\theta) \le \alpha
$$

2.  *Power Constraint:* The power of the test must be at least $1 - \beta$ for all parameters corresponding to a [minimum detectable effect](/D/mde), $\delta$. This is represented by a specified subset of the alternative hypothesis space, $\Theta_{1,\delta} \subset \Theta_1$.
$$
\label{eq:power}
\inf_{\theta \in \Theta_{1,\delta}} \kappa_n(\theta) \ge 1 - \beta
$$

The *minimum required sample size*, $n_{m}$, is the smallest integer $n$ so that the hypothesis test simultaneously satisfies both the significance and power constraints.

**Example**

Suppose that a researcher is testing the effect of an intervention on IQ scores. From previous testing, the population has normally distributed scores, with an average of $100$ with standard deviation $\sigma = 15$.

Let the (unknown) post-intervention mean of IQ scores be $\theta$, and assume that the post-intervention standard deviation is also $\sigma = 15$. The researcher wants to test the null hypothesis $H_0: \theta = 100$ against $H_1: \theta > 100$. The researcher will perform a one-sided [one-sample t-test](/P/ug-ttest1) to test the hypothesis. This satisfies the condition that the probability of Type I error is at most $\alpha$. If the researcher is only interested in a positive result if the average IQ increases by at least 2 points, then we have $\delta = 2,  \Theta_{1, \delta} = \{\theta \in \mathbb{R} \mid \theta > \theta_0 + \delta\} = \{\theta \in \mathbb{R} \mid \theta > 100 + 2\}$.

The researcher needs the probability of rejecting $H_0$ if $\theta > 102$ to be at least $1 - \beta$. How many subjects they will need to recruit in order to be able to detect an increase of at least $2$ points with power $1 - \beta$? Using the formula from [Power analysis, minimum detectable effect, minimum required sample size for a one-sample t-test](/P/ug-t1power), we have
$$
\label{eq:mrss-one-sided}
n_m \geq \frac{\sigma^2(z_\alpha + z_\beta)^2}{\delta^2}.
$$
Assuming $\alpha = 0.05, \beta = 0.2$ (so the significance level is $0.05$ and the power is $0.8$), the minimum required sample size is
$$
\label{eq:mrss-one-sided-calculation}
\frac{15^2(1.64 + 0.84)^2}{2^2} = 345.96,
$$
so the minimum required sample size is 346 participants. 

You can see that increasing $\sigma$ will increase the minimum required sample size. And decreasing $\alpha, \beta$ or $\delta$ will increase the minimum required sample size.
