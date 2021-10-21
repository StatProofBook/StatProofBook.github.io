---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-12 08:15:00

title: "Probability density function of the t-distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "t-distribution"
theorem: "Probability density function"

sources:
  - authors: "Computation Empire"
    year: 2021
    title: "Student's t Distribution: Derivation of PDF"
    in: "YouTube"
    pages: "retrieved on 2021-10-11"
    url: "https://www.youtube.com/watch?v=6BraaGEVRY8"

proof_id: "P263"
shortcut: "t-pdf"
username: "JoramSoch"
---


**Theorem:** Let $T$ be a [random variable](/D/rvar) following a [t-distribution](/D/t):

$$ \label{eq:t}
T \sim t(\nu) \; .
$$

Then, the [probability density function](/D/pdf) of $T$ is

$$ \label{eq:t-pdf}
f_T(t) = \frac{\Gamma\left( \frac{\nu+1}{2} \right)}{\Gamma\left( \frac{\nu}{2} \right) \cdot \sqrt{\nu \pi}} \cdot \left( \frac{t^2}{\nu}+1 \right)^{-\frac{\nu+1}{2}} \; .
$$


**Proof:** A [t-distributed random variable](/D/t) is defined as the ratio of a [standard normal random variable](/D/snorm) and the square root of a [chi-squared random variable](/D/chi2), divided by its [degrees of freedom](/D/dof)

$$ \label{eq:t-def}
X \sim \mathcal{N}(0,1), \; Y \sim \chi^2(\nu) \quad \Rightarrow \quad T = \frac{X}{\sqrt{Y/\nu}} \sim t(\nu)
$$

where $X$ and $Y$ are [independent of each other](/D/ind).

The [probability density function](/P/norm-pdf) of the [standard normal distribution](/D/snorm) is

$$ \label{eq:snorm-pdf}
f_X(x) = \frac{1}{\sqrt{2 \pi}} \cdot e^{-\frac{x^2}{2}}
$$

and the [probability density function of the chi-squared distribution](/P/chi2-pdf) is

$$ \label{eq:chi2-pdf}
f_Y(y) = \frac{1}{\Gamma\left( \frac{\nu}{2} \right) \cdot 2^{\nu/2}} \cdot y^{\frac{\nu}{2}-1} \cdot e^{-\frac{y}{2}} \; .
$$

Define the random variables $T$ and $W$ as functions of $X$ and $Y$

$$ \label{eq:TW-XY}
\begin{split}
T &= X \cdot \sqrt{\frac{\nu}{Y}} \\
W &= Y \; ,
\end{split}
$$

such that the inverse functions $X$ and $Y$ in terms of $T$ and $W$ are

$$ \label{eq:XY-TW}
\begin{split}
X &= T \cdot \sqrt{\frac{W}{\nu}} \\
Y &= W \; .
\end{split}
$$

This implies the following Jacobian matrix and determinant:

$$ \label{eq:XY-TW-jac}
\begin{split}
J &= \left[ \begin{matrix}
\frac{\mathrm{d}X}{\mathrm{d}T} & \frac{\mathrm{d}X}{\mathrm{d}W} \\
\frac{\mathrm{d}Y}{\mathrm{d}T} & \frac{\mathrm{d}Y}{\mathrm{d}W}
\end{matrix} \right]
= \left[ \begin{matrix}
\sqrt{\frac{W}{\nu}} & \frac{T}{2 \sqrt{W/\nu}} \\
0 & 1
\end{matrix} \right] \\
\lvert J \rvert  &= \sqrt{\frac{W}{\nu}} \; .
\end{split}
$$

Because $X$ and $Y$ are [independent](/D/ind), the [joint density](/D/dist-joint) of $X$ and $Y$ is [equal to the product](/P/prob-ind) of the [marginal densities](/D/dist-marg):

$$ \label{eq:f-XY}
f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y) \; .
$$

With the [probability density function of an invertible function](/P/pdf-invfct), the [joint density](/D/dist-joint) of $T$ and $W$ can be derived as:

$$ \label{eq:f-TW-s1}
f_{T,W}(t,w) = f_{X,Y}(x,y) \cdot \lvert J \rvert \; .
$$

