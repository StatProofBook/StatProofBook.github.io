---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-03-07 03:51:00

title: "Cross-validated log model evidence for multinomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Multinomial observations"
theorem: "Cross-validated log model evidence"

sources:

proof_id: "P493"
shortcut: "mult-cvlme"
username: "JoramSoch"
---


**Theorem:** Let $y = [y_1, \ldots, y_k] \in \mathbb{N}_0^{1 \times k}$ be the number of observations in $k$ categories resulting from $n$ independent trials with unknown category probabilities $p = [p_1, \ldots, p_k]$, such that $y$ follows a [multinomial distribution](/D/mult):

$$ \label{eq:Mult}
y \sim \mathrm{Mult}(n,p) \; .
$$

Moreover, assume two [statistical models](/D/fpm), one assuming that each $p_j$ is $1/k$ ([null model](/D/h0)), the other imposing a [Dirichlet distribution](/P/mult-prior) as the [prior distribution](/D/prior) on the model parameters $p_1, \ldots, p_k$ ([alternative](/D/h1)):

$$ \label{eq:Mult-m01}
\begin{split}
m_0 &: \; y \sim \mathrm{Mult}(n,p), \; p = [1/k, \ldots, 1/k] \\
m_1 &: \; y \sim \mathrm{Mult}(n,p), \; p \sim \mathrm{Dir}(\alpha_0) \; .
\end{split}
$$

Then, the [cross-validated log model evidences](/D/cvlme) of $m_0$ and $m_1$ are

$$ \label{eq:Mult-cvLME-m01}
\begin{split}
\mathrm{cvLME}(m_0) &= -n \log(k) + \sum_{i=1}^S \left[ \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} \right] \\
\mathrm{cvLME}(m_1) &= S \cdot \log \frac{\Gamma(n_1)}{\Gamma(y)} + \sum_{i=1}^S \left[ \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} - \sum_{j=1}^k \log \left( \frac{y_{1j}^{(i)}}{y_j} \right) \right] \; .
\end{split}
$$

where $y_1^{(i)}$ and $y_2^{(i)}$ are the training and test data, respectively, in the $i$-th cross-validation fold with $n_1$ and $n_2$ data points, respectively, $S$ is the [number of data subsets](/D/cvlme) and $\Gamma(x)$ is the gamma function.


**Proof:** For evaluation of the [cross-validated log model evidences](/D/cvlme) (cvLME), we assume that $n$ data points are divided into $S \mid n$ data subsets without remainder. Then, the number of training data points $n_1$ and test data points $n_2$ are given by

$$ \label{eq:CV-n12}
\begin{split}
n   &= n_1 + n_2 \\
n_1 &= \frac{S-1}{S} n \\
n_2 &= \frac{1}{S} n \; ,
\end{split}
$$

such that $y_1^{(i)}$ are the [number of category observations](/D/mult) from the $n_1$ [trials of the training set](/D/mult-data) and $y_2^{(i)}$ is the [number of category observations](/D/mult) from the $n_2$ [trials of the test set](/D/mult-data) in the $i$-th cross-validation fold and it holds that

$$ \label{eq:CV-y12}
y = y_1^{(i)} + y_2^{(i)}
$$

as well as

$$ \label{eq:CV-ny12}
\begin{split}
n   &= \sum_{j=1}^{k} y_j \\
n_1 &= \sum_{j=1}^{k} y_{1j}^{(i)} \\
n_2 &= \sum_{j=1}^{k} y_{2j}^{(i)} \; .
\end{split}
$$

<br>
First, we consider the null model $m_0$ assuming $p_j = 1/k$ for each $j = 1,\ldots,k$. Because this model has no free parameter, nothing is estimated from the training data and the assumed parameter value is applied to the test data. Consequently, the [out-of-sample log model evidence](/D/cvlme) (oosLME) is equal to the [log-likelihood function](/P/mult-mle) of the test data at $p = [1/k, \ldots, 1/k]$:

$$ \label{eq:Mult-m0-oosLME}
\begin{split}
   \mathrm{oosLME}_i(m_0)
&= \log \mathrm{p}\left( \left. y_2^{(i)} \right| p = [1/k, \ldots, 1/k] \right) \\
&= \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} + \sum_{j=1}^{k} y_{2j}^{(i)} \log (1/k) \\
&= \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} + n_2 \log \frac{1}{k} \; .
\end{split}
$$

