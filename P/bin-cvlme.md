---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-03-07 03:16:00

title: "Cross-validated log model evidence for binomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Binomial observations"
theorem: "Cross-validated log model evidence"

sources:

proof_id: "P492"
shortcut: "bin-cvlme"
username: "JoramSoch"
---


**Theorem:** Let $y$ be the number of successes resulting from $n$ independent trials with unknown success probability $p$, such that $y$ follows a binomial distribution:

$$ \label{eq:Bin}
y \sim \mathrm{Bin}(n,p) \; .
$$

Moreover, assume two [statistical models](/D/fpm), one assuming that $p$ is 0.5 ([null model](/D/h0)), the other imposing a [beta distribution](/P/bin-prior) as the [prior distribution](/D/prior) on the model parameter $p$ ([alternative](/D/h1)):

$$ \label{eq:Bin-m01}
\begin{split}
m_0 &: \; y \sim \mathrm{Bin}(n,p), \; p = 0.5 \\
m_1 &: \; y \sim \mathrm{Bin}(n,p), \; p \sim \mathrm{Bet}(\alpha_0, \beta_0) \; .
\end{split}
$$

Then, the [cross-validated log model evidences](/D/cvlme) of $m_0$ and $m_1$ are

$$ \label{eq:Bin-cvLME-m01}
\begin{split}
\mathrm{cvLME}(m_0) &= -n \log(2) + \sum_{i=1}^S \left[ \log {n_2 \choose y_2^{(i)}} \right] \\
\mathrm{cvLME}(m_1) &= S \cdot \log B(y, n-y) + \sum_{i=1}^S \left[ \log {n_2 \choose y_2^{(i)}} - \log B \left( y_1^{(i)}, n_1 - y_1^{(i)} \right) \right]
\end{split}
$$

where $y_1^{(i)}$ and $y_2^{(i)}$ are the training and test data, respectively, in the $i$-th cross-validation fold with $n_1$ and $n_2$ data points, respectively, $S$ is the [number of data subsets](/D/cvlme) and $B(x,y)$ is the beta function.


**Proof:** For evaluation of the [cross-validated log model evidences](/D/cvlme) (cvLME), we assume that $n$ data points are divided into $S \mid n$ data subsets without remainder. Then, the number of training data points $n_1$ and test data points $n_2$ are given by

$$ \label{eq:CV-n12}
\begin{split}
n   &= n_1 + n_2 \\
n_1 &= \frac{S-1}{S} n \\
n_2 &= \frac{1}{S} n \; ,
\end{split}
$$

such that $y_1^{(i)}$ is the [number of successes](/D/bin) from the $n_1$ [trials of the training set](/D/bin-data) and $y_2^{(i)}$ is the [number of successes](/D/bin) from the $n_2$ [trials of the test set](/D/bin-data) in the $i$-th cross-validation fold and it holds that

$$ \label{eq:CV-y12}
y = y_1^{(i)} + y_2^{(i)} \; .
$$

<br>
First, we consider the null model $m_0$ assuming $p = 0.5$. Because this model has no free parameter, nothing is estimated from the training data and the assumed parameter value is applied to the test data. Consequently, the [out-of-sample log model evidence](/D/cvlme) (oosLME) is equal to the [log-likelihood function](/P/bin-mle) of the test data at $p = 0.5$:

$$ \label{eq:Bin-m0-oosLME}
\begin{split}
   \mathrm{oosLME}_i(m_0)
&= \log \mathrm{p}\left( \left. y_2^{(i)} \right| p = 0.5 \right) \\
&= \log {n_2 \choose y_2^{(i)}} + y_2^{(i)} \log 0.5 + \left( n_2 - y_2^{(i)} \right) \log (1-0.5) \\
&= \log {n_2 \choose y_2^{(i)}} + n_2 \log \frac{1}{2} \; .
\end{split}
$$

By definition, [the cross-validated log model evidence is the sum of out-of-sample log model evidences](/D/cvlme) over cross-validation folds, such that the cvLME of $m_0$ is:

$$ \label{eq:Bin-m0-cvLME}
\begin{split}
   \mathrm{cvLME}(m_0)
