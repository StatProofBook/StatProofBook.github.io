---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-04-21 16:15:41

title: "Full width at half maximum for the von Mises distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "von Mises distribution"
theorem: "Full width at half maximum"

sources:

proof_id: "P535"
shortcut: "vm-fwhm"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [von Mises distribution](/D/vm):

$$ \label{eq:vm}
X \sim \mathrm{vM}(\mu, \kappa) \; .
$$

Then, the [full width at half maximum](/D/fwhm) (FWHM) of $X$ is

$$ \label{eq:vm-fwhm}
\mathrm{FWHM}(X) = 2 \left[ \pi - \arccos\left(1 - \frac{\ln 2}{\kappa} \right) \right] \; .
$$

Moreover, the FWHM of $X$ is not defined, if

$$ \label{eq:vm-fwhm-nd}
\kappa < \frac{1}{2} \ln 2 \approx 0.347 \; .
$$


**Proof:**

1) The [probability density function of the von Mises distribution](/P/vm-pdf) is

$$ \label{eq:vm-pdf}
f_X(x) = \frac{1}{2 \pi I_0(\kappa)} \cdot \exp \left[ \kappa \cos(x-\mu) \right]
$$

and the [mode of the von Mises distribution](/P/vm-mode) is

$$ \label{eq:vm-mode}
\mathrm{mode}(X) = \mu \; ,
$$

such that

$$ \label{eq:vm-pdf-max}
  f_\mathrm{max}
= f_X(\mathrm{mode}(X))
\overset{\eqref{eq:vm-mode}}{=} f_X(\mu)
\overset{\eqref{eq:vm-pdf}}{=} \frac{\exp[\kappa]}{2 \pi I_0(\kappa)} \; .
$$

The FWHM bounds [satisfy the equation](/D/fwhm)

$$ \label{eq:x-FHWM}
  f_X(x_\mathrm{FWHM})
= \frac{1}{2} f_\mathrm{max} \overset{\eqref{eq:vm-pdf-max}}{=} \frac{\exp[\kappa]}{4 \pi I_0(\kappa)} \; .
$$

Using \eqref{eq:vm-pdf}, we can develop this equation as follows:

$$ \label{eq:x-FHWM-s1}
\begin{split}
\frac{1}{2 \pi I_0(\kappa)} \cdot \exp \left[ \kappa \cos(x-\mu) \right] &= \frac{\exp[\kappa]}{4 \pi I_0(\kappa)} \\
\exp \left[ \kappa \cos(x-\mu) \right] &= \frac{1}{2} \exp[\kappa] \\
\kappa \cos(x-\mu) &= \kappa + \ln \frac{1}{2} \\
\cos(x-\mu) &= 1 - \frac{\ln 2}{\kappa} \\
x_{\mathrm{FHWM}} &= \arccos\left(1 - \frac{\ln 2}{\kappa} \right) + \mu \; .
\end{split}
$$

Considering the nature of the arccosine function, this implies the following two solutions for $x_\mathrm{FWHM}$

$$ \label{eq:x-FHWM-s2}
\begin{split}
x_1 &= \arccos\left(1 - \frac{\ln 2}{\kappa} \right) + \mu \\
x_2 &= \left( 2\pi - \arccos\left(1 - \frac{\ln 2}{\kappa} \right) \right) + \mu \; ,
\end{split}
$$

such that the [full width at half maximum](/D/fwhm) of $X$ is

$$ \label{eq:vm-fwhm-qed}
\begin{split}
   \mathrm{FWHM}(X)
&= \Delta x = x_2 - x_1 \\
&\overset{\eqref{eq:x-FHWM-s2}}{=} \left[ \left( 2\pi - \arccos\left(1 - \frac{\ln 2}{\kappa} \right) \right) + \mu \right] - \left[ \arccos\left(1 - \frac{\ln 2}{\kappa} \right) + \mu \right] \\
&= 2 \left[ \pi - \arccos\left(1 - \frac{\ln 2}{\kappa} \right) \right] \; .
\end{split}
$$

2) Since $\arccos(x)$ is only defined for $-1 \leq x \leq +1$ and since $\ln 2 \approx 0.693$ and $\kappa$ [are positive](/D/vm), the following must hold for $\mathrm{FWHM}(X)$ to be defined:

$$ \label{eq:vm-fwhm-nd-qed}
\begin{split}
1 - \frac{\ln 2}{\kappa} &\geq -1 \\
- \frac{\ln 2}{\kappa} &\geq -2 \\
\ln 2 &\leq 2\kappa \\
\kappa &\geq \frac{1}{2} \ln 2 \; .
\end{split}
$$

In the case that $\kappa < \frac{1}{2} \ln 2$, the probability density function is so flat that $f_\mathrm{min} = f_X(\mu-\pi)$ exceeds $\frac{1}{2} f_\mathrm{max} = \frac{1}{2} f_X(\mu)$ which means that condition \eqref{eq:x-FHWM} cannot be satisfied, such that the FWHM of $X$ is not defined.