By definition, [the cross-validated log model evidence is the sum of out-of-sample log model evidences](/D/cvlme) over cross-validation folds, such that the cvLME of $m_0$ is:

$$ \label{eq:Mult-m0-cvLME}
\begin{split}
   \mathrm{cvLME}(m_0)
&= \sum_{i=1}^S \mathrm{oosLME}_i(m_0) \\
&= \sum_{i=1}^S \left[ \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} + n_2 \log \left( \frac{1}{k} \right) \right] \\
&= S \cdot n_2 \log \left( \frac{1}{k} \right) + \sum_{i=1}^S \left[ \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} \right] \\
&= -n \log(k) + \sum_{i=1}^S \left[ \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} \right] \; .
\end{split}
$$

<br>
Next, we have a look at the alternative $m_1$ assuming $p_j = 1/k$ for at least one $j = 1,\ldots,k$. First, the training data $y_1^{(i)}$ are analyzed [using a non-informative prior distribution](/D/prior-inf) and applying the [posterior distribution for multinomial observations](/P/mult-post):

$$ \label{eq:Mult-m1-y1}
\alpha_0^{(1)} = 0_{1k} \quad \Rightarrow \quad
\alpha_n^{(1)} = \alpha_0^{(1)} + y_1^{(i)} = y_1^{(i)} \; .
$$

This results in a posterior characterized by $\alpha_n^{(1)}$. Then, the test data $y_2^{(i)}$ are analyzed using this posterior [as an informative prior distribution](/D/prior-inf), again applying the [posterior distribution for multinomial observations](/P/mult-post):

$$ \label{eq:Mult-m1-y2}
\begin{split}
\alpha_0^{(2)} = \alpha_n^{(1)} = y_1^{(i)} \quad \Rightarrow \quad
\alpha_n^{(2)} = \alpha_0^{(2)} + y_2^{(i)} = y \; .
\end{split}
$$

In the test data, we now have a prior characterized by $\alpha_0^{(2)}$ and a posterior characterized $\alpha_n^{(2)}$. Applying the [log model evidence for multinomial observations](/P/mult-lme), the [out-of-sample log model evidence](/D/cvlme) (oosLME) therefore follows as

$$ \label{eq:Mult-m1-oosLME}
\begin{split}
   \mathrm{oosLME}_i(m_1)
=&\; \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} + \log \Gamma \left( \sum_{j=1}^{k} \alpha_{0j}^{(2)} \right) - \log \Gamma \left( \sum_{j=1}^{k} \alpha_{nj}^{(2)} \right) \\
 &+  \sum_{j=1}^k \log \Gamma(\alpha_{nj}^{(2)}) - \sum_{j=1}^k \log \Gamma(\alpha_{0j}^{(2)}) \\
=&\; \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} + \log \Gamma \left( \sum_{j=1}^{k} y_{1j}^{(i)} \right) - \log \Gamma \left( \sum_{j=1}^{k} y_j \right) \\
 &+  \sum_{j=1}^k \log \Gamma \left( y_j \right) - \sum_{j=1}^k \log \Gamma \left( y_{1j}^{(i)} \right) \\
=&\; \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} + \log \frac{\Gamma(n_1)}{\Gamma(y)} - \sum_{j=1}^k \log \left( \frac{y_{1j}^{(i)}}{y_j} \right) \; .
\end{split}
$$

Again, because [the cross-validated log model evidence is the sum of out-of-sample log model evidences](/D/cvlme) over cross-validation folds, the cvLME of $m_1$ becomes:

$$ \label{eq:Mult-m1-cvLME}
\begin{split}
   \mathrm{cvLME}(m_1)
&= \sum_{i=1}^S \mathrm{oosLME}_i(m_1) \\
&= \sum_{i=1}^S \left[ \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} + \log \frac{\Gamma(n_1)}{\Gamma(y)} - \sum_{j=1}^k \log \left( \frac{y_{1j}^{(i)}}{y_j} \right) \right] \\
&= S \cdot \log \frac{\Gamma(n_1)}{\Gamma(y)} + \sum_{i=1}^S \left[ \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} - \sum_{j=1}^k \log \left( \frac{y_{1j}^{(i)}}{y_j} \right) \right] \; .
\end{split}
$$

Together, \eqref{eq:Mult-m0-cvLME} and \eqref{eq:Mult-m1-cvLME} conform to the results given in \eqref{eq:Mult-cvLME-m01}.