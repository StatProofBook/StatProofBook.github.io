---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-11-01 12:36:44

title: "Mutual information of the multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Mutual information"

sources:
  - authors: "a06e"
    year: 2019
    title: "Mutual information between subsets of variables in the multivariate normal distribution"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2024-11-01"
    url: "https://stats.stackexchange.com/a/438613/270304"

proof_id: "P477"
shortcut: "mvn-mi"
username: "JoramSoch"
---


**Theorem:** Let $X \in \mathbb{R}^n$ and $Y \in \mathbb{R}^m$ be [random vectors](/D/rvec) that are [jointly multivariate normal](/D/mvn):

$$ \label{eq:bvn}
\left[ \begin{matrix} X \\ Y \end{matrix} \right] \sim
\mathcal{N}\left( \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right], \left[ \begin{matrix} \Sigma_1 & \Sigma_{12} \\ \Sigma_{21} & \Sigma_2 \end{matrix} \right] \right) \; .
$$

Then, the [mutual information](/D/mi) of $X$ and $Y$ is

$$ \label{eq:bvn-lincomb}
\mathrm{I}(X,Y) = \frac{1}{2} \ln \left[ \frac{|\Sigma_1| |\Sigma_2|}{|\Sigma|} \right]
$$

where $\mu \in \mathbb{R}^p$ and $\Sigma \in \mathbb{R}^{p \times p}$ are the [mean](/D/mean) and [covariance matrix](/D/covmat) of the [random vector](/D/rvec) $\left[ \begin{matrix} X \\\\ Y \end{matrix} \right] \in \mathbb{R}^p$, respectively, where $p = n + m$.


**Proof:** [Mutual information can be written in terms of marginal and joint differential entropy](/P/cmi-mjde):

$$ \label{eq:cmi-mjde}
\mathrm{I}(X,Y) = \mathrm{h}(X) + \mathrm{h}(Y) - \mathrm{h}(X,Y) \; .
$$

The [marginal distributions of the multivariate normal distribution are also multivariate normal]

$$ \label{eq:mvn-marg}
\left[ \begin{matrix} X_1 \\ X_2 \end{matrix} \right] \sim
\mathcal{N}\left( \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right], \left[ \begin{matrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{matrix} \right] \right)
\quad \Rightarrow \quad
X_1 \sim \mathcal{N}\left( \mu_1, \Sigma_{11} \right) \; ,
$$

such that the [marginals](/D/marg) of $X$ and $Y$ are:

$$ \label{eq:X-Y-marg}
X \sim \mathcal{N}\left( \mu_1, \Sigma_1 \right)
\quad \text{and} \quad
Y \sim \mathcal{N}\left( \mu_2, \Sigma_2 \right) \; .
$$

The [differential entropy of the multivariate normal distribution](/P/mvn-dent) is

$$ \label{eq:mvn-dent}
\mathrm{h}(x) = \frac{n}{2} \ln(2\pi) + \frac{1}{2} \ln|\Sigma| + \frac{1}{2} n
$$

where $\lvert \Sigma \rvert$ is the determinant of $\Sigma$. Combining \eqref{eq:cmi-mjde} with \eqref{eq:mvn-dent}, we get:

$$ \label{eq:bvn-mi}
\begin{split}
\mathrm{I}(X,Y)
&\overset{\eqref{eq:cmi-mjde}}{=} \mathrm{h}(X) + \mathrm{h}(Y) - \mathrm{h}(X,Y) \\
&\overset{\eqref{eq:X-Y-marg}}{=} \mathrm{h}\left[ \mathcal{N}\left( \mu_1, \Sigma_1 \right) \right] + \mathrm{h}\left[ \mathcal{N}\left( \mu_2, \Sigma_2 \right) \right] - \mathrm{h}\left[ \mathcal{N}\left( \mu, \Sigma \right) \right] \\
&\overset{\eqref{eq:mvn-dent}}{=} \left[ \frac{n}{2} \ln(2\pi) + \frac{1}{2} \ln|\Sigma_1| + \frac{1}{2} n \right] + \left[ \frac{m}{2} \ln(2\pi) + \frac{1}{2} \ln|\Sigma_2| + \frac{1}{2} m \right] - \left[ \frac{p}{2} \ln(2\pi) + \frac{1}{2} \ln|\Sigma| + \frac{1}{2} p \right] \\
&= \left( \frac{n+m-p}{2} \ln(2\pi) + \frac{1}{2}(n+m-p) \right) + \left( \frac{1}{2} \ln|\Sigma_1| + \frac{1}{2} \ln|\Sigma_2| - \frac{1}{2} \ln|\Sigma| \right) \\
&= \frac{1}{2} \left( \ln|\Sigma_1| + \ln|\Sigma_2| - \ln|\Sigma| \right) \\
&= \frac{1}{2} \ln \left[ \frac{|\Sigma_1| |\Sigma_2|}{|\Sigma|} \right] \; .
\end{split}
$$