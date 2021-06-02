---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-29 21:42:00

title: "Marginal distributions of the normal-gamma distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Normal-gamma distribution"
theorem: "Marginal distributions"

sources:

proof_id: "P36"
shortcut: "ng-marg"
username: "JoramSoch"
---


**Theorem:** Let $x$ and $y$ follow a [normal-gamma distribution](/D/ng):

$$ \label{eq:ng}
x,y \sim \mathrm{NG}(\mu, \Lambda, a, b) \; .
$$

Then, the [marginal distribution](/D/dist-marg) of $y$ is a [gamma distribution](/D/gam)

$$ \label{eq:ng-marg-y}
y \sim \mathrm{Gam}(a, b)
$$

and the [marginal distribution](/D/dist-marg) of $x$ is a [multivariate t-distribution](/D/mvt)

$$ \label{eq:ng-marg-x}
x \sim t\left( \mu, \left(\frac{a}{b} \Lambda \right)^{-1}, 2a \right) \; .
$$


**Proof:** The [probability density function of the normal-gamma distribution](/P/ng-pdf) is given by

$$ \label{eq:ng-pdf}
\begin{split}
p(x,y) &= p(x|y) \cdot p(y) \\
p(x|y) &= \mathcal{N}(x; \mu, (y \Lambda)^{-1}) \\
p(y) &= \mathrm{Gam}(y; a, b) \; .
\end{split}
$$

<br>
Using the [law of marginal probability](/D/prob-marg), the marginal distribution of $y$ can be derived as

$$ \label{eq:ng-marg-y-qed}
\begin{split}
p(y) &= \int p(x,y) \, \mathrm{d}x \\
&= \int \mathcal{N}(x; \mu, (y \Lambda)^{-1}) \, \mathrm{Gam}(y; a, b) \, \mathrm{d}x \\
&= \mathrm{Gam}(y; a, b) \int \mathcal{N}(x; \mu, (y \Lambda)^{-1}) \, \mathrm{d}x \\
&= \mathrm{Gam}(y; a, b)
\end{split}
$$

which is the [probability density function of the gamma distribution](/P/gam-pdf) with shape parameter $a$ and rate parameter $b$.

<br>
Using the [law of marginal probability](/D/prob-marg), the marginal distribution of $x$ can be derived as

