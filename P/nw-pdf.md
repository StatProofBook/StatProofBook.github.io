---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-05-14 23:58:00

title: "Probability density function of the normal-Wishart distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Normal-Wishart distribution"
theorem: "Probability density function"

sources:

proof_id: "P323"
shortcut: "nw-pdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ follow a [normal-Wishart distribution](/D/nw):

$$ \label{eq:nw}
X,Y \sim \mathrm{NW}(M, U, V, \nu) \; .
$$

Then, the [joint probability](/D/prob-joint) [density function](/D/pdf) of $X$ and $Y$ is

$$ \label{eq:nw-pdf}
\begin{split}
p(X,Y) = \; & \frac{1}{\sqrt{(2\pi)^{np} |U|^p |V|^{\nu}}} \cdot \frac{\sqrt{2^{-\nu p}}}{\Gamma_p \left( \frac{\nu}{2} \right)} \cdot |Y|^{(\nu+n-p-1)/2} \cdot \\
& \exp\left[-\frac{1}{2} \mathrm{tr}\left( Y \left[ (X-M)^\mathrm{T} \, U^{-1} (X-M) + V^{-1} \right] \right) \right] \; .
\end{split}
$$


**Proof:** The [normal-Wishart distribution](/D/nw) is defined as $X$ conditional on $Y$ following a [matrix-normal distribution](/D/matn) and $Y$ following a [Wishart distribution](/D/wish):

$$ \label{eq:matn-wish}
\begin{split}
X \vert Y &\sim \mathcal{MN}(M, U, Y^{-1}) \\
Y &\sim \mathcal{W}(V, \nu) \; .
\end{split}
$$

Thus, using the [probability density function of the matrix-normal distribution](/P/matn-pdf) and the [probability density function of the Wishart distribution](/P/wish-pdf), we have the following probabilities:

$$ \label{eq:matn-wish-pdf}
\begin{split}
p(X \vert Y) &= \mathcal{MN}(X; M, U, Y^{-1}) \\
&= \sqrt{\frac{|Y|^n}{(2\pi)^{np} |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( Y (X-M)^\mathrm{T} \, U^{-1} (X-M) \right) \right] \\
p(Y) &= \mathcal{W}(Y; V, \nu) \\
&= \frac{1}{\Gamma_p \left( \frac{\nu}{2} \right)} \cdot \frac{1}{\sqrt{2^{\nu p} |V|^{\nu}}} \cdot |Y|^{(\nu-p-1)/2} \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( V^{-1} Y \right) \right] \; .
\end{split}
$$

The [law of conditional probability](/D/prob-cond) implies that

$$ \label{eq:prob-cond}
p(X,Y) = p(X \vert Y) \, p(Y) \; ,
$$

such that the normal-Wishart density function becomes:

$$ \label{eq:nw-pdf-qed}
\begin{split}
p(X,Y) = \; & \mathcal{MN}(X; M, U, Y^{-1}) \cdot \mathcal{W}(Y; V, \nu) \\
= \; & \sqrt{\frac{|Y|^n}{(2\pi)^{np} |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( Y (X-M)^\mathrm{T} \, U^{-1} (X-M) \right) \right] \cdot \\
& \frac{1}{\Gamma_p \left( \frac{\nu}{2} \right)} \cdot \frac{1}{\sqrt{2^{\nu p} |V|^{\nu}}} \cdot |Y|^{(\nu-p-1)/2} \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( V^{-1} Y \right) \right] \\
= \; & \frac{1}{\sqrt{(2\pi)^{np} |U|^p |V|^{\nu}}} \cdot \frac{\sqrt{2^{-\nu p}}}{\Gamma_p \left( \frac{\nu}{2} \right)} \cdot |Y|^{(\nu+n-p-1)/2} \cdot \\
& \exp\left[-\frac{1}{2} \mathrm{tr}\left( Y \left[ (X-M)^\mathrm{T} \, U^{-1} (X-M) + V^{-1} \right] \right) \right] \; .
\end{split}
$$