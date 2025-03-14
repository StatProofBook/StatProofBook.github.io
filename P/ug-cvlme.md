---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-03-06 16:43:00

title: "Cross-validated log model evidence for the univariate Gaussian"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian"
theorem: "Cross-validated log model evidence"

sources:

proof_id: "P490"
shortcut: "ug-cvlme"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:UG}
y = \left\lbrace y_1, \ldots, y_n \right\rbrace, \quad y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n
$$

be a [univariate Gaussian data set](/D/ug) with unknown mean $\mu$ and unknown variance $\sigma^2$. Moreover, assume two [statistical models](/D/fpm), one assuming that $\mu$ is zero ([null model](/D/h0)), the other imposing a [normal distribution](/P/ug-prior) as the [prior distribution](/D/prior) on the [mean parameter](/D/mean) $\mu$ ([alternative](/D/h1)) and both imposing a [gamma distribtion](/P/ug-prior) on the [precision parameter](/D/prec) $\tau = 1/\sigma^2$:

$$ \label{eq:UG-m01}
\begin{split}
m_0 &: \; y_i \sim \mathcal{N}(\mu, \tau^{-1}), \; \mu = 0, \; \tau \sim \mathrm{Gam}(a_0, b_0) \\
m_1 &: \; y_i \sim \mathcal{N}(\mu, \tau^{-1}), \; \mu|\tau \sim \mathcal{N}(\mu_0, (\tau \lambda_0)^{-1}), \; \tau \sim \mathrm{Gam}(a_0, b_0)
\end{split}
$$

Then, the [cross-validated log model evidences](/D/cvlme) of $m_0$ and $m_1$ are

$$ \label{eq:UG-cvLME-m01}
\begin{split}
  \mathrm{cvLME}(m_0)
= & - \frac{n}{2} \log (2 \pi) + S \cdot \log \Gamma \left( \frac{n}{2} \right) - S \cdot \log \Gamma \left( \frac{1}{2} \frac{S-1}{S} n \right) \\
  &- \frac{S \cdot n}{2} \log \left[ \frac{1}{2} \left( y^\mathrm{T} y \right) \right] + \frac{n_1}{2} \sum_{i=1}^S \log \left[ \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} \right) \right] \\
  \mathrm{cvLME}(m_1)
= & - \frac{n}{2} \log (2 \pi) + \frac{S}{2} \log \left( \frac{S-1}{S} \right) + S \cdot \log \Gamma \left( \frac{n}{2} \right) - S \cdot \log \Gamma \left( \frac{1}{2} \frac{S-1}{S} n \right) \\
  &- \frac{S \cdot n}{2} \log \left[ \frac{1}{2} \left( y^\mathrm{T} y - n {\bar{y}}^2 \right) \right] + \frac{n_1}{2} \sum_{i=1}^S \log \left[ \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} - n_1 \bar{y}_1^{(i)} \right) \right]
\end{split}
$$

where $\bar{y}$ is the [sample mean](/D/mean-samp), $y_1^{(i)}$ are the training data in the $i$-th cross-validation fold with $n_1$ data points and $S$ is the [number of data subsets](/D/cvlme).


**Proof:** For evaluation of the [cross-validated log model evidences](/D/cvlme) (cvLME), we assume that $n$ data points are divided into $S \mid n$ data subsets without remainder. Then, the number of training data points $n_1$ and test data points $n_2$ are given by

$$ \label{eq:CV-n12}
\begin{split}
n   &= n_1 + n_2 \\
n_1 &= \frac{S-1}{S} n \\
n_2 &= \frac{1}{S} n \; ,
\end{split}
$$

such that training data $y_1$ and test data $y_2$ in the $i$-th cross-validation fold are

$$ \label{eq:CV-y12}
\begin{split}
y         &= \left\lbrace y_1, \ldots, y_n \right\rbrace \\
y_1^{(i)} &= \left\lbrace x \in y \mid x \notin y_2^{(i)} \right\rbrace = y \backslash y_2^{(i)} \\
y_2^{(i)} &= \left\lbrace y_{(i-1) \cdot n_2 + 1}, \ldots, y_{i \cdot n_2} \right\rbrace \; .
\end{split}
$$

