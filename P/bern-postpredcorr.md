---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-17 23:10:00

title: "Positive dependence between future Bernoulli observations after parameter integration"
chapter: "Statistical Models"
section: "Count data"
topic: "Binomial observations"
theorem: "Posterior predictive covariance and correlation"

sources:
  - authors: "Gary Koop, Dale J. Poirier, Justin L. Tobias"
    year: 2007
    title: "Prediction"
    in: "Bayesian Econometric Methods"
    pages: "Exercise 7.1, p. 73"

proof_id: "P559"
shortcut: "bern-postpredcorr"
username: "kjpetrykowski"
---

**Theorem:** Fix an observed data set $x$. Suppose $\theta\mid x\sim\mathrm{Bet}(A,B)$, where $A,B>0$ are posterior shape parameters, with density

$$ \label{eq:bern-postpredcorr-beta}
p(\theta\mid x)=\frac{\theta^{A-1}(1-\theta)^{B-1}}{\mathcal{B}(A,B)},
\qquad 0<\theta<1 \; .
$$

Here, $\mathcal{B}(A,B)=\Gamma(A)\Gamma(B)/\Gamma(A+B)$ is the beta function. Given $\theta$ and $x$, let $Y_1^{\ast},Y_2^{\ast}$ be independent $\mathrm{Bern}(\theta)$ variables. They represent two future observations from the same parameter. Then

$$ \label{eq:bern-postpredcorr-result}
\begin{split}
\mathrm{Cov}(Y_1^{\ast},Y_2^{\ast}\mid x)
&=\frac{AB}{(A+B)^2(A+B+1)},\\
\mathrm{Corr}(Y_1^{\ast},Y_2^{\ast}\mid x)
&=\frac{1}{A+B+1} \; .
\end{split}
$$

All probabilities and moments in this proof condition on the same fixed data set $x$.

**Proof:** Integrating $\theta$ and $\theta^2$ against the posterior density increases its first beta shape by one and two, respectively. The identity $\mathcal{B}(u,v)=\Gamma(u)\Gamma(v)/\Gamma(u+v)$ and the recurrence $\Gamma(z+1)=z\Gamma(z)$ simplify the resulting ratios:

$$ \label{eq:bern-postpredcorr-beta-moments}
\begin{split}
\mathrm{E}(\theta\mid x)&=\frac{\mathcal{B}(A+1,B)}{\mathcal{B}(A,B)}=\frac{A}{A+B},\\
\mathrm{E}(\theta^2\mid x)&=\frac{\mathcal{B}(A+2,B)}{\mathcal{B}(A,B)}
=\frac{A(A+1)}{(A+B)(A+B+1)} \; .
\end{split}
$$

Subtracting the squared mean shows that $\mathrm{Var}(\theta\mid x)=AB/[(A+B)^2(A+B+1)]$.

We can see that [beta mean](/P/beta-mean) and [beta variance](/P/beta-var) give the same moment calculations.

A Bernoulli variable with success probability $\theta$ has mean $\theta$. Hence, for either future variable, [total expectation](/P/mean-tot) gives

$$ \label{eq:bern-postpredcorr-future-mean}
\begin{split}
\mathrm{E}(Y_j^{\ast}\mid x)
&=\mathrm{E}[\mathrm{E}(Y_j^{\ast}\mid\theta,x)\mid x]\\
&=\mathrm{E}(\theta\mid x)=\frac{A}{A+B},\qquad j\in\{1,2\} \; .
\end{split}
$$

[Conditional independence](/D/ind-cond) makes the conditional expectation of the product equal to the product of the conditional expectations:

$$ \label{eq:bern-postpredcorr-conditional-product}
\begin{split}
&\mathrm{E}(Y_1^{\ast}Y_2^{\ast}\mid\theta,x)\\
&\qquad=\mathrm{E}(Y_1^{\ast}\mid\theta,x)\,
 \mathrm{E}(Y_2^{\ast}\mid\theta,x)\\
&\qquad=\theta^2 \; .
\end{split}
$$

Applying total expectation again,

$$ \label{eq:bern-postpredcorr-covariance}
\begin{split}
\mathrm{Cov}(Y_1^{\ast},Y_2^{\ast}\mid x)
&=\mathrm{E}(Y_1^{\ast}Y_2^{\ast}\mid x)
 -\mathrm{E}(Y_1^{\ast}\mid x)\mathrm{E}(Y_2^{\ast}\mid x)\\
&=\mathrm{E}(\theta^2\mid x)-[\mathrm{E}(\theta\mid x)]^2\\
&=\mathrm{Var}(\theta\mid x)
=\frac{AB}{(A+B)^2(A+B+1)} \; .
\end{split}
$$

Each $Y_j^{\ast}$ takes only the values zero and one. A zero-one variable with mean $q$ has variance $q(1-q)$, because its square equals itself. Using $q=A/(A+B)$ therefore gives

$$ \label{eq:bern-postpredcorr-future-variance}
\mathrm{Var}(Y_j^{\ast}\mid x)=\frac{AB}{(A+B)^2},\qquad j\in\{1,2\} \; .
$$

These variances are positive. Dividing the covariance by the product of their standard deviations gives $1/(A+B+1)$, proving \eqref{eq:bern-postpredcorr-result}.

The future observations are independent given their shared parameter. Averaging over its posterior creates dependence: their predictive covariance equals the posterior variance of that parameter.
