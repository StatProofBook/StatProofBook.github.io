---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-26 11:42:00

title: "Posterior probability of the alternative model for binomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Binomial observations"
theorem: "Posterior probability"

sources:

proof_id: "P384"
shortcut: "bin-pp"
username: "JoramSoch"
---


**Theorem:** Let $y$ be the number of successes resulting from $n$ independent trials with unknown success probability $p$, such that $y$ follows a [binomial distribution](/D/bin):

$$ \label{eq:Bin}
y \sim \mathrm{Bin}(n,p) \; .
$$

Moreover, assume two [statistical models](/D/fpm), one assuming that $p$ is 0.5 ([null model](/D/h0)), the other imposing a [beta distribution](/P/bin-prior) as the [prior distribution](/D/prior) on the model parameter $p$ ([alternative](/D/h1)):

$$ \label{eq:Bin-m01}
\begin{split}
m_0&: \; y \sim \mathrm{Bin}(n,p), \; p = 0.5 \\
m_1&: \; y \sim \mathrm{Bin}(n,p), \; p \sim \mathrm{Bet}(\alpha_0, \beta_0) \; .
\end{split}
$$

Then, the [posterior probability](/D/pmp) of the [alternative model](/D/h1) is given by

$$ \label{eq:Bin-PP1}
p(m_1|y) = \frac{1}{1 + 2^{-n} \left[ B(\alpha_0,\beta_0) / B(\alpha_n,\beta_n) \right]}
$$

where $B(x,y)$ is the beta function and $\alpha_n$ and $\beta_n$ are the [posterior hyperparameters for binomial observations](/P/bin-post) which are functions of the [number of trials](/D/bin) $n$ and the [number of successes](/D/bin) $y$.


**Proof:** [The posterior probability for one of two models is a function of the log Bayes factor in favor of this model](/P/pmp-lbf):

$$ \label{eq:PP-LBF}
p(m_1|y) = \frac{\exp(\mathrm{LBF}_{12})}{\exp(\mathrm{LBF}_{12}) + 1} \; .
$$

The [log Bayes factor in favor of the alternative model for binomial observations](/P/bin-lbf) is given by

$$ \label{eq:Bin-LBF10}
\mathrm{LBF}_{10} = \log B(\alpha_n,\beta_n) - \log B(\alpha_0,\beta_0) - n \log \left( \frac{1}{2} \right) \; .
$$

and the corresponding [Bayes factor](/D/bf), i.e. [exponentiated log Bayes factor](/P/lbf-der), is equal to

$$ \label{eq:Bin-BF10}
\mathrm{BF}_{10} = \exp(\mathrm{LBF}_{10}) = 2^n \cdot \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)} \; .
$$

Thus, the posterior probability of the alternative, assuming a prior distribution over the probability $p$, compared to the null model, assuming a fixed probability $p = 0.5$, follows as

$$ \label{eq:Bin-PP1-qed}
\begin{split}
p(m_1|y) &\overset{\eqref{eq:PP-LBF}}{=} \frac{\exp(\mathrm{LBF}_{10})}{\exp(\mathrm{LBF}_{10}) + 1} \\
&\overset{\eqref{eq:Bin-BF10}}{=} \frac{2^n \cdot \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)}}{2^n \cdot \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)} + 1} \\
&= \frac{2^n \cdot \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)}}{2^n \cdot \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)} \left( 1 + 2^{-n} \frac{B(\alpha_0,\beta_0)}{B(\alpha_n,\beta_n)} \right)} \\
&= \frac{1}{1 + 2^{-n} \left[ B(\alpha_0,\beta_0) / B(\alpha_n,\beta_n) \right]}
\end{split}
$$

where the [posterior hyperparameters](/D/post) [are given by](/P/bin-post)

$$ \label{eq:Bin-post-par}
\begin{split}
\alpha_n &= \alpha_0 + y \\
\beta_n &= \beta_0 + (n-y)
\end{split}
$$

with the [number of trials](/D/bin) $n$ and the [number of successes](/D/bin) $y$.