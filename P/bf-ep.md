---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2020-09-02 12:00:00

title: "Encompassing Prior Method for computing Bayes Factors"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Bayes factor"
theorem: "Computation using Encompassing Prior Method"

sources:
  - authors: "Klugkist, I., Kato, B., and Hoijtink, H."
    year: 2005
    title: "Bayesian model selection using encompassing priors"
    in: "Statistica Neerlandica"
    pages: "vol. 59, no. 1., pp. 57-69"
    url: "https://dx.doi.org/10.1111/j.1467-9574.2005.00279.x"
    doi: "10.1111/j.1467-9574.2005.00279.x"
  - authors: "Faulkenberry, Thomas J."
    year: 2019
    title: "A tutorial on generalizing the default Bayesian t-test via posterior sampling and encompassing priors"
    in: "Communications for Statistical Applications and Methods"
    pages: "vol. 26, no. 2, pp. 217-238"
    url: "https://dx.doi.org/10.29220/CSAM.2019.26.2.217"
    doi: "10.29220/CSAM.2019.26.2.217"

proof_id: "P157"
shortcut: "bf-ep"
username: "tomfaulkenberry"
---


**Theorem:** Consider two models $m_1$ and $m_e$, where $m_1$ is nested within an [encompassing model](/D/encm) $m_e$ via an inequality constraint on some parameter $\theta$, and $\theta$ is unconstrained under $m_e$. Then, the [Bayes factor](/D/bf) is

$$ \label{eq:bf-ep}
  \text{BF}_{1e} = \frac{c}{d} = \frac{1/d}{1/c}
$$

where $1/d$ and $1/c$ represent the proportions of the posterior and prior of the encompassing model, respectively, that are in agreement with the inequality constraint imposed by the nested model $m_1$.

**Proof:** Consider first that for any model $m_1$ on data $y$ with parameter $\theta$, [Bayes' theorem](/P/bayes-th) implies

$$ \label{eq:bayesth}
  p(\theta \mid y,m_1) = \frac{p(y \mid \theta,m_1) \cdot p(\theta \mid m_1)}{p(y \mid m_1)}.
$$

Rearranging equation \eqref{eq:bayesth} allows us to write the [marginal likelihood](/D/ml) for $y$ under $m_1$ as

$$ \label{eq:marginal}
  p(y \mid m_1) = \frac{p(y \mid \theta,m_1) \cdot p(\theta \mid m_1)}{p(\theta \mid y,m_1)}.
$$

Taking the ratio of the marginal likelihoods for $m_1$ and the [encompassing model](/D/encm) $m_e$ yields the following [Bayes factor](/D/bf):

$$ \label{eq:bayesfactor}
  \text{BF}_{1e} = \frac{p(y \mid \theta,m_1) \cdot p(\theta \mid m_1) / p(\theta \mid y,m_1)}{p(y \mid \theta,m_e) \cdot p(\theta \mid m_e) / p(\theta \mid y,m_e)}.
$$

Now, both the constrained model $m_1$ and the [encompassing model](/D/encm) $m_e$ contain the same parameter vector $\theta$. Choose a specific value of $\theta$, say $\theta'$, that exists in the support of both models $m_1$ and $m_e$ (we can do this, because $m_1$ is nested within $m_e$). Then, for this parameter value $\theta'$, we have $p(y \mid \theta',m_1)=p(y \mid \theta',m_e)$, so the expression for the Bayes factor in equation \eqref{eq:bayesfactor} reduces to an expression involving only the priors and posteriors for $\theta'$ under $m_1$ and $m_e$:

$$ \label{eq:bayesfactor2}
  \text{BF}_{1e} = \frac{p(\theta' \mid m_1) / p(\theta' \mid y,m_1)}{p(\theta' \mid m_e) / p(\theta' \mid y,m_e)}.
$$

Because $m_1$ is nested within $m_e$ via an inequality constraint, the prior $p(\theta' \mid m_1)$ is simply a truncation of the encompassing prior $p(\theta' \mid m_e)$. Thus, we can express $p(\theta' \mid m_1)$ in terms of the encompassing prior $p(\theta' \mid m_e)$ by multiplying the encompassing prior by an indicator function over $m_1$ and then normalizing the resulting product.  That is,

$$ \label{eq:normalize}
\begin{split}
  p(\theta' \mid m_1) & = \frac{p(\theta' \mid m_e) \cdot I_{\theta' \in m_1}}{\int p(\theta' \mid m_e) \cdot I_{\theta' \in m_1} \, \mathrm{d}\theta'}\\
                      & = \Biggl(\frac{I_{\theta' \in m_1}}{\int p(\theta' \mid m_e) \cdot I_{\theta' \in m_1} \, \mathrm{d}\theta'}\Biggr) \cdot p(\theta' \mid m_e),
\end{split}
$$

where $I_{\theta' \in m_1}$ is an indicator function. For parameters $\theta' \in m_1$, this indicator function is identically equal to 1, so the expression in parentheses reduces to a constant, say $c$, allowing us to write the prior as

$$ \label{eq:prior}
  p(\theta' \mid m_1) = c \cdot p(\theta' \mid m_e).
$$

By similar reasoning, we can write the posterior as

$$ \label{eq:posterior}
  p(\theta' \mid y,m_1) = \Biggl(\frac{I_{\theta' \in m_1}}{\int p(\theta' \mid y,m_e) \cdot I_{\theta' \in m_1} \, \mathrm{d}\theta'}\Biggr)\cdot p(\theta' \mid y,m_e) = d \cdot p(\theta' \mid y,m_e).
$$

Plugging \eqref{eq:prior} and \eqref{eq:posterior} into \eqref{eq:bayesfactor2}, this gives us

$$ \label{eq:bayesfactor3}
  \text{BF}_{1e} = \frac{c \cdot p(\theta' \mid m_e) / d \cdot p(\theta' \mid y,m_e)}{p(\theta' \mid m_e) / p(\theta' \mid y,m_e)} = \frac{c}{d} = \frac{1/d}{1/c},
$$

which completes the proof. Note that by definition, $1/d$ represents the proportion of the posterior distribution for $\theta$ under the [encompassing model](/D/encm) $m_e$ that agrees with the constraints imposed by $m_1$.  Similarly, $1/c$ represents the proportion of the prior distribution for $\theta$ under the [encompassing model](/D/encm) $m_e$ that agrees with the constraints imposed by $m_1$.