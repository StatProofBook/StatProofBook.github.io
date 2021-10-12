---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-12 09:00:00

title: "Probability density function of the F-distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "F-distribution"
theorem: "Probability density function"

sources:
  - authors: "statisticsmatt"
    year: 2018
    title: "Statistical Distributions: Derive the F Distribution"
    in: "YouTube"
    pages: "retrieved on 2021-10-11"
    url: "https://www.youtube.com/watch?v=AmHiOKYmHkI"

proof_id: "P264"
shortcut: "f-pdf"
username: "JoramSoch"
---


**Theorem:** Let $F$ be a [random variable](/D/rvar) following an [F-distribution](/D/f):

$$ \label{eq:f}
F \sim F(u,v) \; .
$$

Then, the [probability density function](/D/pdf) of $F$ is

$$ \label{eq:f-pdf}
f_F(f) = \frac{\Gamma\left( \frac{u+v}{2} \right)}{\Gamma\left( \frac{u}{2} \right) \cdot \Gamma\left( \frac{v}{2} \right)} \cdot \left( \frac{u}{v} \right)^{\frac{u}{2}} \cdot f^{\frac{u}{2}-1} \cdot \left( \frac{u}{v}f+1 \right)^{-\frac{u+v}{2}} \; .
$$


**Proof:** An [F-distributed random variable](/D/f) is defined as the ratio of two [chi-squared random variables](/D/chi2), divided by their [degrees of freedom](/D/dof)

$$ \label{eq:f-def}
X \sim \chi^2(u), \; Y \sim \chi^2(v) \quad \Rightarrow \quad F = \frac{X/u}{Y/v} \sim F(u,v)
$$

where $X$ and $Y$ are [independent of each other](/D/ind).

The [probability density function of the chi-squared distribution](/P/chi2-pdf) is

$$ \label{eq:chi2-pdf}
f_X(x) = \frac{1}{\Gamma\left( \frac{u}{2} \right) \cdot 2^{u/2}} \cdot x^{\frac{u}{2}-1} \cdot e^{-\frac{x}{2}} \; .
$$

Define the random variables $F$ and $W$ as functions of $X$ and $Y$

$$ \label{eq:FW-XY}
\begin{split}
F &= \frac{X/u}{Y/v} \\
W &= Y \; ,
\end{split}
$$

such that the inverse functions $X$ and $Y$ in terms of $F$ and $W$ are

$$ \label{eq:XY-FW}
\begin{split}
X &= \frac{u}{v} F W \\
Y &= W \; .
\end{split}
$$

This implies the following Jacobian matrix and determinant:

$$ \label{eq:XY-FW-jac}
\begin{split}
J &= \left[ \begin{matrix}
\frac{\mathrm{d}X}{\mathrm{d}F} & \frac{\mathrm{d}X}{\mathrm{d}W} \\
\frac{\mathrm{d}Y}{\mathrm{d}F} & \frac{\mathrm{d}Y}{\mathrm{d}W}
\end{matrix} \right]
= \left[ \begin{matrix}
\frac{u}{v} W & \frac{u}{v} F \\
0 & 1
\end{matrix} \right] \\
\lvert J \rvert  &= \frac{u}{v} W \; .
\end{split}
$$

Because $X$ and $Y$ are [independent](/D/ind), the [joint density](/D/dist-joint) of $X$ and $Y$ is [equal to the product](/P/prob-ind) of the [marginal densities](/D/dist-marg):

$$ \label{eq:f-XY}
f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y) \; .
$$

With the [probability density function of an invertible function](/P/pdf-invfct), the [joint density](/D/dist-joint) of $T$ and $W$ can be derived as:

$$ \label{eq:f-FW-s1}
f_{F,W}(f,w) = f_{X,Y}(x,y) \cdot \lvert J \rvert \; .
$$

Substituting \eqref{eq:XY-FW} into \eqref{eq:chi2-pdf}, and then with \eqref{eq:XY-FW-jac} into \eqref{eq:f-FW-s1}, we get:

