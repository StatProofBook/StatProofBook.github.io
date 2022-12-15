---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-02 17:47:00

title: "Log Bayes factor for multinomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Multinomial observations"
theorem: "Log Bayes factor"

sources:

proof_id: "P387"
shortcut: "mult-lbf"
username: "JoramSoch"
---


**Theorem:** Let $y = [y_1, \ldots, y_k]$ be the number of observations in $k$ categories resulting from $n$ independent trials with unknown category probabilities $p = [p_1, \ldots, p_k]$, such that $y$ follows a [multinomial distribution](/D/mult):

$$ \label{eq:Mult}
y \sim \mathrm{Mult}(n,p) \; .
$$

Moreover, assume two [statistical models](/D/fpm), one assuming that each $p_j$ is $1/k$ ([null model](/D/h0)), the other imposing a [Dirichlet distribution](/P/mult-prior) as the [prior distribution](/D/prior) on the model parameters $p_1, \ldots, p_k$ ([alternative](/D/h1)):

$$ \label{eq:Mult-m01}
\begin{split}
m_0&: \; y \sim \mathrm{Mult}(n,p), \; p = [1/k, \ldots, 1/k] \\
m_1&: \; y \sim \mathrm{Mult}(n,p), \; p \sim \mathrm{Dir}(\alpha_0) \; .
\end{split}
$$

Then, the [log Bayes factor](/D/lbf) in favor of $m_1$ against $m_0$ is

$$ \label{eq:Mult-LBF}
\begin{split}
\mathrm{LBF}_{10} &= \log \Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right) - \log \Gamma \left( \sum_{j=1}^{k} \alpha_{nj} \right) \\
&+ \sum_{j=1}^k \log \Gamma(\alpha_{nj}) - \sum_{j=1}^k \log \Gamma(\alpha_{0j}) - n \log \left( \frac{1}{k} \right)
\end{split}
$$

where $\Gamma(x)$ is the gamma function and $\alpha_n$ are the [posterior hyperparameters for multinomial observations](/P/mult-post) which are functions of the [numbers of observations](/D/mult) $y_1, \ldots, y_k$.


**Proof:** [The log Bayes factor is equal to the difference of two log model evidences](/P/lbf-lme):

$$ \label{eq:LBF-LME}
\mathrm{LBF}_{12} = \mathrm{LME}(m_1) - \mathrm{LME}(m_2) \; .
$$

The LME of the alternative $m_1$ is equal to the [log model evidence for multinomial observations](/P/mult-lme):

$$ \label{eq:Mult-LME-m1}
\begin{split}
\mathrm{LME}(m_1) = \log p(y|m_1) &= \log \Gamma(n+1) - \sum_{j=1}^{k} \log \Gamma(k_j+1) \\
&+ \log \Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right) - \log \Gamma \left( \sum_{j=1}^{k} \alpha_{nj} \right) \\
&+ \sum_{j=1}^k \log \Gamma(\alpha_{nj}) - \sum_{j=1}^k \log \Gamma(\alpha_{0j}) \; .
\end{split}
$$

Because the null model $m_0$ has no free parameter, its [log model evidence](/D/lme) (logarithmized [marginal likelihood](/D/ml)) is equal to the [log-likelihood function for multinomial observations](/P/mult-mle) at the value $p_0 = [1/k, \ldots, 1/k]$:

$$ \label{eq:Mult-LME-m0}
\begin{split}
\mathrm{LME}(m_0) = \log p(y|p = p_0) &= \log {n \choose {y_1, \ldots, y_k}} + \sum_{j=1}^{k} y_j \log \left( \frac{1}{k} \right) \\
&= \log {n \choose {y_1, \ldots, y_k}} + n \log \left( \frac{1}{k} \right) \; .
\end{split}
$$

Subtracting the two LMEs from each other, the LBF emerges as

$$ \label{eq:Mult-LBF-m10}
\begin{split}
\mathrm{LBF}_{10} &= \log \Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right) - \log \Gamma \left( \sum_{j=1}^{k} \alpha_{nj} \right) \\
&+ \sum_{j=1}^k \log \Gamma(\alpha_{nj}) - \sum_{j=1}^k \log \Gamma(\alpha_{0j}) - n \log \left( \frac{1}{k} \right)
\end{split}
$$

where the [posterior hyperparameters](/D/post) [are given by](/P/mult-post)

$$ \label{eq:Mult-post-par}
\begin{split}
\alpha_n &= \alpha_0 + y \\
&= [\alpha_{01}, \ldots, \alpha_{0k}] + [y_1, \ldots, y_k] \\
&= [\alpha_{01} + y_1, \ldots, \alpha_{0k} + y_k] \\
\text{i.e.} \quad \alpha_{nj} &= \alpha_{0j} + y_j \quad \text{for all} \quad j = 1, \ldots, k
\end{split}
$$

with the [numbers of observations](/D/mult) $y_1, \ldots, y_k$.