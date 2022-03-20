---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-03-18 17:00:00

title: "Corrected Akaike information criterion converges to uncorrected Akaike information criterion when infinite data are available"
chapter: "Model Selection"
section: "Classical information criteria"
topic: "Akaike information criterion"
theorem: "Corrected AIC and uncorrected AIC"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Akaike information criterion"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-03-18"
    url: "https://en.wikipedia.org/wiki/Akaike_information_criterion#Modification_for_small_sample_size"

proof_id: "P316"
shortcut: "aicc-aic"
username: "JoramSoch"
---


**Theorem:** In the infinite data limit, the [corrected Akaike information criterion](/D/aicc) converges to the [uncorrected Akaike information criterion](/D/aic)

$$ \label{eq:aicc-aic}
\lim_{n \to \infty} \mathrm{AIC}_\mathrm{c}(m) = \mathrm{AIC}(m) \; .
$$


**Proof:** The [corrected Akaike information criterion](/D/aicc) is defined as

$$ \label{eq:aicc}
\mathrm{AIC}_\mathrm{c}(m) = \mathrm{AIC}(m) + \frac{2k^2 + 2k}{n-k-1} \; .
$$

Note that the number of free model parameters $k$ is finite. Thus, we have:

$$ \label{eq:aicc-aic-qed}
\begin{split}
\lim_{n \to \infty} \mathrm{AIC}_\mathrm{c}(m) &= \lim_{n \to \infty} \left[ \mathrm{AIC}(m) + \frac{2k^2 + 2k}{n-k-1} \right] \\
&= \lim_{n \to \infty} \mathrm{AIC}(m) + \lim_{n \to \infty} \frac{2k^2 + 2k}{n-k-1} \\
&= \mathrm{AIC}(m) + 0 \\
&= \mathrm{AIC}(m) \; .
\end{split}
$$