---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-02 18:03:00

title: "Posterior probability of the alternative model for multinomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Multinomial observations"
theorem: "Posterior probability"

sources:

proof_id: "P388"
shortcut: "mult-pp"
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

Then, the [posterior probability](/D/pmp) of the [alternative model](/D/h1) is given by

$$ \label{eq:Mult-PP1}
p(m_1|y) = \frac{1}{1 + k^{-n} \cdot \frac{\Gamma \left( \sum_{j=1}^{k} \alpha_{nj} \right)}{\Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right)} \cdot \frac{\prod_{j=1}^k \Gamma(\alpha_{0j})}{\prod_{j=1}^k \Gamma(\alpha_{nj})}}
$$

where $\Gamma(x)$ is the gamma function and $\alpha_n$ are the [posterior hyperparameters for multinomial observations](/P/mult-post) which are functions of the [numbers of observations](/D/mult) $y_1, \ldots, y_k$.


**Proof:** [The posterior probability for one of two models is a function of the log Bayes factor in favor of this model](/P/pmp-lbf):

$$ \label{eq:PP-LBF}
p(m_1|y) = \frac{\exp(\mathrm{LBF}_{12})}{\exp(\mathrm{LBF}_{12}) + 1} \; .
$$

The [log Bayes factor in favor of the alternative model for multinomial observations](/P/mult-lbf) is given by

$$ \label{eq:Mult-LBF10}
\begin{split}
\mathrm{LBF}_{10} &= \log \Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right) - \log \Gamma \left( \sum_{j=1}^{k} \alpha_{nj} \right) \\
&+ \sum_{j=1}^k \log \Gamma(\alpha_{nj}) - \sum_{j=1}^k \log \Gamma(\alpha_{0j}) - n \log \left( \frac{1}{k} \right)
\end{split}
$$

and the corresponding [Bayes factor](/D/bf), i.e. [exponentiated log Bayes factor](/P/lbf-der), is equal to

$$ \label{eq:Mult-BF10}
\mathrm{BF}_{10} = \exp(\mathrm{LBF}_{10}) = k^n \cdot \frac{\Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right)}{\Gamma \left( \sum_{j=1}^{k} \alpha_{nj} \right)} \cdot \frac{\prod_{j=1}^k \Gamma(\alpha_{nj})}{\prod_{j=1}^k \Gamma(\alpha_{0j})} \; .
$$

Thus, the posterior probability of the alternative, assuming a prior distribution over the probabilities $p_1, \ldots, p_k$, compared to the null model, assuming fixed probabilities $p = [1/k, \ldots, 1/k]$, follows as

$$ \label{eq:Mult-PP1-qed}
\begin{split}
p(m_1|y) &\overset{\eqref{eq:PP-LBF}}{=} \frac{\exp(\mathrm{LBF}_{10})}{\exp(\mathrm{LBF}_{10}) + 1} \\
&\overset{\eqref{eq:Mult-BF10}}{=} \frac{k^n \cdot \frac{\Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right)}{\Gamma \left( \sum_{j=1}^{k} \alpha_{nj} \right)} \cdot \frac{\prod_{j=1}^k \Gamma(\alpha_{nj})}{\prod_{j=1}^k \Gamma(\alpha_{0j})}}{k^n \cdot \frac{\Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right)}{\Gamma \left( \sum_{j=1}^{k} \alpha_{nj} \right)} \cdot \frac{\prod_{j=1}^k \Gamma(\alpha_{nj})}{\prod_{j=1}^k \Gamma(\alpha_{0j})} + 1} \\
&= \frac{k^n \cdot \frac{\Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right)}{\Gamma \left( \sum_{j=1}^{k} \alpha_{nj} \right)} \cdot \frac{\prod_{j=1}^k \Gamma(\alpha_{nj})}{\prod_{j=1}^k \Gamma(\alpha_{0j})}}{k^n \cdot \frac{\Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right)}{\Gamma \left( \sum_{j=1}^{k} \alpha_{nj} \right)} \cdot \frac{\prod_{j=1}^k \Gamma(\alpha_{nj})}{\prod_{j=1}^k \Gamma(\alpha_{0j})} \left( 1 + k^{-n} \cdot \frac{\Gamma \left( \sum_{j=1}^{k} \alpha_{nj} \right)}{\Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right)} \cdot \frac{\prod_{j=1}^k \Gamma(\alpha_{0j})}{\prod_{j=1}^k \Gamma(\alpha_{nj})} \right)} \\
&= \frac{1}{1 + k^{-n} \cdot \frac{\Gamma \left( \sum_{j=1}^{k} \alpha_{nj} \right)}{\Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right)} \cdot \frac{\prod_{j=1}^k \Gamma(\alpha_{0j})}{\prod_{j=1}^k \Gamma(\alpha_{nj})}}
\end{split}
$$

where the [posterior hyperparameters](/D/post) [are given by](/P/mult-post)

$$ \label{eq:Mult-post-par}
\alpha_n = \alpha_0 + y, \quad \text{i.e.} \quad \alpha_{nj} = \alpha_{0j} + y_j
$$

with the [numbers of observations](/D/mult) $y_1, \ldots, y_k$.