$$ \label{eq:ng-marg-x-qed}
\begin{split}
p(x) &= \int p(x,y) \, \mathrm{d}y \\
&= \int \mathcal{N}(x; \mu, (y \Lambda)^{-1}) \, \mathrm{Gam}(y; a, b) \, \mathrm{d}y \\
&= \int \sqrt{\frac{|y \Lambda|}{(2 \pi)^n}} \, \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} (y \Lambda) (x-\mu) \right] \cdot \frac{b^a}{\Gamma(a)} \, y^{a-1} \exp[-b y] \, \mathrm{d}y \\
&= \int \sqrt{\frac{y^n |\Lambda|}{(2 \pi)^n}} \, \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} (y \Lambda) (x-\mu) \right] \cdot \frac{b^a}{\Gamma(a)} \, y^{a-1} \exp[-b y] \, \mathrm{d}y \\
&= \int \sqrt{\frac{|\Lambda|}{(2 \pi)^n}} \cdot \frac{b^a}{\Gamma(a)} \cdot y^{a+\frac{n}{2}-1} \cdot \exp \left[ -\left( b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right) y \right] \mathrm{d}y \\
&= \int \sqrt{\frac{|\Lambda|}{(2 \pi)^n}} \cdot \frac{b^a}{\Gamma(a)} \cdot \frac{\Gamma\left( a+\frac{n}{2} \right)}{\left( b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right)^{a+\frac{n}{2}}} \cdot \mathrm{Gam}\left( y; a+\frac{n}{2}, b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right) \mathrm{d}y \\
&= \sqrt{\frac{|\Lambda|}{(2 \pi)^n}} \cdot \frac{b^a}{\Gamma(a)} \cdot \frac{\Gamma\left( a+\frac{n}{2} \right)}{\left( b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right)^{a+\frac{n}{2}}} \int \mathrm{Gam}\left( y; a+\frac{n}{2}, b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right) \mathrm{d}y \\
&= \sqrt{\frac{|\Lambda|}{(2 \pi)^n}} \cdot \frac{b^a}{\Gamma(a)} \cdot \frac{\Gamma\left( a+\frac{n}{2} \right)}{\left( b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right)^{a+\frac{n}{2}}} \\
&= \frac{\sqrt{|\Lambda|}}{(2 \pi)^\frac{n}{2}} \cdot \frac{\Gamma\left( \frac{2a+n}{2} \right)}{\Gamma\left( \frac{2a}{2} \right)} \cdot b^a \cdot \left( b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right)^{-\left( a+\frac{n}{2} \right)} \\
&= \frac{\sqrt{|\Lambda|}}{\pi^\frac{n}{2}} \cdot \frac{\Gamma\left( \frac{2a+n}{2} \right)}{\Gamma\left( \frac{2a}{2} \right)} \cdot \left( \frac{1}{b} \right)^{-a} \cdot \left( b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right)^{-a} \cdot 2^{-\frac{n}{2}} \cdot \left( b + \frac{1}{2} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right)^{-\frac{n}{2}} \\
&= \frac{\sqrt{|\Lambda|}}{\pi^\frac{n}{2}} \cdot \frac{\Gamma\left( \frac{2a+n}{2} \right)}{\Gamma\left( \frac{2a}{2} \right)} \cdot \left( 1 + \frac{1}{2b} (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right)^{-a} \cdot \left( 2b + (x-\mu)^\mathrm{T} \Lambda (x-\mu) \right)^{-\frac{n}{2}} \\
&= \frac{\sqrt{|\Lambda|}}{\pi^\frac{n}{2}} \cdot \frac{\Gamma\left( \frac{2a+n}{2} \right)}{\Gamma\left( \frac{2a}{2} \right)} \cdot \left( \frac{1}{2a} \right)^{-a} \cdot \left( 2a + (x-\mu)^\mathrm{T} \left( \frac{a}{b}\Lambda \right) (x-\mu) \right)^{-a} \cdot \left( \frac{b}{a} \right)^{-\frac{n}{2}} \cdot \left( 2a + (x-\mu)^\mathrm{T} \left( \frac{a}{b}\Lambda \right) (x-\mu) \right)^{-\frac{n}{2}} \\
&= \frac{\sqrt{\left( \frac{a}{b} \right)^n |\Lambda|}}{(2a)^{-a}\,\pi^\frac{n}{2}} \cdot \frac{\Gamma\left( \frac{2a+n}{2} \right)}{\Gamma\left( \frac{2a}{2} \right)} \cdot \left( 2a + (x-\mu)^\mathrm{T} \left( \frac{a}{b}\Lambda \right) (x-\mu) \right)^{-a} \cdot \left( 2a + (x-\mu)^\mathrm{T} \left( \frac{a}{b}\Lambda \right) (x-\mu) \right)^{-\frac{n}{2}} \\
&= \frac{\sqrt{\left( \frac{a}{b} \right)^n |\Lambda|}}{(2a)^{-a}\,\pi^\frac{n}{2}} \cdot \frac{\Gamma\left( \frac{2a+n}{2} \right)}{\Gamma\left( \frac{2a}{2} \right)} \cdot (2a)^{-a} \cdot \left( 1 + \frac{1}{2a} (x-\mu)^\mathrm{T} \left( \frac{a}{b}\Lambda \right) (x-\mu) \right)^{-a} \cdot (2a)^{-\frac{n}{2}} \cdot \left( 1 + \frac{1}{2a} (x-\mu)^\mathrm{T} \left( \frac{a}{b}\Lambda \right) (x-\mu) \right)^{-\frac{n}{2}} \\
&= \frac{\sqrt{\left( \frac{a}{b} \right)^n |\Lambda|}}{(2a)^\frac{n}{2}\,\pi^\frac{n}{2}} \cdot \frac{\Gamma\left( \frac{2a+n}{2} \right)}{\Gamma\left( \frac{2a}{2} \right)} \cdot \left( 1 + \frac{1}{2a} (x-\mu)^\mathrm{T} \left( \frac{a}{b}\Lambda \right) (x-\mu) \right)^{-\frac{2a+n}{2}} \\
&= \sqrt{\frac{\left| \frac{a}{b}\,\Lambda \right|}{(2a\,\pi)^n}} \cdot \frac{\Gamma\left( \frac{2a+n}{2} \right)}{\Gamma\left( \frac{2a}{2} \right)} \cdot \left( 1 + \frac{1}{2a} (x-\mu)^\mathrm{T} \left( \frac{a}{b}\Lambda \right) (x-\mu) \right)^{-\frac{2a+n}{2}} \\
\end{split}
$$

which is the [probability density function of a multivariate t-distribution](/P/mvt-pdf) with mean vector $\mu$, shape matrix $\left( \frac{a}{b}\Lambda \right)^{-1}$ and $2a$ degrees of freedom.