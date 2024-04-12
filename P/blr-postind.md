---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-04-12 16:31:00

title: "Combined posterior distribution for Bayesian linear regression when analyzing conditionally independent data sets"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression"
theorem: "Combined posterior distribution from independent data sets"

sources:

proof_id: "P447"
shortcut: "blr-postind"
username: "JoramSoch"
---


**Theorem:** Let $y = \left\lbrace y_1, \ldots, y_S \right\rbrace$ be a set of $S$ [conditionally independent data sets](/D/ind-cond) assumed to follow [linear regression models](/D/mlr) with [design matrices](/D/mlr) $X_1, \ldots, X_S$, [number of data points](/D/mlr) $n_1, \ldots, n_S$ and [precision matrices](/P/blr-prior) $P_1, \ldots, P_n$, governed by identical [regression coefficients](/D/mlr) $\beta$ and identical [noise precision](/D/blr-prior) $\tau$:

$$ \label{eq:GLM-NG-S}
\begin{split}
y_1 &= X_1 \beta + \varepsilon_1, \; \varepsilon_1 \sim \mathcal{N}(0, \sigma^2 V_1), \; \sigma^2 V_1 = (\tau P_1)^{-1} \\
&\;\;\vdots \\
y_S &= X_S \beta + \varepsilon_S, \; \varepsilon_S \sim \mathcal{N}(0, \sigma^2 V_S), \; \sigma^2 V_S = (\tau P_S)^{-1} \; .
\end{split}
$$

Moreover, assume a [normal-gamma prior distribution](/P/blr-prior) over the model parameters $\beta$ and $\tau = 1/\sigma^2$:

$$ \label{eq:GLM-NG-prior}
p(\beta,\tau) = \mathcal{N}(\beta; \mu_0, (\tau \Lambda_0)^{-1}) \cdot \mathrm{Gam}(\tau; a_0, b_0) \; .
$$

Then, the [combined posterior distribution](/P/post-ind) from observing these [conditionally independent data sets](/D/ind-cond) is also given by a [normal-gamma distribution](/D/ng)

$$ \label{eq:GLM-NG-post}
p(\beta,\tau|y) = \mathcal{N}(\beta; \mu_n, (\tau \Lambda_n)^{-1}) \cdot \mathrm{Gam}(\tau; a_n, b_n)
$$

with the [posterior hyperparameters](/D/post)

$$ \label{eq:GLM-NG-S-post-par}
\begin{split}
\mu_n &= \Lambda_n^{-1} \left( \sum_{i=1}^S X_i^\mathrm{T} P_i y_i + \Lambda_0 \mu_0 \right) \\
\Lambda_n &= \sum_{i=1}^S X_i^\mathrm{T} P_i X_i + \Lambda_0 \\
a_n &= a_0 + \frac{1}{2} \sum_{i=1}^S n_i \\
b_n &= b_0 + \frac{1}{2} \left( \sum_{i=1}^S y_i^\mathrm{T} P_i y_i + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n \right) \; .
\end{split}
$$


