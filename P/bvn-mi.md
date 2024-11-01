---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-11-01 11:51:06

title: "Mutual information of the bivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Bivariate normal distribution"
theorem: "Mutual information"

sources:
  - authors: "Krafft, Peter"
    year: 2013
    title: "Correlation and Mutual Information"
    in: "Princeton University Department of Computer Science: Laboratory for Intelligent Probabilistic Systems"
    pages: "February 13, 2013"
    url: "https://lips.cs.princeton.edu/correlation-and-mutual-information/"

proof_id: "P476"
shortcut: "bvn-mi"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ follow a [bivariate normal distribution](/D/bvn):

$$ \label{eq:bvn}
\left[ \begin{matrix} X \\ Y \end{matrix} \right] \sim
\mathcal{N}\left( \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right], \left[ \begin{matrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{matrix} \right] \right) \; .
$$

Then, the [mutual information](/D/mi) of $X$ and $Y$ is

$$ \label{eq:bvn-lincomb}
\mathrm{I}(X,Y) = -\frac{1}{2} \ln \left( 1-\rho^2 \right)
$$

where $\rho$ is the [correlation](/D/corr) of $X$ and $Y$.


**Proof:** [Mutual information can be written in terms of marginal and joint differential entropy](/P/cmi-mjde):

$$ \label{eq:cmi-mjde}
\mathrm{I}(X,Y) = \mathrm{h}(X) + \mathrm{h}(Y) - \mathrm{h}(X,Y) \; .
$$

The [marginal distributions of the multivariate normal distribution are also multivariate normal](/P/mvn-marg)

$$ \label{eq:mvn-marg}
\left[ \begin{matrix} X_1 \\ X_2 \end{matrix} \right] \sim
\mathcal{N}\left( \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right], \left[ \begin{matrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{matrix} \right] \right)
\quad \Rightarrow \quad
X_1 \sim \mathcal{N}\left( \mu_1, \Sigma_{11} \right) \; ,
$$

such that the [marginals](/D/marg) of the [bivariate normal distribution](/D/bvn) are [univariate normal distribution](/D/norm):

$$ \label{eq:bvn-marg}
\left[ \begin{matrix} X \\ Y \end{matrix} \right] \sim
\mathcal{N}\left( \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right], \left[ \begin{matrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{matrix} \right] \right)
\quad \Rightarrow \quad
X \sim \mathcal{N}\left( \mu_1, \sigma_1^2 \right)
\quad \text{and} \quad
Y \sim \mathcal{N}\left( \mu_2, \sigma_2^2 \right) \; .
$$

The [differential entropy of the univariate normal distribution](/P/norm-dent) is

$$ \label{eq:norm-dent}
\mathrm{h}(X) = \frac{1}{2} \ln\left( 2 \pi \sigma^2 e \right)
$$

and the [differential entropy of the multivariate normal distribution](/P/mvn-dent) is

$$ \label{eq:mvn-dent}
\mathrm{h}(x) = \frac{n}{2} \ln(2\pi) + \frac{1}{2} \ln|\Sigma| + \frac{1}{2} n
$$

where $\lvert \Sigma \rvert$ is the determinant of the [covariance matrix](/D/covmat) $\Sigma$. A two-dimensional [covariance matrix can be rewritten in terms of correlations](/P/covmat-corrmat) as follows:

$$ \label{eq:Sigma}
\begin{split}
\Sigma
&= \left[ \begin{matrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{matrix} \right] \left[ \begin{matrix} 1 & \rho \\ \rho & 1 \end{matrix} \right] \left[ \begin{matrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{matrix} \right] \\
&= \left[ \begin{matrix} \sigma_1^2 & \rho \, \sigma_1 \sigma_2 \\ \rho \, \sigma_1 \sigma_2 & \sigma_2^2 \end{matrix} \right] \; .
\end{split}
$$

Combining \eqref{eq:cmi-mjde} with \eqref{eq:norm-dent} and \eqref{eq:mvn-dent}, applying $n = 2$, we get:

$$ \label{eq:bvn-mi}
\begin{split}
\mathrm{I}(X,Y)
&\overset{\eqref{eq:cmi-mjde}}{=} \mathrm{h}(X) + \mathrm{h}(Y) - \mathrm{h}(X,Y) \\
&\overset{\eqref{eq:bvn-marg}}{=} \mathrm{h}\left[ \mathcal{N}\left( \mu_1, \sigma_1^2 \right) \right] + \mathrm{h}\left[ \mathcal{N}\left( \mu_2, \sigma_2^2 \right) \right] - \mathrm{h}\left[ \mathcal{N}\left( \mu, \Sigma \right) \right] \\
&\overset{\eqref{eq:Sigma}}{=} \left[ \frac{1}{2} \ln\left( 2 \pi \sigma_1^2 e \right) \right] + \left[ \frac{1}{2} \ln\left( 2 \pi \sigma_2^2 e \right) \right] - \left[ \frac{2}{2} \ln(2\pi) + \frac{1}{2} \ln \left| \left[ \begin{matrix} \sigma_1^2 & \rho \, \sigma_1 \sigma_2 \\ \rho \, \sigma_1 \sigma_2 & \sigma_2^2 \end{matrix} \right] \right| + \frac{1}{2} \cdot 2 \right] \\
&= \left( \frac{2}{2} \ln(2\pi) + \frac{2}{2} \ln(e) - \ln(2\pi) - 1 \right) + \left( \frac{1}{2} \ln\left( \sigma_1^2 \right) + \frac{1}{2} \ln\left( \sigma_2^2 \right) - \frac{1}{2} \ln \left| \left[ \begin{matrix} \sigma_1^2 & \rho \, \sigma_1 \sigma_2 \\ \rho \, \sigma_1 \sigma_2 & \sigma_2^2 \end{matrix} \right] \right| \right) \\
&= \frac{1}{2} \left[ \ln\left( \sigma_1^2 \right) + \ln\left( \sigma_2^2 \right) - \ln\left( \sigma_1^2 \sigma_2^2 - (\rho \, \sigma_1 \sigma_2)^2 \right) \right] \\
&= \frac{1}{2} \ln \left[ \frac{\sigma_1^2 \sigma_2^2}{\sigma_1^2 \sigma_2^2 - (\rho \, \sigma_1 \sigma_2)^2} \right] \\
&= \frac{1}{2} \ln \left[ \frac{\sigma_1^2 \sigma_2^2}{\sigma_1^2 \sigma_2^2 (1-\rho^2)} \right] \\
&= \frac{1}{2} \ln \left[ \frac{1}{1-\rho^2} \right] \\
&= -\frac{1}{2} \ln \left( 1-\rho^2 \right) \; .
\end{split}
$$