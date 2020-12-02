---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-19 17:15:00

title: "Construction of confidence intervals using Wilks' theorem"
chapter: "General Theorems"
section: "Estimation theory"
topic: "Interval estimates"
theorem: "Construction of confidence intervals using Wilks' theorem"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Confidence interval"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-19"
    url: "https://en.wikipedia.org/wiki/Confidence_interval#Methods_of_derivation"
  - authors: "Wikipedia"
    year: 2020
    title: "Likelihood-ratio test"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-19"
    url: "https://en.wikipedia.org/wiki/Likelihood-ratio_test#Definition"
  - authors: "Wikipedia"
    year: 2020
    title: "Wilks' theorem"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-19"
    url: "https://en.wikipedia.org/wiki/Wilks%27_theorem"

proof_id: "P56"
shortcut: "ci-wilks"
username: "JoramSoch"
---


**Theorem:** Let $m$ be a [generative model](/D/gm) for measured data $y$ with model parameters $\theta$, consisting of a parameter of interest $\phi$ and nuisance parameters $\lambda$:

$$ \label{eq:mod-par}
m: p(y|\theta) = \mathcal{D}(y; \theta), \quad \theta = \left\lbrace \phi, \lambda \right\rbrace \; .
$$

Further, let $\hat{\theta}$ be an estimate of $\theta$, obtained using [maximum-likelihood-estimation](/D/mle):

$$ \label{eq:theta-mle}
\hat{\theta} = \operatorname*{arg\,max}_{\theta} \log p(y|\theta), \quad \hat{\theta} = \left\lbrace \hat{\phi}, \hat{\lambda} \right\rbrace \; .
$$

Then, an asymptotic [confidence interval](/D/ci) for $\theta$ is given by

$$ \label{eq:ci-wilks}
\mathrm{CI}_{1-\alpha}(\hat{\phi}) = \left\lbrace \phi \, \vert \, \log p(y|\phi,\hat{\lambda}) \geq \log p(y|\hat{\phi},\hat{\lambda}) - \frac{1}{2} \chi^2_{1,1-\alpha} \right\rbrace
$$

where $1-\alpha$ is the confidence level and $\chi^2_{1,1-\alpha}$ is the $(1-\alpha)$-quantile of the [chi-squared distribution](/D/chi2) with 1 [degree of freedom](/D/dof).


**Proof:** The [confidence interval](/D/ci) is defined as the interval that, under infinitely repeated [random experiments](/D/rexp), contains the true parameter value with a certain probability.

Let us define the [likelihood ratio](/D/lr)

$$ \label{eq:lr}
\Lambda(\phi) = \frac{p(y|\phi,\hat{\lambda})}{p(y|\hat{\phi},\hat{\lambda})}
$$

and compute the [log-likelihood ratio](/D/llr)

$$ \label{eq:llr}
\log \Lambda(\phi) = \log p(y|\phi,\hat{\lambda}) - \log p(y|\hat{\phi},\hat{\lambda}) \; .
$$

[Wilks' theorem](/P/llr-wilks) states that, when comparing two statistical models with parameter spaces $\Theta_1$ and $\Theta_0 \subset \Theta_1$, as the sample size approaches infinity, the quantity calculated as $-2$ times the log-ratio of maximum likelihoods follows a [chi-squared distribution](/D/chi2), if the null hypothesis is true:

$$ \label{eq:wilks}
H_0: \theta \in \Theta_0 \quad \Rightarrow \quad -2 \log \frac{\operatorname*{max}_{\theta \in \Theta_0} p(y|\theta)}{\operatorname*{max}_{\theta \in \Theta_1} p(y|\theta)} \sim \chi^2_{\Delta k}
$$

where $\Delta k$ is the difference in dimensionality between $\Theta_0$ and $\Theta_1$. Applied to our example in \eqref{eq:llr}, we note that $\Theta_1 = \left\lbrace \phi, \hat{\phi} \right\rbrace$ and $\Theta_0 = \left\lbrace \phi \right\rbrace$, such that $\Delta k = 1$ and Wilks' theorem implies:

$$ \label{eq:llr-wilks}
-2 \log \Lambda(\phi) \sim  \chi^2_1 \; .
$$

Using the [quantile function](/D/qf) $\chi^2_{k,p}$ of the [chi-squared distribution](/D/chi2), an $(1-\alpha)$-confidence interval is therefore given by all values $\phi$ that satisfy

$$ \label{eq:llr-chi2}
-2 \log \Lambda(\phi) \leq \chi^2_{1,1-\alpha} \; .
$$

Applying \eqref{eq:llr} and rearranging, we can evaluate

$$ \label{eq:llr-chi2-dev}
\begin{split}
-2 \left[ \log p(y|\phi,\hat{\lambda}) - \log p(y|\hat{\phi},\hat{\lambda}) \right] &\leq \chi^2_{1,1-\alpha} \\
\log p(y|\phi,\hat{\lambda}) - \log p(y|\hat{\phi},\hat{\lambda}) &\geq -\frac{1}{2} \chi^2_{1,1-\alpha} \\
\log p(y|\phi,\hat{\lambda}) &\geq \log p(y|\hat{\phi},\hat{\lambda}) - \frac{1}{2} \chi^2_{1,1-\alpha}
\end{split}
$$

which is equivalent to the confidence interval given by \eqref{eq:ci-wilks}.