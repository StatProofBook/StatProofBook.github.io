---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-04-04 14:41:13

title: "Beta distribution is a special case of Dirichlet distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Beta distribution"
theorem: "Special case of Dirichlet distribution"

sources:

proof_id: "P496"
shortcut: "beta-dir"
username: "JoramSoch"
---


**Theorem:** The [beta distribution](/D/beta) with shape parameters $\alpha$ and $\beta$ is a special case of the [Dirichlet distribution](/D/mult) with concentration parameters $\alpha_1 = \alpha$ and $\alpha_2 = \beta$:

$$ \label{eq:beta-dir}
X \sim \mathrm{Dir}(\left[ \alpha, \beta \right])
\quad \Rightarrow \quad
X \sim \mathrm{Bet}(\alpha, \beta) \; .
$$


**Proof:** The [probability density function of the Dirichlet distribution](/P/dir-pdf), where $x$ is a $1 \times k$ vector with $x_i \in [0,1]$ for $i = 1,\ldots,k$, is as follows:

$$ \label{eq:dir-pdf}
\mathrm{Dir}(x; \left[ \alpha_1, \ldots, \alpha_k \right]) = \frac{\Gamma\left( \sum_{i=1}^k \alpha_i \right)}{\prod_{i=1}^k \Gamma(\alpha_i)} \, \prod_{i=1}^k {x_i}^{\alpha_i-1} \; .
$$

If we let $k = 2$, $\alpha_1 = \alpha$ and $\alpha_2 = \beta$, we obtain

$$ \label{eq:dir-pdf-beta-s1}
\mathrm{Dir}(x; \left[ \alpha, \beta \right]) = \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \, \Gamma(\beta)} \, x_1^{\alpha-1} \, x_2^{\beta-1} \; .
$$

Applying the beta function $\mathrm{B}(x,y) = \Gamma(x) \Gamma(y) / \Gamma(x+y)$, we have

$$ \label{eq:dir-pdf-beta-s2}
\mathrm{Dir}(x; \left[ \alpha, \beta \right]) = \frac{1}{\mathrm{B}(\alpha,\beta)} \, x_1^{\alpha-1} \, x_2^{\beta-1} \; .
$$

Recognizing that $\sum_{i=1}^{k} x_i = 1$, such that $x_2 = 1 - x_1$, we get

$$ \label{eq:dir-pdf-beta-s3}
\mathrm{Dir}(x; \left[ \alpha, \beta \right]) = \frac{1}{\mathrm{B}(\alpha,\beta)} \, x_1^{\alpha-1} \, (1-x_1)^{\beta-1}
$$

which is equivalent to the [probability density function of the beta distribution](/P/beta-pdf).