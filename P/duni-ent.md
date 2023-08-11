---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-08-11 13:13:00

title: "Entropy of the discrete uniform distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Discrete uniform distribution"
theorem: "Shannon entropy"

sources:

proof_id: "P140"
shortcut: "duni-ent"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [discrete uniform distribution](/D/duni):

$$ \label{eq:duni}
X \sim \mathcal{U}(a,b) \; .
$$

Then, the [(Shannon) entropy](/D/ent) of $X$ in nats is

$$ \label{eq:duni-ent}
\mathrm{H}(X) = \ln(b-a+1) \; .
$$


**Proof:** The [entropy](/D/ent) is defined as the probability-weighted average of the logarithmized probabilities for all possible values:

$$ \label{eq:ent}
\mathrm{H}(X) = - \sum_{x \in \mathcal{X}} p(x) \cdot \log_b p(x) \; .
$$

Entropy is measured in nats by setting $b = e$. Then, with the [probability mass function of the discrete uniform distribution](/P/duni-pmf), we have:

$$ \label{eq:duni-ent-qed}
\begin{split}
\mathrm{H}(X) &= - \sum_{x \in \mathcal{X}} p(x) \cdot \log_e p(x) \\
&= - \sum_{x=a}^{b} p(x) \cdot \ln p(x) \\
&= - \sum_{x=a}^{b} \frac{1}{b-a+1} \cdot \ln{\frac{1}{b-a+1}} \\
&= - (b-a+1) \cdot \frac{1}{b-a+1} \cdot \ln{\frac{1}{b-a+1}} \\
&= - \ln{\frac{1}{b-a+1}} \\
&= \ln(b-a+1) \; .
\end{split}
$$