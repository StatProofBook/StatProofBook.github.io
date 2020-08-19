---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-19 08:36:00

title: "Moment-generating function of linear combination of independent random variables"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Moment-generating function of linear combination"

sources:
  - authors: "ProofWiki"
    year: 2020
    title: "Moment Generating Function of Linear Combination of Independent Random Variables"
    in: "ProofWiki"
    pages: "retrieved on 2020-08-19"
    url: "https://proofwiki.org/wiki/Moment_Generating_Function_of_Linear_Combination_of_Independent_Random_Variables"

proof_id: "P155"
shortcut: "mgf-lincomb"
username: "JoramSoch"
---


**Theorem:** Let $X_1, \ldots, X_n$ be $n$ [independent](/D/ind) [random variables](/D/rvar) with [moment-generating functions](/D/mgf) $M_{X_i}(t)$. Then, the moment-generating function of the linear combination $X = \sum_{i=1}^{n} a_i X_i$ is given by

$$ \label{eq:mgf-lincomb}
M_X(t) = \prod_{i=1}^{n} M_{X_i}(a_i t)
$$

where $a_1, \ldots, a_n$ are $n$ real numbers.


**Proof:** The [moment-generating function of a random variable](/D/mgf) $X_i$ is

$$ \label{eq:mfg-vect}
M_{X_i}(t) = \mathrm{E} \left( \exp \left[ t X_i \right] \right)
$$

and therefore the moment-generating function of the linear combination $X$ is given by

$$ \label{eq:mgf-lincomb-s1}
\begin{split}
M_X(t) &= \mathrm{E} \left( \exp \left[ t X \right] \right) \\
&= \mathrm{E} \left( \exp \left[ t \sum_{i=1}^{n} a_i X_i \right] \right) \\
&= \mathrm{E} \left( \prod_{i=1}^{n} \exp \left[ t \, a_i X_i \right] \right) \; .
\end{split}
$$

Because the [expected value is multiplicative for independent random variables](/P/mean-mult), we have

$$ \label{eq:mgf-lincomb-s2}
\begin{split}
M_X(t) &= \prod_{i=1}^{n} \mathrm{E} \left( \exp \left[ (a_i t) X_i \right] \right) \\
&= \prod_{i=1}^{n} M_{X_i}(a_i t) \; .
\end{split}
$$