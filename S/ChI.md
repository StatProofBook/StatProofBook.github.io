---
layout: page
title: "Special: General Theorems"
---


**Proofs** and *Definitions* on [General Theorems](/I/ToC#General%20Theorems) in the StatProofBook, as of 2021-12-21.

| Concept | Definition | Properties | Relationships | Other |
|:------- |:---------- |:---------- |:------------- |:----- |
| **Probability theory** |  |  |  |  |
| Probability | *[prob](/D/prob)*<br>*[prob-joint](/D/prob-joint)*<br>*[prob-marg](/D/prob-marg)*<br>*[prob-cond](/D/prob-cond)* | **[prob-ind](/P/prob-ind)**<br>**[prob-exc](/P/prob-exc)** |  |  |
| Probability axioms | *[prob-ax](/D/prob-ax)* | **[prob-mon](/P/prob-mon)**<br>**[prob-emp](/P/prob-emp)**<br>**[prob-emp](/P/prob-emp)**<br>**[prob-comp](/P/prob-comp)**<br>**[prob-add](/P/prob-add)**<br>**[prob-exh](/P/prob-exh)** |  | **[prob-tot](/P/prob-tot)** |
| Probability mass function | *[pmf](/D/pmf)* | **[pmf-sumind](/P/pmf-sumind)**<br>**[pmf-sifct](/P/pmf-sifct)**<br>**[pmf-sdfct](/P/pmf-sdfct)**<br>**[pmf-invfct](/P/pmf-invfct)** |  |  |
| Probability density function | *[pdf](/D/pdf)* | **[pdf-sumind](/P/pdf-sumind)**<br>**[pdf-sifct](/P/pdf-sifct)**<br>**[pdf-sdfct](/P/pdf-sdfct)**<br>**[pdf-invfct](/P/pdf-invfct)**<br>**[pdf-linfct](/P/pdf-linfct)** | **[pdf-cdf](/P/pdf-cdf)** |  |
| Cumulative distribution function | *[cdf](/D/cdf)*<br>*[cdf-joint](/D/cdf-joint)* | **[cdf-sumind](/P/cdf-sumind)**<br>**[cdf-sifct](/P/cdf-sifct)**<br>**[cdf-sdfct](/P/cdf-sdfct)** | **[cdf-pmf](/P/cdf-pmf)**<br>**[cdf-pdf](/P/cdf-pdf)** | **[cdf-pit](/P/cdf-pit)**<br>**[cdf-itm](/P/cdf-itm)**<br>**[cdf-dt](/P/cdf-dt)** |
| Quantile function | *[qf](/D/qf)* |  | **[qf-cdf](/P/qf-cdf)** |  |
| Characteristic function | *[cf](/D/cf)* | **[cf-fct](/P/cf-fct)** |  |  |
| Moment-generating function | *[mgf](/D/mgf)* | **[mgf-fct](/P/mgf-fct)** |  | **[mgf-ltt](/P/mgf-ltt)**<br>**[mgf-lincomb](/P/mgf-lincomb)** |
| Cumulant-generating function | *[cgf](/D/cgf)* |  |  |  |
| Probability-generating function | *[pgf](/D/pgf)* |  |  |  |
| Expected value | *[mean](/D/mean)*<br>*[mean-samp](/D/mean-samp)*<br>*[mean-rvec](/D/mean-rvec)*<br>*[mean-rmat](/D/mean-rmat)* | **[mean-nnrvar](/P/mean-nnrvar)**<br>**[mean-nonneg](/P/mean-nonneg)**<br>**[mean-lin](/P/mean-lin)**<br>**[mean-mono](/P/mean-mono)**<br>**[mean-mult](/P/mean-mult)**<br>**[mean-tr](/P/mean-tr)**<br>**[mean-qf](/P/mean-qf)** | **[mean-tot](/P/mean-tot)** | **[mean-lotus](/P/mean-lotus)** |
| Variance | *[var](/D/var)*<br>*[var-samp](/D/var-samp)* | **[var-nonneg](/P/var-nonneg)**<br>**[var-const](/P/var-const)**<br>**[var-inv](/P/var-inv)**<br>**[var-scal](/P/var-scal)**<br>**[var-sum](/P/var-sum)**<br>**[var-lincomb](/P/var-lincomb)**<br>**[var-add](/P/var-add)** | **[var-mean](/P/var-mean)** | **[var-tot](/P/var-tot)** |
| Covariance | *[cov](/D/cov)*<br>*[cov-samp](/D/cov-samp)*<br>*[covmat](/D/covmat)*<br>*[covmat-samp](/D/covmat-samp)* | **[cov-ind](/P/cov-ind)** | **[cov-mean](/P/cov-mean)**<br>**[cov-corr](/P/cov-corr)**<br>**[covmat-mean](/P/covmat-mean)**<br>**[covmat-corrmat](/P/covmat-corrmat)** | **[cov-tot](/P/cov-tot)** |
| Correlation | *[corr](/D/corr)*<br>*[corr-samp](/D/corr-samp)*<br>*[corrmat](/D/corrmat)*<br>*[corrmat-samp](/D/corrmat-samp)* | **[corr-range](/P/corr-range)** | **[corr-z](/P/corr-z)** |  |
| Median | *[med](/D/med)* |  |  |  |
| Mode | *[mode](/D/mode)* |  |  |  |
| Standard deviation | *[std](/D/std)* |  |  |  |
| Full width at half maximum | *[fwhm](/D/fwhm)* |  |  |  |
| Minimum | *[min](/D/min)* |  |  |  |
| Maximum | *[max](/D/max)* |  |  |  |
| Moments | *[mom](/D/mom)*<br>*[mom-raw](/D/mom-raw)*<br>*[mom-cent](/D/mom-cent)*<br>*[mom-stand](/D/mom-stand)* | **[momraw-1st](/P/momraw-1st)**<br>**[momraw-2nd](/P/momraw-2nd)**<br>**[momcent-1st](/P/momcent-1st)**<br>**[momcent-2nd](/P/momcent-2nd)** | **[mom-mgf](/P/mom-mgf)** |  |
| **Information theory** |  |  |  |  |
| Shannon entropy | *[ent](/D/ent)*<br>*[ent-cond](/D/ent-cond)*<br>*[ent-joint](/D/ent-joint)*<br>*[ent-cross](/D/ent-cross)* | **[ent-nonneg](/P/ent-nonneg)**<br>**[ent-conc](/P/ent-conc)**<br>**[entcross-conv](/P/entcross-conv)** |  | **[gibbs-ineq](/P/gibbs-ineq)**<br>**[logsum-ineq](/P/logsum-ineq)** |
| Differential entropy | *[dent](/D/dent)*<br>*[dent-cond](/D/dent-cond)*<br>*[dent-joint](/D/dent-joint)*<br>*[dent-cross](/D/dent-cross)* | **[dent-neg](/P/dent-neg)**<br>**[dent-inv](/P/dent-inv)**<br>**[dent-add](/P/dent-add)**<br>**[dent-addvec](/P/dent-addvec)**<br>**[dent-noninv](/P/dent-noninv)** |  |  |
| Discrete mutual information | *[mi](/D/mi)* |  | **[dmi-mce](/P/dmi-mce)**<br>**[dmi-mje](/P/dmi-mje)**<br>**[dmi-jce](/P/dmi-jce)** |  |
| Continuous mutual information | *[mi](/D/mi)* |  | **[cmi-mcde](/P/cmi-mcde)**<br>**[cmi-mjde](/P/cmi-mjde)**<br>**[cmi-jcde](/P/cmi-jcde)** |  |
| Kullback-Leibler divergence | *[kl](/D/kl)* | **[kl-nonneg](/P/kl-nonneg)**<br>**[kl-nonsymm](/P/kl-nonsymm)**<br>**[kl-conv](/P/kl-conv)**<br>**[kl-add](/P/kl-add)**<br>**[kl-inv](/P/kl-inv)** | **[kl-ent](/P/kl-ent)**<br>**[kl-dent](/P/kl-dent)** |  |
| **Estimation theory** |  |  |  |  |
| Mean squared error |  |  | **[mse-bnv](/P/mse-bnv)** |  |
| Confidence interval |  |  |  | **[ci-wilks](/P/ci-wilks)** |
| **Frequentist statistics** |  |  |  |  |
| Likelihood theory | *[lf](/D/lf)*<br>*[llf](/D/llf)*<br>*[mle](/D/mle)*<br>*[mll](/D/mll)* |  |  |  |
| **Bayesian statistics** |  |  |  |  |
| Probabilistic modeling | *[gm](/D/gm)*<br>*[lf](/D/lf)*<br>*[prior](/D/prior)*<br>*[fpm](/D/fpm)*<br>*[jl](/D/jl)*<br>*[post](/D/post)*<br>*[ml](/D/ml)* |  | **[jl-lfnprior](/P/jl-lfnprior)**<br>**[post-jl](/P/post-jl)**<br>**[ml-jl](/P/ml-jl)** | **[bayes-th](/P/bayes-th)**<br>**[bayes-rule](/P/bayes-rule)** |