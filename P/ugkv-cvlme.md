---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-24 10:57:00

title: "Cross-validated log model evidence for the univariate Gaussian with known variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian with known variance"
theorem: "Cross-validated log model evidence"

sources:

proof_id: "P217"
shortcut: "ugkv-cvlme"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:ugkv}
y = \left\lbrace y_1, \ldots, y_n \right\rbrace, \quad y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n
$$

be a [univariate Gaussian data set](/D/ugkv) with unknown mean $\mu$ and known variance $\sigma^2$. Moreover, assume two [statistical models](/D/fpm), one assuming that $\mu$ is zero ([null model](/D/h0)), the other imposing a [normal distribution](/P/ugkv-prior) as the [prior distribution](/D/prior) on the model parameter $\mu$ ([alternative](/D/h1)):

$$\label{eq:UGkv-m01}
\begin{split}
m_0&: \; y_i \sim \mathcal{N}(\mu, \sigma^2), \; \mu = 0 \\
m_1&: \; y_i \sim \mathcal{N}(\mu, \sigma^2), \; \mu \sim \mathcal{N}(\mu_0, \lambda_0^{-1}) \; .
\end{split}
$$

Then, the [cross-validated log model evidences](/D/cvlme) of $m_0$ and $m_1$ are

$$ \label{eq:UGkv-cvLME-m01}
\begin{split}
\mathrm{cvLME}(m_0) &= \frac{n}{2} \log\left( \frac{\tau}{2 \pi} \right) - \frac{1}{2} \left( \tau y^\mathrm{T} y \right) \\
\mathrm{cvLME}(m_1) &= \frac{n}{2} \log \left( \frac{\tau}{2 \pi} \right) + \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{\tau}{2} \left[ y^\mathrm{T} y + \sum_{i=1}^S \left( \frac{\left(n_1 \bar{y}_1^{(i)}\right)^2}{n_1} - \frac{(n \bar{y})^2}{n} \right) \right]
\end{split}
$$

where $\bar{y}$ is the [sample mean](/D/mean-samp), $\tau = 1/\sigma^2$ is the [inverse variance or precision](/D/prec), $y_1^{(i)}$ are the training data in the $i$-th cross-validation fold and $S$ is the [number of data subsets](/D/cvlme).


**Proof:** For evaluation of the [cross-validated log model evidences](/D/cvlme) (cvLME), we assume that $n$ data points are divided into $S \mid n$ data subsets without remainder. Then, the number of training data points $n_1$ and test data points $n_2$ are given by

$$ \label{eq:CV-n12}
\begin{split}
n &= n_1 + n_2 \\
n_1 &= \frac{S-1}{S} n \\
n_2 &= \frac{1}{S} n \; ,
\end{split}
$$

such that training data $y_1$ and test data $y_2$ in the $i$-th cross-validation fold are

$$ \label{eq:CV-y12}
\begin{split}
y &= \left\lbrace y_1, \ldots, y_n \right\rbrace \\
y_1^{(i)} &= \left\lbrace x \in y \mid x \notin y_2^{(i)} \right\rbrace = y \backslash y_2^{(i)} \\
y_2^{(i)} &= \left\lbrace y_{(i-1) \cdot n_2 + 1}, \ldots, y_{i \cdot n_2} \right\rbrace \; .
\end{split}
$$

<br>
First, we consider the null model $m_0$ assuming $\mu = 0$. Because this model has no free parameter, nothing is estimated from the training data and the assumed parameter value is applied to the test data. Consequently, the [out-of-sample log model evidence](/D/ooslme) (oosLME) is equal to the [log-likelihood function](/P/ugkv-mle) of the test data at $\mu = 0$:

$$ \label{eq:UGkv-m0-oosLME}
\mathrm{oosLME}_i(m_0) = \log p\left( \left. y_2^{(i)} \right| \mu=0 \right) = \frac{n_2}{2} \log \left( \frac{\tau}{2 \pi} \right) - \frac{1}{2} \left[ \tau {y_2^{(i)}}^\mathrm{T} y_2^{(i)} \right] \; .
$$

By definition, [the cross-validated log model evidence is the sum of out-of-sample log model evidences](/D/cvlme) over cross-validation folds, such that the cvLME of $m_0$ is:

$$ \label{eq:UGkv-m0-cvLME}
\begin{split}
\mathrm{cvLME}(m_0) &= \sum_{i=1}^S \mathrm{oosLME}_i(m_0) \\
&= \sum_{i=1}^S \left( \frac{n_2}{2} \log \left( \frac{\tau}{2 \pi} \right) - \frac{1}{2} \left[ \tau {y_2^{(i)}}^\mathrm{T} y_2^{(i)} \right] \right) \\
&= \frac{n}{2} \log \left( \frac{\tau}{2 \pi} \right) - \frac{1}{2} \left[ \tau y^\mathrm{T} y \right] \; .
\end{split}
$$

