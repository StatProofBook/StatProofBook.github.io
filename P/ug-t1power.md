---
layout: proof
mathjax: true

author: "Alexander D. Bolton"
affiliation: "The Book of Statistical Proofs"
e_mail: "StatProofBook@gmail.com"
date: 2025-07-23 00:00:00

title: "Power analysis, minimum detectable effect and minimum required sample size for a one-sample t-test"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian"
theorem: "Power analysis for one-sample t-test"

sources:
  - authors: "Sylvain Chabé-Ferret"
    year: 2025
    title: "Power Analysis"
    in: "Statistical Tools for Causal Inference"
    pages: "retrieved on 2025-07-05"
    url: "https://chabefer.github.io/STCI/Power.html"

proof_id: "P511"
shortcut: "ug-ttest1power"
username: "alexanderdbolton"
---

**Theorem:** Let there be $n$ i.i.d. observations $Y_1, \dots, Y_n \sim N(\mu, \sigma^2)$ (with both $\mu, \sigma^2$ unknown). Further, let $z_x = \Phi^{-1}(1 - x)$, where $\Phi$ is the CDF of a $N(0, 1)$ distribution. Equivalently, with $Z \sim N(0, 1)$,

$$ \label{eq:zx-definition}
z_x = \Phi^{-1}(1 - x) \Leftrightarrow \Phi(z_x) = 1 - x \Leftrightarrow \mathbb{P}(Z \leq z_x) = 1 - x \Leftrightarrow \mathbb{P}(z_x \leq Z) = x.
$$

1) One-sided one-sample t-test:

We perform a one-sided one-sample $t$-test of the [null hypothesis](/D/h0) $H_0: \mu \leq \mu_0$ vs $H_1: \mu > \mu_0$. The test has [significance level](/D/alpha) $\alpha$. If $H_1$ is true and $\mu = \mu_0 + \delta$, then the [power](/D/power) of the test is

$$ \label{eq:power-one-sided}
\Phi\left(\frac{\delta\sqrt{n}}{\sigma} - z_\alpha\right).
$$

If we keep $\alpha, n, \sigma^2$ the same as before, and require that the power is at least $1 - \beta$, then the [minimum detectable effect](/D/mde) is

$$ \label{eq:mde-one-sided}
\frac{(z_\alpha + z_\beta)\sigma}{\sqrt{n}}.
$$

If we keep $\alpha, \sigma^2, \delta, \beta$ the same as before then the [minimum required sample size](/D/mrss) is

$$ \label{eq:mrss-one-sided}
\frac{\sigma^2(z_\alpha + z_\beta)^2}{\delta^2}.
$$

2) Two-sided one-sample t-test:

We perform a two-sided one-sample $t$-test of hypothesis $H_0: \mu = \mu_0$ vs $H_1: \mu \neq \mu_0$. The test has size $\alpha$. If $H_1$ is true and $\mu = \mu_0 + \delta$ (assuming $\delta > 0$ without loss of generality), then the [power](/D/power) of the test is

$$ \label{eq:power-two-sided}
\Phi\left(\frac{\delta\sqrt{n}}{\sigma} - z_{\alpha/2}\right) + \Phi\left(-z_{\alpha/2} - \frac{\delta\sqrt{n}}{\sigma}\right) \approx \Phi\left(\frac{\delta\sqrt{n}}{\sigma} - z_{\alpha/2}\right).
$$

If we keep $\alpha, n, \sigma^2$ the same as before, and require that the power is at least $1 - \beta$, then the [minimum detectable effect](/D/mde) is

$$ \label{eq:mde-two-sided}
\frac{(z_{\alpha/2} + z_\beta) \sigma}{\sqrt{n}}.
$$

If we keep $\alpha, \sigma^2, \delta, \beta$ the same as before then the [minimum required sample size](/D/mde) is

$$ \label{eq:sample-size-two-sided}
\frac{\sigma^2(z_{\alpha/2} + z_\beta)^2}{\delta^2}.
$$


**Proof:** The $t$-statistic is

$$ \label{eq:t-statistic}
T = \frac{\bar{Y} - \mu_0}{s/\sqrt{n}}.
$$

which [has a $t(n-1)$ distribution](/P/ug-ttest1). Unless $n$ is very small, the $t(n-1)$ distribution is very close to a $N(0, 1)$ distribution, and we will assume that this is a good approximation in this proof.

1) One-sided one-sample t-test:

The test has [size](/D/size) $\alpha$, we reject the null if

$$ \label{eq:one-sided-rejection}
T > z_\alpha.
$$

So the [power](/D/power) of the test is

$$ \label{eq:one-sided-power-prob}
\mathbb{P}\left(\frac{\bar{Y} - \mu_0}{s/\sqrt{n}} > z_\alpha\right).
$$

If the true mean is $\mu = \mu_0 + \delta$, where $\delta > 0$, then the power is

$$ \label{eq:one-sided-power-shift}
\mathbb{P}\left(\frac{\bar{Y} - \mu_0 - \delta}{s/\sqrt{n}} + \frac{\delta\sqrt{n}}{s} > z_\alpha\right).
$$