<br>
First, we have a look at the alternative $m_1$ assuming $\mu \neq 0$. To begin, the training data $y_1^{(i)}$ are analyzed [using a non-informative prior distribution](/D/prior-inf) and applying the [posterior distribution for the univariate Gaussian](/P/ug-post):

$$ \label{eq:UG-m1-y1}
\begin{split}
\mu_0^{(1)} &= 0 \quad \Rightarrow \quad
\mu_n^{(1)}  = \frac{\lambda_0^{(1)} \mu_0^{(1)} + n_1 \bar{y}_1^{(i)}}{\lambda_0^{(1)} + n_1} = \bar{y}_1^{(i)} \\
\lambda_0^{(1)} &= 0 \quad \Rightarrow \quad
\lambda_n^{(1)}  = \lambda_0^{(1)} + n_1 = n_1 \\
a_0^{(1)} &= 0 \quad \Rightarrow \quad
a_n^{(1)}  = a_0^{(1)} + \frac{n_1}{2} = \frac{n_1}{2} \\
b_0^{(1)} &= 0 \quad \Rightarrow \quad
b_n^{(1)}  = b_0^{(1)} + \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} + \lambda_0^{(1)} {\mu_0^{(1)}}^2 - \lambda_n^{(1)} {\mu_n^{(1)}}^2 \right) = \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} - n_1 \left( \bar{y}_1^{(i)} \right)^2 \right) \; .
\end{split}
$$

This results in a posterior characterized by $\mu_n^{(1)}$, $\lambda_n^{(1)}$, $a_n^{(1)}$ and $b_n^{(1)}$. Then, the test data $y_2^{(i)}$ are analyzed using this posterior [as an informative prior distribution](/D/prior-inf), again applying the [posterior distribution for the univariate Gaussian](/P/ug-post):

$$ \label{eq:UG-m1-y2}
\begin{split}
\mu_0^{(2)} &= \mu_n^{(1)} = \bar{y}_1^{(i)} \\
\Rightarrow \quad \mu_n^{(2)} &= \frac{\lambda_0^{(2)} \mu_0^{(2)} + n_2 \bar{y}_2^{(i)}}{\lambda_0^{(2)} + n_2} \\
&= \frac{n_1 \bar{y}_1^{(i)} + n_2 \bar{y}_2^{(i)}}{n_1 + n_2} = \frac{n \bar{y}}{n} = \bar{y} \\
\lambda_0^{(2)} &= \lambda_n^{(1)} = n_1 \\
\Rightarrow \quad \lambda_n^{(2)} &= \lambda_0^{(2)} + n_2 = n_1 + n_2 = n \\
a_0^{(2)} &= a_n^{(1)} = \frac{n_1}{2} \\
\Rightarrow \quad a_n^{(2)}  &= a_0^{(2)} + \frac{n_2}{2} = \frac{n_1}{2} + \frac{n_2}{2} = \frac{n}{2} \\
b_0^{(2)} &= b_n^{(1)} = \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} - n_1 \bar{y}_1^{(i)} \right) \\
\Rightarrow \quad b_n^{(2)} &= b_0^{(2)} + \frac{1}{2} \left( {y_2^{(i)}}^\mathrm{T} y_2^{(i)} + \lambda_0^{(2)} {\mu_0^{(2)}}^2 - \lambda_n^{(2)} {\mu_n^{(2)}}^2 \right) \\
&= \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} - n_1 \left( \bar{y}_1^{(i)} \right)^2 \right) + \frac{1}{2} \left( {y_2^{(i)}}^\mathrm{T} y_2^{(i)} + n_1 \left( \bar{y}_1^{(i)} \right)^2 - n {\bar{y}}^2 \right) \\
&= \frac{1}{2} \left( y^\mathrm{T} y - n {\bar{y}}^2 \right) \; .
\end{split}
$$

In the test data, we now have a prior characterized by $\mu_0^{(2)}$, $\lambda_0^{(2)}$, $a_0^{(2)}$ and $b_0^{(2)}$ and a posterior characterized $\mu_n^{(2)}$, $\lambda_n^{(2)}$, $a_n^{(2)}$ and $b_n^{(2)}$. Applying the [log model evidence for the univariate Gaussian](/P/ug-lme), the [out-of-sample log model evidence](/D/cvlme) (oosLME) therefore follows as

