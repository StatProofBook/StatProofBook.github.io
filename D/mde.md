---
layout: definition
mathjax: true

author: "Alexander D. Bolton"
affiliation: "The Book of Statistical Proofs"
e_mail: "StatProofBook@gmail.com"
date: 2025-07-15 00:00:00

title: "Minimum detectable effect"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Hypothesis testing"
definition: "Minimum detectable effect"

sources:
  - authors: "Sylvain Chabé-Ferret"
    year: 2025
    title: "Power Analysis"
    in: "Statistical Tools for Causal Inference"
    pages: "retrieved on 2025-07-05"
    url: "https://chabefer.github.io/STCI/Power.html"

def_id: "D224"
shortcut: "mde"
username: "alexanderdbolton"
---


**Definition:** Consider a [hypothesis test](/D/test) concerning parameter $\theta$. We have $H_0: \theta \in \Theta_0$ versus $H_1: \theta \in \Theta_1$, where $\{\Theta_0, \Theta_1\}$ is a partition of $\Theta$. Let the probability of rejecting the null hypothesis for the test with $n$ observations be $\kappa_n(\theta)$. The number of samples $n$ is fixed.

The effect size for a parameter $\theta \in \Theta_1$ is the distance of $\theta$ from the null parameter space $\Theta_0, d(\theta, \Theta_0)$. It can be defined as

$$ \label{eq:distancefromTheta0}
d(\theta, \Theta_0) = \inf_{\theta_0 \in \Theta_0} ||\theta - \theta_0||
$$

Let the test have a given [significance level](/D/alpha) $\alpha$ and desired [power](/D/power) $1 - \beta$. The minimum detectable effect, $\delta$, is the smallest $\delta$ so that the hypothesis test simultaneously satisfies has [size](/D/size) less than or equal to $\alpha$ and power at least $1 - \beta$:

$$ \label{eq:mdeconditions}
\left(\sup_{\theta \in \Theta_0} \kappa_n(\theta) \leq \alpha\right) \wedge \left(\inf_{\theta: d(\theta, \Theta_0) \leq \delta} \kappa_n(\theta) \geq 1 - \beta\right)
$$

**Example:**

Suppose that a researcher is testing the effect of an intervention on IQ scores. From previous testing, the population has normally distributed scores, with an average of $100$ with standard deviation $\sigma = 15$.

Let the (unknown) post-intervention mean of IQ scores be $\theta$, and assume that the post-intervention standard deviation is also $\sigma = 15$. The researcher wants to test the null hypothesis $H_0: \theta = 100$ against $H_1: \theta > 100$. The researcher will perform a one-sided [one-sample t-test](/P/ug-ttest1) to test the hypothesis. This satisfies the condition that the probability of Type I error is at most $\alpha$. The researcher has 346 participants available.

The researcher wants to know: what is the minimum detectable effect with power $1 - \beta$? Using the formula from [power analysis for the one-sample t-test](/P/ug-ttest1power), we have

$$ \label{eq:mde-one-sided}
\delta \geq \frac{(z_\alpha + z_\beta)\sigma}{\sqrt{n}}
$$

Assuming $\alpha = 0.05, \beta = 0.2$ (so the significance level is $0.05$ and the power is $0.8$), the minimum detectable effect is

$$ \label{eq:mde-one-sided-calculation}
\frac{(1.64 + 0.84)15}{\sqrt{346}} \approx 2. 
$$

As one can see, the minimum detectable effect will increase, if $\sigma$ increases or if any of $\alpha$, $\beta$ or $n$ decreases.