Now that we're subtracting the true mean, the first term in the sum has a $t$ distribution, which we approximate with a $N(0, 1)$ distribution, $Z$. We also approximate $s$ with $\sigma$, since it should be a good approximation, and the error here doesn't make much difference to the calculation. The power is therefore approximately

$$ \label{eq:one-sided-power-final}
\mathbb{P}\left(Z > z_\alpha - \frac{\delta\sqrt{n}}{\sigma}\right) = \mathbb{P}\left(Z < \frac{\delta\sqrt{n}}{\sigma} - z_\alpha\right) = \Phi\left(\frac{\delta\sqrt{n}}{\sigma} - z_\alpha\right).
$$

To calculate the [minimum detectable effect](/D/mde), we want the smallest $\delta$ such that the power is at least $1-\beta$. If the power is at least $1-\beta$ then

$$ \label{eq:one-sided-power-threshold}
1 - \beta \leq \Phi\left(\frac{\delta\sqrt{n}}{\sigma} - z_\alpha\right),
$$

Using $z_\beta = \Phi^{-1}(1 - \beta)$ and rearranging, we get

$$ \label{eq:one-sided-delta-ineq}
z_\beta + z_\alpha \leq \frac{\delta \sqrt{n}}{\sigma}.
$$

Therefore,

$$ \label{eq:one-sided-delta}
\frac{(z_\beta + z_\alpha)\sigma}{\sqrt{n}} \leq \delta,
$$

and taking the minimum value for $\delta$ gives the minimum detectable effect.

To calculate the [minimum required sample size](/D/mrss), we want the smallest $n$ such that the power is at least $1 - \beta$. Rearranging \eqref{eq:one-sided-power-threshold}, we have

$$ \label{eq:one-sided-n}
\frac{\sigma^2(z_\alpha + z_\beta)^2}{\delta^2} \leq n.
$$

2) Two-sided one-sample t-test:

The test has [size](/D/size) $\alpha$, we reject the null if

$$ \label{eq:two-sided-rejection}
|T| > z_{\alpha/2}.
$$

So the [power](/D/power) of the test is

$$ \label{eq:two-sided-power-prob}
\mathbb{P}\left(\left(\frac{\bar{Y} - \mu_0}{s/\sqrt{n}} > z_{\alpha/2}\right) \wedge \left(\frac{\bar{Y} - \mu_0}{s/\sqrt{n}} < -z_{\alpha/2}\right)\right).
$$

If the true mean is $\mu = \mu_0 + \delta$, where $\delta > 0$ without loss of generality, then the power is

$$ \label{eq:two-sided-power-shift}
\mathbb{P}\left(\left(\frac{\bar{Y} - \mu_0 - \delta}{s/\sqrt{n}} + \frac{\delta\sqrt{n}}{\sigma} > z_{\alpha/2}\right) \wedge \left(\frac{\bar{Y} - \mu_0 - \delta}{s/\sqrt{n}} + \frac{\delta\sqrt{n}}{\sigma} < -z_{\alpha/2}\right)\right).
$$

As before, we use a $N(0, 1)$ distribution, denoted $Z$. And we approximate $s$ with $\sigma$. The power is therefore approximately

$$ \label{eq:two-sided-power-almost-final}
\Phi\left(\frac{\delta\sqrt{n}}{\sigma} - z_{\alpha/2}\right) + \Phi\left(-z_{\alpha/2} - \frac{\delta\sqrt{n}}{\sigma}\right).
$$

If we have a large enough $\delta$ then the second term, which is the probability of rejecting the null hypothesis but with a sign error on $\delta$, will be small. For the later calculations, we will set it to $0$ and use the approximation

$$ \label{eq:two-sided-power-final}
\Phi\left(\frac{\delta\sqrt{n}}{\sigma} - z_{\alpha/2}\right)
$$

for the power.

To calculate the [minimum detectable effect](/D/mde), we want the smallest $\delta$ such that the power is at least $1-\beta$. If the power is at least $1-\beta$ then

$$ \label{eq:two-sided-power-threshold}
1 - \beta \leq \Phi\left(\frac{\delta\sqrt{n}}{\sigma} - z_{\alpha/2}\right),
$$

Using $z_\beta = \Phi^{-1}(1 - \beta)$ and rearranging, we get

$$ \label{eq:two-sided-delta-ineq}
z_\beta + z_{\alpha/2} \leq \frac{\delta \sqrt{n}}{\sigma}.
$$

Therefore

$$ \label{eq:two-sided-delta}
\frac{(z_\beta + z_{\alpha/2})\sigma}{\sqrt{n}} \leq \delta,
$$

and taking the minimum value for $\delta$ gives the minimum detectable effect.

To calculate the [minimum required sample size](/D/mrss), we want the smallest $n$ such that the power is at least $1 - \beta$. Rearranging \eqref{eq:two-sided-power-threshold}, we have

$$ \label{eq:two-sided-n}
\frac{\sigma^2(z_{\alpha/2} + z_\beta)^2}{\delta^2} \leq n.
$$