$$ \label{eq:UG-m1-oosLME}
\begin{split}
  \mathrm{oosLME}_i(m_1) =
  &- \frac{n_2}{2} \log (2 \pi) + \frac{1}{2} \log \frac{\lambda_0^{(2)}}{\lambda_n^{(2)}} + \log \Gamma \left( a_n^{(2)} \right) - \log \Gamma \left( a_0^{(2)} \right) \\
  &+ a_0^{(2)} \log b_0^{(2)} - a_n^{(2)} \log b_n^{(2)} \\
= &- \frac{n_2}{2} \log (2 \pi) + \frac{1}{2} \log \left( \frac{n_1}{n} \right) + \log \Gamma \left( \frac{n}{2} \right) - \log \Gamma \left( \frac{n_1}{2} \right) \\
  &+ \frac{n_1}{2} \log \left[ \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} - n_1 \bar{y}_1^{(i)} \right) \right] - \frac{n}{2} \log \left[ \frac{1}{2} \left( y^\mathrm{T} y - n {\bar{y}}^2 \right) \right] \\
= &- \frac{n}{2S} \log (2 \pi) + \frac{1}{2} \log \left( \frac{S-1}{S} \right) + \log \Gamma \left( \frac{n}{2} \right) - \log \Gamma \left( \frac{(S-1)n}{2S} \right) \\
  &+ \frac{(S-1)n}{2S} \log \left[ \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} - n_1 \bar{y}_1^{(i)} \right) \right] - \frac{n}{2} \log \left[ \frac{1}{2} \left( y^\mathrm{T} y - n {\bar{y}}^2 \right) \right] \; .
\end{split}
$$

By definition, [the cross-validated log model evidence is the sum of out-of-sample log model evidences](/D/cvlme) over cross-validation folds, such that the cvLME of $m_1$ is:

$$ \label{eq:UG-m1-cvLME}
\begin{split}
  \mathrm{cvLME}(m_1) =
  &\sum_{i=1}^S \mathrm{oosLME}_i(m_1) \\
= &\sum_{i=1}^S \left( - \frac{n}{2S} \log (2 \pi) + \frac{1}{2} \log \left( \frac{S-1}{S} \right) + \log \Gamma \left( \frac{n}{2} \right) - \log \Gamma \left( \frac{(S-1)n}{2S} \right) \right. \\
  &+ \left. \frac{(S-1)n}{2S} \log \left[ \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} - n_1 \bar{y}_1^{(i)} \right) \right] - \frac{n}{2} \log \left[ \frac{1}{2} \left( y^\mathrm{T} y - n {\bar{y}}^2 \right) \right] \right) \\
= & - \frac{n}{2} \log (2 \pi) + \frac{S}{2} \log \left( \frac{S-1}{S} \right) + S \cdot \log \Gamma \left( \frac{n}{2} \right) - S \cdot \log \Gamma \left( \frac{1}{2} \frac{S-1}{S} n \right) \\
  &- \frac{S \cdot n}{2} \log \left[ \frac{1}{2} \left( y^\mathrm{T} y - n {\bar{y}}^2 \right) \right] + \frac{n_1}{2} \sum_{i=1}^S \log \left[ \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} - n_1 \bar{y}_1^{(i)} \right) \right] \; .
\end{split}
$$

<br>
Next, we consider the null model $m_0$ assuming $\mu = 0$. Because this model has no parameter for $\mu$, there are no hyperparameters $\mu_0$ and $\lambda_0$, but only hyperparameters $a_0$ and $b_0$ for the parameter $\tau$. In the first step, the training data $y_1^{(i)}$ are analyzed [using a non-informative prior distribution](/D/prior-inf) and applying the [posterior distribution for the univariate Gaussian](/P/ug-post):

$$ \label{eq:UG-m0-y1}
\begin{split}
a_0^{(1)} &= 0 \quad \Rightarrow \quad
a_n^{(1)}  = a_0^{(1)} + \frac{n_1}{2} = \frac{n_1}{2} \\
b_0^{(1)} &= 0 \quad \Rightarrow \quad
b_n^{(1)}  = b_0^{(1)} + \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} \right) = \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} \right) \; .
\end{split}
$$

