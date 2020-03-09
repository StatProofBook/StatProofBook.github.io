---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-03 11:29:00

title: "Moment-generating function of the normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Moment-generating function"

sources:
  - authors: "ProofWiki"
    year: 2020
    title: "Moment Generating Function of Gaussian Distribution"
    in: "ProofWiki"
    pages: "retrieved on 2020-03-03"
    url: "https://proofwiki.org/wiki/Moment_Generating_Function_of_Gaussian_Distribution"

proof_id: "P71"
shortcut: "norm-mgf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [normal distribution](/D/norm):

$$ \label{eq:norm}
X \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [moment-generating function](/D/mgf) of $X$ is

$$ \label{eq:norm-mgf}
M_X(t) = \exp\left[ \mu t + \frac{1}{2} \sigma^2 t^2 \right] \; .
$$


**Proof:** The [probability density function of the normal distribution](/P/norm-pdf) is

$$ \label{eq:norm-pdf}
f_X(x) = \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right]
$$

and the [moment-generating function](/D/mgf) is defined as

$$ \label{eq:mgf-var}
M_X(t) = \mathrm{E} \left[ e^{tX} \right] \; .
$$

Using the [expected value for continuous random variables](/D/mean), the moment-generating function of $X$ therefore is

$$ \label{eq:norm-mgf-s1}
\begin{split}
M_X(t) &= \int_{-\infty}^{+\infty} \exp[tx] \cdot \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \, \mathrm{d}x \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \int_{-\infty}^{+\infty} \exp\left[ tx - \frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \, \mathrm{d}x \; .
\end{split}
$$

Substituting $u = (x-\mu)/(\sqrt{2}\sigma)$, i.e. $x = \sqrt{2}\sigma u + \mu$, we have

$$ \label{eq:norm-mgf-s2}
\begin{split}
M_X(t) &= \frac{1}{\sqrt{2 \pi} \sigma} \int_{(-\infty-\mu)/(\sqrt{2}\sigma)}^{(+\infty-\mu)/(\sqrt{2}\sigma)} \exp\left[ t\left( \sqrt{2} \sigma u + \mu \right) - \frac{1}{2} \left( \frac{ \sqrt{2} \sigma u + \mu - \mu}{\sigma} \right)^2 \right] \, \mathrm{d}\left( \sqrt{2} \sigma u + \mu \right) \\
&= \frac{\sqrt{2} \sigma}{\sqrt{2 \pi} \sigma} \int_{-\infty}^{+\infty} \exp\left[ \left( \sqrt{2} \sigma u + \mu \right) t - u^2 \right] \, \mathrm{d}u \\
&= \frac{\exp(\mu t)}{\sqrt{\pi}} \int_{-\infty}^{+\infty} \exp\left[ \sqrt{2} \sigma u t - u^2 \right] \, \mathrm{d}u \\
&= \frac{\exp(\mu t)}{\sqrt{\pi}} \int_{-\infty}^{+\infty} \exp\left[ - \left( u^2 - \sqrt{2} \sigma u t \right) \right] \, \mathrm{d}u \\
&= \frac{\exp(\mu t)}{\sqrt{\pi}} \int_{-\infty}^{+\infty} \exp\left[ - \left( u - \frac{\sqrt{2}}{2} \sigma t \right)^2 + \frac{1}{2} \sigma^2 t^2 \right] \, \mathrm{d}u \\
&= \frac{\exp\left[ \mu t + \frac{1}{2} \sigma^2 t^2 \right]}{\sqrt{\pi}} \int_{-\infty}^{+\infty} \exp\left[ - \left( u - \frac{\sqrt{2}}{2} \sigma t \right)^2 \right] \, \mathrm{d}u
\end{split}
$$

Now substituting $v = u - \sqrt{2}/2 \, \sigma t$, i.e. $u = v + \sqrt{2}/2 \, \sigma t$, we have

$$ \label{eq:norm-mgf-s3}
\begin{split}
M_X(t) &= \frac{\exp\left[ \mu t + \frac{1}{2} \sigma^2 t^2 \right]}{\sqrt{\pi}} \int_{-\infty - \sqrt{2}/2 \, \sigma t}^{+\infty - \sqrt{2}/2 \, \sigma t} \exp\left[ -v^2 \right] \, \mathrm{d}\left( v + \sqrt{2}/2 \, \sigma t \right) \\
&= \frac{\exp\left[ \mu t + \frac{1}{2} \sigma^2 t^2 \right]}{\sqrt{\pi}} \int_{-\infty}^{+\infty} \exp\left[ -v^2 \right] \, \mathrm{d}v \; .
\end{split}
$$

With the [Gaussian integral](/P/norm-gi)

$$ \label{eq:gauss}
\int_{-\infty}^{+\infty} \exp\left[ -x^2 \right] \, \mathrm{d}x = \sqrt{\pi} \; ,
$$

this finally becomes

$$ \label{eq:norm-mgf-qed}
M_X(t) = \exp\left[ \mu t + \frac{1}{2} \sigma^2 t^2 \right] \; .
$$