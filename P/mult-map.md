---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-12-08 15:14:47

title: "Maximum-a-posteriori estimation for multinomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Multinomial observations"
theorem: "Maximum-a-posteriori estimation"

sources:

proof_id: "P428"
shortcut: "mult-map"
username: "JoramSoch"
---


**Theorem:** Let $y = [y_1, \ldots, y_k]$ be the number of observations in $k$ categories resulting from $n$ independent trials with unknown category probabilities $p = [p_1, \ldots, p_k]$, such that $y$ follows a [multinomial distribution](/D/mult):

$$ \label{eq:Mult}
y \sim \mathrm{Mult}(n,p) \; .
$$

Moreover, assume a [Dirichlet prior distribution](/P/mult-prior) over the model parameter $p$:

$$ \label{eq:Mult-prior}
\mathrm{p}(p) = \mathrm{Dir}(p; \alpha_0) \; .
$$

Then, the [maximum-a-posteriori estimates](/D/map) of $p$ are

$$ \label{eq:Mult-MAP}
\hat{p}_\mathrm{MAP} = \frac{\alpha_0+y-1}{\sum_{j=1}^k \alpha_{0j} + n - k} \; .
$$


**Proof:** Given the [prior distribution](/D/prior) in \eqref{eq:Mult-prior}, the [posterior distribution](/D/post) for [multinomial observations](/D/mult-data) [is also a Dirichlet distribution](/P/mult-post)

$$ \label{eq:Mult-post}
\mathrm{p}(p|y) = \mathrm{Dir}(p; \alpha_n)
$$

where the [posterior hyperparameters](/D/post) are equal to

$$ \label{eq:Mult-post-par}
\alpha_{nj} = \alpha_{0j} + y_j, \; j = 1,\ldots,k \; .
$$

The [mode of the Dirichlet distribution](/P/dir-mode) is given by:

$$ \label{eq:Dir-mode}
X \sim \mathrm{Dir}(\alpha) \quad \Rightarrow \quad \mathrm{mode}(X_i) = \frac{\alpha_i-1}{\sum_j \alpha_j - k} \; .
$$

Applying \eqref{eq:Dir-mode} to \eqref{eq:Mult-post} with \eqref{eq:Mult-post-par}, the [maximum-a-posteriori estimates](/D/map) of $p$ follow as

$$ \label{eq:Mult-MAP-s1}
\begin{split}
\hat{p}_{i,\mathrm{MAP}} &= \frac{\alpha_{ni} - 1}{\sum_j \alpha_{nj} - k} \\
&\overset{\eqref{eq:Mult-post-par}}{=} \frac{\alpha_{0i} + y_i - 1}{\sum_j (\alpha_{0j} + y_j) - k} \\
&= \frac{\alpha_{0i} + y_i - 1}{\sum_j \alpha_{0j} + \sum_j y_j - k} \; .
\end{split}
$$

Since $y_1 + \ldots + y_k = n$ [by definition](/D/mult-data), this becomes

$$ \label{eq:Mult-MAP-s2}
\hat{p}_{i,\mathrm{MAP}} = \frac{\alpha_{0i} + y_i - 1}{\sum_j \alpha_{0j} + n - k} \end{equation}

which, using the $1 \times k$ [vectors](/D/mult-data) $y$, $p$ and $\alpha_0$, can be written as:

\begin{equation} \label{eq:Mult-MAP-qed}
\hat{p}_\mathrm{MAP} = \frac{\alpha_0+y-1}{\sum_{j=1}^k \alpha_{0j} + n - k} \; .
$$