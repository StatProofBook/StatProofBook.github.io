---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-11-26 11:38:00

title: "Law of total covariance"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
theorem: "Law of total covariance"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Law of total covariance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-11-26"
    url: "https://en.wikipedia.org/wiki/Law_of_total_covariance#Proof"

proof_id: "P293"
shortcut: "cov-tot"
username: "JoramSoch"
---


**Theorem:** (law of total covariance, also called "conditional covariance formula") Let $X$, $Y$ and $Z$ be [random variables](/D/rvar) defined on the same [probability space](/D/prob-spc) and assume that the [covariance](/D/cov) of $X$ and $Y$ is finite. Then, the sum of the [expectation](/D/mean) of the conditional covariance and the [covariance](/D/cov) of the conditional expectations of $X$ and $Y$ given $Z$ is equal to the [covariance](/D/cov) of $X$ and $Y$:

$$ \label{eq:cov-tot}
\mathrm{Cov}(X,Y) = \mathrm{E}[\mathrm{Cov}(X,Y \vert Z)] + \mathrm{Cov}[\mathrm{E}(X \vert Z),\mathrm{E}(Y \vert Z)] \; .
$$


**Proof:** The [covariance can be decomposed into expected values](/P/cov-mean) as follows:

$$ \label{eq:cov-tot-s1}
\mathrm{Cov}(X,Y) = \mathrm{E}(XY) - \mathrm{E}(X) \mathrm{E}(Y) \; .
$$

Then, conditioning on $Z$ and applying the [law of total expectation](/P/mean-tot), we have:

$$ \label{eq:cov-tot-s2}
\mathrm{Cov}(X,Y) = \mathrm{E}\left[ \mathrm{E}(XY \vert Z) \right] - \mathrm{E}\left[ \mathrm{E}(X \vert Z ) \right] \mathrm{E}\left[ \mathrm{E}(Y \vert Z) \right] \; .
$$

Applying the [decomposition of covariance into expected values](/P/cov-mean) to the first term gives:

$$ \label{eq:cov-tot-s3}
\mathrm{Cov}(X,Y) = \mathrm{E}\left[ \mathrm{Cov}(X,Y \vert Z) + \mathrm{E}(X \vert Z) \mathrm{E}(Y \vert Z) \right] - \mathrm{E}\left[ \mathrm{E}(X \vert Z ) \right] \mathrm{E}\left[ \mathrm{E}(Y \vert Z) \right] \; .
$$

With the [linearity of the expected value](/P/mean-lin), the terms can be regrouped to give:

$$ \label{eq:cov-tot-s4}
\mathrm{Cov}(X,Y) = \mathrm{E}\left[ \mathrm{Cov}(X,Y \vert Z) \right] + \left( \mathrm{E}\left[ \mathrm{E}(X \vert Z) \mathrm{E}(Y \vert Z) \right] - \mathrm{E}\left[ \mathrm{E}(X \vert Z ) \right] \mathrm{E}\left[ \mathrm{E}(Y \vert Z) \right] \right) \; .
$$

Once more using the [decomposition of covariance into expected values](/P/cov-mean), we finally have:

$$ \label{eq:var-tot-s5}
\mathrm{Cov}(X,Y) = \mathrm{E}[\mathrm{Cov}(X,Y \vert Z)] + \mathrm{Cov}[\mathrm{E}(X \vert Z),\mathrm{E}(Y \vert Z)] \; .
$$