$$ \label{eq:f-FW-s2}
\begin{split}
f_{F,W}(f,w) &= f_X\left( \frac{u}{v} f w \right) \cdot f_Y(w) \cdot \lvert J \rvert \\
&= \frac{1}{\Gamma\left( \frac{u}{2} \right) \cdot 2^{u/2}} \cdot \left( \frac{u}{v} f w \right)^{\frac{u}{2}-1} \cdot e^{-\frac{1}{2} \left( \frac{u}{v} f w \right)} \cdot \frac{1}{\Gamma\left( \frac{v}{2} \right) \cdot 2^{v/2}} \cdot w^{\frac{v}{2}-1} \cdot e^{-\frac{w}{2}} \cdot \frac{u}{v} w \\
&= \frac{\left( \frac{u}{v} \right)^{\frac{u}{2}} \cdot f^{\frac{u}{2}-1}}{\Gamma\left( \frac{u}{2} \right) \cdot \Gamma\left( \frac{v}{2} \right) \cdot 2^{(u+v)/2}} \cdot w^{\frac{u+v}{2}-1} \cdot e^{-\frac{w}{2} \left( \frac{u}{v} f + 1 \right)} \; .
\end{split}
$$

The [marginal density](/D/dist-marg) of $F$ can now be [obtained by integrating out](/D/prob-marg) $W$:

$$ \label{eq:f-F-s1}
\begin{split}
f_F(f) &= \int_{0}^{\infty} f_{F,W}(f,w) \, \mathrm{d}w \\
&= \frac{\left( \frac{u}{v} \right)^{\frac{u}{2}} \cdot f^{\frac{u}{2}-1}}{\Gamma\left( \frac{u}{2} \right) \cdot \Gamma\left( \frac{v}{2} \right) \cdot 2^{(u+v)/2}} \cdot \int_{0}^{\infty} w^{\frac{u+v}{2}-1} \cdot \mathrm{exp}\left[ -\frac{1}{2} \left( \frac{u}{v} f + 1 \right) w \right] \, \mathrm{d}w \\
&= \frac{\left( \frac{u}{v} \right)^{\frac{u}{2}} \cdot f^{\frac{u}{2}-1}}{\Gamma\left( \frac{u}{2} \right) \cdot \Gamma\left( \frac{v}{2} \right) \cdot 2^{(u+v)/2}} \cdot \frac{\Gamma\left( \frac{u+v}{2} \right)}{\left[ \frac{1}{2}\left( \frac{u}{v} f + 1 \right) \right]^{(u+v)/2}} \cdot \int_{0}^{\infty} \frac{\left[ \frac{1}{2}\left( \frac{u}{v} f + 1 \right) \right]^{(u+v)/2}}{\Gamma\left( \frac{u+v}{2} \right)} \cdot w^{\frac{u+v}{2}-1} \cdot \mathrm{exp}\left[ -\frac{1}{2} \left( \frac{u}{v} f + 1 \right) w \right] \, \mathrm{d}w \; .
\end{split}
$$

At this point, we can recognize that the integrand is equal to the [probability density function of a gamma distribution](/P/gam-pdf) with

$$ \label{eq:f-W-gam-ab}
a = \frac{u+v}{2} \quad \text{and} \quad b = \frac{1}{2}\left( \frac{u}{v} f + 1 \right) \; ,
$$

and [because a probability density function integrates to one](/D/pdf), we finally have:

$$ \label{eq:f-F-s2}
\begin{split}
f_F(f) &= \frac{\left( \frac{u}{v} \right)^{\frac{u}{2}} \cdot f^{\frac{u}{2}-1}}{\Gamma\left( \frac{u}{2} \right) \cdot \Gamma\left( \frac{v}{2} \right) \cdot 2^{(u+v)/2}} \cdot \frac{\Gamma\left( \frac{u+v}{2} \right)}{\left[ \frac{1}{2}\left( \frac{u}{v} f + 1 \right) \right]^{(u+v)/2}} \\
&= \frac{\Gamma\left( \frac{u+v}{2} \right)}{\Gamma\left( \frac{u}{2} \right) \cdot \Gamma\left( \frac{v}{2} \right)} \cdot \left( \frac{u}{v} \right)^{\frac{u}{2}} \cdot f^{\frac{u}{2}-1} \cdot \left( \frac{u}{v}f+1 \right)^{-\frac{u+v}{2}} \; .
\end{split}
$$