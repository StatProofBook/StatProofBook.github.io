---
layout: page
title: "Special: Statistical Models"
---


**Proofs** and *Definitions* on [Statistical Models](/I/ToC#Statistical%20Models) in the StatProofBook, as of 2021-12-21.

| Model | Definition | Estimation | Maximum<br>likelihood<br>estimation | Conjugate<br>prior | Posterior<br>distribution | Log<br>model<br>evidence | Other |
|:----- |:---------- |:---------- |:----------------------------------- |:------------------ |:------------------------- |:------------------------ |:----- |
| **Univariate<br>normal data** |  |  |  |  |  |  |  |
| Univariate Gaussian | *[ug](/D/ug)* |  | **[ug-mle](/P/ug-mle)** | **[ug-prior](/P/ug-prior)** | **[ug-post](/P/ug-post)** | **[ug-lme](/P/ug-lme)**<br>**[ug-anc](/P/ug-anc)** | **[ug-ttest1](/P/ug-ttest1)**<br>**[ug-ttest2](/P/ug-ttest2)**<br>**[ug-ttestp](/P/ug-ttestp)** |
| Univariate Gaussian with known variance | *[ugkv](/D/ugkv)* |  | **[ugkv-mle](/P/ugkv-mle)** | **[ugkv-prior](/P/ugkv-prior)** | **[ugkv-post](/P/ugkv-post)** | **[ugkv-lme](/P/ugkv-lme)**<br>**[ugkv-anc](/P/ugkv-anc)**<br>**[ugkv-cvlme](/P/ugkv-cvlme)** | **[ugkv-ztest1](/P/ugkv-ztest1)**<br>**[ugkv-ztest2](/P/ugkv-ztest2)**<br>**[ugkv-ztestp](/P/ugkv-ztestp)**<br>**[ugkv-lbf](/P/ugkv-lbf)**<br>**[ugkv-lbfmean](/P/ugkv-lbfmean)**<br>**[ugkv-cvlbf](/P/ugkv-cvlbf)**<br>**[ugkv-cvlbfmean](/P/ugkv-cvlbfmean)** |
| Simple linear regression | *[slr](/D/slr)* | **[slr-ols](/P/slr-ols)**<br>**[slr-olsmean](/P/slr-olsmean)**<br>**[slr-olsvar](/P/slr-olsvar)**<br>**[slr-olsdist](/P/slr-olsdist)**<br>**[slr-wls](/P/slr-wls)** | **[slr-mle](/P/slr-mle)** |  |  |  | **[slr-mlr](/P/slr-mlr)**<br>**[slr-meancent](/P/slr-meancent)**<br>**[slr-comp](/P/slr-comp)**<br>**[slr-proj](/P/slr-proj)**<br>**[slr-sss](/P/slr-sss)**<br>**[slr-mat](/P/slr-mat)**<br>**[slr-ressum](/P/slr-ressum)**<br>**[slr-rescorr](/P/slr-rescorr)**<br>**[slr-resvar](/P/slr-resvar)**<br>**[slr-corr](/P/slr-corr)**<br>**[slr-rsq](/P/slr-rsq)** |
| Multiple linear regression | *[mlr](/D/mlr)* | **[mlr-ols](/P/mlr-ols)**<br>**[mlr-wls](/P/mlr-wls)** | **[mlr-mle](/P/mlr-mle)** |  |  |  | **[mlr-pss](/P/mlr-pss)**<br>**[mlr-mat](/P/mlr-mat)**<br>**[mlr-idem](/P/mlr-idem)** |
| Bayesian linear regression |  |  |  | **[blr-prior](/P/blr-prior)** | **[blr-post](/P/blr-post)** | **[blr-lme](/P/blr-lme)** | **[blr-pp](/P/blr-pp)**<br>**[blr-pcr](/P/blr-pcr)** |
| **Multivariate<br>normal data** |  |  |  |  |  |  |  |
| General linear model | *[glm](/D/glm)* | **[glm-ols](/P/glm-ols)**<br>**[glm-wls](/P/glm-wls)** | **[glm-mle](/P/glm-mle)** |  |  |  |  |
| Transformed general linear model | *[tglm](/D/tglm)* |  |  |  |  |  | **[tglm-dist](/P/tglm-dist)**<br>**[tglm-para](/P/tglm-para)** |
| Inverse general linear model | *[iglm](/D/iglm)*<br>*[cfm](/D/cfm)* |  |  |  |  |  | **[iglm-dist](/P/iglm-dist)**<br>**[iglm-blue](/P/iglm-blue)**<br>**[cfm-para](/P/cfm-para)**<br>**[cfm-exist](/P/cfm-exist)** |
| Multivariate Bayesian linear regression |  |  |  | **[mblr-prior](/P/mblr-prior)** | **[mblr-post](/P/mblr-post)** | **[mblr-lme](/P/mblr-lme)** |  |
| **Poisson data** |  |  |  |  |  |  |  |
| Poisson-distributed data | *[poiss](/D/poiss-data)* |  | **[poiss-mle](/P/poiss-mle)** | **[poiss-prior](/P/poiss-prior)** | **[poiss-post](/P/poiss-post)** | **[poiss-lme](/P/poiss-lme)** |  |
| Poisson distribution with exposure values | *[poissexp](/D/poissexp)* |  | **[poissexp-mle](/P/poissexp-mle)** | **[poissexp-prior](/P/poissexp-prior)** | **[poissexp-post](/P/poissexp-post)** | **[poissexp-lme](/P/poissexp-lme)** |  |
| **Probability data** |  |  |  |  |  |  |  |
| Beta-distributed data | *[beta](/D/beta-data)* | **[beta-mom](/P/beta-mom)** |  |  |  |  |  |
| Dirichlet-distributed data | *[dir](/D/dir-data)* |  | **[dir-mle](/P/dir-mle)** |  |  |  |  |
| **Categorical data** |  |  |  |  |  |  |  |
| Binomial observations | *[bin](/D/bin-data)* |  |  | **[bin-prior](/P/bin-prior)** | **[bin-post](/P/bin-post)** | **[bin-lme](/P/bin-lme)** |  |
| Multinomial observations | *[mult](/D/mult-data)* |  |  | **[mult-prior](/P/mult-prior)** | **[mult-post](/P/mult-post)** | **[mult-lme](/P/mult-lme)** |  |
| Logistic regression | *[logreg](/D/logreg)* |  |  |  |  |  | **[logreg-pnlo](/P/logreg-pnlo)**<br>**[logreg-lonp](/P/logreg-lonp)** |