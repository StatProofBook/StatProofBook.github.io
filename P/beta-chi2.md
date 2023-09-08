---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-07 13:20:00

title: "Relationship between chi-squared distribution and beta distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Beta distribution"
theorem: "Relationship to chi-squared distribution"

sources:
  - authors: "Probability Fact"
    year: 2021
    title: "If X ~ chisq(m) and Y ~ chisq(n) are independent"
    in: "Twitter"
    pages: "retrieved on 2022-10-17"
    url: "https://twitter.com/ProbFact/status/1450492787854647300"

proof_id: "P356"
shortcut: "beta-chi2"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be [independent](/D/ind) [random variables](/D/rvar) following [chi-squared distributions](/D/chi2):

$$ \label{eq:chi2}
X \sim \chi^2(m) \quad \text{and} \quad Y \sim \chi^2(n) \; .
$$

Then, the quantity $X/(X+Y)$ follows a [beta distribution](/D/beta):

$$ \label{eq:beta-chi2}
\frac{X}{X+Y} \sim \mathrm{Bet}\left( \frac{m}{2}, \frac{n}{2} \right) \; .
$$


**Proof:** The [probability density function of the chi-squared distribution](/P/chi2-pdf) is

$$ \label{eq:chi2-pdf}
X \sim \chi^2(u) \quad \Rightarrow \quad f_X(x) = \frac{1}{\Gamma\left( \frac{u}{2} \right) \cdot 2^{u/2}} \cdot x^{\frac{u}{2}-1} \cdot e^{-\frac{x}{2}} \; .
$$

Define the random variables $Z$ and $W$ as functions of $X$ and $Y$

$$ \label{eq:ZW-XY}
\begin{split}
Z &= \frac{X}{X+Y} \\
W &= Y \; ,
\end{split}
$$

such that the inverse functions $X$ and $Y$ in terms of $Z$ and $W$ are

$$ \label{eq:XY-ZW}
\begin{split}
X &= \frac{ZW}{1-Z} \\
Y &= W \; .
\end{split}
$$

This implies the following Jacobian matrix and determinant:

$$ \label{eq:XY-ZW-jac}
\begin{split}
J &= \left[ \begin{matrix}
\frac{\mathrm{d}X}{\mathrm{d}Z} & \frac{\mathrm{d}X}{\mathrm{d}W} \\
\frac{\mathrm{d}Y}{\mathrm{d}Z} & \frac{\mathrm{d}Y}{\mathrm{d}W}
\end{matrix} \right]
= \left[ \begin{matrix}
\frac{W}{(1-Z)^2} & \frac{Z}{1-Z} \\
0 & 1
\end{matrix} \right] \\
\lvert J \rvert  &= \frac{W}{(1-Z)^2} \; .
\end{split}
$$

Because $X$ and $Y$ are [independent](/D/ind), the [joint density](/D/dist-joint) of $X$ and $Y$ is [equal to the product](/P/prob-ind) of the [marginal densities](/D/dist-marg):

$$ \label{eq:f-XY}
f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y) \; .
$$

With the [probability density function of an invertible function](/P/pdf-invfct), the [joint density](/D/dist-joint) of $Z$ and $W$ can be derived as:

$$ \label{eq:f-ZW-s1}
f_{Z,W}(z,w) = f_{X,Y}(x,y) \cdot \lvert J \rvert \; .
$$

Substituting \eqref{eq:XY-ZW} into \eqref{eq:chi2-pdf}, and then with \eqref{eq:XY-ZW-jac} into \eqref{eq:f-ZW-s1}, we get:

$$ \label{eq:f-ZW-s2}
\begin{split}
f_{Z,W}(z,w) &= f_X\left( \frac{zw}{1-z} \right) \cdot f_Y(w) \cdot \lvert J \rvert \\
&= \frac{1}{\Gamma\left( \frac{m}{2} \right) \cdot 2^{m/2}} \cdot \left( \frac{zw}{1-z} \right)^{\frac{m}{2}-1} \cdot e^{-\frac{1}{2} \left( \frac{zw}{1-z} \right)} \cdot \frac{1}{\Gamma\left( \frac{n}{2} \right) \cdot 2^{n/2}} \cdot w^{\frac{n}{2}-1} \cdot e^{-\frac{w}{2}} \cdot \frac{w}{(1-z)^2} \\
&= \frac{1}{\Gamma\left( \frac{m}{2} \right) \Gamma\left( \frac{n}{2} \right) \cdot 2^{m/2} 2^{n/2}} \cdot \left( \frac{z}{1-z} \right)^{\frac{m}{2}-1} \left( \frac{1}{(1-z)} \right)^2 \cdot w^{\frac{m}{2}+\frac{n}{2}-1} e^{-\frac{1}{2} \left( \frac{zw}{1-z} + \frac{w(1-z)}{1-z} \right)} \\
&= \frac{1}{\Gamma\left( \frac{m}{2} \right) \Gamma\left( \frac{n}{2} \right) \cdot 2^{(m+n)/2}} \cdot z^{\frac{m}{2}-1} \cdot (1-z)^{-\frac{m}{2}-1} \cdot w^{\frac{m+n}{2}-1} \cdot e^{-\frac{1}{2} \left( \frac{w}{1-z} \right)} \; .
\end{split}
$$

