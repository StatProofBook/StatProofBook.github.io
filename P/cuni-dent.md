---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 20221-12-20 18:21:00

title: "Differential entropy of the continuous uniform distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Continuous uniform distribution"
theorem: "Differential entropy"

sources:

proof_id: "P397"
shortcut: "cuni-dent"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [continuous uniform distribution](/D/cuni):

$$ \label{eq:cuni}
X \sim \mathcal{U}(a, b) \; .
$$

Then, the [differential entropy](/D/dent) of $X$ is

$$ \label{eq:cuni-dent}
\mathrm{h}(X) = \ln(b-a) \; .
$$


**Proof:** The [differential entropy](/D/dent) of a random variable is defined as

$$ \label{eq:dent}
\mathrm{h}(X) = - \int_{\mathcal{X}} p(x) \, \log_b p(x) \, \mathrm{d}x \; .
$$

To measure $h(X)$ in nats, we set $b = e$, such that

$$ \label{eq:dent-nats}
\mathrm{h}(X) = - \int_{\mathcal{X}} p(x) \, \ln p(x) \, \mathrm{d}x \; .
$$

With the [probability density function of the continuous uniform distribution](/P/cuni-pdf), the differential entropy of $X$ is:

$$ \label{eq:cuni-dent-qed}
\begin{split}
\mathrm{h}(X) &= - \int_a^b \frac{1}{b-a} \, \ln \left( \frac{1}{b-a} \right) \, \mathrm{d}x \\
&= \frac{1}{b-a} \cdot \int_a^b \ln(b-a) \, \mathrm{d}x \\
&= \frac{1}{b-a} \cdot \left[ x \cdot \ln(b-a) \right]_a^b \\
&= \frac{1}{b-a} \cdot \left[ b \cdot \ln(b-a) - a \cdot \ln(b-a) \right] \\
&= \frac{1}{b-a} (b-a) \ln(b-a) \\
&= \ln(b-a) \; .
\end{split}
$$