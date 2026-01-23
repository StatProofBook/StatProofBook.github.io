---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-02-06 11:27:25

title: "Entropy of the Poisson distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Poisson distribution"
theorem: "Shannon entropy"

sources:

proof_id: "P486"
shortcut: "poiss-ent"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [Poisson distribution](/D/poiss):

$$ \label{eq:poiss}
X \sim \mathrm{Poiss}(\lambda) \; .
$$

Then, the [(Shannon) entropy](/D/ent) of $X$ in nats is

$$ \label{eq:poiss-ent}
\mathrm{H}(X) = \lambda \left( 1 - \ln \lambda \right) + e^{-\lambda} \sum_{x=0}^{\infty} \frac{\lambda^x \ln x!}{x!} \; .
$$


**Proof:** The [entropy](/D/ent) is defined as the probability-weighted average of the logarithmized probabilities for all possible values:

$$ \label{eq:ent}
\mathrm{H}(X) = - \sum_{x \in \mathcal{X}} p(x) \cdot \log_b p(x) \; .
$$

Entropy is measured in nats by setting $b = e$. Then, with the [probability mass function of the Poisson distribution](/P/poiss-pmf), we have:

$$ \label{eq:poiss-ent-s1}
\begin{split}
   \mathrm{H}(X)
&= - \sum_{x \in \mathcal{X}} p(x) \cdot \log_e p(x) \\
&= - \sum_{x=0}^{\infty} \frac{\lambda^x e^{-\lambda}}{x!} \cdot \ln \frac{\lambda^x e^{-\lambda}}{x!} \\
&= - e^{-\lambda} \sum_{x=0}^{\infty} \frac{\lambda^x}{x!} \left[ \ln \lambda^x + \ln e^{-\lambda} - \ln x! \right] \\
&= - e^{-\lambda} \sum_{x=0}^{\infty} \frac{\lambda^x \ln \lambda^x}{x!}
   - e^{-\lambda} \sum_{x=0}^{\infty} \frac{\lambda^x \ln e^{-\lambda}}{x!}
   + e^{-\lambda} \sum_{x=0}^{\infty} \frac{\lambda^x \ln x!}{x!} \\
&= - e^{-\lambda} \sum_{x=0}^{\infty} \frac{\lambda^x x \cdot \ln \lambda}{x!}
   - e^{-\lambda} \sum_{x=0}^{\infty} \frac{\lambda^x (-\lambda) \cdot \ln e}{x!}
   + e^{-\lambda} \sum_{x=0}^{\infty} \frac{\lambda^x \ln x!}{x!} \\
&= - e^{-\lambda} \ln \lambda \sum_{x=0}^{\infty} \frac{\lambda^x \cdot x}{x!}
   + e^{-\lambda} \lambda \sum_{x=0}^{\infty} \frac{\lambda^x}{x!}
   + e^{-\lambda} \sum_{x=0}^{\infty} \frac{\lambda^x \ln x!}{x!} \; .
\end{split}
$$

Using the relation $x!/x = (x-1)!$, the first term can be developped as follows

$$ \label{eq:poiss-ent-term1}
\begin{split}
   e^{-\lambda} \ln \lambda \sum_{x=0}^{\infty} \frac{\lambda^x \cdot x}{x!}
&= e^{-\lambda} \cdot \ln \lambda \cdot \sum_{x=0}^{\infty} \lambda \cdot \frac{\lambda^x}{\lambda} \cdot \frac{x}{x!} \\
&= e^{-\lambda} \cdot \lambda \cdot \ln \lambda \cdot \sum_{x=0}^{\infty} \frac{\lambda^{x-1}}{(x-1)!} \\
&= e^{-\lambda} \cdot \lambda \cdot \ln \lambda \cdot \left( \frac{\lambda^{-1}}{(-1)!} + \sum_{x=0}^{\infty} \frac{\lambda^x}{x!} \right) \\
&= e^{-\lambda} \cdot \lambda \cdot \ln \lambda \cdot \left( \frac{1}{\lambda} \cdot \frac{0}{0!} + \sum_{x=0}^{\infty} \frac{\lambda^x}{x!} \right) \\
&= e^{-\lambda} \cdot \lambda \cdot \ln \lambda \cdot \sum_{x=0}^{\infty} \frac{\lambda^x}{x!} \; ,
\end{split}
$$

such that equation \eqref{eq:poiss-ent-s1} becomes

$$ \label{eq:poiss-ent-s2}
   \mathrm{H}(X)
 = - e^{-\lambda} \lambda \ln \lambda \sum_{x=0}^{\infty} \frac{\lambda^x}{x!}
   + e^{-\lambda} \lambda \sum_{x=0}^{\infty} \frac{\lambda^x}{x!}
   + e^{-\lambda} \sum_{x=0}^{\infty} \frac{\lambda^x \ln x!}{x!} \; .
$$

Using the power series form of the exponential function

$$ \label{eq:exp-sum}
e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} \; ,
$$

equation \eqref{eq:poiss-ent-s2} finally becomes

$$ \label{eq:poiss-ent-s3}
\begin{split}
   \mathrm{H}(X)
&= - e^{-\lambda} \lambda \ln \lambda e^{\lambda}
   + e^{-\lambda} \lambda e^{\lambda}
   + e^{-\lambda} \sum_{x=0}^{\infty} \frac{\lambda^x \ln x!}{x!} \\
&= - \lambda \ln \lambda + \lambda + e^{-\lambda} \sum_{x=0}^{\infty} \frac{\lambda^x \ln x!}{x!} \\
&= \lambda \left( 1 - \ln \lambda \right) + e^{-\lambda} \sum_{x=0}^{\infty} \frac{\lambda^x \ln x!}{x!} \; .
\end{split}
$$