&= \sum_{i=1}^S \mathrm{oosLME}_i(m_0) \\
&= \sum_{i=1}^S \left[ \log {n_2 \choose y_2^{(i)}} + n_2 \log \left( \frac{1}{2} \right) \right] \\
&= S \cdot n_2 \log \left( \frac{1}{2} \right) + \sum_{i=1}^S \left[ \log {n_2 \choose y_2^{(i)}} \right] \\
&= -n \log(2) + \sum_{i=1}^S \left[ \log {n_2 \choose y_2^{(i)}} \right] \; .
\end{split}
$$

<br>
Next, we have a look at the alternative $m_1$ assuming $p \neq 0.5$. First, the training data $y_1^{(i)}$ are analyzed [using a non-informative prior distribution](/D/prior-inf) and applying the [posterior distribution for binomial observations](/P/bin-post):

$$ \label{eq:Bin-m1-y1}
\begin{split}
\alpha_0^{(1)} = 0 \quad &\Rightarrow \quad
\alpha_n^{(1)} = \alpha_0^{(1)} + y_1^{(i)} = y_1^{(i)} \\
\beta_0^{(1)}  = 0 \quad &\Rightarrow \quad
\beta_n^{(1)}  = \beta_0^{(1)} + \left( n_1 - y_1^{(i)} \right) = n_1 - y_1^{(i)} \; .
\end{split}
$$

This results in a posterior characterized by $\alpha_n^{(1)}$ and $\beta_n^{(1)}$. Then, the test data $y_2^{(i)}$ are analyzed using this posterior [as an informative prior distribution](/D/prior-inf), again applying the [posterior distribution for binomial observations](/P/bin-post):

$$ \label{eq:Bin-m1-y2}
\begin{split}
\alpha_0^{(2)} = \alpha_n^{(1)} = y_1^{(i)} \quad &\Rightarrow \quad
\alpha_n^{(2)} = \alpha_0^{(2)} + y_2^{(i)} = y \\
\beta_0^{(2)}  = \beta_n^{(1)} = n_1 - y_1^{(i)} \quad &\Rightarrow \quad
\beta_n^{(2)}  = \beta_0^{(2)} + \left( n_2 - y_2^{(i)} \right) = n - y \; .
\end{split}
$$

In the test data, we now have a prior characterized by $\alpha_0^{(2)}$ and $\beta_0^{(2)}$ and a posterior characterized $\alpha_n^{(2)}$ and $\beta_n^{(2)}$. Applying the [log model evidence for binomial observations](/P/bin-lme), the [out-of-sample log model evidence](/D/cvlme) (oosLME) therefore follows as

$$ \label{eq:Bin-m1-oosLME}
\begin{split}
   \mathrm{oosLME}_i(m_1)
&= \log {n_2 \choose y_2^{(i)}} + \log B(\alpha_n^{(2)}, \beta_n^{(2)}) - \log B(\alpha_0^{(2)}, \beta_0^{(2)}) \\
&= \log {n_2 \choose y_2^{(i)}} + \log B(y, n-y) - \log B \left( y_1^{(i)}, n_1 - y_1^{(i)} \right) \; .
\end{split}
$$

Again, because [the cross-validated log model evidence is the sum of out-of-sample log model evidences](/D/cvlme) over cross-validation folds, the cvLME of $m_1$ becomes:

$$ \label{eq:Bin-m1-cvLME}
\begin{split}
\mathrm{cvLME}(m_1) &= \sum_{i=1}^S \mathrm{oosLME}_i(m_1) \\
&= \sum_{i=1}^S \left[ \log {n_2 \choose y_2^{(i)}} + \log B(y, n-y) - \log B \left( y_1^{(i)}, n_1 - y_1^{(i)} \right) \right] \\
&= S \cdot \log B(y, n-y) + \sum_{i=1}^S \left[ \log {n_2 \choose y_2^{(i)}} - \log B \left( y_1^{(i)}, n_1 - y_1^{(i)} \right) \right]
\end{split}
$$

Together, \eqref{eq:Bin-m0-cvLME} and \eqref{eq:Bin-m1-cvLME} conform to the results given in \eqref{eq:Bin-cvLME-m01}.