The [marginal density](/D/dist-marg) of $Z$ can now be [obtained by integrating out](/D/dist-marg) $W$:

$$ \label{eq:f-Z-s1}
\begin{split}
f_Z(z) &= \int_{0}^{\infty} f_{Z,W}(z,w) \, \mathrm{d}w \\
&= \frac{1}{\Gamma\left( \frac{m}{2} \right) \Gamma\left( \frac{n}{2} \right) \cdot 2^{(m+n)/2}} \cdot z^{\frac{m}{2}-1} \cdot (1-z)^{-\frac{m}{2}-1} \cdot \int_{0}^{\infty} w^{\frac{m+n}{2}-1} \cdot e^{-\frac{1}{2} \left( \frac{w}{1-z} \right)} \, \mathrm{d}w \\
&= \frac{1}{\Gamma\left( \frac{m}{2} \right) \Gamma\left( \frac{n}{2} \right) \cdot 2^{(m+n)/2}} \cdot z^{\frac{m}{2}-1} \cdot (1-z)^{-\frac{m}{2}-1} \cdot \frac{\Gamma\left( \frac{m+n}{2} \right)}{\left( \frac{1}{2(1-z)} \right)^{\frac{m+n}{2}}} \cdot \\
&\hphantom{=} \int_{0}^{\infty} \frac{\left( \frac{1}{2(1-z)} \right)^{\frac{m+n}{2}}}{\Gamma\left( \frac{m+n}{2} \right)} \cdot w^{\frac{m+n}{2}-1} \cdot e^{-\frac{1}{2(1-z)} \, w} \, \mathrm{d}w \; .
\end{split}
$$

At this point, we can recognize that the integrand is equal to the [probability density function of a gamma distribution](/P/gam-pdf) with

$$ \label{eq:f-W-gam-ab}
a = \frac{m+n}{2} \quad \text{and} \quad b = \frac{1}{2(1-z)} \; ,
$$

and [because a probability density function integrates to one](/D/pdf), we have:

$$ \label{eq:f-Z-s2}
\begin{split}
f_Z(z) &= \frac{1}{\Gamma\left( \frac{m}{2} \right) \Gamma\left( \frac{n}{2} \right) \cdot 2^{(m+n)/2}} \cdot z^{\frac{m}{2}-1} \cdot (1-z)^{-\frac{m}{2}-1} \cdot \frac{\Gamma\left( \frac{m+n}{2} \right)}{\left( \frac{1}{2(1-z)} \right)^{\frac{m+n}{2}}} \\
&= \frac{\Gamma\left( \frac{m+n}{2} \right) \cdot 2^{(m+n)/2}}{\Gamma\left( \frac{m}{2} \right) \Gamma\left( \frac{n}{2} \right) \cdot 2^{(m+n)/2}} \cdot z^{\frac{m}{2}-1} \cdot (1-z)^{-\frac{m}{2}+\frac{m+n}{2}-1} \\
&= \frac{\Gamma\left( \frac{m+n}{2} \right)}{\Gamma\left( \frac{m}{2} \right) \Gamma\left( \frac{n}{2} \right)} \cdot z^{\frac{m}{2}-1} \cdot (1-z)^{\frac{n}{2}-1} \; .
\end{split}
$$

With the [definition of the beta function](/P/beta-mean), this becomes

$$ \label{eq:f-Z-s3}
f_Z(z) = \frac{1}{\mathrm{B}\left( \frac{m}{2}, \frac{n}{2} \right)} \cdot z^{\frac{m}{2}-1} \cdot (1-z)^{\frac{n}{2}-1}
$$

which is the [probability density function of the beta distribution](/P/beta-pdf) with parameters

$$ \label{eq:beta-chi2-para}
\alpha = \frac{m}{2} \quad \mathrm{and} \quad \beta = \frac{n}{2} \; ,
$$

such that

$$ \label{eq:beta-chi2-qed}
Z \sim \mathrm{Bet}\left( \frac{m}{2}, \frac{n}{2} \right) \; .
$$