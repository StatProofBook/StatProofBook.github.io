---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-02 17:00:00

title: "Maximum likelihood estimation for multinomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Multinomial observations"
theorem: "Maximum likelihood estimation"

sources:

proof_id: "P385"
shortcut: "mult-mle"
username: "JoramSoch"
---


**Theorem:** Let $y = [y_1, \ldots, y_k]$ be the number of observations in $k$ categories resulting from $n$ independent trials with unknown category probabilities $p = [p_1, \ldots, p_k]$, such that $y$ follows a [multinomial distribution](/D/mult):

$$ \label{eq:Mult}
y \sim \mathrm{Mult}(n,p) \; .
$$

Then, the [maximum likelihood estimator](/P/mle) of $p$ is

$$ \label{eq:Mult-MLE}
\hat{p} = \frac{1}{n} y , \quad \text{i.e.} \quad \hat{p}_j = \frac{y_j}{n} \quad \text{for all} \quad j = 1, \ldots, k \; .
$$


**Proof:** Note that [the marginal distribution of each element in a multinomial random vector is a binomial distribution](/P/mult-marg)

$$ \label{eq:Mult-marg}
X \sim \mathrm{Mult}(n,p) \quad \Rightarrow \quad X_j \sim \mathrm{Bin}(n, p_j) \quad \text{for all} \quad j = 1, \ldots, k \; .
$$

Thus, combining \eqref{eq:Mult} with \eqref{eq:Mult}, we have

$$ \label{eq:Mult-Bin}
y_j \sim \mathrm{Bin}(n,p_j)
$$

which [implies the likelihood function](/P/bin-mle)

$$ \label{eq:Bin-LF}
\mathrm{p}(y|p_j) = \mathrm{Bin}(y_j; n, p_j) = {n \choose y_j} \, p_j^{y_j} \, (1-p_j)^{n-y_j} \; .
$$

To this, we can apply [maximum likelihood estimation for binomial observations](/P/bin-mle), such that the MLE for each $p_j$ is

$$ \label{eq:Mult-MLE-qed}
\hat{p}_j = \frac{y_j}{n} \; .
$$