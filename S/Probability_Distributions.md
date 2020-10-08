---
layout: page
title: "Special: Probability Distributions"
---


**Proofs** and *Definitions* on [Probability Distributions](/I/Table_of_Contents#Probability%20Distributions) in the StatProofBook, as of 2020-09-09.

| Distribution | Def | PDF | CDF | QF | Mean | Med | Mode | Var | Ent | KL | Marg | Cond | Other |
|:------------ |:--- |:--- |:--- |:-- |:---- |:--- |:---- |:--- |:--- |:-- |:---- |:---- |:----- |
| **Univariate<br>discrete<br>distributions** |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Discrete uniform distribution | *[duni](/D/duni)* | **[duni-pmf](/P/duni-pmf)** | **[duni-cdf](/P/duni-cdf)** | **[duni-qf](/P/duni-qf)** |  |  |  |  |  |  |  |  |  |
| Bernoulli distribution | *[bern](/D/bern)* | **[bern-pmf](/P/bern-pmf)** |  |  | **[bern-mean](/P/bern-mean)** |  |  |  |  |  |  |  |  |
| Binomial distribution | *[bin](/D/bin)* | **[bin-pmf](/P/bin-pmf)** |  |  | **[bin-mean](/P/bin-mean)** |  |  |  |  |  |  |  |  |
| Poisson distribution | *[poiss](/D/poiss)* | **[poiss-pmf](/P/poiss-pmf)** |  |  | **[poiss-mean](/P/poiss-mean)** |  |  |  |  |  |  |  |  |
| **Multivariate<br>discrete<br>distributions** |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Categorical distribution | *[cat](/D/cat)* | **[cat-pmf](/P/cat-pmf)** |  |  | **[cat-mean](/P/cat-mean)** |  |  |  |  |  |  |  |  |
| Multinomial distribution | *[mult](/D/mult)* | **[mult-pmf](/P/mult-pmf)** |  |  | **[mult-mean](/P/mult-mean)** |  |  |  |  |  |  |  |  |
| **Univariate<br>continuous<br>distributions** |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Continuous uniform distribution | *[cuni](/D/cuni)* | **[cuni-pdf](/P/cuni-pdf)** | **[cuni-cdf](/P/cuni-cdf)** | **[cuni-qf](/P/cuni-qf)** | **[cuni-mean](/P/cuni-mean)** | **[cuni-med](/P/cuni-med)** | **[cuni-mode](/P/cuni-mode)** |  |  |  |  |  |  |
| Normal distribution | *[norm](/D/norm)*<br>*[snorm](/D/snorm)* | **[norm-pdf](/P/norm-pdf)** | **[norm-cdf](/P/norm-cdf)**<br>**[norm-cdfwerf](/P/norm-cdfwerf)** | **[norm-qf](/P/norm-qf)** | **[norm-mean](/P/norm-mean)** | **[norm-med](/P/norm-med)** | **[norm-mode](/P/norm-mode)** | **[norm-var](/P/norm-var)** | **[norm-dent](/P/norm-dent)** |  |  |  | **[norm-snorm](/P/norm-snorm)**<br>**[norm-mgf](/P/norm-mgf)**<br>**[norm-fwhm](/P/norm-fwhm)** |
| Gamma distribution | *[gam](/D/gam)*<br>*[sgam](/D/sgam)* | **[gam-pdf](/P/gam-pdf)** |  |  | **[gam-mean](/P/gam-mean)**<br>**[gam-logmean](/P/gam-logmean)** |  |  | **[gam-var](/P/gam-var)** |  | **[gam-kl](/P/gam-kl)** |  |  | **[gam-sgam](/P/gam-sgam)** |
| Exponential distribution | *[exp](/D/exp)* | **[exp-pdf](/P/exp-pdf)** | **[exp-cdf](/P/exp-cdf)** | **[exp-qf](/P/exp-qf)** | **[exp-mean](/P/exp-mean)** | **[exp-med](/P/exp-med)** | **[exp-mode](/P/exp-mode)** |  |  |  |  |  | **[exp-gam](/P/exp-gam)** |
| Beta distribution | *[beta](/D/beta)* | **[beta-pdf](/P/beta-pdf)** |  |  |  |  |  |  |  |  |  |  |  |
| Wald distribution | *[wald](/D/wald)* | **[wald-pdf](/P/wald-pdf)** |  |  |  |  |  |  |  |  |  |  |  |
| **Multivariate<br>continuous<br>distributions** |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Multivariate normal distribution | *[mvn](/D/mvn)* | **[mvn-pdf](/P/mvn-pdf)** |  |  |  |  |  |  | **[mvn-dent](/P/mvn-dent)** | **[mvn-kl](/P/mvn-kl)** | **[mvn-marg](/P/mvn-marg)** | **[mvn-cond](/P/mvn-cond)** | **[mvn-ltt](/P/mvn-ltt)** |
| Normal-gamma distribution | *[ng](/D/ng)* | **[ng-pdf](/P/ng-pdf)** |  |  |  |  |  |  |  | **[ng-kl](/P/ng-kl)** | **[ng-marg](/P/ng-marg)** | **[ng-cond](/P/ng-cond)** |  |
| Dirichlet distribution | *[dir](/D/dir)* | **[dir-pdf](/P/dir-pdf)** |  |  |  |  |  |  |  |  |  |  |  |
| **Matrix-variate<br>continuous<br>distributions** |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Matrix-normal distribution | *[matn](/D/matn)* | **[matn-pdf](/P/matn-pdf)** |  |  |  |  |  |  |  |  |  |  | **[matn-mvn](/P/matn-mvn)**<br>**[matn-ltt](/P/matn-ltt)**<br>**[matn-trans](/P/matn-trans)** |
| Wishart distribution | *[wish](/D/wish)* |  |  |  |  |  |  |  |  |  |  |  |  |