<br>
Next, we have a look at the alternative $m_1$ assuming $\mu \neq 0$. First, the training data $y_1^{(i)}$ are analyzed [using a non-informative prior distribution](/D/prior-inf) and applying the [posterior distribution for the univariate Gaussian with known variance](/P/ugkv-post):

$$ \label{eq:UGkv-m1-y1}
\begin{split}
\mu_0^{(1)} &= 0 \\
\lambda_0^{(1)} &= 0 \\
\mu_n^{(1)} &= \frac{\tau n_1 \bar{y}_1^{(i)} + \lambda_0^{(1)} \mu_0^{(1)}}{\tau n_1 + \lambda_0^{(1)}} = \bar{y}_1^{(i)} \\
\lambda_n^{(1)} &= \tau n_1 + \lambda_0^{(1)} = \tau n_1 \; .
\end{split}
$$

This results in a posterior characterized by $\mu_n^{(1)}$ and $\lambda_n^{(1)}$. Then, the test data $y_2^{(i)}$ are analyzed using this posterior [as an informative prior distribution](/D/prior-inf), again applying the [posterior distribution for the univariate Gaussian with known variance](/P/ugkv-post):

$$ \label{eq:UGkv-m1-y2}
\begin{split}
\mu_0^{(2)} &= \mu_n^{(1)} = \bar{y}_1^{(i)} \\
\lambda_0^{(2)} &= \lambda_n^{(1)} = \tau n_1 \\
\mu_n^{(2)} &= \frac{\tau n_2 \bar{y}_2^{(i)} + \lambda_0^{(2)} \mu_0^{(2)}}{\tau n_2 + \lambda_0^{(2)}} = \bar{y} \\
\lambda_n^{(2)} &= \tau n_2 + \lambda_0^{(2)} = \tau n \; .
\end{split}
$$

In the test data, we now have a prior characterized by $\mu_0^{(2)}$/$\lambda_0^{(2)}$ and a posterior characterized $\mu_n^{(2)}$/$\lambda_n^{(2)}$. Applying the [log model evidence for the univariate Gaussian with known variance](/P/ugkv-lme), the [out-of-sample log model evidence](/D/ooslme) (oosLME) therefore follows as

$$ \label{eq:UGkv-m1-oosLME}
\begin{split}
\mathrm{oosLME}_i(m_1) &= \frac{n_2}{2} \log \left( \frac{\tau}{2 \pi} \right) + \frac{1}{2} \log \left( \frac{\lambda_0^{(2)}}{\lambda_n^{(2)}} \right) - \frac{1}{2} \left[ \tau {y_2^{(i)}}^\mathrm{T} y_2^{(i)} + \lambda_0^{(2)} {\mu_0^{(2)}}^2 - \lambda_n^{(2)} {\mu_n^{(2)}}^2 \right] \\
&= \frac{n_2}{2} \log \left( \frac{\tau}{2 \pi} \right) + \frac{1}{2} \log \left( \frac{n_1}{n} \right) - \frac{1}{2} \left[ \tau {y_2^{(i)}}^\mathrm{T} y_2^{(i)} + \frac{\tau}{n_1}\left(n_1 \bar{y}_1^{(i)}\right)^2 - \frac{\tau}{n}(n \bar{y})^2 \right] \; .
\end{split}
$$

Again, because [the cross-validated log model evidence is the sum of out-of-sample log model evidences](/D/cvlme) over cross-validation folds, the cvLME of $m_1$ becomes:

$$ \label{eq:UGkv-m1-cvLME}
\begin{split}
\mathrm{cvLME}(m_1) &= \sum_{i=1}^S \mathrm{oosLME}_i(m_1) \\
&= \sum_{i=1}^S \left( \frac{n_2}{2} \log \left( \frac{\tau}{2 \pi} \right) + \frac{1}{2} \log \left( \frac{n_1}{n} \right) - \frac{1}{2} \left[ \tau {y_2^{(i)}}^\mathrm{T} y_2^{(i)} + \frac{\tau}{n_1}\left(n_1 \bar{y}_1^{(i)}\right)^2 - \frac{\tau}{n}(n \bar{y})^2 \right] \right) \\
&= \frac{S \cdot n_2}{2} \log \left( \frac{\tau}{2 \pi} \right) + \frac{S}{2} \log \left( \frac{n_1}{n} \right) - \frac{\tau}{2} \sum_{i=1}^S \left[ {y_2^{(i)}}^\mathrm{T} y_2^{(i)} + \frac{\left(n_1 \bar{y}_1^{(i)}\right)^2}{n_1} - \frac{(n \bar{y})^2}{n} \right] \\
&= \frac{n}{2} \log \left( \frac{\tau}{2 \pi} \right) + \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{\tau}{2} \left[ y^\mathrm{T} y + \sum_{i=1}^S \left( \frac{\left(n_1 \bar{y}_1^{(i)}\right)^2}{n_1} - \frac{(n \bar{y})^2}{n} \right) \right] \; .
\end{split}
$$

Together, \eqref{eq:UGkv-m0-cvLME} and \eqref{eq:UGkv-m1-cvLME} conform to the results given in \eqref{eq:UGkv-cvLME-m01}.