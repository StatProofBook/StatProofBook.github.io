---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-11 02:01:00

title: "Probability-generating function is expectation of function of random variable"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Probability-generating function in terms of expected value"

sources:
  - authors: "ProofWiki"
    year: 2022
    title: "Probability Generating Function as Expectation"
    in: "ProofWiki"
    pages: "retrieved on 2022-10-11"
    url: "https://proofwiki.org/wiki/Probability_Generating_Function_as_Expectation"

proof_id: "P360"
shortcut: "pgf-mean"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [discrete](/D/rvar-disc) [random variable](/D/rvar) whose set of possible values $\mathcal{X}$ is a subset of the natural numbers $\mathbb{N}$. Then, the [probability-generating function](/D/pgf) of $X$ can be expressed in terms of an [expected value](/D/mean) of a function of $X$

$$ \label{eq:pgf-mean}
G_X(z) = \mathrm{E}\left[ z^X \right]
$$

where $z \in \mathbb{C}$.


**Proof:** The [law of the unconscious statistician](/P/mean-lotus) states that

$$ \label{eq:mean-lotus}
\mathrm{E}[g(X)] = \sum_{x \in \mathcal{X}} g(x) f_X(x)
$$

where $f_X(x)$ is the [probability mass function](/D/pmf) of $X$. Here, we have $g(X) = z^X$, such that

$$ \label{eq:E-zX-s1}
\mathrm{E}\left[ z^X \right] = \sum_{x \in \mathcal{X}} z^x f_X(x) \; .
$$

By the definition of $X$, this is equal to

$$ \label{eq:E-zX-s2}
\mathrm{E}\left[ z^X \right] = \sum_{x=0}^{\infty} f_X(x) \, z^x \; .
$$

The right-hand side is equal to the [probability-generating function](/D/pgf) of $X$:

$$ \label{eq:pgf-mean-qed}
\mathrm{E}\left[ z^X \right] = G_X(z) \; .
$$