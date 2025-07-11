---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-03-18 17:26:00

title: "Maximum likelihood estimation can result in biased estimates"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Likelihood theory"
theorem: "MLE can be biased"

sources:

proof_id: "P317"
shortcut: "mle-bias"
username: "JoramSoch"
---


**Theorem:** [Maximum likelihood estimation](/D/mle) can result in [biased estimates](/D/est-bias) of [model parameters](/D/para), i.e. [estimates](/D/est) whose long-term [expected value](/D/mean) is unequal to the quantities they estimate:

$$ \label{eq:aicc-aic}
\mathrm{E}\left[ \hat{\theta}_\mathrm{MLE} \right] = \mathrm{E}\left[ \operatorname*{arg\,max}_\theta \mathrm{LL}_m(\theta) \right] \neq \theta \; .
$$


**Proof:** Consider a [set of independent and identical normally distributed observations](/D/ug) $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ with unknown [mean](/D/mean) $\mu$ and [variance](/D/var) $\sigma^2$:

$$ \label{eq:ug}
x_i \overset{\text{i.i.d.}}{\sim} \mathcal{N}(\mu, \sigma^2), \quad i = 1,\ldots,n \; .
$$

Then, we know that the [maximum likelihood estimator for the variance](/P/ug-mle) $\sigma^2$ is [underestimating the true variance of the data distribution](/P/resvar-bias):

$$ \label{eq:resvar-bias}
\mathrm{E}\left[ \hat{\sigma}^2_\mathrm{MLE} \right] = \frac{n-1}{n} \sigma^2 \neq \sigma^2 \; .
$$

This proofs the existence of cases such as those stated by the theorem.