Substituting \eqref{eq:XY-TW} into \eqref{eq:snorm-pdf} and \eqref{eq:chi2-pdf}, and then with \eqref{eq:XY-TW-jac} into \eqref{eq:f-TW-s1}, we get:

$$ \label{eq:f-TW-s2}
\begin{split}
f_{T,W}(t,w) &= f_X\left( t \cdot \sqrt{\frac{w}{\nu}} \right) \cdot f_Y(w) \cdot \lvert J \rvert \\
&= \frac{1}{\sqrt{2 \pi}} \cdot e^{-\frac{\left( t \cdot \sqrt{\frac{w}{\nu}} \right)^2}{2}} \cdot \frac{1}{\Gamma\left( \frac{\nu}{2} \right) \cdot 2^{\nu/2}} \cdot w^{\frac{\nu}{2}-1} \cdot e^{-\frac{w}{2}} \cdot \sqrt{\frac{w}{\nu}} \\
&= \frac{1}{\sqrt{2 \pi \nu} \cdot \Gamma\left( \frac{\nu}{2} \right) \cdot 2^{\nu/2}} \cdot w^{\frac{\nu+1}{2}-1} \cdot e^{-\frac{w}{2} \left( \frac{t^2}{\nu} + 1 \right)} \; .
\end{split}
$$

The [marginal density](/D/dist-marg) of $T$ can now be [obtained by integrating out](/D/prob-marg) $W$:

$$ \label{eq:f-T-s1}
\begin{split}
f_T(t) &= \int_{0}^{\infty} f_{T,W}(t,w) \, \mathrm{d}w \\
&= \frac{1}{\sqrt{2 \pi \nu} \cdot \Gamma\left( \frac{\nu}{2} \right) \cdot 2^{\nu/2}} \cdot \int_{0}^{\infty} w^{\frac{\nu+1}{2}-1} \cdot \mathrm{exp}\left[ -\frac{1}{2}\left( \frac{t^2}{\nu}+1 \right) w \right] \, \mathrm{d}w \\
&= \frac{1}{\sqrt{2 \pi \nu} \cdot \Gamma\left( \frac{\nu}{2} \right) \cdot 2^{\nu/2}} \cdot \frac{\Gamma\left( \frac{\nu+1}{2} \right)}{\left[ \frac{1}{2}\left( \frac{t^2}{\nu}+1 \right) \right]^{(\nu+1)/2}} \cdot \int_{0}^{\infty} \frac{\left[ \frac{1}{2}\left( \frac{t^2}{\nu}+1 \right) \right]^{(\nu+1)/2}}{\Gamma\left( \frac{\nu+1}{2} \right)} \cdot w^{\frac{\nu+1}{2}-1} \cdot \mathrm{exp}\left[ -\frac{1}{2}\left( \frac{t^2}{\nu}+1 \right) w \right] \, \mathrm{d}w \; .
\end{split}
$$

At this point, we can recognize that the integrand is equal to the [probability density function of a gamma distribution](/P/gam-pdf) with

$$ \label{eq:f-W-gam-ab}
a = \frac{\nu+1}{2} \quad \text{and} \quad b = \frac{1}{2}\left( \frac{t^2}{\nu}+1 \right) \; ,
$$

and [because a probability density function integrates to one](/D/pdf), we finally have:

$$ \label{eq:f-T-s2}
\begin{split}
f_T(t) &= \frac{1}{\sqrt{2 \pi \nu} \cdot \Gamma\left( \frac{\nu}{2} \right) \cdot 2^{\nu/2}} \cdot \frac{\Gamma\left( \frac{\nu+1}{2} \right)}{\left[ \frac{1}{2}\left( \frac{t^2}{\nu}+1 \right) \right]^{(\nu+1)/2}} \\
&= \frac{\Gamma\left( \frac{\nu+1}{2} \right)}{\Gamma\left( \frac{\nu}{2} \right) \cdot \sqrt{\nu \pi}} \cdot \left( \frac{t^2}{\nu}+1 \right)^{-\frac{\nu+1}{2}} \; .
\end{split}
$$