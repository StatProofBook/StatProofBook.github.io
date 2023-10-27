---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-09-22 12:59:11

title: "Probability density function of the bivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Probability density function of the bivariate normal distribution"

sources:

proof_id: "P416"
shortcut: "bvn-pdf"
username: "JoramSoch"
---


**Theorem:** Let $X = \left[ \begin{matrix} X_1 \\\\ X_2 \end{matrix} \right]$ follow a [bivariate normal distribution](/D/bvn):

$$ \label{eq:bvn}
X \sim \mathcal{N}\left( \mu = \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right], \Sigma = \left[ \begin{matrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{matrix} \right] \right) \; .
$$

Then, the [probability density function](/D/pdf) of $X$ is:

$$ \label{eq:bvn-pdf}
f_X(x) = \frac{1}{2 \pi \sqrt{\sigma_1^2 \sigma_2^2 - \sigma_{12}^2}} \cdot \exp \left[ -\frac{1}{2} \frac{\sigma_2^2 (x_1-\mu_1)^2 - 2 \sigma_{12} (x_1-\mu_1)(x_2-\mu_2) + \sigma_1^2 (x_2-\mu_2)^2}{\sigma_1^2 \sigma_2^2 - \sigma_{12}^2} \right] \; .
$$


**Proof:** The [probability density function of the multivariate normal distribution](/P/mvn-pdf) for an $n \times 1$ [random vector](/D/rvec) $x$ is:

$$ \label{eq:mvn-pdf}
f_X(x) = \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] \; .
$$

Plugging in $n = 2$, $\mu = \left[ \begin{matrix} \mu_1 \\\\ \mu_2 \end{matrix} \right]$ and $\Sigma = \left[ \begin{matrix} \sigma_1^2 \& \sigma_{12} \\\\ \sigma_{12} \& \sigma_2^2 \end{matrix} \right]$, we obtain:

$$ \label{eq:bvn-pdf-s1}
\begin{split}
f_X(x) &= \frac{1}{\sqrt{(2 \pi)^2 \left| \left[ \begin{matrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{matrix} \right] \right|}} \cdot \exp \left[ -\frac{1}{2} \left( \left[ \begin{matrix} x_1 \\ x_2 \end{matrix} \right] - \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right] \right)^\mathrm{T} \left[ \begin{matrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{matrix} \right]^{-1} \left( \left[ \begin{matrix} x_1 \\ x_2 \end{matrix} \right] - \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right] \right) \right] \\
&= \frac{1}{2 \pi \left| \left[ \begin{matrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{matrix} \right] \right|^\frac{1}{2}} \cdot \exp \left[ -\frac{1}{2} \left[ \begin{matrix} (x_1-\mu_1) & (x_2-\mu_2) \end{matrix} \right] \left[ \begin{matrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{matrix} \right]^{-1} \left[ \begin{matrix} (x_1-\mu_1) \\ (x_2-\mu_2) \end{matrix} \right] \right] \; .
\end{split}
$$

Using the determinant of a $2 \times 2$ matrix

$$ \label{eq:det-2x2}
\left| \left[ \begin{matrix} a & b \\ c & d \end{matrix} \right] \right| = a d - b c
$$

and the inverse of of a $2 \times 2$ matrix

$$ \label{eq:inv-2x2}
\left[ \begin{matrix} a & b \\ c & d \end{matrix} \right]^{-1} = \frac{1}{a d - b c} \left[ \begin{matrix} d & -b \\ -c & a \end{matrix} \right] \; ,
$$

the [probability density function](/D/pdf) becomes:

$$ \label{eq:bvn-pdf-s2}
\begin{split}
f_X(x) &= \frac{1}{2 \pi \sqrt{\sigma_1^2 \sigma_2^2 - \sigma_{12}^2}} \cdot \exp \left[ -\frac{1}{2 (\sigma_1^2 \sigma_2^2 - \sigma_{12}^2)} \left[ \begin{matrix} (x_1-\mu_1) & (x_2-\mu_2) \end{matrix} \right] \left[ \begin{matrix} \sigma_2^2 & -\sigma_{12} \\ -\sigma_{12} & \sigma_1^2 \end{matrix} \right] \left[ \begin{matrix} (x_1-\mu_1) \\ (x_2-\mu_2) \end{matrix} \right] \right] \\
&= \frac{1}{2 \pi \sqrt{\sigma_1^2 \sigma_2^2 - \sigma_{12}^2}} \cdot \exp \left[ -\frac{1}{2 (\sigma_1^2 \sigma_2^2 - \sigma_{12}^2)} \left[ \begin{matrix} \sigma_2^2 (x_1-\mu_1) - \sigma_{12} (x_2-\mu_2) & \sigma_1^2 (x_2-\mu_2) - \sigma_{12} (x_1-\mu_1) \end{matrix} \right] \left[ \begin{matrix} (x_1-\mu_1) \\ (x_2-\mu_2) \end{matrix} \right] \right] \\
&= \frac{1}{2 \pi \sqrt{\sigma_1^2 \sigma_2^2 - \sigma_{12}^2}} \cdot \exp \left[ -\frac{1}{2 (\sigma_1^2 \sigma_2^2 - \sigma_{12}^2)} (\sigma_2^2 (x_1-\mu_1)^2 - \sigma_{12} (x_1-\mu_1)(x_2-\mu_2) + \sigma_1^2 (x_2-\mu_2)^2 - \sigma_{12} (x_1-\mu_1)(x_2-\mu_2)) \right] \\
&= \frac{1}{2 \pi \sqrt{\sigma_1^2 \sigma_2^2 - \sigma_{12}^2}} \cdot \exp \left[ -\frac{1}{2} \frac{\sigma_2^2 (x_1-\mu_1)^2 - 2 \sigma_{12} (x_1-\mu_1)(x_2-\mu_2) + \sigma_1^2 (x_2-\mu_2)^2}{\sigma_1^2 \sigma_2^2 - \sigma_{12}^2} \right] \; .
\end{split}
$$