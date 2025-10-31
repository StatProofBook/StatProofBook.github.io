---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-11-08 10:46:00

title: "Moment-generating function of a sum of independent random variables"
chapter: "General Theorems"
section: "Probability theory"
topic: "Moment-generating function"
theorem: "Moment-generating function of sum of independents"

sources:
  - authors: "Probability Fact"
    year: 2021
    title: "If X and Y are independent, the moment generating function (MGF)"
    in: "X"
    pages: "retrieved on 2024-11-08"
    url: "https://x.com/ProbFact/status/1468264616706859016"

proof_id: "P478"
shortcut: "mgf-sumind"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be two [independent](/D/ind) [random variables](/D/rvar) and let $Z = X + Y$. Then, the [moment-generating function](/D/mgf) of $Z$ is given by

$$ \label{eq:mgf-sumind}
M_Z(t) = M_X(t) \cdot M_Y(t)
$$

where $M_X(t)$, $M_Y(t)$ and $M_Z(t)$ are the [moment-generating functions](/D/mgf) of $X$, $Y$ and $Z$.


**Proof:** The [moment-generating function of a random variable](/D/mgf) $X$ is

$$ \label{eq:mfg}
M_X(t) = \mathrm{E} \left( \exp \left[ t X \right] \right)
$$

and therefore the moment-generating function of the sum $Z$ is given by

$$ \label{eq:mgf-sumind-s1}
\begin{split}
M_Z(t)
&= \mathrm{E} \left( \exp \left[ t Z \right] \right) \\
&= \mathrm{E} \left( \exp \left[ t (X + Y) \right] \right) \\
&= \mathrm{E} \left( \exp \left[ t X \right] \cdot \exp \left[ t Y \right] \right) \; .
\end{split}
$$

Because the [expected value is multiplicative for independent random variables](/P/mean-mult), we have

$$ \label{eq:mgf-sumind-s2}
\begin{split}
M_Z(t)
&= \mathrm{E} \left( \exp \left[ t X \right] \right) \cdot \mathrm{E} \left( \exp \left[ t Y \right] \right) \\
&= M_X(t) \cdot M_Y(t) \; .
\end{split}
$$