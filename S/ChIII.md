---
layout: special
title: "Statistical Models"
shortcut: "ChIII"
---


**Proofs** and *Definitions* on [Statistical Models](/I/ToC#Statistical%20Models) in the StatProofBook, as of 2023-12-23.

| Model | Definition | Estimation | Maximum<br>likelihood<br>estimation | Conjugate<br>prior | Posterior<br>distribution | Log<br>model<br>evidence | Other |
|:----- |:---------- |:---------- |:----------------------------------- |:------------------ |:------------------------- |:------------------------ |:----- |
| **Univariate<br>normal data** |  |  |  |  |  |  |  |
| Univariate Gaussian | *[ug](/D/ug)* |  | **[ug-mle](/P/ug-mle)** | **[ug-prior](/P/ug-prior)** | **[ug-post](/P/ug-post)** | **[ug-lme](/P/ug-lme)**<br>**[ug-anc](/P/ug-anc)** | **[ug-ttest1](/P/ug-ttest1)**<br>**[ug-ttest2](/P/ug-ttest2)**<br>**[ug-ttestp](/P/ug-ttestp)** |
| Univariate Gaussian with known variance | *[ugkv](/D/ugkv)* |  | **[ugkv-mle](/P/ugkv-mle)** | **[ugkv-prior](/P/ugkv-prior)** | **[ugkv-post](/P/ugkv-post)** | **[ugkv-lme](/P/ugkv-lme)**<br>**[ugkv-anc](/P/ugkv-anc)**<br>**[ugkv-cvlme](/P/ugkv-cvlme)** | **[ugkv-ztest1](/P/ugkv-ztest1)**<br>**[ugkv-ztest2](/P/ugkv-ztest2)**<br>**[ugkv-ztestp](/P/ugkv-ztestp)**<br>**[ugkv-lbf](/P/ugkv-lbf)**<br>**[ugkv-lbfmean](/P/ugkv-lbfmean)**<br>**[ugkv-cvlbf](/P/ugkv-cvlbf)**<br>**[ugkv-cvlbfmean](/P/ugkv-cvlbfmean)** |
| One-way analysis of variance | *[anova1](/D/anova1)* | **[anova1-ols](/P/anova1-ols)** |  |  |  |  | **[anova1-pss](/P/anova1-pss)**<br>**[anova1-f](/P/anova1-f)**<br>**[anova1-fols](/P/anova1-fols)**<br>**[anova1-repara](/P/anova1-repara)** |
| Two-way analysis of variance | *[anova2](/D/anova2)* | **[anova2-ols](/P/anova2-ols)** |  |  |  |  | **[anova2-pss](/P/anova2-pss)**<br>**[anova2-cochran](/P/anova2-cochran)**<br>**[anova2-fme](/P/anova2-fme)**<br>**[anova2-fia](/P/anova2-fia)**<br>**[anova2-fgm](/P/anova2-fgm)**<br>**[anova2-fols](/P/anova2-fols)** |
| Simple linear regression | *[slr](/D/slr)* | **[slr-ols](/P/slr-ols)**<br>**[slr-olsmean](/P/slr-olsmean)**<br>**[slr-olsvar](/P/slr-olsvar)**<br>**[slr-olsdist](/P/slr-olsdist)**<br>**[slr-olscorr](/P/slr-olscorr)**<br>**[slr-wls](/P/slr-wls)** | **[slr-mle](/P/slr-mle)** |  |  |  | **[slr-mlr](/P/slr-mlr)**<br>**[slr-meancent](/P/slr-meancent)**<br>**[slr-comp](/P/slr-comp)**<br>**[slr-proj](/P/slr-proj)**<br>**[slr-sss](/P/slr-sss)**<br>**[slr-mat](/P/slr-mat)**<br>**[slr-ressum](/P/slr-ressum)**<br>**[slr-rescorr](/P/slr-rescorr)**<br>**[slr-resvar](/P/slr-resvar)**<br>**[slr-corr](/P/slr-corr)**<br>**[slr-rsq](/P/slr-rsq)** |
| Multiple linear regression | *[mlr](/D/mlr)* | **[mlr-olstr](/P/mlr-olstr)**<br>**[mlr-ols](/P/mlr-ols)**<br>**[mlr-wls](/P/mlr-wls)**<br>**[mlr-olsdist](/P/mlr-olsdist)**<br>**[mlr-wlsdist](/P/mlr-wlsdist)**<br>**[mlr-rssdist](/P/mlr-rssdist)**<br>**[mlr-ind](/P/mlr-ind)** | **[mlr-mle](/P/mlr-mle)**<br>**[mlr-mll](/P/mlr-mll)**<br>**[mlr-dev](/P/mlr-dev)** |  |  |  | **[mlr-glm](/P/mlr-glm)**<br>**[mlr-pss](/P/mlr-pss)**<br>**[mlr-mat](/P/mlr-mat)**<br>**[mlr-idem](/P/mlr-idem)**<br>**[mlr-symm](/P/mlr-symm)**<br>**[mlr-t](/P/mlr-t)**<br>**[mlr-f](/P/mlr-f)**<br>**[mlr-aic](/P/mlr-aic)**<br>**[mlr-aicc](/P/mlr-aicc)**<br>**[mlr-bic](/P/mlr-bic)** |
| Bayesian linear regression |  |  |  | **[blr-prior](/P/blr-prior)** | **[blr-post](/P/blr-post)** | **[blr-lme](/P/blr-lme)** | **[blr-pp](/P/blr-pp)**<br>**[blr-pcr](/P/blr-pcr)**<br>**[blr-dic](/P/blr-bic)** |
| **Multivariate<br>normal data** |  |  |  |  |  |  |  |
| General linear model | *[glm](/D/glm)* | **[glm-ols](/P/glm-ols)**<br>**[glm-wls](/P/glm-wls)** | **[glm-mle](/P/glm-mle)** |  |  |  |  |
| Transformed general linear model | *[tglm](/D/tglm)* |  |  |  |  |  | **[tglm-dist](/P/tglm-dist)**<br>**[tglm-para](/P/tglm-para)** |
| Inverse general linear model | *[iglm](/D/iglm)*<br>*[cfm](/D/cfm)* |  |  |  |  |  | **[iglm-dist](/P/iglm-dist)**<br>**[iglm-blue](/P/iglm-blue)**<br>**[cfm-para](/P/cfm-para)**<br>**[cfm-exist](/P/cfm-exist)** |
| Multivariate Bayesian linear regression |  |  |  | **[mblr-prior](/P/mblr-prior)** | **[mblr-post](/P/mblr-post)** | **[mblr-lme](/P/mblr-lme)** |  |
| **Poisson data** |  |  |  |  |  |  |  |
| Poisson-distributed data | *[poiss](/D/poiss-data)* |  | **[poiss-mle](/P/poiss-mle)** | **[poiss-prior](/P/poiss-prior)** | **[poiss-post](/P/poiss-post)** | **[poiss-lme](/P/poiss-lme)** |  |
| Poisson distribution with exposure values | *[poissexp](/D/poissexp)* |  | **[poissexp-mle](/P/poissexp-mle)** | **[poissexp-prior](/P/poissexp-prior)** | **[poissexp-post](/P/poissexp-post)** | **[poissexp-lme](/P/poissexp-lme)** |  |
| **Probability data** |  |  |  |  |  |  |  |
| Beta-distributed data | *[beta](/D/beta-data)* | **[beta-mome](/P/beta-mome)** |  |  |  |  |  |
| Dirichlet-distributed data | *[dir](/D/dir-data)* |  | **[dir-mle](/P/dir-mle)** |  |  |  |  |
| Beta-binomial data | *[betabin-data](/D/betabin-data)* | **[betabin-mome](/P/betabin-mome)** |  |  |  |  |  |
| **Categorical data** |  |  |  |  |  |  |  |
| Binomial observations | *[bin](/D/bin-data)* |  | **[bin-mle](/P/bin-mle)**<br>**[bin-mll](/P/bin-mll)** | **[bin-prior](/P/bin-prior)** | **[bin-post](/P/bin-post)**<br>**[bin-map](/P/bin-map)** | **[bin-lme](/P/bin-lme)** | **[bin-test](/P/bin-test)**<br>**[bin-lbf](/P/bin-lbf)**<br>**[bin-pp](/P/bin-pp)** |
| Multinomial observations | *[mult](/D/mult-data)* |  | **[mult-mle](/P/mult-mle)**<br>**[mult-mll](/P/mult-mll)** | **[mult-prior](/P/mult-prior)** | **[mult-post](/P/mult-post)**<br>**[mult-map](/P/mult-map)** | **[mult-lme](/P/mult-lme)** | **[mult-test](/P/mult-test)**<br>**[mult-lbf](/P/mult-lbf)**<br>**[mult-pp](/P/mult-pp)** |
| Logistic regression | *[logreg](/D/logreg)* |  |  |  |  |  | **[logreg-pnlo](/P/logreg-pnlo)**<br>**[logreg-lonp](/P/logreg-lonp)** |