In the second step, the test data $y_2^{(i)}$ are analyzed using this posterior [as an informative prior distribution](/D/prior-inf), again applying the [posterior distribution for the univariate Gaussian](/P/ug-post):

$$ \label{eq:UG-m0-y2}
\begin{split}
a_0^{(2)} &= a_n^{(1)} = \frac{n_1}{2} \\
\Rightarrow \quad a_n^{(2)}  &= a_0^{(2)} + \frac{n_2}{2} = \frac{n_1}{2} + \frac{n_2}{2} = \frac{n}{2} \\
b_0^{(2)} &= b_n^{(1)} = \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} \right) \\
\Rightarrow \quad b_n^{(2)} &= b_0^{(2)} + \frac{1}{2} \left( {y_2^{(i)}}^\mathrm{T} y_2^{(i)} \right) = \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} \right) + \frac{1}{2} \left( {y_2^{(i)}}^\mathrm{T} y_2^{(i)} \right) = \frac{1}{2} \left( y^\mathrm{T} y \right) \; .
\end{split}
$$

In the test data, we now have a prior characterized by $a_0^{(2)}$ and $b_0^{(2)}$ and a posterior characterized $a_n^{(2)}$ and $b_n^{(2)}$. Applying the [log model evidence for the univariate Gaussian](/P/ug-lme), the [out-of-sample log model evidence](/D/cvlme) (oosLME) therefore follows as

$$ \label{eq:UG-m0-oosLME}
\begin{split}
  \mathrm{oosLME}_i(m_1) =
  &- \frac{n_2}{2} \log (2 \pi) + \log \Gamma \left( a_n^{(2)} \right) - \log \Gamma \left( a_0^{(2)} \right) \\
  &+ a_0^{(2)} \log b_0^{(2)} - a_n^{(2)} \log b_n^{(2)} \\
= &- \frac{n_2}{2} \log (2 \pi) + \log \Gamma \left( \frac{n}{2} \right) - \log \Gamma \left( \frac{n_1}{2} \right) \\
  &+ \frac{n_1}{2} \log \left[ \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} \right) \right] - \frac{n}{2} \log \left[ \frac{1}{2} \left( y^\mathrm{T} y \right) \right] \\
= &- \frac{n}{2S} \log (2 \pi) + \log \Gamma \left( \frac{n}{2} \right) - \log \Gamma \left( \frac{(S-1)n}{2S} \right) \\
  &+ \frac{(S-1)n}{2S} \log \left[ \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} \right) \right] - \frac{n}{2} \log \left[ \frac{1}{2} \left( y^\mathrm{T} y \right) \right] \; .
\end{split}
$$

Again, because [the cross-validated log model evidence is the sum of out-of-sample log model evidences](/D/cvlme) over cross-validation folds, the cvLME of $m_0$ becomes:

$$ \label{eq:UG-m0-cvLME}
\begin{split}
  \mathrm{cvLME}(m_0) =
  &\sum_{i=1}^S \mathrm{oosLME}_i(m_0) \\
= &\sum_{i=1}^S \left( - \frac{n}{2S} \log (2 \pi) + \log \Gamma \left( \frac{n}{2} \right) - \log \Gamma \left( \frac{(S-1)n}{2S} \right) \right. \\
  &+ \left. \frac{(S-1)n}{2S} \log \left[ \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} \right) \right] - \frac{n}{2} \log \left[ \frac{1}{2} \left( y^\mathrm{T} y \right) \right] \right) \\
= & - \frac{n}{2} \log (2 \pi) + S \cdot \log \Gamma \left( \frac{n}{2} \right) - S \cdot \log \Gamma \left( \frac{1}{2} \frac{S-1}{S} n \right) \\
  &- \frac{S \cdot n}{2} \log \left[ \frac{1}{2} \left( y^\mathrm{T} y \right) \right] + \frac{n_1}{2} \sum_{i=1}^S \log \left[ \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} \right) \right] \; .
\end{split}
$$

Together, \eqref{eq:UG-m0-cvLME} and \eqref{eq:UG-m1-cvLME} conform to the results given in \eqref{eq:UG-cvLME-m01}.