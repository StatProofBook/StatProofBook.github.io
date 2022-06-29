---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-05-20 18:23:00

title: "Normal-gamma distribution is a special case of normal-Wishart distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Normal-gamma distribution"
theorem: "Special case of normal-Wishart distribution"

sources:

proof_id: "P324"
shortcut: "ng-nw"
username: "JoramSoch"
---


**Theorem:** The [normal-gamma distribution](/D/ng) is a special case of the [normal-Wishart distribution](/D/nw) where the number of columns of the [random matrices](/D/rmat) is $p = 1$.


**Proof:** Let $X$ be an $n \times p$ real matrix and let $Y$ be a $p \times p$ positive-definite symmetric matrix, such that $X$ and $Y$ jointly follow a [normal-Wishart distribution](/D/nw):

$$ \label{eq:nw}
X,Y \sim \mathrm{NW}(M, U, V, \nu) \; .
$$

Then, $X$ and $Y$ [are described by the probability density function](/P/nw-pdf)

$$ \label{eq:nw-pdf}
\begin{split}
p(X,Y) = \; & \frac{1}{\sqrt{(2\pi)^{np} |U|^p |V|^{\nu}}} \cdot \frac{\sqrt{2^{-\nu p}}}{\Gamma_p \left( \frac{\nu}{2} \right)} \cdot |Y|^{(\nu+n-p-1)/2} \cdot \\
& \exp\left[-\frac{1}{2} \mathrm{tr}\left( Y \left[ (X-M)^\mathrm{T} \, U^{-1} (X-M) + V^{-1} \right] \right) \right]
\end{split}
$$

where $\lvert A \rvert$ is a matrix determinant, $A^{-1}$ is a matrix inverse and $\Gamma_p(x)$ is the multivariate gamma function of order $p$. If $p = 1$, then $\Gamma_p(x) = \Gamma(x)$ is the ordinary gamma function, $x = X$ is a column vector and $y = Y$ is a real number. Thus, the [probability density function](/D/pdf) of $x$ and $y$ can be developed as

$$ \label{eq:ng-pdf-s1}
\begin{split}
p(x,y) = \; & \frac{1}{\sqrt{(2\pi)^n |U| |V|^{\nu}}} \cdot \frac{\sqrt{2^{-\nu}}}{\Gamma \left( \frac{\nu}{2} \right)} \cdot y^{(\nu+n-2)/2} \cdot \\
& \exp\left[-\frac{1}{2} \mathrm{tr}\left( y \left[ (x-M)^\mathrm{T} \, U^{-1} (x-M) + V^{-1} \right] \right) \right] \\
= \; & \sqrt{\frac{|U^{-1}|}{(2\pi)^n}} \cdot \frac{\sqrt{\left(2 |V|\right)^{-\nu}}}{\Gamma \left( \frac{\nu}{2} \right)} \cdot y^{\frac{\nu}{2}+\frac{n}{2}-1} \cdot \\
& \exp\left[-\frac{1}{2} \left( y \left[ (x-M)^\mathrm{T} \, U^{-1} (x-M) + 2 \left(2 V\right)^{-1} \right] \right) \right] \\
= \; & \sqrt{\frac{|U^{-1}|}{(2\pi)^n}} \cdot \frac{\left(\frac{1}{2 |V|}\right)^{\frac{\nu}{2}}}{\Gamma \left( \frac{\nu}{2} \right)} \cdot y^{\frac{\nu}{2}+\frac{n}{2}-1} \cdot \\
& \exp\left[-\frac{y}{2} \left( (x-M)^\mathrm{T} \, U^{-1} (x-M) + 2 \left(\frac{1}{2 V}\right) \right) \right] \\
\end{split}
$$

In the [matrix-normal distribution](/D/matn), we have $M \in \mathbb{R}^{n \times p}$, $U \in \mathbb{R}^{n \times n}$, $V \in \mathbb{R}^{p \times p}$ and $\nu \in \mathbb{R}$. Thus, with $p = 1$, $M$ becomes a column vector and $V$ becomes a real number, such that $V = \lvert V \rvert = 1/V^{-1}$. Finally, substituting $\mu = M$, $\Lambda = U^{-1}$, $a = \frac{\nu}{2}$ and $b = \frac{1}{2V}$, we get

$$ \label{eq:ng-pdf-s2}
p(x,y) = \sqrt{\frac{|\Lambda|}{(2 \pi)^n}} \frac{b^a}{\Gamma(a)} \cdot y^{a+\frac{n}{2}-1} \exp \left[ -\frac{y}{2} \left( (x-\mu)^\mathrm{T} \Lambda (x-\mu) + 2b \right) \right]
$$

which is the [probability density function of the normal-gamma distribution](/P/ng-pdf).