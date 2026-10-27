---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-17 23:10:00

title: "Posterior predictive covariance and correlation of future Bernoulli observations based on observed binomial data"
chapter: "Statistical Models"
section: "Count data"
topic: "Binomial observations"
theorem: "Posterior predictive correlation"

sources:
  - authors: "Gary Koop, Dale J. Poirier, Justin L. Tobias"
    year: 2007
    title: "Prediction"
    in: "Bayesian Econometric Methods"
    pages: "Exercise 7.1, p. 73"

proof_id: "P559"
shortcut: "bin-postpredcorr"
username: "kjpetrykowski"
---


**Theorem:** Let $x$ be a [binomial data set](/D/bin-data). Suppose $\theta \mid x \sim \mathrm{Bet}(A,B)$, where $A,B>0$ are [posterior](/D/post) [shape parameters](/P/para-shape), with [density](/D/pdf)

$$ \label{eq:bern-postpredcorr-beta}
p(\theta \mid x) = \frac{\theta^{A-1}(1-\theta)^{B-1}}{\mathrm{B}(A,B)},
\qquad 0<\theta<1
$$

where $\mathrm{B}(u,v)=\Gamma(u)\Gamma(v)/\Gamma(u+v)$ is the beta function. Given $\theta$ and $x$, let $Y_1,Y_2$ be [independent](/D/ind) [$\mathrm{Bern}(\theta)$ variables](/D/bern), i.e. two future observations, given the same parameter $\theta$. Then,

$$ \label{eq:bern-postpredcorr-result}
\begin{split}
   \mathrm{Cov}(Y_1,Y_2 \mid x)
&= \frac{AB}{(A+B)^2(A+B+1)} \; , \\
   \mathrm{Corr}(Y_1,Y_2 \mid x)
&= \frac{1}{A+B+1} \; .
\end{split}
$$


**Proof:** All [probabilities](/D/prob) and [moments](/D/mom) in this proof condition on the same [fixed data set](/D/data) $x$. Integrating $\theta$ and $\theta^2$ against the [posterior density](/D/post) increases its first [beta shape parameter](/D/beta) by one and two, respectively. The identity $\mathrm{B}(u,v)=\Gamma(u)\Gamma(v)/\Gamma(u+v)$ and the recurrence $\Gamma(z+1)=z\Gamma(z)$ simplify the resulting ratios:

$$ \label{eq:bern-postpredcorr-beta-moments}
\begin{split}
   \mathrm{E}(\theta \mid x)
&= \frac{\mathrm{B}(A+1,B)}{\mathrm{B}(A,B)}
 = \frac{A}{A+B} \; , \\
   \mathrm{E}(\theta^2 \mid x)
&= \frac{\mathrm{B}(A+2,B)}{\mathrm{B}(A,B)}
 = \frac{A(A+1)}{(A+B)(A+B+1)} \; .
\end{split}
$$

[Subtracting the squared expectation from the expectation of the square](/P/var-mean) shows that $\mathrm{Var}(\theta \mid x)=AB/[(A+B)^2(A+B+1)]$.

$$ \label{eq:bern-postpredcorr-beta-var}
  \mathrm{Var}(\theta \mid x)
= \frac{AB}{(A+B)^2(A+B+1)} \; .
$$

The same results are obtained when [computing mean](/P/beta-mean) and [variance of the beta distribution](/P/beta-var).

A Bernoulli variable with [success probability](/D/bern) $\theta$ [has mean](/P/bern-mean) $\theta$. Hence, for either future variable $Y_j$, with $j \in \lbrace 1,2 \rbrace$, the [total expectation](/P/mean-tot) is

$$ \label{eq:bern-postpredcorr-future-mean}
\begin{split}
   \mathrm{E}(Y_j \mid x)
&= \mathrm{E}[\mathrm{E}(Y_j \mid \theta,x) \mid x]\\
&= \mathrm{E}(\theta \mid x)=\frac{A}{A+B}, \qquad j \in \lbrace 1,2 \rbrace \; .
\end{split}
$$

[Conditional independence](/D/ind-cond) makes the [conditional expectation of the product equal to the product of the conditional expectations](/P/mean-mult):

$$ \label{eq:bern-postpredcorr-conditional-product}
  \mathrm{E}(Y_1 Y_2 \mid \theta,x)
= \mathrm{E}(Y_1 \mid \theta,x) \mathrm{E}(Y_2 \mid \theta,x)
= \theta^2 \; .
\end{split}
$$

Applying [total expectation](/P/cov-mean) again, we have

$$ \label{eq:bern-postpredcorr-covariance}
\begin{split}
   \mathrm{Cov}(Y_1,Y_2 \mid x)
&= \mathrm{E}(Y_1 Y_2 \mid x) - \mathrm{E}(Y_1 \mid x)\mathrm{E}(Y_2 \mid x) \\
&= \mathrm{E}(\theta^2 \mid x) - [\mathrm{E}(\theta \mid x)]^2 \\
&= \mathrm{Var}(\theta \mid x)
 = \frac{AB}{(A+B)^2(A+B+1)} \; .
\end{split}
$$

Each $Y_j$ [takes only the values zero and one](/D/bern). A zero-one variable with mean $q$ [has variance](/P/bern-var) $q(1-q)$, because its square equals itself. Using $q=A/(A+B)$ therefore gives

$$ \label{eq:bern-postpredcorr-future-variance}
\mathrm{Var}(Y_j \mid x) = \frac{AB}{(A+B)^2},
\qquad j \in \lbrace 1,2 \rbrace \; .
$$

These variances are positive. [Dividing the covariance by the product of their standard deviations](/D/corr) gives $1/(A+B+1)$, proving \eqref{eq:bern-postpredcorr-result}.

By definition, the future observations $Y_1$ and $Y_2$ are independent given their shared parameter $\theta$. [Integrating over its posterior](/D/prob-marg) creates dependence: their predictive covariance equals the posterior variance of that parameter.