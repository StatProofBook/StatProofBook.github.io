---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-09-01 13:46:43

title: "___"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
theorem: "___"

sources:

proof_id: "___"
shortcut: "post-ind"
username: "JoramSoch"
---


**Theorem:** Let $p(\theta \vert y_1)$ and $p(\theta \vert y_2)$ be [posterior distributions](/D/post), obtained using the same [prior distribution](/D/prior) from [conditionally independent](/D/ind-cond) data sets $y_1$ and $y_2$:

$$ \label{eq:ind-cond}
p(y_1,y_2|\theta) = p(y_1|\theta) \cdot p(y_2|\theta) \; .
$$

Then, the combined posterior [distribution](/D/dist) is proportional to the product of the individual posterior [densities](/D/pdf), divided by the prior density:

$$ \label{eq:post-ind}
p(\theta|y_1,y_2) \propto \frac{p(\theta|y_1) \cdot p(\theta|y_2)}{p(\theta)} \; .
$$


**Proof:** Since $p(\theta \vert y_1)$ and $p(\theta \vert y_2)$ are [posterior distributions](/D/post), [Bayes' theorem](/P/bayes-th) holds for them:

$$ \label{eq:bayes-th}
\begin{split}
p(\theta|y_1) &= \frac{p(y_1|\theta) \cdot p(\theta)}{p(y_1)} \\
p(\theta|y_2) &= \frac{p(y_2|\theta) \cdot p(\theta)}{p(y_2)} \; .
\end{split}
$$

Moreover, [Bayes' theorem must also hold for the combined posterior distribution](/P/post-jl):

$$ \label{eq:post-ind-s1}
p(\theta|y_1,y_2) = \frac{p(y_1,y_2|\theta) \cdot p(\theta)}{p(y_1,y_2)} \; .
$$

With that, we can express the combined posterior distribution as follows:

$$ \label{eq:post-ind-s2}
\begin{split}
p(\theta|y_1,y_2) &\overset{\eqref{eq:post-ind-s1}}{=} \frac{p(y_1,y_2|\theta) \cdot p(\theta)}{p(y_1,y_2)} \\
&\overset{\eqref{eq:ind-cond}}{=} p(y_1|\theta) \cdot p(y_2|\theta) \cdot \frac{p(\theta)}{p(y_1,y_2)} \\
&\overset{\eqref{eq:bayes-th}}{=} \frac{p(\theta|y_1) \cdot p(y_1)}{p(\theta)} \cdot \frac{p(\theta|y_2) \cdot p(y_2)}{p(\theta)} \cdot \frac{p(\theta)}{p(y_1,y_2)} \\
&= \frac{p(\theta|y_1) \cdot p(\theta|y_2)}{p(\theta)} \cdot \frac{p(y_1) \cdot p(y_2)}{p(y_1,y_2)} \; .
\end{split}
$$

Note that the second fraction does not depend on $\theta$ and thus, the posterior distribution over $\theta$ is proportional to the first fraction:

$$ \label{eq:post-ind-s3}
p(\theta|y_1,y_2) \propto \frac{p(\theta|y_1) \cdot p(\theta|y_2)}{p(\theta)} \; .
$$
