---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-12-01 14:36:54

title: "Maximum-a-posteriori estimation for binomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Binomial observations"
theorem: "Maximum-a-posteriori estimation"

sources:

proof_id: "P427"
shortcut: "bin-map"
username: "JoramSoch"
---


**Theorem:** Let $y$ be the number of successes resulting from $n$ independent trials with unknown success probability $p$, such that $y$ follows a [binomial distribution](/D/bin):

$$ \label{eq:Bin}
y \sim \mathrm{Bin}(n,p) \; .
$$

Moreover, assume a [beta prior distribution](/P/bin-prior) over the model parameter $p$:

$$ \label{eq:Bin-prior}
\mathrm{p}(p) = \mathrm{Bet}(p; \alpha_0, \beta_0) \; .
$$

Then, the [maximum-a-posteriori estimate](/D/map) of $p$ is

$$ \label{eq:Bin-MLE}
\hat{p}_\mathrm{MAP} = \frac{\alpha_0+y-1}{\alpha_0+\beta_0+n-2} \; .
$$


**Proof:** Given the [prior distribution](/D/prior) in \eqref{eq:Bin-prior}, the [posterior distribution](/D/post) for [binomial observations](/D/bin-data) [is also a beta distribution](/P/bin-post)

$$ \label{eq:Bin-post}
\mathrm{p}(p|y) = \mathrm{Bet}(p; \alpha_n, \beta_n)
$$

where the [posterior hyperparameters](/D/post) are equal to

$$ \label{eq:Bin-post-par}
\begin{split}
\alpha_n &= \alpha_0 + y \\
\beta_n &= \beta_0 + (n-y) \; .
\end{split}
$$

The [mode of the beta distribution](/P/beta-mode) is given by:

$$ \label{eq:beta-mode}
X \sim \mathrm{Bet}(\alpha, \beta) \quad \Rightarrow \quad \mathrm{mode}(X) = \frac{\alpha-1}{\alpha+\beta-2} \; .
$$

Applying \eqref{eq:beta-mode} to \eqref{eq:Bin-post} with \eqref{eq:Bin-post-par}, the [maximum-a-posteriori estimate](/D/map) of $p$ follows as:

$$ \label{eq:Bin-MAP}
\begin{split}
\hat{p}_\mathrm{MAP} &= \frac{\alpha_n-1}{\alpha_n+\beta_n-2} \\
&\overset{\eqref{eq:Bin-post-par}}{=} \frac{\alpha_0+y-1}{\alpha_0+y+\beta_0+(n-y)-2} \\
&= \frac{\alpha_0+y-1}{\alpha_0+\beta_0+n-2} \; .
\end{split}
$$