**Proof:** This can be seen by sequentially applying [Bayes' theorem](/P/bayes-th) for [calculating the posterior distribution](/P/post-jl), while using the posterior after one iteration as the prior for the next iteration.

Let $\mu_0^{(i)}, \Lambda_0^{(i)}, a_0^{(i)}, b_0^{(i)}$ denote the [prior hyperparameters](/D/prior) before analyzing the $i$-th data set, such that e.g. $\mu_0^{(1)}$ is identical to $\mu_0$ in \eqref{eq:GLM-NG-prior}:

$$ \label{eq:GLM-NG-S-prior-y1}
\begin{split}
\mu_0^{(1)} &= \mu_0 \\
\Lambda_0^{(1)} &= \Lambda_0 \\
a_0^{(1)} &= a_0 \\
b_0^{(1)} &= b_0 \; .
\end{split}
$$

Moreover, let $\mu_n^{(i)}, \Lambda_n^{(i)}, a_n^{(i)}, b_n^{(i)}$ denote the [posterior hyperparameters](/D/post) after analyzing the $i$-th data set, such that e.g. $\mu_n^{(S)}$ is identical to $\mu_n$ in \eqref{eq:GLM-NG-post}:

$$ \label{eq:GLM-NG-S-post-yS}
\begin{split}
\mu_n^{(S)} &= \mu_n \\
\Lambda_n^{(S)} &= \Lambda_n \\
a_n^{(S)} &= a_n \\
b_n^{(S)} &= b_n \; .
\end{split}
$$

The [posterior](/D/post) after seeing the $i$-th data set is equal to the [prior](/D/prior) before seeing the $(i+1)$-th data set, so we have the relation:

$$ \label{eq:GLM-NG-S-prior-post}
\begin{split}
\mu_0^{(i+1)} &= \mu_n^{(i)} \\
\Lambda_0^{(i+1)} &= \Lambda_n^{(i)} \\
a_0^{(i+1)} &= a_n^{(i)} \\
b_0^{(i+1)} &= b_n^{(i)} \; .
\end{split}
$$

The posterior distribution for Bayesian linear regression when observing a single data set is given by the [following hyperparameter equations](/P/blr-post):

$$ \label{eq:GLM-NG-post-par}
\begin{split}
\mu_n &= \Lambda_n^{-1} (X^\mathrm{T} P y + \Lambda_0 \mu_0) \\
\Lambda_n &= X^\mathrm{T} P X + \Lambda_0 \\
a_n &= a_0 + \frac{n}{2} \\
b_n &= b_0 + \frac{1}{2} (y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n) \; .
\end{split}
$$

We can apply \eqref{eq:GLM-NG-post-par} to calculate the posterior hyperparameters after seeing the first data set:

$$ \label{eq:GLM-NG-S-post-y1}
\begin{split}
\mu_n^{(1)} &= {\Lambda_n^{(1)}}^{-1} \left( X_1^\mathrm{T} P_1 y_1 + \Lambda_0^{(1)} \mu_0^{(1)} \right) \\
&= {\Lambda_n^{(1)}}^{-1} \left( X_1^\mathrm{T} P_1 y_1 + \Lambda_0 \mu_0 \right) \\
\Lambda_n^{(1)} &= X_1^\mathrm{T} P_1 X_1 + \Lambda_0^{(1)} \\
&= X_1^\mathrm{T} P_1 X_1 + \Lambda_0 \\
a_n^{(1)} &= a_0^{(1)} + \frac{1}{2} n_1 \\
&= a_0 + \frac{1}{2} n_1 \\
b_n^{(1)} &= b_0^{(1)} + \frac{1}{2} \left( y_1^\mathrm{T} P_1 y_1 + {\mu_0^{(1)}}^\mathrm{T} \Lambda_0^{(1)} \mu_0^{(1)} - {\mu_n^{(1)}}^\mathrm{T} \Lambda_n^{(1)} \mu_n^{(1)} \right) \\
&= b_0 + \frac{1}{2} \left( y_1^\mathrm{T} P_1 y_1 + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - {\mu_n^{(1)}}^\mathrm{T} \Lambda_n^{(1)} \mu_n^{(1)} \right) \; .
\end{split}
$$

These are the prior hyperparameters before seeing the second data set:

$$ \label{eq:GLM-NG-S-prior-y2}
\begin{split}
\mu_0^{(2)} &= \mu_n^{(1)} \\
\Lambda_0^{(2)} &= \Lambda_n^{(1)} \\
a_0^{(2)} &= a_n^{(1)} \\
b_0^{(2)} &= b_n^{(1)} \; .
\end{split}
$$

Thus, we can again use \eqref{eq:GLM-NG-post-par} to calculate the posterior hyperparameters after seeing the second data set:

$$ \label{eq:GLM-NG-S-post-y2}
\begin{split}
\mu_n^{(2)} &= {\Lambda_n^{(2)}}^{-1} \left( X_2^\mathrm{T} P_2 y_2 + \Lambda_0^{(2)} \mu_0^{(2)} \right) \\
&= {\Lambda_n^{(2)}}^{-1} \left( X_2^\mathrm{T} P_2 y_2 + \Lambda_n^{(1)} {\Lambda_n^{(1)}}^{-1} \left( X_1^\mathrm{T} P_1 y_1 + \Lambda_0 \mu_0 \right) \right) \\
&= {\Lambda_n^{(2)}}^{-1} \left( X_1^\mathrm{T} P_1 y_1 + X_2^\mathrm{T} P_2 y_2 + \Lambda_0 \mu_0 \right) \\
\Lambda_n^{(2)} &= X_2^\mathrm{T} P_2 X_2 + \Lambda_0^{(2)} \\
&= X_2^\mathrm{T} P_2 X_2 + X_1^\mathrm{T} P_1 X_1 + \Lambda_0 \\
&= X_1^\mathrm{T} P_1 X_1 + X_2^\mathrm{T} P_2 X_2 + \Lambda_0 \\
a_n^{(2)} &= a_0^{(2)} + \frac{1}{2} n_2 \\
&= a_0 + \frac{1}{2} n_1 + \frac{1}{2} n_2 \\
&= a_0 + \frac{1}{2} \left( n_1 + n_2 \right) \\
b_n^{(2)} &= b_0^{(2)} + \frac{1}{2} \left( y_2^\mathrm{T} P_2 y_2 + {\mu_0^{(2)}}^\mathrm{T} \Lambda_0^{(2)} \mu_0^{(2)} - {\mu_n^{(2)}}^\mathrm{T} \Lambda_n^{(2)} \mu_n^{(2)} \right) \\
&= b_0 + \frac{1}{2} \left( y_1^\mathrm{T} P_1 y_1 + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - {\mu_n^{(1)}}^\mathrm{T} \Lambda_n^{(1)} \mu_n^{(1)} \right) + \frac{1}{2} \left( y_2^\mathrm{T} P_2 y_2 + {\mu_n^{(1)}}^\mathrm{T} \Lambda_n^{(1)} \mu_n^{(1)} - {\mu_n^{(2)}}^\mathrm{T} \Lambda_n^{(2)} \mu_n^{(2)} \right) \\
&= b_0 + \frac{1}{2} \left( y_1^\mathrm{T} P_1 y_1 + y_2^\mathrm{T} P_2 y_2 + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - {\mu_n^{(2)}}^\mathrm{T} \Lambda_n^{(2)} \mu_n^{(2)} \right) \; .
\end{split}
$$

These are the prior hyperparameters before seeing the third data set:

$$ \label{eq:GLM-NG-S-prior-y3}
\begin{split}
\mu_0^{(3)} &= \mu_n^{(2)} \\
\Lambda_0^{(3)} &= \Lambda_n^{(2)} \\
a_0^{(3)} &= a_n^{(2)} \\
b_0^{(3)} &= b_n^{(2)} \; .
\end{split}
$$

Generalizing this, we have after observing the $j$-th data set:

$$ \label{eq:GLM-NG-S-post-yi}
\begin{split}
\mu_n^{(j)} &= {\Lambda_n^{(j)}}^{-1} \left( \sum_{i=1}^j X_i^\mathrm{T} P_i y_i + \Lambda_0 \mu_0 \right) \\
\Lambda_n^{(j)} &= \sum_{i=1}^j X_i^\mathrm{T} P_i X_i + \Lambda_0 \\
a_n^{(j)} &= a_0 + \frac{1}{2} \sum_{i=1}^j n_i \\
b_n^{(j)} &= b_0 + \frac{1}{2} \left( \sum_{i=1}^j y_i^\mathrm{T} P_i y_i + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - {\mu_n^{(j)}}^\mathrm{T} \Lambda_n^{(j)} \mu_n^{(j)} \right) \; .
\end{split}
$$

Plugging in $j = S$, we obtain the final posterior distribution:

$$ \label{eq:GLM-NG-S-post-par-qed}
\begin{split}
\mu_n = \mu_n^{(S)} &= {\Lambda_n^{(S)}}^{-1} \left( \sum_{i=1}^S X_i^\mathrm{T} P_i y_i + \Lambda_0 \mu_0 \right) = \Lambda_n^{-1} \left( \sum_{i=1}^S X_i^\mathrm{T} P_i y_i + \Lambda_0 \mu_0 \right) \\
\Lambda_n = \Lambda_n^{(S)} &= \sum_{i=1}^S X_i^\mathrm{T} P_i X_i + \Lambda_0 \\
a_n = a_n^{(S)} &= a_0 + \frac{1}{2} \sum_{i=1}^S n_i \\
b_n = b_n^{(S)} &= b_0 + \frac{1}{2} \left( \sum_{i=1}^S y_i^\mathrm{T} P_i y_i + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - {\mu_n^{(S)}}^\mathrm{T} \Lambda_n^{(S)} \mu_n^{(S)} \right) \\
&= b_0 + \frac{1}{2} \left( \sum_{i=1}^S y_i^\mathrm{T} P_i y_i + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n \right) \; .
\end{split}
$$

This result is also compatible with the [general theorem about combined posterior distributions in terms of individual posterior distributions](/P/post-ind) when analyzing independent data sets.