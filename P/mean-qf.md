---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-13 21:59:00

title: "Expectation of a quadratic form"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Expectation of a quadratic form"

sources:
  - authors: "Kendrick, David"
    year: 1981
    title: "Expectation of a quadratic form"
    in: "Stochastic Control for Economic Models"
    pages: "pp. 170-171"
  - authors: "Wikipedia"
    year: 2020
    title: "Multivariate random variable"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-07-13"
    url: "https://en.wikipedia.org/wiki/Multivariate_random_variable#Expectation_of_a_quadratic_form"
  - authors: "Halvorsen, Kjetil B."
    year: 2012
    title: "Expected value and variance of trace function"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2020-07-13"
    url: "https://stats.stackexchange.com/questions/34477/expected-value-and-variance-of-trace-function"
  - authors: "Sarwate, Dilip"
    year: 2013
    title: "Expected Value of Quadratic Form"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2020-07-13"
    url: "https://stats.stackexchange.com/questions/48066/expected-value-of-quadratic-form"

proof_id: "P131"
shortcut: "mean-qf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n \times 1$ [random vector](/D/rvec) with [mean](/D/mean) $\mu$ and [covariance](/D/cov) $\Sigma$ and let $A$ be a symmetric $n \times n$ matrix. Then, the expectation of the quadratic form $X^\mathrm{T} A X$ is

$$ \label{eq:mean-qf}
\mathrm{E}\left[ X^\mathrm{T} A X \right] = \mu^\mathrm{T} A \mu + \mathrm{tr}(A \Sigma) \; .
$$


**Proof:** Note that $X^\mathrm{T} A X$ is a $1 \times 1$ matrix. We can therefore write

$$ \label{eq:mean-qf-s1}
\mathrm{E}\left[ X^\mathrm{T} A X \right] =  \mathrm{E}\left[ \mathrm{tr} \left( X^\mathrm{T} A X \right) \right] \; .
$$

Using the trace property $\mathrm{tr}(ABC) = \mathrm{tr}(BCA)$, this becomes

$$ \label{eq:mean-qf-s2}
\mathrm{E}\left[ X^\mathrm{T} A X \right] =  \mathrm{E}\left[ \mathrm{tr} \left( A X X^\mathrm{T} \right) \right] \; .
$$

Because [mean and trace are linear operators](/P/mean-tr), we have

$$ \label{eq:mean-qf-s3}
\mathrm{E}\left[ X^\mathrm{T} A X \right] =  \mathrm{tr} \left( A \; \mathrm{E}\left[ X X^\mathrm{T} \right] \right) \; .
$$

Note that the [covariance matrix can be partitioned into expected values](/P/covmat-mean)

$$ \label{eq:covmat-mean}
\mathrm{Cov}(X,X) = \mathrm{E}(X X^\mathrm{T}) - \mathrm{E}(X) \mathrm{E}(X)^\mathrm{T} \; ,
$$

such that the expected value of the quadratic form becomes

$$ \label{eq:mean-qf-s4}
\mathrm{E}\left[ X^\mathrm{T} A X \right] =  \mathrm{tr} \left( A \left[ \mathrm{Cov}(X,X) + \mathrm{E}(X) \mathrm{E}(X)^\mathrm{T} \right] \right) \; .
$$

Finally, applying mean and covariance of $X$, we have

$$ \label{eq:mean-qf-s5}
\begin{split}
\mathrm{E}\left[ X^\mathrm{T} A X \right] &= \mathrm{tr} \left( A \left[ \Sigma + \mu \mu^\mathrm{T} \right] \right) \\
&= \mathrm{tr} \left( A \Sigma + A \mu \mu^\mathrm{T} \right) \\
&= \mathrm{tr}(A \Sigma) + \mathrm{tr}(A \mu \mu^\mathrm{T}) \\
&= \mathrm{tr}(A \Sigma) + \mathrm{tr}(\mu^\mathrm{T} A \mu) \\
&= \mu^\mathrm{T} A \mu + \mathrm{tr}(A \Sigma) \; .
\end{split}
$$