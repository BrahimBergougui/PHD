# Better Scores, Same Emissions? Legislative Capacity and Corporate Carbon Management

**Authors:** Brahim Bergougui, [CO-AUTHORS]

1. International Institute of Social Studies (ISS), Erasmus University Rotterdam, The Hague, the Netherlands

2. National Higher School of Statistics and Applied Economics (ENSSEA), Koléa, Algeria

3. College of Business and Economics, Qatar University, Doha, Qatar

## Abstract

We ask whether country-level political and economic risk is associated with how firms manage carbon and with how much they emit. We relate ICRG risk components to the MSCI Carbon Emissions Score, a rating of carbon risk management. The base sample has 17,636 firm-year observations for 3,861 firms in 64 countries (fiscal years 2007 to 2020), and the baseline regressions use 17,008 after singleton firms are dropped. With firm and year fixed effects, stronger legislative capacity is associated with higher scores but not with total GHG emissions or emission intensity, although the score result is absent for the MSCI environmental pillar. Better growth conditions are associated with higher scores and higher emissions. Lower civil disorder is associated with higher scores and lower emission intensity, but this result is not stable across specifications. We put the two sides of the comparison on the same scale: expressed in standard-deviation units of the outcome, the association with the score is several times larger than the association with emissions wherever the latter is non-negligible, and the emission estimates are precise enough to exclude, at 95 percent confidence, any association between legislative strength and total emissions larger than about 3.5 percent in absolute value. Instrumental variable, difference-in-differences and event study designs are inconclusive: lag instruments are imprecise, Lewbel instruments could be computed only for growth conditions and fail an overidentification test, and the event study shows large differences before 2016. The evidence supports associations, not causal relations, and "same emissions" means no detectable association within these bounds. The implied magnitude for legislative strength is small. The score is a rating, not a measure of emissions, and part of its country-level variation may come from how the rating is built.

**Keywords:** carbon management; legislative capacity; institutional quality; MSCI Carbon Emissions Score; ICRG; ESG ratings; symbolic versus substantive responses; firm fixed effects

## 1. Introduction

Firms face growing pressure to manage and report their carbon emissions. A growing literature asks whether investors care about carbon risk (Bolton and Kacperczyk, 2021), and rating agencies turn firm practices and disclosures into scores that investors can compare. Investors use these scores for a range of purposes, from engagement to risk management and product design (Amel-Zadeh and Serafeim, 2018), and a parallel literature measures the climate exposure of firms directly from their own communication (Sautner, van Lent, Vilkov and Zhang, 2023). The pressure is not the same everywhere. Country differences account for a large part of the variation in corporate social performance (Ioannou and Serafeim, 2012; Cai, Pan and Statman, 2016). A natural question follows. Which features of a country's political and economic environment are associated with better corporate carbon management, and does a better rating reflect lower emissions?

The question matters for researchers and for managers. For researchers, carbon scores are widely used as dependent or explanatory variables, and the interpretation of a result depends on what the score measures. If a score reflects management and reporting, then a study that treats it as a measure of emissions will misread its own findings. For managers and investors, the answer indicates how closely a country's institutional setting is related to the signals that ratings send. International samples are useful for this purpose because institutions differ a lot between countries, while within-country samples have little institutional variation to exploit. Carbon is also a good test case. Emissions are measurable and reported in standard formats, and rating providers publish a separate score for carbon risk management, so the two sides of the question can be compared directly.

Three features of rating data make this comparison necessary rather than optional. First, ratings are reactive: firms change what they disclose and how they present it after they are rated (Chatterji and Toffel, 2010). Second, ratings are built from disclosed information, and more disclosure does not reduce disagreement between raters; it increases it, because raters weight the same information differently (Christensen, Serafeim and Sikochi, 2022; Berg, Kölbel and Rigobon, 2022). Third, ratings are not neutral with respect to firm attributes: firm size alone explains a large part of the variation in ESG scores, which raises the possibility that a score picks up the rater's coverage and information environment as much as the firm's conduct (Drempetic, Klein and Zwergel, 2020). Each of these features implies that a country-institutions association with a score need not be an association with emissions.

Existing studies mostly relate broad social or environmental ratings to composite governance indices, or relate country institutions to emission outcomes directly. Recent cross-country work finds that democracy and electoral rules are associated with lower corporate greenhouse gas intensity (Muttakin, Rana and Mihret, 2022; Muttakin, Mihret and Rana, 2021), that economic freedom is associated with lower corporate carbon emissions (Ren, Li, Cheng and Zheng, 2024), and that national institutions shape a country's willingness to commit to climate policy (Bättig and Bernauer, 2009). Two problems limit what these studies can say about carbon management. First, a composite index hides which institutional feature matters. Legislative capacity, social stability and growth conditions may relate to firm behaviour in different ways. Second, ESG ratings combine management practices, disclosure and outcomes, and ratings from different providers diverge (Berg, Kölbel and Rigobon, 2022). A higher score does not have to mean lower emissions.

We address both problems. We use the components of the International Country Risk Guide (ICRG) one at a time, and we compare each component with two kinds of outcome. The first is the MSCI Carbon Emissions Score `ces`), a 0 to 10 rating in which higher values indicate better management of carbon risk. The second is a set of emission measures: the log of total GHG emissions `ln_ghg`) and a log emission intensity `ln_ghg_int`). The base sample covers 17,636 firm-year observations for 3,861 firms in 64 countries over fiscal years 2007 to 2020, and it extends the dataset of Lee et al. (2026). All regressions include firm and year fixed effects, so the estimates compare a firm with itself over time and net out common yearly shocks. This choice removes stable differences between firms, such as industry or ownership, which are a major source of bias in cross-sectional comparisons of ratings. It also means that the estimates use only the changes in country ratings that occur during the sample period, which is a limited amount of variation.

Our main finding is a gap between scores and emissions for legislative strength. A one-point higher ICRG legislative strength rating is associated with a 0.2678 higher carbon score (t = 4.03), but its association with total emissions (-0.0007, t = -0.04) and with emission intensity (0.0251, t = 1.60) is not distinguishable from zero. The implied magnitude is small: a one within-firm standard deviation higher legislative strength rating corresponds to a 0.0700 higher score, which is 2.33 percent of the overall standard deviation of the score (3.002). Growth conditions show a different pattern. A higher growth rating is associated with a higher score (0.2278, t = 7.62) and also with higher emissions (0.0296, t = 4.45) and higher emission intensity (0.0274, t = 4.25). Lower civil disorder is associated with a higher score (0.4536, t = 4.67) and with lower emission intensity (-0.0515, t = -2.42), but not with total emissions. The score and emissions do not move together within firms: the coefficient of the score on `ln_ghg` is 0.0548 (t = 1.19).

We are careful about what these numbers show. The baseline design does not identify causal relations. We tried three strategies and none gave a conclusive answer. The two-year lag instruments produce imprecise estimates (0.1061 for legislative strength, t = 0.18) or fail a relevance test. The Lewbel heteroskedasticity-based instruments could be computed only for growth conditions, and they fail an overidentification test. A continuous difference-in-differences design around 2016 gives an insignificant coefficient (0.1451, t = 0.79), and the event study shows large and significant coefficients in every year before 2016. We therefore report associations, and we treat the design as unable to support a causal reading.

The associations also vary in how well they survive our checks. Legislative strength stays positive in all four sensitivity specifications, but its significance falls to 10 percent when we add industry-by-year fixed effects (0.1201, t = 1.81), and its coefficient on the MSCI environmental pillar, which contains the carbon score, is not significant (-0.0405, t = -0.91). The civil disorder association is the least stable: it is insignificant with one-year lags (0.1111, t = 1.03). Growth conditions are the most stable association, but the Oster bound for this variable is not reassuring (a proportionality ratio of 0.28275 would bring the coefficient to zero). We report these results next to the main findings and not in an appendix, because they limit how far the main findings can be pushed.

We add two pieces of analysis that the earlier version of the paper did not have, because both bear on how the results should be read. First, we put the score and the emission results on the same scale by dividing each coefficient by the standard deviation of its outcome (Section 5.2.1). Second, we convert the insignificant emission coefficients into the range of associations that the data can exclude (Section 5.2.2), and we check how the heterogeneity results survive a correction for multiple testing (Section 5.10). Both exercises use only numbers that the tables already report.

The paper makes three contributions. The first is to decompose political and economic risk and to show which components are associated with carbon management scores. Legislative strength, popular support, growth conditions and civil disorder are associated with higher scores. External pressures are not. We also find that legislative strength is not special within government stability: popular support has a similar coefficient (0.2413, t = 4.85), and government unity is also significant (0.1277, t = 2.23). The pattern is a feature of the domestic political system more than of one component.

The second contribution is to compare the same institutional variables with a management score and with emissions. This comparison separates a statement about ratings from a statement about physical outcomes. The comparison is consistent with the label "better scores, same emissions" for legislative strength only, in the sense that the emission coefficients are not distinguishable from zero and the data exclude all but small associations. We do not test formally that the score and emission coefficients are equal. For growth conditions the label does not hold, because emissions rise together with scores. For civil disorder the evidence is mixed, because emission intensity is lower where disorder risk is lower.

The third contribution is to show where the association sits. The legislative strength association is concentrated among larger firms: the interaction with a large-firm indicator is 0.3549 (t = 2.62), while the coefficient for smaller firms is 0.0737 (t = 0.73). This interaction does not survive a Bonferroni correction across the fifteen interaction tests we report, and it does survive a false-discovery-rate correction at 5 percent, so we treat it as suggestive rather than established (Section 5.10). We do not find a clear pattern across industries or between EU and non-EU firms for legislative strength. Quantile estimates (MMQR) are too imprecise to say whether the association differs across the score distribution: legislative strength is not significant at any of the five quantiles.

Readers should take two points from these results. The first is that the associations in the baseline are statistically clear but economically small for legislative strength. The second is that the comparison with emissions matters more for interpretation than the size of any single coefficient, because it shows that a higher score cannot be read as a lower emission level.

The remainder of the paper is organized as follows. Section 2 develops the theory and five hypotheses. Section 3 describes the data and Section 4 the empirical strategy. Section 5 reports the results, including the sensitivity and endogeneity checks. Section 6 discusses the findings and Section 7 concludes with limitations.

## 2. Literature and hypotheses

### 2.1 Institutional pressure, legitimacy and legislative capacity

Organizations seek legitimacy, which Suchman (1995) defines as a generalized perception that their actions are desirable and appropriate within a socially constructed system of norms. In institutional theory, firms adopt practices because regulators and peers expect them to. DiMaggio and Powell (1983) describe coercive, mimetic and normative routes through which organizations in the same field become similar. Legislatures are a source of coercive pressure. A strong legislature can pass climate and disclosure rules and can sustain them across governments, so firms in such countries expect that carbon requirements will bind. Firms that expect binding requirements have a reason to build carbon management systems early. Normative and mimetic pressure work in the same direction. Where the legislature sets visible standards, industry peers copy them, and firms that do not follow risk losing standing with their peers and with investors. The legitimacy argument does not require the firm to cut emissions. It requires the firm to be seen as responding in the way that the institutional environment expects, and the form of that response depends on what regulators and stakeholders can observe. This argument links legislative capacity to the quality of carbon management, which is what the MSCI score is designed to rate.

Cross-country studies treat the national setting as a determinant of corporate social performance. Ioannou and Serafeim (2012) study the role of nation-level institutions, Cai, Pan and Statman (2016) ask why countries matter so much, and Liang and Renneboog (2017) study the legal and institutional foundations of corporate social responsibility. These studies establish that the country of operation matters. They mostly work with broad social performance measures and with summary descriptions of national institutions, so they say little about which institutional feature is relevant for carbon in particular. A second branch of this literature works with emission outcomes rather than with social performance ratings. Bättig and Bernauer (2009) find that national institutions, and democracy in particular, shape a country's cooperation in climate policy. Muttakin, Rana and Mihret (2022) find that firms in more democratic countries have lower greenhouse gas intensity, and Muttakin, Mihret and Rana (2021) find that the electoral system and corporate political donations are associated with emission intensity across countries. Ren, Li, Cheng and Zheng (2024) report that economic freedom is associated with lower corporate carbon emissions. These studies show that country institutions are associated with emission outcomes, which makes our null result for emissions more interesting rather than less: the same kind of country variable that other work links to emissions is linked here to a rating and not to the emissions we can measure.

The ICRG offers a more detailed description. It rates separate components of political risk, such as government unity, legislative strength and popular support, and these components can be studied one at a time.

We start with legislative strength because it is the component closest to rule-making. We do not predict that it matters more than the other government stability components. Government unity and popular support also bear on whether a government can pass and keep a climate policy, and we report them in the appendix. Our expectation for legislative strength is the following.

**H1:** Stronger legislative capacity is associated with higher corporate carbon management scores.

### 2.2 Policy credibility and long-horizon investment

Carbon management often needs investment that is costly to reverse, for example in monitoring systems, process changes or lower-carbon equipment. Investment under uncertainty is subject to a value of waiting: when future policy is uncertain, firms delay commitments that cannot be undone (Dixit and Pindyck, 1994). Gulen and Ion (2016) find that corporate investment falls with policy uncertainty, and that the relation is stronger for firms with more irreversible investment. A capable legislature reduces uncertainty about the policy path, which lowers the cost of waiting and makes long-horizon investments more attractive. This policy credibility argument is compatible with H1 and applies to both management practices and emissions. It also suggests a possible link between legislative capacity and emissions, which we test in Section 5.2 rather than assume.

The argument that uncertainty raises emissions has direct support. Tee, Wong and Hooy (2023) find, in an international sample, that economic policy uncertainty is associated with a larger corporate carbon footprint, and that stronger institutional governance weakens that association. This is the mechanism we have in mind, and it makes our null result for emissions informative: if the credibility channel operated through abatement investment in our setting, we should see it in `ln_ghg` or `ln_ghg_int`, and we do not.

The credibility argument has a limit. Firms may lower uncertainty by investing in management systems, which are cheap and reversible, while they still delay the irreversible investments that cut emissions. Management systems and reporting need less capital than abatement does. The same credible policy path that makes firms willing to build such systems may therefore leave total emissions unchanged in the short run. Which of the two responses dominates is an empirical matter, and we cannot observe the investment mix directly. We use intangible assets and sales growth as proxies in Section 5.3, and we recognize that they are imperfect. Capital expenditure is already a control variable, so it does not give an independent test.

Recent work suggests one reason why the two responses can come apart: the effect of a policy on emissions depends on the national capability environment in which firms operate. Andreou, Anyfantaki, Cabolis and Dellis (2026) show, using verified installation-level emissions from the EU Emissions Trading System, that firms facing identical carbon prices abate more where institutional quality and innovation-system capabilities are stronger. Credible policy may therefore be a necessary condition for abatement rather than a sufficient one, and its absence in our estimates is compatible with that reading.

### 2.3 Slack resources and growth conditions

Firms invest more in sustainability when they have resources to spare. Hong, Kubik and Scheinkman (2012) argue that financial constraints limit corporate goodness. When an economy grows well, firms have more cash flow and easier access to finance, and they can devote part of it to carbon management. The same growth also raises output, and higher output usually raises emissions. The slack argument therefore predicts a higher carbon score in better growth conditions, but it does not predict lower emissions. We state the expectation for the score.

The size of the score response to growth is not obvious from theory. MSCI describes its carbon emissions key issue score as combining an exposure score and a management score, so that higher exposure requires stronger demonstrated management for the same overall score (MSCI ESG Research LLC, 2023). The key issue score is computed as $KI_i = 7 - (\max(EXP_i, 2) - MGT_i)$, where $EXP$ is the exposure score and $MGT$ the management score. We do not know whether the `ces` field in our data is identical to that key issue score. If growth raises both output and the resources for management, the score may rise even when emissions rise as well. This is a reason to look at the score and the emission measures together, as we do in Section 5.2, and not to read a higher score in a growing economy as evidence of lower emissions.

**H2:** Better macroeconomic growth conditions are associated with higher corporate carbon management scores.

### 2.4 Civil disorder and the enforcement environment

Civil disorder is a feature of the social environment rather than of the legislature. Where disorder risk is low, the state is more able to enforce rules, and stakeholders can monitor and press firms without the disruption that disorder brings. Two literatures support this step. Work on environmental policy formation finds that political instability weakens environmental policy: Fredriksson and Svensson (2003) show that the stringency of environmental policy falls with political instability, and that the interaction between instability and corruption shapes the outcome. Work on state capacity treats the ability to tax, regulate and enforce as an investment that governments make, and shows that internal conflict and political instability reduce the incentive to make it (Besley and Persson, 2010). A stable social environment also lets managers plan over long horizons, which supports the same investment logic as in Section 2.2. We treat this argument as less developed than the other two, and we expect the same sign as for legislative strength.

There is also a reason to doubt the sign. Social unrest can raise public attention to firms and to the state, and in that case firms in unstable countries might react more strongly. Vasi and King (2012) show that activism by secondary stakeholders raises the perceived environmental risk of targeted firms and lowers their market value, and Reid and Toffel (2009) show that firms disclose climate change strategies in response to both public politics, such as activist pressure, and private politics, such as shareholder resolutions. If disorder is accompanied by more activism and more scrutiny, firms facing it may disclose and manage more, not less. The two arguments therefore predict opposite signs, and the literature does not settle which dominates. The ICRG civil disorder component varies little in our sample (mean 2.937 on a 0 to 4 scale, with the median at 3), so a significant coefficient would be estimated from a small number of countries and years with lower ratings. We state H3 as an association, and we treat the evidence for it with the caution that this limited variation requires.

**H3:** Lower civil disorder is associated with higher corporate carbon management scores.

### 2.5 Ratings versus emissions: symbolic and substantive responses

The theory does not say that institutional pressure must reduce emissions. Meyer and Rowan (1977) argue that organizations adopt formal structures to signal conformity, and these structures can be decoupled from technical activity. Bansal and Clelland (2004) study how firms use impression management to protect legitimacy when they face environmental scrutiny. Walker and Wan (2012) separate symbolic actions, such as communication, from substantive actions that change environmental performance. Delmas and Burbano (2011) review the conditions in which firms communicate more than they do, and Lyon and Montgomery (2015) survey the wider greenwashing literature. The common thread in this work is that a firm can gain legitimacy from visible actions that are cheaper than the underlying change, and that the gap between what firms say and what they do is larger where scrutiny is uneven. Matsumura, Prakash and Vera-Muñoz (2014) show that emissions and disclosures are both relevant to firm value, which gives firms a reason to improve disclosure even when emissions are unchanged.

ESG ratings are built from management practices and disclosure as well as outcomes, and they diverge across providers (Berg, Kölbel and Rigobon, 2022). A rating of carbon risk management can therefore improve through better systems and reporting while emissions stay where they are. Two further features of ratings push in the same direction. Ratings are reactive: firms adjust the behaviour that the rater measures once they know they are being rated (Chatterji and Toffel, 2010). And more disclosure does not make raters converge: Christensen, Serafeim and Sikochi (2022) find that greater ESG disclosure is associated with greater disagreement between raters, which means that the disclosed information enters the score through the rater's own weighting. If institutional pressure works mainly through such managerial and reporting responses, institutional variables will be more strongly associated with the score than with emissions.

Disclosure does sometimes have real effects, and knowing when helps to interpret our null result. Downar, Ernstberger, Reichelstein, Schwenen and Zaklan (2021) study a UK mandate and find that firms subject to it reduce their emissions, and Krueger, Sautner, Tang and Zhong (2024) document effects of mandatory ESG disclosure around the world on disclosure and on several real outcomes. Christensen, Hail and Leuz (2021) conclude in their review that real effects of disclosure mandates are more likely where the mandate carries enforcement and monitoring. Our setting differs from these studies in one important way: we compare countries with different institutional ratings rather than firms before and after a mandate with enforcement. The comparison therefore suggests that the level of legislative capacity in our sample is associated with more and better disclosed carbon management, but not with the compliance pressure that turns disclosure into abatement.

**H4:** The association between institutional quality and carbon management scores is stronger than its association with emissions (a symbolic rather than a substantive response).

We test H4 separately for each institutional variable. The score and the emission measures are on different scales, so the comparison rests on statistical significance and sign, and on the standardized comparison in Section 5.2.1, not on a ratio of raw coefficients.

Two cautions apply to this test. First, a statistically insignificant coefficient for emissions does not prove that the true association is zero. It means that the data cannot distinguish it from zero, and we report the t-statistics so that readers can judge precision. In Section 5.2.2 we go one step further and report the range of associations that the data can exclude. Second, the emission measures are available for fewer firm-years than the score, so we compare the score and the emissions on the same sample. The comparison also does not separate a symbolic response from a substantive response that is slow to show up in emissions. If firms start abatement projects that reduce emissions only after several years, a contemporaneous regression will find no association even when the response is substantive. The data cannot rule this out.

### 2.6 Visibility and firm size

Larger firms are more visible, and visible firms face more scrutiny from regulators and investors. Marquis, Toffel and Zhou (2016) show in a global study that scrutiny and local norms shape how firms disclose environmental information. If institutional pressure works through scrutiny, the association between institutions and the carbon score should be stronger for larger firms. Investor pressure is also concentrated on large emitters: Azar, Duro, Kadach and Ormazabal (2021) find that the three largest asset managers focus their climate engagements on large firms with high emissions and significant stakes, and that their ownership is followed by lower emissions among index constituents.

Size has other meanings that predict the same sign. Larger firms have more staff and more resources for reporting, and rating providers cover them in more detail. Drempetic, Klein and Zwergel (2020) show that firm size alone explains a large part of the variation in ESG scores, which means that a size difference in the association may reflect the construction of the rating rather than a difference in behaviour. A stronger association among large firms is therefore compatible with a visibility argument, with a resource argument and with a rating-construction argument. We cannot separate these explanations, and we say so when we interpret the result. We also expect the association to differ across industries and periods, and we report those splits as exploratory, without formal hypotheses.

**H5:** The associations are stronger for larger firms.

### 2.7 Summary of expectations

The five hypotheses rest on different arguments and carry different risks. H1 and H3 rest on policy credibility and enforcement, and both predict a positive sign for the score; H3 also has a counter-argument that predicts the opposite sign. H2 rests on slack resources, and it predicts a positive sign for the score without any prediction about emissions. H4 is the test that separates ratings from outcomes, and it can fail for each variable separately. H5 follows from visibility, but it has competing explanations. We state at the outset that a hypothesis is not supported when the data contradict it, and we apply that rule in Section 5.9.

## 3. Data

### 3.1 Sources and sample

The firm-level carbon score and emission data come from MSCI ESG Ratings (MSCI ESG Research LLC, n.d.). Balance sheet and income statement variables come from S&P Compustat Global (S&P Global Market Intelligence, n.d.). Country risk ratings come from the PRS Group International Country Risk Guide (ICRG; PRS Group, n.d.), and inflation and unemployment come from the World Bank World Development Indicators (World Bank, n.d.). All ICRG variables are coded so that higher values mean lower risk. The data are an unbalanced panel that extends the dataset of Lee et al. (2026).

The raw file has 31,790 rows. The duplicate report finds 31,460 firm-year observations that appear once, 6 rows that appear twice (3 surplus rows) and 324 rows that appear four times (243 surplus rows). We apply a sequence of rules to remove duplicates: exact copies, the main Compustat identifier `gvkey`), and the latest fiscal-year month. None of these rules removes any row, so all 246 removed duplicates are dropped by the final tie-break, which keeps the first row after sorting by `gvkey` and `isin_code`. The deduplicated file has 31,544 rows. The tie-break is arbitrary when the duplicate rows differ in content, and we flag this in the limitations.

The base sample keeps observations with non-missing values for `ces`, all seven ICRG components, the six firm controls and the two country controls. It has 17,636 firm-year observations for 3,861 firms in 64 countries. The fiscal years in the base sample run from 2007 to 2020, and the median year is 2017. The deduplicated file runs to 2024, but the base sample ends in 2020: the year indicators for 2021 to 2024 have no observations in the base sample (analysis log). We have not verified which of the required variables is missing after 2020. The estimation sample is smaller in each table because the fixed effects estimator drops singleton observations. Table 2 uses 17,008 observations after dropping 628 singletons (3,233 firms remain). Table 4 uses 15,753 observations, because `ln_ghg` and `ln_ghg_int` are missing for some firms and singleton firms are dropped.

The sample is concentrated in a few countries. Japan accounts for 23.83 percent of the base sample, the United Kingdom for 10.95 percent, China for 8.41 percent and Australia for 7.28 percent, so four countries contribute 50.48 percent of the observations. Appendix Table A2 lists all 64 countries.

### 3.2 Variables

Table A1 in the appendix defines each variable. The outcome is the MSCI Carbon Emissions Score `ces`), which runs from 0 to 10 and is higher when a firm manages carbon risk better. It is a management and exposure score, not an emissions volume. We use `ces_m`, an alternative version of the score whose exact definition we have not verified, only as a sensitivity check. We also use the MSCI environmental pillar score `env`), which includes `ces` as a component. Total GHG emissions `ghg`) come from MSCI, and the definition of the field in the source is ambiguous, so we treat it as an emissions level. We use `ln_ghg`, the log of one plus GHG, and `ln_ghg_int`, the log of one plus GHG minus the log of sales, as an emission intensity proxy.

Three properties of the MSCI carbon score matter for interpretation, and we use them in Sections 5.2 and 6. First, the score is exposure-adjusted. MSCI computes the carbon emissions key issue score as $KI_i = 7 - (\max(EXP_i, 2) - MGT_i)$, so a firm with higher exposure must demonstrate stronger management to obtain the same score (MSCI ESG Research LLC, 2023). The score is therefore a statement about management relative to exposure, and not a statement about the level of emissions. Second, the exposure score itself has a country component. It combines a business exposure score with a geographic exposure score, and the geographic exposure score for a country is determined by the annual reduction in greenhouse gas emissions required to meet that country's publicly disclosed emission targets (MSCI ESG Research LLC, 2023). The rating therefore contains a country-level input that is plausibly correlated with national climate policy, and hence with the institutional variables we study. Third, the management score contains a performance component that compares a firm's emissions intensity, and its trend, with those of industry peers. A firm can improve that component by outperforming its peers rather than by cutting its own emissions. All three properties imply that part of the association between country institutions and the score can come from the construction of the rating rather than from the conduct of the firm, and we develop this point in Section 6.1.

The ICRG variables are government stability `icrg_govstab`, 0 to 12), legislative strength `icrg_legis`, 0 to 4), civil disorder `icrg_civdis`, 0 to 4), foreign pressures `icrg_forpress`, 0 to 4), exchange rate stability `icrg_fx`, 0 to 10), foreign debt `icrg_fdebt`, 0 to 10) and real GDP growth `icrg_gdpg`, 0 to 10). Government stability is the sum of government unity `icrg_govunity`), legislative strength and popular support. We derive popular support `icrg_popsup`) as a residual. The core variables are `icrg_legis`, `icrg_gdpg` and `icrg_civdis`. Firm controls are `size` (log of total assets), `lev` (total liabilities over assets), `roa`, `cash`, `capx` (capital expenditure over sales) and `ocf`. Country controls are inflation `wdi_infl`) and unemployment `wdi_unemp`).

### 3.3 Descriptive statistics

Table 1 reports descriptive statistics for the base sample. The carbon score has a mean of 6.060 and a standard deviation of 3.002. The score has mass at both ends of its range: its 10th percentile is 0.1 and its 90th percentile is 10, so many firms sit at the bounds. The ICRG variables have limited spread. Legislative strength has a mean of 2.436 and a standard deviation of 0.404, and civil disorder has a mean of 2.937 with its median and 75th percentile at 3.

**Table 1. Descriptive statistics (base sample, N = 17,636 unless stated)**

| Variable | N | Mean | SD | p25 | p50 | p75 |

|---|---|---|---|---|---|---|

| ces | 17,636 | 6.060 | 3.002 | 4.400 | 6.600 | 8.300 |

| ces_m | 17,636 | 5.672 | 2.931 | 3.696 | 6.300 | 7.834 |

| env | 17,635 | 4.674 | 2.188 | 3.280 | 4.660 | 6.200 |

| ln_ghg | 16,298 | 13.89 | 2.067 | 12.58 | 13.90 | 15.28 |

| ln_ghg_int | 16,292 | 4.246 | 2.319 | 2.415 | 4.603 | 5.957 |

| icrg_govstab | 17,636 | 7.331 | 1.083 | 6.583 | 7.208 | 8.208 |

| icrg_legis | 17,636 | 2.436 | 0.404 | 2.042 | 2.458 | 2.667 |

| icrg_civdis | 17,636 | 2.937 | 0.442 | 2.667 | 3 | 3 |

| icrg_forpress | 17,636 | 2.973 | 0.315 | 2.812 | 3 | 3 |

| icrg_fx | 17,636 | 9.490 | 0.830 | 9.500 | 9.792 | 9.958 |

| icrg_fdebt | 17,636 | 5.691 | 2.008 | 4.333 | 5.500 | 7.500 |

| icrg_gdpg | 17,636 | 6.709 | 1.981 | 6.083 | 6.750 | 7.875 |

| icrg_govunity | 17,636 | 2.854 | 0.463 | 2.500 | 2.833 | 3.208 |

| icrg_popsup | 17,636 | 2.041 | 0.431 | 1.917 | 2.062 | 2.250 |

| size | 17,636 | 9.838 | 2.522 | 7.872 | 9.634 | 11.88 |

| lev | 17,636 | 0.514 | 0.196 | 0.378 | 0.519 | 0.649 |

| roa | 17,636 | 0.0421 | 0.0795 | 0.0181 | 0.0430 | 0.0748 |

| cash | 17,636 | 0.149 | 0.129 | 0.0580 | 0.112 | 0.202 |

| capx | 17,636 | 0.0805 | 0.201 | 0.0214 | 0.0419 | 0.0751 |

| ocf | 17,636 | 0.0849 | 0.0710 | 0.0498 | 0.0817 | 0.119 |

| wdi_infl | 17,636 | 1.780 | 2.783 | 0.484 | 1.451 | 2.456 |

| wdi_unemp | 17,636 | 5.809 | 3.961 | 3.589 | 4.624 | 6.833 |

*Note: Statistics are computed on the base sample before singleton observations are dropped. The ICRG variables are coded so that higher values mean lower risk.*

Legislative strength is strongly correlated with government stability (0.8778), which is expected because it is one of its components. It has a low correlation with the carbon score (0.0380). The variance inflation factor is 4.85 for legislative strength and 4.75 for government stability when all seven ICRG variables enter one regression, and the mean is 1.80. Because of this overlap, we enter each ICRG variable in a separate regression.

## 4. Empirical strategy

### 4.1 Baseline specification

We estimate one regression for each ICRG variable:

$$CES_{i,c,t} = \alpha_i + \lambda_t + \beta\, ICRG^{k}_{c,t} + \gamma' X_{i,t} + \delta' Z_{c,t} + \varepsilon_{i,c,t}$$

where $i$ is the firm, $c$ the country and $t$ the year. $ICRG^{k}$ is one ICRG dimension, $X$ is the vector of firm controls, $Z$ the vector of country controls, $\alpha_i$ a firm fixed effect and $\lambda_t$ a year fixed effect. The main tables use heteroskedasticity-robust standard errors, which is the authors' choice. Country-clustered standard errors are reported as a sensitivity check in Table 11, and we do not claim that the main tables are clustered. For the emission outcomes we replace $CES$ with `ln_ghg` or `ln_ghg_int` in the same equation.

Two features of the research design make the choice of standard errors matter. The regressor of interest varies at the country-year level, so the residuals are likely to be correlated within country, and clustering is the natural response. The number of countries is small relative to the number of observations, and conventional cluster-robust standard errors can be severely inflated when the number of clusters is a non-negligible fraction of the number of clusters in the population (Abadie, Athey, Imbens and Wooldridge, 2023). With 61 to 64 clusters, we therefore report both robust and clustered standard errors, we interpret the clustered results as the more demanding test, and we note that a wild cluster bootstrap would give a better small-cluster approximation than either (Cameron, Gelbach and Miller, 2008).

The coefficient $\beta$ is identified from changes over time within firms, after removing common yearly shocks. The ICRG variables vary by country and year, so most of their within-firm variation comes from changes in country ratings. A within-firm design removes fixed differences between firms, but it does not remove time-varying omitted factors that move with country ratings. We read $\beta$ as an association.

### 4.2 Investment channels

We study candidate channels with a two-step procedure. Let $M_{i,t}$ be a candidate channel variable. The first step regresses $M$ on the ICRG variable, and the second step adds $M$ to the baseline equation:

$$M_{i,t} = \alpha_i + \lambda_t + a\, ICRG^{k}_{c,t} + \ldots \qquad CES_{i,c,t} = \alpha_i + \lambda_t + \beta'\, ICRG^{k}_{c,t} + b\, M_{i,t} + \ldots$$

The product $a \times b$ is the indirect association through $M$. We use the log of intangible assets `ln_intan`) for all three core variables, and sales growth `sgrowth`) for growth conditions. We call these results suggestive, because the second step treats $M$ as exogenous. We also report a regression with capital expenditure `capx`) for growth conditions, but `capx` is one of the firm controls in every regression. That regression therefore reproduces the baseline and is not an independent channel test.

### 4.3 Omitted variables

We use three tools. The impact threshold for a confounding variable (ITCV; Frank, 2000; Frank et al., 2013) gives the correlation that an omitted variable would need with both the outcome and the regressor to remove statistical significance. The Oster (2019) bound reports the coefficient under proportional selection on unobservables with $R_{max} = 1.3 \times R^2$, and the value of the proportionality ratio $\delta$ that would bring the coefficient to zero. Both are computed on within-demeaned data with robust standard errors. The third tool is entropy balancing (Hainmueller, 2012). We split each core variable at its median, reweight the observations so that the means of the eight controls match between the two groups, and re-estimate the baseline equation with these weights and the continuous variable. We balance first moments only.

### 4.4 Endogeneity

We use three designs. The first is a two-year lag instrument: the instrument for the ICRG variable in year $t$ is its value in year $t-2$, estimated with firm and year fixed effects. The second is the Lewbel (2012) approach, which builds instruments from heteroskedasticity in the demeaned data. The third is a continuous difference-in-differences design around 2016, the first year after the Paris Agreement, with treatment intensity equal to the country mean of legislative strength over 2010 to 2015:

$$CES_{i,c,t} = \alpha_i + \lambda_t + \theta\, (Post2016_t \times \overline{LEGIS}^{2010-2015}_{c}) + \gamma' X_{i,t} + \delta' Z_{c,t} + \varepsilon_{i,c,t}$$

The event study replaces $Post2016_t$ with year indicators, with 2015 as the base year:

$$CES_{i,c,t} = \alpha_i + \lambda_t + \sum_{s \neq 2015} \theta_s\, (\mathbb{1}[t=s] \times \overline{LEGIS}^{2010-2015}_{c}) + \gamma' X_{i,t} + \delta' Z_{c,t} + \varepsilon_{i,c,t}$$

Lagged instruments are valid only if the lagged ICRG rating affects the score solely through the current rating, which is a strong assumption for slow-moving variables (Bellemare, Masaki and Pepinsky, 2017). The Lewbel instruments need heteroskedasticity that is unrelated to the structural error. The difference-in-differences design needs parallel trends before 2016. We state each assumption again when we report the results.

### 4.5 Heterogeneity and distributional estimates

For heterogeneity we interact each core variable with an indicator for large firms (size at or above the sample median), carbon-intensive industries (SIC 2-digit codes 10, 12, 13, 14, 26, 28, 29, 32 and 33), EU firms, crisis years (2007 to 2012 and 2020; the indicator also includes 2021, which does not occur in the base sample) and firms with high intangible assets (above the median of `ln_intan`):

$$CES_{i,c,t} = \alpha_i + \lambda_t + \beta\, ICRG^{k}_{c,t} + \phi\, (ICRG^{k}_{c,t} \times G_{i,t}) + \gamma' X_{i,t} + \delta' Z_{c,t} + \varepsilon_{i,c,t}$$

where $G$ is the group indicator. Two features of this specification should be kept in mind when reading Table 13. The large-firm indicator is based on current size, which is also a control variable, so the interaction partly compares firms at different points of their own size distribution. A group indicator fixed at a firm's first observed size would be a cleaner test. And the fifteen interaction tests in Table 13 are reported without a correction for multiplicity, which we address in Section 5.10. To study the score distribution we use the method of moments quantile regression (MMQR) of Machado and Santos Silva (2019), with firm fixed effects and year dummies, at the 0.10, 0.25, 0.50, 0.75 and 0.90 quantiles.

## 5. Results

### 5.1 Baseline associations

Table 2 reports the baseline estimates. Legislative strength is positively associated with the carbon score (0.2678, t = 4.03). Civil disorder has a positive coefficient (0.4536, t = 4.67), which means that lower disorder risk goes with a higher score, and growth conditions have a positive coefficient (0.2278, t = 7.62). Government stability, the composite, is also positive (0.0959, t = 4.43). Foreign pressures are not associated with the score (0.0443, t = 0.28). Exchange rate stability has a negative coefficient significant at 10 percent (-0.0553, t = -1.90), and foreign debt has a positive coefficient significant at 10 percent (0.0840, t = 1.73). Among the controls, `size` is positive and significant in every column (from 0.4105 to 0.4274), while `lev` and `roa` are negative and `wdi_unemp` is positive.

**Table 2. Baseline regressions: ICRG risk components and the MSCI Carbon Emissions Score**

| | (1) | (2) | (3) | (4) | (5) | (6) | (7) |

|---|---|---|---|---|---|---|---|

| icrg_govstab | 0.0959*** | | | | | | |

| | (4.43) | | | | | | |

| icrg_legis | | 0.2678*** | | | | | |

| | | (4.03) | | | | | |

| icrg_civdis | | | 0.4536*** | | | | |

| | | | (4.67) | | | | |

| icrg_forpress | | | | 0.0443 | | | |

| | | | | (0.28) | | | |

| icrg_fx | | | | | -0.0553* | | |

| | | | | | (-1.90) | | |

| icrg_fdebt | | | | | | 0.0840* | |

| | | | | | | (1.73) | |

| icrg_gdpg | | | | | | | 0.2278*** |

| | | | | | | | (7.62) |

| Firm and country controls | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

| Observations | 17,008 | 17,008 | 17,008 | 17,008 | 17,008 | 17,008 | 17,008 |

| Firm fixed effects | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

| Year fixed effects | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

| Within R-squared | 0.00531 | 0.00512 | 0.00558 | 0.00413 | 0.00432 | 0.00436 | 0.00784 |

*Note: The dependent variable is* `ces`*. Each column is a separate regression with firm and year fixed effects and the controls* `size`*,* `lev`*,* `roa`*,* `cash`*,* `capx`*,* `ocf`*,* `wdi_infl` *and* `wdi_unemp`*. Robust t-statistics are in parentheses.*  **p&lt;0.01,**  p&lt;0.05,  *p&lt;0.1. Government unity and popular support are in Appendix Table A3.*

The magnitudes are small. Table 3 converts each coefficient into the implied change in the score for a one within-firm standard deviation increase in the ICRG variable. For legislative strength the implied change is 0.0700 points, or 2.33 percent of the overall standard deviation of `ces` (3.002). For civil disorder it is 0.0893 points (2.98 percent). Growth conditions have the largest implied change, 0.3305 points (11.01 percent), because the within-firm variation in this variable is larger. The within R-squared in Table 2 is below 0.01 in every column, so the ICRG variables explain a very small part of the within-firm variation in the score.

**Table 3. Economic magnitudes**

| Variable | Within SD | Coefficient | Implied change for 1 within SD | Change as % of overall SD of ces |

|---|---|---|---|---|

| icrg_govstab | 0.8065 | 0.0959 | 0.0773 | 2.58 |

| icrg_legis | 0.2614 | 0.2678 | 0.0700 | 2.33 |

| icrg_civdis | 0.1969 | 0.4536 | 0.0893 | 2.98 |

| icrg_forpress | 0.1305 | 0.0443 | 0.0058 | 0.19 |

| icrg_fx | 0.6821 | -0.0553 | -0.0377 | -1.26 |

| icrg_fdebt | 0.6643 | 0.0840 | 0.0558 | 1.86 |

| icrg_gdpg | 1.4504 | 0.2278 | 0.3305 | 11.01 |

*Note: The within SD is the standard deviation of the variable after removing firm means. The implied change multiplies it by the Table 2 coefficient. The last column divides the implied change by the overall standard deviation of* `ces` *(3.002), not by the within-firm standard deviation.*

The data support H1, H2 and H3 as associations in the baseline specification. We return to their sensitivity in Sections 5.4 to 5.6. The government stability components also matter. Table A3 shows that government unity (0.1277, t = 2.23) and popular support (0.2413, t = 4.85) are both positively associated with the score. Legislative strength is therefore one of several domestic political components with this sign, and we cannot say that it matters more than popular support.

### 5.2 Scores versus emissions

Table 4 compares the score with the two emission measures on the same sample of 15,753 observations. Each cell comes from a separate regression.

**Table 4. ICRG variables, the carbon score and emissions**

| | ces | ln_ghg | ln_ghg_int |

|---|---|---|---|

| icrg_legis | 0.2622*** | -0.0007 | 0.0251 |

| | (3.81) | (-0.04) | (1.60) |

| icrg_gdpg | 0.2352*** | 0.0296*** | 0.0274*** |

| | (7.68) | (4.45) | (4.25) |

| icrg_civdis | 0.4484*** | -0.0064 | -0.0515** |

| | (4.43) | (-0.29) | (-2.42) |

| ces on ln_ghg | | 0.0548 | |

| | | (1.19) | |

| ces on ln_ghg_int | | | 0.0512 |

| | | | (1.07) |

*Note: Each cell is a separate regression with firm and year fixed effects and the Table 2 controls (Yes), on 15,753 observations. In the last two rows the dependent variable is* `ces` *and the regressor is the emission measure named in the row, reported under that measure's column. Robust t-statistics are in parentheses.*  **p&lt;0.01,**  p&lt;0.05,  *p&lt;0.1. Within R-squared for the* `icrg_legis`*,* `icrg_gdpg` *and* `icrg_civdis` *regressions:* `ces` *0.00499, 0.00808 and 0.00544;* `ln_ghg` *0.0771, 0.0784 and 0.0771;* `ln_ghg_int` *0.0228, 0.0238 and 0.0230.*

For legislative strength, the pattern matches the label "better scores, same emissions". The coefficient is 0.2622 (t = 3.81) for the score, and it is close to zero for `ln_ghg` (-0.0007, t = -0.04) and not significant for `ln_ghg_int` (0.0251, t = 1.60). H4 is not rejected for legislative strength: the score coefficient is significant and the emission coefficients are not distinguishable from zero. This is not a formal test of equality between the score and emission coefficients, and an insignificant coefficient does not prove a zero association. Sections 5.2.1 and 5.2.2 make both statements more precise.

H4 is not supported for growth conditions and is supported only for total emissions in the case of civil disorder. For growth conditions, the coefficient is positive and significant for the score (0.2352, t = 7.68), for `ln_ghg` (0.0296, t = 4.45) and for `ln_ghg_int` (0.0274, t = 4.25). Better growth conditions are associated with a higher score and with higher emissions, so the "same emissions" reading does not hold. Because the outcomes are on different scales, we cannot say from the raw estimates whether the association is stronger for the score; the standardized comparison in Section 5.2.1 addresses this point. For civil disorder, the score coefficient is 0.4484 (t = 4.43), and total emissions are not associated (-0.0064, t = -0.29). Emission intensity, however, is lower where disorder risk is lower (-0.0515, t = -2.42). H4 therefore holds for total emissions but not for intensity. A lower intensity could reflect either a smaller numerator or a larger denominator, and we cannot separate them here.

The score and emissions do not move together within firms. The coefficient of the score on `ln_ghg` is 0.0548 (t = 1.19) and on `ln_ghg_int` is 0.0512 (t = 1.07), and neither is significant. This is consistent with the score capturing something other than emission volumes, but it is not a test of the symbolic response argument.

#### 5.2.1 A standardized comparison of the two sets of associations

The outcomes in Table 4 are measured in different units, so the raw coefficients cannot be compared directly. They can be compared after rescaling each coefficient by the standard deviation of its own outcome. Table 4b does this in two ways: the coefficient divided by the standard deviation of the outcome, and the implied change in standard-deviation units of the outcome for a one within-firm standard deviation change in the ICRG variable.

**Table 4b. Standardized comparison of the score and emission associations**

| ICRG variable | Outcome | Coefficient | 95% CI | Coefficient / SD of outcome | Change in SD of outcome for 1 within SD | 95% CI |

|---|---|---|---|---|---|---|

| icrg_legis | ces | 0.2622 | [0.1273, 0.3971] | 0.0873 | 0.0228 | [0.0111, 0.0346] |

| icrg_legis | ln_ghg | -0.0007 | [-0.0350, 0.0336] | -0.0003 | -0.0001 | [-0.0044, 0.0043] |

| icrg_legis | ln_ghg_int | 0.0251 | [-0.0056, 0.0558] | 0.0108 | 0.0028 | [-0.0006, 0.0063] |

| icrg_gdpg | ces | 0.2352 | [0.1752, 0.2952] | 0.0784 | 0.1136 | [0.0846, 0.1426] |

| icrg_gdpg | ln_ghg | 0.0296 | [0.0166, 0.0426] | 0.0143 | 0.0208 | [0.0116, 0.0299] |

| icrg_gdpg | ln_ghg_int | 0.0274 | [0.0148, 0.0400] | 0.0118 | 0.0171 | [0.0092, 0.0250] |

| icrg_civdis | ces | 0.4484 | [0.2500, 0.6468] | 0.1494 | 0.0294 | [0.0164, 0.0424] |

| icrg_civdis | ln_ghg | -0.0064 | [-0.0497, 0.0369] | -0.0031 | -0.0006 | [-0.0047, 0.0035] |

| icrg_civdis | ln_ghg_int | -0.0515 | [-0.0932, -0.0098] | -0.0222 | -0.0044 | [-0.0079, -0.0008] |

*Note: Computed from the coefficients and robust t-statistics reported in Table 4. The standard deviation of the outcome is taken from Table 1 (ces 3.002, ln_ghg 2.067, ln_ghg_int 2.319). The change for one within-firm standard deviation uses the within SD from Table 3 (legis 0.2614, gdpg 1.4504, civdis 0.1969). Confidence intervals are coefficient ± 1.96 × |coefficient / t| (that is, ± 1.96 robust standard errors). The standard deviations come from the base sample and not from the Table 4 sample of 15,753 observations, so these figures should be recomputed on the exact Table 4 sample before submission.*

Three readings follow from Table 4b. First, in standard-deviation units the score association is between five and eight times larger than the emission association wherever the emission association is itself non-negligible: 0.1136 against 0.0208 for growth conditions and total emissions, and 0.0294 against -0.0044 for civil disorder and emission intensity. Where the emission association is estimated at essentially zero, the gap is larger still: 0.0228 against -0.0001 for legislative strength and total emissions. Second, for legislative strength the confidence interval for the emissions association in standard-deviation units, [-0.0044, 0.0043], is about a third of the width of the interval for the score, [0.0111, 0.0346]. The result is not that the emissions association is small; it is that the emissions association is estimated to be small with enough precision to matter. Third, the growth conditions case is different in kind: the standardized association with emissions (0.0208, CI [0.0116, 0.0299]) is of the same order as the association with the score once the larger within-firm variation in growth conditions is taken into account. Growth conditions are the one variable for which the two sides move together.

#### 5.2.2 What the emission estimates can and cannot rule out

A null result is informative only if the estimates are precise. Table 4c converts the reported coefficients and t-statistics into 95 percent confidence intervals, in log points and in percent, and states the largest association in each direction that the data can exclude.

**Table 4c. Precision of the emission estimates**

| ICRG variable | Outcome | Coefficient (t) | 95% CI, log points | 95% CI, percent | Reading |

|---|---|---|---|---|---|

| icrg_legis | ln_ghg | -0.0007 (-0.04) | [-0.0350, 0.0336] | [-3.44, +3.42] | excludes changes beyond ±3.5% |

| icrg_legis | ln_ghg_int | 0.0251 (1.60) | [-0.0056, 0.0558] | [-0.56, +5.74] | excludes intensity falls beyond 0.6% |

| icrg_gdpg | ln_ghg | 0.0296 (4.45) | [0.0166, 0.0426] | [+1.67, +4.36] | positive; 1.7% to 4.4% |

| icrg_gdpg | ln_ghg_int | 0.0274 (4.25) | [0.0148, 0.0400] | [+1.49, +4.08] | positive; 1.5% to 4.1% |

| icrg_civdis | ln_ghg | -0.0064 (-0.29) | [-0.0497, 0.0369] | [-4.84, +3.75] | excludes changes beyond ±4.9% |

| icrg_civdis | ln_ghg_int | -0.0515 (-2.42) | [-0.0932, -0.0098] | [-8.90, -0.97] | negative; 1.0% to 8.9% |

*Note: Computed from the coefficients and robust t-statistics in Table 4 as coefficient ± 1.96 × |coefficient / t| (that is, ± 1.96 robust standard errors), with percent changes as 100 × (exp(interval) - 1). These intervals are computed from reported statistics and should be replaced by intervals from the estimation output before submission.*

For legislative strength the intervals are informative. The data exclude, at 95 percent confidence, any association with total emissions larger than 3.5 percent in absolute value, and any fall in emission intensity larger than 0.6 percent. The "same emissions" label is therefore a statement with content: it is not that we know nothing about the emissions association, it is that we know it is small. Two limits apply. The intervals describe the association that the within-firm design can estimate, and they inherit the sampling variability of that design; the civil disorder interval for intensity, [-8.90, -0.97] percent, is wide enough to cover both a negligible and a material reduction. And an interval of this kind is not an equivalence test in the formal sense: it bounds the association but does not test the hypothesis that the association lies inside a pre-specified region. A formal equivalence test would require the authors to choose that region before looking at the data (Lakens, 2017), and we have not done so.

### 5.3 Investment channels

Tables 5 and 6 report the two-step channel regressions. They do not support a mediation story, and we read them as suggestive at best. The `capx` columns in Table 6 are not a channel test, as explained below.

Legislative strength is positively associated with intangible assets (0.1306, t = 5.72), but intangible assets are not associated with the score once legislative strength is included (-0.0037, t = -0.12), and the indirect product is -0.0005. For growth conditions the first step is not significant for intangibles (-0.0112, t = -1.24), and the second-step coefficient is 0.0059 (t = 0.18) with an indirect product of -0.0001. For civil disorder, the first step is -0.0529 (t = -1.86) and the second step is 0.0058 (t = 0.18), with an indirect product of -0.0003. Direct coefficients in the second step stay at 0.2606 for legislative strength, 0.2273 for growth conditions and 0.4573 for civil disorder.

**Table 5. Channel: intangible assets**

| | (1) ln_intan | (2) ces | (3) ln_intan | (4) ces | (5) ln_intan | (6) ces |

|---|---|---|---|---|---|---|

| icrg_legis | 0.1306*** | 0.2606*** | | | | |

| | (5.72) | (3.89) | | | | |

| icrg_gdpg | | | -0.0112 | 0.2273*** | | |

| | | | (-1.24) | (7.59) | | |

| icrg_civdis | | | | | -0.0529* | 0.4573*** |

| | | | | | (-1.86) | (4.69) |

| ln_intan | | -0.0037 | | 0.0059 | | 0.0058 |

| | | (-0.12) | | (0.18) | | (0.18) |

| Observations | 16,919 | 16,919 | 16,919 | 16,919 | 16,919 | 16,919 |

| Firm and year fixed effects | Yes | Yes | Yes | Yes | Yes | Yes |

*Note: Columns with* `ln_intan` *use the log of one plus intangible assets as the dependent variable, and columns with* `ces` *use the carbon score. All columns include the Table 2 controls. Robust t-statistics are in parentheses.*  **p&lt;0.01,**  p&lt;0.05,  *p&lt;0.1.*

For growth conditions we also report regressions with sales growth and capital expenditure (Table 6). Growth conditions are not significantly associated with sales growth (0.0037, t = 0.99), and sales growth has a negative coefficient on the score (-0.4148, t = -3.53). The indirect product is -0.0015, which has the opposite sign to the total association. Columns (3) and (4) of Table 6 are not a channel test. The variable `capx` is one of the firm controls in every regression, so column (4) reproduces Table 2 column (7) (0.2278 for growth conditions and -0.0421 for `capx`), and column (3) regresses a control variable on the ICRG variable (0.0026, t = 1.94). The indirect product for `capx` (-0.0001) therefore carries no information about mediation. A proper capital expenditure channel needs the baseline without `capx` among the controls, which we have not run. The slack-resource argument of Section 2.3 is not supported by the intangibles and sales growth proxies, and the `capx` columns give no evidence for or against it. In Table 6 the sales growth regressions use 13,636 observations, and the direct coefficient of growth conditions in column (2) is 0.1527 (t = 4.37). We do not report the total coefficient on this smaller sample, so we do not compare the two.

**Table 6. Channels: sales growth and capital expenditure for growth conditions**

| | (1) sgrowth | (2) ces | (3) capx | (4) ces |

|---|---|---|---|---|

| icrg_gdpg | 0.0037 | 0.1527*** | 0.0026* | 0.2278*** |

| | (0.99) | (4.37) | (1.94) | (7.62) |

| sgrowth | | -0.4148*** | | |

| | | (-3.53) | | |

| capx | | | | -0.0421 |

| | | | | (-0.27) |

| Observations | 13,636 | 13,636 | 17,008 | 17,008 |

| Firm and year fixed effects | Yes | Yes | Yes | Yes |

*Note: Robust t-statistics are in parentheses.*  **p&lt;0.01,**  p&lt;0.05,  *p&lt;0.1. All columns include the Table 2 controls. Columns (3) and (4) are not a mediation test:* `capx` *is also one of the Table 2 controls, so column (4) reproduces Table 2 column (7).*

### 5.4 Omitted variables

Table 7 summarizes the three omitted-variable checks. They give a mixed picture, and the checks differ by variable.

**Table 7. Omitted-variable diagnostics and entropy balancing**

| | icrg_legis | icrg_gdpg | icrg_civdis |

|---|---|---|---|

| Baseline coefficient (Table 2) | 0.2678 | 0.2278 | 0.4536 |

| ITCV, unconditional: correlation with outcome / with regressor | 0.121 / 0.138 | 0.195 / 0.089 | 0.138 / 0.142 |

| ITCV, conditional: correlation with outcome and regressor | 0.139 | 0.223 | 0.157 |

| Conditional ITCV as impact (product) | 0.019 | 0.05 | 0.025 |

| Oster R_max | 0.3057 | 0.3084 | 0.3062 |

| Oster bound coefficient (delta = 1) | 0.13092 | -3.53862 (alternative solution 0.57042) | 0.86162 |

| Oster delta for a zero coefficient | 1.87376 | 0.28275 | -1.26673 |

| Entropy balancing coefficient | 0.3442*** | 0.2185*** | 0.7293*** |

| Entropy balancing t-statistic | (4.90) | (7.20) | (5.65) |

*Note: ITCV and Oster statistics come from regressions on within-firm demeaned data with year indicators and the Table 2 controls, with robust standard errors, at the 5 percent level. Entropy balancing uses an above-median indicator of each ICRG variable as the treatment and balances the means of the eight controls. The entropy balancing regressions have 17,008 observations, firm and year fixed effects, and robust t-statistics.* ** p&lt;0.01.*

For legislative strength, an omitted variable would need a correlation of 0.139 with both the score and the regressor, after conditioning on observed covariates, to remove significance. The largest conditional impact among the observed covariates is 0.0171 in absolute value for a year indicator, which is below the threshold impact of 0.019 but not by a wide margin. The largest among the firm and country controls is 0.0026 in absolute value. The Oster bound is 0.13092 under equal selection ($\delta = 1$), which keeps the sign, and the value of $\delta$ needed to bring the coefficient to zero is 1.87376. By the usual rule that $\delta$ above 1 is reassuring, this result is favorable to the legislative strength association. The unconditional comparison is less favorable: in the raw impact table, year indicators have impacts up to 0.0303, above the unconditional threshold of 0.017. The year indicators are among the controls in these regressions, so the conditional comparison is the relevant one, but we do not want to overstate it.

For growth conditions the picture is weaker. The Oster $\delta$ for a zero coefficient is 0.28275, below 1, and the bound coefficient under $\delta = 1$ is -3.53862, which changes sign and is not interpretable as an estimate. The uncontrolled coefficient (0.40529) is larger than the controlled one (0.22784). The conditional ITCV impact threshold is 0.05, and the largest observed impact is 0.0384 in absolute value for a year indicator. The unconditional threshold is 0.017, and raw impacts of year indicators reach 0.1872, far above it. The ITCV is therefore somewhat favorable in the conditional comparison, less so in the unconditional one, and the Oster result is not favorable.

For civil disorder, the Oster results cannot be interpreted. The uncontrolled coefficient is negative (-0.56164) and the controlled coefficient is positive (0.45359), so the controls change the sign. The $\delta$ for a zero coefficient is negative (-1.26673). We draw no inference from it. The conditional ITCV impact threshold is 0.025, and several year indicators have larger absolute impacts (up to 0.0354), so the ITCV gives little reassurance for this variable either. The raw impacts are smaller than the unconditional threshold of 0.02 (the largest is 0.0144 in absolute value), but the conditional comparison is the more relevant one.

Entropy balancing does not change the baseline conclusions. The coefficients are 0.3442 for legislative strength (t = 4.90), 0.2185 for growth conditions (t = 7.20) and 0.7293 for civil disorder (t = 5.65), and the algorithm converged in all three cases. The means of the controls match exactly after weighting. Variances do not: after weighting, the variance of `wdi_infl` in the control group for growth conditions is 330.7, against 4.045 in the treated group. Entropy balancing helps with observed covariate imbalance, and it cannot address unobserved confounding.

### 5.5 Endogeneity

**Lag instruments.** Table 8 reports two-year lag instruments for the three core variables, on 10,522 observations. The instrument is relevant for legislative strength (Kleibergen-Paap F = 194.7) and growth conditions (F = 97.13). The second-stage coefficients are 0.1061 (t = 0.18) for legislative strength, with a 95 percent confidence interval from -1.054 to 1.266, and 0.0360 (t = 0.14) for growth conditions, with an interval from -0.472 to 0.544. Both intervals include zero and the OLS estimate, so the IV estimates do not tell us whether the association is causal or not. For civil disorder the instrument is weak (F = 0.106, underidentification p = 0.717) and the coefficient is -51.4473 (t = -0.32), which has no plausible interpretation. Anderson-Rubin tests, which stay valid under weak instruments, give p-values of 0.8578 for legislative strength, 0.8895 for growth conditions and 0.0592 for civil disorder. The Hansen J statistic printed in the log is 0.000 for these models, but each model has one instrument for one endogenous variable, so the overidentification test is not defined and cannot be used to judge validity.

A further concern applies to every lag IV. A two-year lag of a slow-moving country rating is probably correlated with unobserved country factors that also relate to the current score. The exclusion restriction is therefore doubtful, and lagging a regressor does not by itself remove endogeneity (Bellemare, Masaki and Pepinsky, 2017).

**Table 8. Instrumental variable estimates**

| | (1) icrg_legis, lag IV | (2) icrg_gdpg, lag IV | (3) icrg_civdis, lag IV | (4) icrg_gdpg, Lewbel |

|---|---|---|---|---|

| Coefficient | 0.1061 | 0.0360 | -51.4473 | 0.1887*** |

| t-statistic | (0.18) | (0.14) | (-0.32) | (3.85) |

| Observations | 10,522 | 10,522 | 10,522 | 17,636 |

| Firm fixed effects | Yes | Yes | Yes | Yes (demeaned) |

| Year fixed effects | Yes | Yes | Yes | Year indicators included |

| Instrument | Two-year lag | Two-year lag | Two-year lag | Generated (Lewbel) |

| Kleibergen-Paap rk Wald F | 194.7 | 97.13 | 0.106 | 282.6 |

| Underidentification p | 0 | 0 | 0.717 | |

| Hansen J p | not defined (exactly identified) | not defined (exactly identified) | not defined (exactly identified) | 0.000 |

*Note: The dependent variable is* `ces`*. Columns (1) to (3) include the Table 2 controls with firm and year fixed effects and robust t-statistics. Column (4) uses within-firm demeaned data with the demeaned controls and year indicators. The log prints a Hansen J of 0.000 for columns (1) to (3), but the equation is exactly identified. The Lewbel estimates for* `icrg_legis` *and* `icrg_civdis` *could not be computed (the routine failed with a variable-naming error, return code 198).* ** p&lt;0.01.*

**Lewbel instruments.** The Lewbel routine ran only for growth conditions. It gives a positive and significant coefficient (0.1887, t = 3.85) with a Kleibergen-Paap F of 282.6. The Hansen J statistic is 136.448 and its p-value is 0.000, so the overidentification test rejects the joint validity of the generated instruments. We do not treat this estimate as evidence of a causal relation. The routine failed for legislative strength and civil disorder (return code 198), so we have no Lewbel estimate for them, and we did not alter the code to force a result.

**Difference-in-differences and event study.** Table 9 reports the continuous difference-in-differences estimate. The coefficient is 0.1451, with a robust t-statistic of 0.79 and a country-clustered t-statistic of 0.43 (55 countries). The design needs parallel trends, and the event study in Table 10 and Figure 1 shows that this condition does not hold.

**Table 9. Continuous difference-in-differences (Paris Agreement, 2016)**

| | (1) Robust SE | (2) Country-clustered SE |

|---|---|---|

| Post2016 x pre-2016 icrg_legis | 0.1451 | 0.1451 |

| t-statistic | (0.79) | (0.43) |

| Observations | 16,992 | 16,992 |

| Firm and year fixed effects | Yes | Yes |

| Countries | | 55 |

*Note: The dependent variable is* `ces`*. Treatment intensity is the country mean of* `icrg_legis` *over 2010 to 2015. Both columns include the Table 2 controls.*

**Figure 1. Event study of the legislative strength interaction (base year 2015)**

![Event study coefficients for the interaction of year indicators with pre-2016 legislative strength, base year 2015, with 95 percent confidence intervals](../output/Fig1_event_study_legis.png)

*Note: Points are coefficients on the interaction of each year indicator with the country mean of* `icrg_legis` *over 2010 to 2015, with firm and year fixed effects and the Table 2 controls. Bars are 95 percent confidence intervals. The vertical axis label in the figure file reads "Effect on carbon emissions score", but the plotted values are regression coefficients on the carbon score* `ces`*) and are not causal effects. The figure shows every coefficient below zero, with all pre-2016 intervals and the 2016 to 2019 intervals excluding zero and the 2020 interval including zero.*

Every pre-2016 coefficient in Table 10 is significant at the 5 percent level, and they are large: they range from -0.6094 (2014) to -2.6969 (2010), compared with a standard deviation of the score of 3.002. Figure 1 shows that all coefficients are negative relative to 2015, both before and after 2016, and that there is no visible break at 2016. The post-2016 coefficients are also negative, from -0.5149 (2020, t = -1.70) to -1.6250 (2018). In every pre-period year, the score of firms in countries with higher legislative strength differed significantly from its 2015 level relative to firms in other countries. The score paths were therefore already different before 2016, and the difference-in-differences estimate cannot be read as a policy response. Possible reasons include the strong growth of the MSCI coverage universe over the sample period and the construction of the treatment variable, which uses ICRG values from 2010 to 2015. A third reason is that the pre-trends may reflect the composition of the rated universe rather than any behaviour: the number of rated firm-years in the deduplicated file grows from 586 in 2007 to 3,121 in 2020, so the countries that enter the panel in later years are not the same as those present in 2007. We have not tested these explanations.

**Table 10. Event study coefficients (base year 2015)**

| Year | Coefficient | SE | t |

|---|---|---|---|

| 2007 | -1.5786 | 0.5631 | -2.8035 |

| 2008 | -2.1257 | 0.4671 | -4.5512 |

| 2009 | -2.3452 | 0.3923 | -5.9782 |

| 2010 | -2.6969 | 0.3862 | -6.9827 |

| 2011 | -2.2083 | 0.3655 | -6.0415 |

| 2012 | -1.0579 | 0.3233 | -3.2727 |

| 2013 | -1.0533 | 0.2862 | -3.6809 |

| 2014 | -0.6094 | 0.2814 | -2.1657 |

| 2016 | -1.0366 | 0.2765 | -3.7495 |

| 2017 | -0.9017 | 0.2722 | -3.3127 |

| 2018 | -1.6250 | 0.2769 | -5.8681 |

| 2019 | -0.6851 | 0.3009 | -2.2766 |

| 2020 | -0.5149 | 0.3034 | -1.6971 |

*Note: Coefficients on year indicators interacted with the country mean of* `icrg_legis` *over 2010 to 2015, with firm and year fixed effects, the Table 2 controls and robust standard errors.*

The three designs are inconclusive. The lag instruments are imprecise or weak. The Lewbel instruments fail overidentification and exist only for one variable. The event study rejects the parallel trends condition. The data contain no credible source of exogenous variation in country institutions, and all results in this paper describe associations.

### 5.6 Sensitivity checks

Table 11 reports four variations of the baseline for the three core variables. The first uses country-clustered standard errors, with 61 countries. The coefficients keep their significance but with lower precision: legislative strength is 0.2678 (t = 2.22), growth conditions 0.2278 (t = 2.48), and civil disorder 0.4536 (t = 1.81), which is significant only at 10 percent. The second uses one-year lagged regressors. Legislative strength (0.2565, t = 3.47) and growth conditions (0.0976, t = 2.91) remain positive and significant, but the civil disorder coefficient is not significant (0.1111, t = 1.03). The third adds industry-by-year fixed effects and gives 0.1201 (t = 1.81) for legislative strength, which is less than half the baseline coefficient and significant at 10 percent, 0.2148 (t = 7.10) for growth conditions and 0.4320 (t = 4.46) for civil disorder. The fourth drops Japan, China and the United Kingdom and leaves 9,682 observations. The coefficients are 0.2938 (t = 2.65), 0.1546 (t = 3.78) and 0.3425 (t = 2.70).

**Table 11. Sensitivity checks**

| | (1) Country-clustered SE | (2) One-year lags | (3) Industry x year FE | (4) Excluding JPN, CHN, GBR |

|---|---|---|---|---|

| icrg_legis | 0.2678** | | 0.1201* | 0.2938*** |

| | (2.22) | | (1.81) | (2.65) |

| L1_icrg_legis | | 0.2565*** | | |

| | | (3.47) | | |

| icrg_gdpg | 0.2278** | | 0.2148*** | 0.1546*** |

| | (2.48) | | (7.10) | (3.78) |

| L1_icrg_gdpg | | 0.0976*** | | |

| | | (2.91) | | |

| icrg_civdis | 0.4536* | | 0.4320*** | 0.3425*** |

| | (1.81) | | (4.46) | (2.70) |

| L1_icrg_civdis | | 0.1111 | | |

| | | (1.03) | | |

| Observations | 17,008 | 16,020 | 16,942 | 9,682 |

| Countries | 61 | | | |

*Note: The dependent variable is* `ces`*. Each cell is a separate regression. Column (1) clusters standard errors by country, column (2) uses one-year lags of the ICRG variable and the controls, column (3) replaces year fixed effects by industry (SIC 2-digit) by year fixed effects, and column (4) excludes firms headquartered in Japan, China and the United Kingdom. All columns include firm fixed effects and the Table 2 controls (lagged in column 2). t-statistics are in parentheses (robust except in column 1).*  **p&lt;0.01,**  p&lt;0.05,  *p&lt;0.1.*

Table 12 uses two alternative outcomes. The alternative score `ces_m` is positively associated with all three variables (0.2005, 0.0871 and 0.2457). The environmental pillar `env` is not associated with legislative strength (-0.0405, t = -0.91), which is a result to consider carefully because `env` contains `ces` as a component. Growth conditions are associated with `env` (0.0591, t = 2.96) and civil disorder at 10 percent (0.1098, t = 1.72). The legislative strength association is therefore specific to the carbon score and the alternative score, and it is not visible in the wider environmental pillar.

The pillar result can be made more precise than "not visible". The MSCI environmental pillar is a weighted average of several environmental key issue scores, each on a 0 to 10 scale, so if only the carbon component responded to legislative strength and the others did not, the pillar coefficient should equal the carbon weight times the carbon coefficient. The carbon coefficient on the comparable sample in Table 4 is 0.2622, with a 95 percent confidence interval of [0.1273, 0.3971]. The observed pillar coefficient is -0.0405, with a 95 percent interval of [-0.1277, 0.0467]. The upper bound of that interval, 0.0467, corresponds to an implied carbon weight of 0.178 at most. A carbon weight of one third, which is plausible for many industries, would imply a pillar coefficient of about 0.087, which the interval excludes. The pillar result is therefore not simply dilution: it is difficult to reconcile with a carbon weight above about 0.18 unless other environmental components move in the opposite direction. Two caveats apply. We do not know the actual key issue weights for our sample, and the environmental pillar regressions use 17,006 observations rather than the 15,753 of Table 4. The calculation is an order-of-magnitude check and not a test.

**Table 12. Alternative outcomes**

| | (1) ces_m | (2) ces_m | (3) ces_m | (4) env | (5) env | (6) env |

|---|---|---|---|---|---|---|

| icrg_legis | 0.2005*** | | | -0.0405 | | |

| | (3.01) | | | (-0.91) | | |

| icrg_gdpg | | 0.0871*** | | | 0.0591*** | |

| | | (3.09) | | | (2.96) | |

| icrg_civdis | | | 0.2457*** | | | 0.1098* |

| | | | (2.61) | | | (1.72) |

| Observations | 17,008 | 17,008 | 17,008 | 17,006 | 17,006 | 17,006 |

| Firm and year fixed effects | Yes | Yes | Yes | Yes | Yes | Yes |

*Note:* `ces_m` *is an alternative version of the carbon score whose definition is unverified, and* `env` *is the MSCI environmental pillar score. All columns include the Table 2 controls. Robust t-statistics are in parentheses.*  **p&lt;0.01,**  p&lt;0.05,  *p&lt;0.1.*

### 5.7 Heterogeneity

Table 13 reports the interaction models. The evidence on H5 is mixed. The legislative strength interaction with the large-firm indicator is 0.3549 (t = 2.62), while the coefficient for smaller firms is 0.0737 (t = 0.73). The growth conditions interaction is 0.1518 (t = 4.85), on top of a coefficient of 0.1826 for smaller firms. For civil disorder the interaction is 0.0176 (t = 0.11), so there is no difference by size. H5 is supported for legislative strength and growth conditions and not supported for civil disorder.

Other splits give a varied picture. In carbon-intensive industries the growth conditions interaction is -0.3124 (t = -9.88), against a coefficient of 0.3160 for other industries, so the interaction almost offsets the baseline association. For civil disorder the interaction is positive (0.6064, t = 3.46), so the association is larger in carbon-intensive industries. For legislative strength there is no significant industry difference (0.1274, t = 0.97). The EU interactions are not significant for legislative strength (0.2259, t = 1.30) or growth conditions (0.0284, t = 0.81), and for civil disorder it is significant at 10 percent (0.3729, t = 1.80). In crisis years the growth conditions interaction is positive (0.1759, t = 5.59) while the coefficient outside crisis years is not significant (0.0589, t = 1.39). The civil disorder interaction in crisis years is negative (-0.2932, t = -2.60), and the legislative strength interaction is not significant (-0.1060, t = -0.91). For firms with high intangible assets, the growth conditions interaction is positive (0.2193, t = 7.31), and the other two interactions are not significant (0.0419 and -0.0309). The `crisis` indicator includes 2021, but the base sample has no observations after 2020, so 2021 plays no role in these estimates.

**Table 13. Heterogeneity: interactions with firm and period groups**

| ICRG variable | Group G | ICRG coefficient (G = 0) | Interaction with G | Observations |

|---|---|---|---|---|

| icrg_legis | Large firm | 0.0737 (0.73) | 0.3549*** (2.62) | 17,008 |

| icrg_gdpg | Large firm | 0.1826*** (5.72) | 0.1518*** (4.85) | 17,008 |

| icrg_civdis | Large firm | 0.4531*** (3.89) | 0.0176 (0.11) | 17,008 |

| icrg_legis | Carbon-intensive | 0.2255*** (2.80) | 0.1274 (0.97) | 17,008 |

| icrg_gdpg | Carbon-intensive | 0.3160*** (10.00) | -0.3124*** (-9.88) | 17,008 |

| icrg_civdis | Carbon-intensive | 0.2722** (2.34) | 0.6064*** (3.46) | 17,008 |

| icrg_legis | EU | 0.2170*** (2.88) | 0.2259 (1.30) | 17,008 |

| icrg_gdpg | EU | 0.2106*** (6.17) | 0.0284 (0.81) | 17,008 |

| icrg_civdis | EU | 0.3292*** (2.99) | 0.3729* (1.80) | 17,008 |

| icrg_legis | Crisis years | 0.3208*** (3.63) | -0.1060 (-0.91) | 17,008 |

| icrg_gdpg | Crisis years | 0.0589 (1.39) | 0.1759*** (5.59) | 17,008 |

| icrg_civdis | Crisis years | 0.5353*** (5.18) | -0.2932*** (-2.60) | 17,008 |

| icrg_legis | High intangibles | 0.2356** (2.26) | 0.0419 (0.32) | 16,919 |

| icrg_gdpg | High intangibles | 0.1254*** (3.77) | 0.2193*** (7.31) | 16,919 |

| icrg_civdis | High intangibles | 0.4717*** (4.09) | -0.0309 (-0.22) | 16,919 |

*Note: The dependent variable is* `ces`*. Each row is a separate regression of* `ces` *on the ICRG variable, the group indicator G and their interaction, with firm and year fixed effects and the Table 2 controls. The "ICRG coefficient (G = 0)" column is the coefficient for the reference group (smaller firms, other industries, non-EU firms, other years, firms with lower intangibles). Robust t-statistics are in parentheses.*  **p&lt;0.01,**  p&lt;0.05,  *p&lt;0.1.*

### 5.8 Distributional estimates

Table 14 reports MMQR estimates on 17,636 observations. For legislative strength, the coefficients decline from 0.3257 at the 0.10 quantile to 0.2275 at the 0.90 quantile, but none is significant (z-statistics from 0.55 to 0.99). We therefore cannot say that the association differs across the score distribution, and we also cannot confirm the baseline result with this estimator. The MMQR standard errors are much larger than those of the baseline regression, and the estimator imposes a location-scale structure that may not fit a bounded score. For growth conditions, the coefficient is significant at the 0.10 quantile (0.4166, z = 2.22) and the 0.25 quantile (0.3417, z = 3.57), and it is not significant at the median or above (0.2065, 0.1361 and 0.0964). The association with growth conditions is therefore visible in the lower part of the score distribution, among firms with weaker carbon management. For civil disorder no quantile is significant.

**Table 14. MMQR estimates for the carbon score**

| | q0.10 | q0.25 | q0.50 | q0.75 | q0.90 |

|---|---|---|---|---|---|

| icrg_legis | 0.3257 | 0.3025 | 0.2615 | 0.2398 | 0.2275 |

| | (0.55) | (0.71) | (0.99) | (0.75) | (0.59) |

| icrg_gdpg | 0.4166** | 0.3417*** | 0.2065 | 0.1361 | 0.0964 |

| | (2.22) | (3.57) | (0.73) | (0.32) | (0.19) |

| icrg_civdis | 0.9095 | 0.7271 | 0.4001 | 0.2301 | 0.1334 |

| | (1.07) | (1.59) | (0.32) | (0.12) | (0.06) |

| Observations | 17,636 | 17,636 | 17,636 | 17,636 | 17,636 |

*Note: Each cell is a separate MMQR regression of* `ces` *with firm fixed effects, year dummies and the Table 2 controls on the base sample. z-statistics are in parentheses.*  **p&lt;0.01,**  p&lt;0.05,  *p&lt;0.1.*

### 5.9 Summary of the hypotheses

H1 is supported as an association for legislative strength in the baseline and in most sensitivity checks, with caveats: the magnitude is small, the clustered result is significant at 5 percent only, the industry-by-year specification gives less than half the baseline coefficient, the environmental pillar shows no association, MMQR shows none, and the causal designs are inconclusive. H2 is supported as an association (0.2278, t = 7.62), but the channels that the slack argument predicts are not found, and Oster's $\delta$ is below 1. H3 is supported in the baseline but is the least stable result: it loses significance with one-year lags and falls to 10 percent with clustered standard errors. H4 is not rejected for legislative strength (the emission coefficients are not distinguishable from zero, the standardized association with the score is much larger, and we run no formal equality test), partly supported for civil disorder (total emissions but not intensity) and not supported for growth conditions, where emissions rise with the score. H5 is supported for legislative strength and growth conditions and not supported for civil disorder, with the qualification in Section 5.10.

### 5.10 How far the estimates can be pushed: precision, equivalence and multiplicity

Three features of the evidence limit how the results should be read, and none of them requires new estimation.

**Precision of the emission results.** As Section 5.2.2 shows, the null emission results for legislative strength are informative rather than empty: the data exclude associations with total emissions larger than about 3.5 percent in absolute value, and intensity reductions larger than about 0.6 percent. The same is not true for civil disorder, where the intensity interval runs from -8.90 to -0.97 percent and therefore covers both negligible and material reductions. The practical implication is that "same emissions" is a strong statement for legislative strength and a weak one for civil disorder.

**Equivalence claims.** Confidence intervals of this kind bound the association but do not test it against a pre-specified region. A formal equivalence test would require the authors to state, before seeing the data, the smallest association that would matter economically, and then to test whether the estimate lies inside it (Lakens, 2017). We recommend this for the next version, because it converts "we find nothing" into "we rule out anything larger than x", which is the claim the title makes.

**Multiplicity.** The paper reports many tests of the same kind: seven baseline specifications, fifteen interaction tests in Table 13, four sensitivity specifications for three variables, and three alternative outcomes. Taking the fifteen interaction tests in Table 13 as one family and computing two-sided p-values from the reported t-statistics, a Bonferroni correction would require p < 0.0033. Five tests meet that standard: growth conditions with large firms (t = 4.85), growth conditions with carbon-intensive industries (t = -9.88), civil disorder with carbon-intensive industries (t = 3.46), growth conditions in crisis years (t = 5.59) and growth conditions with high intangibles (t = 7.31). The legislative strength interaction with large firms (t = 2.62, p = 0.0088) and the civil disorder interaction with crisis years (t = -2.60, p = 0.0093) do not. A Benjamini-Hochberg correction at a 5 percent false discovery rate is less demanding: seven tests pass, and the legislative strength interaction with large firms is among them (p = 0.0088 against a rank-specific threshold of 0.0200).

We draw two conclusions. The heterogeneity result for legislative strength and large firms should be described as suggestive, not established, because its status depends on the correction that the reader prefers. And the growth conditions interactions are the only heterogeneity results that are robust to any correction, which is consistent with the rest of the paper: growth conditions are the variable with the most stable association and the largest magnitude, and also the variable for which the evidence speaks against the "same emissions" reading.

## 6. Discussion

### 6.1 The gap between scores and emissions

The central result is a gap. Firms in countries with stronger legislatures have higher carbon management scores, and they do not have different total emissions or emission intensity. Institutional theory offers a reading in which formal structures and reporting respond to pressure faster than technical activity does (Meyer and Rowan, 1977; Walker and Wan, 2012). Our data are consistent with that reading, but they cannot confirm it, and the standardized comparison in Table 4b shows how large the difference between the two sides is: 0.0228 standard deviations of the score against -0.0001 standard deviations of emissions for the same change in legislative strength.

Three mechanisms could produce this gap, and our design cannot separate them. The first is a behavioural mechanism: firms respond to expected regulation by building management systems and reporting, which are cheap and reversible, and defer abatement, which is not. The second is a measurement mechanism: the score is built to be exposure-adjusted and relative, so it can rise without emissions falling. MSCI computes the carbon key issue score as $KI = 7 - (\max(EXP, 2) - MGT)$, and the management score includes a performance component that compares a firm's emissions intensity and its trend with those of industry peers (MSCI ESG Research LLC, 2023). A firm can improve that component by outperforming peers while its own emissions rise, which is exactly the pattern we see for growth conditions. The third is a rating-practice mechanism: the exposure score itself has a country input, because the geographic exposure score for a country is determined by the annual emissions reduction required to meet that country's disclosed targets (MSCI ESG Research LLC, 2023). Part of the country-level association may therefore come from the rating's own construction rather than from anything the firm did.

The rating-practice mechanism deserves more weight than the earlier version of this paper gave it, and it is now a concrete claim rather than a vague worry. Ratings are reactive, and firms change the behaviour that is measured once they are rated (Chatterji and Toffel, 2010). Disclosure does not remove rater discretion, it increases it: more disclosure is associated with more disagreement between raters, not less (Christensen, Serafeim and Sikochi, 2022). And the level of an ESG score is strongly related to firm size and to the amount of information a rater holds on a firm (Drempetic, Klein and Zwergel, 2020). Since a stronger legislature plausibly comes with more disclosure rules and more public information about firms, the information environment of the rater improves at the same time as the firm's management improves. Our estimate cannot tell these apart.

### 6.2 What the comparison with the disclosure literature adds

It is tempting to read the result as evidence that disclosure and management systems never change emissions. The disclosure literature does not support that reading. Where a disclosure mandate carries monitoring and enforcement, emissions fall: Downar, Ernstberger, Reichelstein, Schwenen and Zaklan (2021) find emission reductions after a UK mandate, and Krueger, Sautner, Tang and Zhong (2024) document changes in disclosure and in several real outcomes after mandates around the world. Christensen, Hail and Leuz (2021) conclude in their review that real effects are more likely where a mandate is accompanied by enforcement and by stakeholders who can act on the information.

Our setting differs from those studies in a way that makes the comparison informative rather than contradictory. Those studies estimate the effect of a mandate that changes the information environment and its enforcement at a point in time. We compare countries that differ in a slow-moving institutional rating, with no change in enforcement that we can isolate. If the level of legislative capacity in our sample were associated with the compliance pressure that turns disclosure into abatement, we should see it in emissions, and we do not. A reading consistent with both sets of results is that legislative capacity in the range observed in our sample is associated with more and better disclosed carbon management, but not with enough pressure to move the tonnes. This reading also matches the mixed evidence on greenwashing: firms communicate more than they do where scrutiny is uneven and where the costs of the visible action are lower than the costs of the underlying change (Lyon and Montgomery, 2015; Delmas and Burbano, 2011).

### 6.3 Which institutions matter, and as what

Our results connect to the literature on national institutions and corporate social performance (Ioannou and Serafeim, 2012; Cai, Pan and Statman, 2016; Liang and Renneboog, 2017). Those studies use broad social performance measures. We find that the association with carbon management scores is present for several domestic political components, including government unity (0.1277) and popular support (0.2413) as well as legislative strength (0.2678), and absent for foreign pressures (0.0443). The association is therefore not specific to the legislature. The results suggest that stable and capable domestic politics are associated with higher carbon scores, and they do not single out the legislature. The weak results for external risk are consistent with the view that the relevant pressure comes from the domestic regulatory environment. Exchange rate stability (-0.0553) and foreign debt (0.0840) have opposite signs and are significant only at 10 percent, so we do not interpret them.

The comparison with work on emission outcomes sharpens the contribution. Studies that relate country institutions to emissions find associations with democracy and electoral rules (Muttakin, Rana and Mihret, 2022; Muttakin, Mihret and Rana, 2021), with economic freedom (Ren, Li, Cheng and Zheng, 2024) and with policy uncertainty interacted with institutional quality (Tee, Wong and Hooy, 2023), and Andreou, Anyfantaki, Cabolis and Dellis (2026) show that institutional quality conditions how much firms abate under an identical carbon price. That literature treats institutions as a boundary condition on the effectiveness of policy. Our results fit that view better than they fit a view in which legislative strength is a lever that moves firms on its own: the institutions in our sample are associated with how firms are rated, and not with how much they emit, which is what one would expect if institutions shape the response to pressure rather than generate pressure by themselves.

Two empirical regularities point in the same direction. Legislative strength is not the strongest of the government stability components: popular support has a comparable coefficient and government unity is also significant, so what matters is the domestic political system rather than one of its parts. And the association is specific to the carbon score, since the wider environmental pillar shows nothing for legislative strength, and the calculation in Section 5.6 suggests that this is not only dilution. Both regularities are easier to explain if the association runs through carbon-specific rules, targets and disclosure practices than through a general tendency of well-governed countries to produce better-managed firms.

### 6.4 Civil disorder: the least stable result, and the one with a mechanism for emissions

Civil disorder shows the only sign of a link with an emission outcome, in the form of lower intensity (-0.0515). Its score association is also the least stable. It is insignificant with one-year lags and weakly significant with clustered standard errors, its instrument is weak, and its Oster diagnostic cannot be interpreted. We read the intensity result with caution, since it is one coefficient among many in this paper, since it does not survive a Bonferroni correction in the interaction family, and since we have not adjusted for multiple testing across the main specifications either.

The theory gives no clear prediction for this variable, and the data do not settle it. On one side, political instability weakens the stringency of environmental policy (Fredriksson and Svensson, 2003), and internal conflict reduces the incentive to invest in the capacity to enforce it (Besley and Persson, 2010), so lower disorder should mean better enforcement and better environmental outcomes. On the other side, unrest raises the attention that stakeholders pay to firms and increases the perceived risk of being targeted (Vasi and King, 2012), and firms disclose climate strategies in response to public and private politics (Reid and Toffel, 2009), so more unrest could mean more disclosure and more management. Our estimates are consistent with the first channel for intensity and say nothing about the second. The wide confidence interval for intensity, from -8.90 to -0.97 percent, is the honest summary: the data allow a negligible and a material reduction.

### 6.5 Size, coverage and the visibility argument

The concentration among larger firms agrees with the visibility argument of Marquis, Toffel and Zhou (2016), which concerns scrutiny. Smaller firms show a coefficient close to zero for legislative strength (0.0737, t = 0.73). Large firms are also more likely to be covered and rated in detail, and firm size itself explains a large part of the variation in ESG scores (Drempetic, Klein and Zwergel, 2020), so the size pattern may reflect rating practice as much as behaviour. Investor pressure is concentrated on large emitters with significant institutional ownership, and where it is applied it is followed by lower emissions (Azar, Duro, Kadach and Ormazabal, 2021), which means the size split is also a split in exposure to engagement.

We cannot separate these explanations, and the correction for multiplicity in Section 5.10 makes the separation less urgent: the interaction for legislative strength is suggestive under a false-discovery-rate correction and not significant under a Bonferroni correction. We therefore treat H5 as supported for growth conditions, and as a promising but unconfirmed pattern for legislative strength. A better test would define size at the firm's first observed year rather than at the current year, because the current-year indicator is mechanically related to the size control.

### 6.6 Implications

**For researchers.** The main implication is negative and practical: the MSCI carbon score should not be used as a proxy for emissions. In our sample the two move independently within firms, the institutional variables that predict one do not predict the other, and the score's own construction makes the two conceptually distinct. Studies that need an emissions measure should use emissions, while recognizing that firm-level carbon data have known problems of comparability and estimation (Busch, Johnson and Pioch, 2022). Studies that need a measure of climate exposure can use text-based measures built from earnings calls (Sautner, van Lent, Vilkov and Zhang, 2023), which capture something different again. Reporting a score result and an emissions result side by side, as we do, is the cheapest way to keep the two apart.

**For managers and investors.** A higher carbon score in a country with a strong legislature is not a reliable signal of lower emissions, and a reader who needs information on emissions should use emission data directly. This matters because investors use ESG information for several distinct purposes, including engagement, risk management and product design (Amel-Zadeh and Serafeim, 2018), and the information value of a score differs across those uses. Where the objective is emission reduction, engagement targeted at large emitters has produced measurable reductions (Azar, Duro, Kadach and Ormazabal, 2021), which suggests that the signal to act on is the emissions level rather than the rating.

**For policy.** Our results do not say that institutions are irrelevant to decarbonization. They say that the institutional variation we study is associated with the rating and not with the emissions, which is compatible with the view that institutions work as a condition on the effectiveness of policy rather than as a substitute for it (Andreou, Anyfantaki, Cabolis and Dellis, 2026; Tee, Wong and Hooy, 2023). Read together with the disclosure literature, the results suggest that rules which change reporting raise scores, and that rules which change reporting and are enforced can also lower emissions (Downar, Ernstberger, Reichelstein, Schwenen and Zaklan, 2021; Christensen, Hail and Leuz, 2021). Since we estimate associations and not effects, we draw no conclusion about the effect of legislative reform.

### 6.7 Limitations and what would change the conclusion

Three alternative explanations deserve attention. The first is a rating-practice explanation: scores may differ by country because of how rating providers collect information, and a stronger legislature may come with stricter disclosure rules that raise the amount of information available to the rater. Section 6.1 makes this explanation concrete, and we cannot test it with our data. The second is a composition explanation. The number of rated firm-years in the deduplicated file grows from 586 in 2007 to 3,121 in 2020, so the mix of firms and countries changes over time, and firm fixed effects do not fully remove changes in the pool of rated firms. This explanation is the most likely source of the pre-trends in Figure 1, and a constant-coverage subsample would test it. The third is reverse association: firms with high scores may locate or lobby in countries with certain institutions, although this seems less likely for the national legislative strength rating.

The paper's most important limits are in identification. The baseline includes firm and year fixed effects, which rule out fixed firm traits and common shocks. They do not rule out country-specific shocks that move both institutions and ratings, and the diagnostics only partly help. The Oster result is favorable for legislative strength and not for the other two variables. The event study suggests that countries with different legislative strength were on different score paths before 2016. The most defensible reading is that firms in countries with stronger legislatures score higher, and not that raising legislative capacity would raise scores.

Four further limits qualify the inference. Standard errors are robust in the main tables and clustered in one sensitivity column; with 61 clusters, conventional cluster-robust standard errors may be inflated, and a wild cluster bootstrap would be a better approximation (Abadie, Athey, Imbens and Wooldridge, 2023; Cameron, Gelbach and Miller, 2008). The civil disorder result is significant at 10 percent under clustering, so the inference for that variable depends on this choice. The paper reports many specifications without a correction for multiplicity, which Section 5.10 addresses for the interaction family only. And the outcome is a bounded score with mass at both ends, so a fractional-response or censored specification would be a more faithful model of the data-generating process than a linear one.

## 7. Conclusion

We study how country-level political and economic risk relates to firm carbon management and emissions in a panel of 17,636 firm-year observations for fiscal years 2007 to 2020 (17,008 in the baseline regressions after singleton firms are dropped). H1 holds as an association: legislative strength is associated with higher MSCI carbon scores (0.2678, t = 4.03), with a small implied magnitude (2.33 percent of the overall standard deviation of the score for a one within-firm standard deviation change). H2 holds as an association for growth conditions, with a moderate implied magnitude (11.01 percent), and growth conditions are also associated with higher emissions. H3 holds in the baseline but is the least stable result: it is insignificant with one-year lags and only weakly significant with clustered standard errors. H4 is not rejected for legislative strength, because the emission coefficients (-0.0007 and 0.0251, t = 1.60) are not distinguishable from zero, and because the standardized association with the score is five to eight times larger than the association with emissions wherever the latter is non-negligible, and is estimated at essentially zero for legislative strength. It does not hold for growth conditions, where emissions are higher, and it holds only in part for civil disorder, where emission intensity is lower. H5 holds for growth conditions, and holds for legislative strength under a false-discovery-rate correction but not under a Bonferroni correction. The instrumental variable, difference-in-differences and event study designs do not provide conclusive evidence, and the paper reports associations only.

These results have limited implications for practice. In our sample, a higher carbon score in a country with a stronger legislature does not come with lower total emissions (-0.0007, t = -0.04) or lower emission intensity (0.0251, t = 1.60), and the data exclude associations with total emissions larger than about 3.5 percent in either direction. Because the results describe associations, we draw no conclusion about the effect of legislative reform. Users of carbon ratings may want to read emission data next to the score.

The study has several limitations. First, no credible exogenous variation in country institutions is available. The lag instruments are imprecise or weak, and the Lewbel instruments fail overidentification and exist for one variable only. The event study also shows pre-trends. Second, the MSCI score is a management rating and not an emissions measure, it has mass at its bounds, and its exposure component contains a country-level input that is plausibly correlated with our regressors, so part of the association may come from the construction of the rating. Third, the GHG field has an ambiguous definition in its source, and we treat it as an emissions level. Fourth, the main tables use robust and not country-clustered standard errors, and with clustering the civil disorder result is significant only at 10 percent. Fifth, the country ratings move slowly, so identification rests on a limited number of rating changes within countries. Sixth, the sample is concentrated in a few countries: Japan, the United Kingdom, China and Australia contribute half of the observations, although excluding the first three keeps the main results. Seventh, the within R-squared of the baseline regressions is below 0.01. Eighth, the duplicate-removal tie-break is arbitrary for rows that differ in content, and the alternative score `ces_m` has an unverified definition. Ninth, we report many specifications and correct for multiplicity in the interaction family only. Finally, we do not run a formal equivalence test on the emission results, so "same emissions" remains a bound rather than a test.

Future work can use settings with plausible exogenous variation, for example legislative changes or elections that alter legislative strength, and firm-level data on disclosure and abatement projects that separate reporting from emission reduction. Matching the rating with verified emission data from regulatory registers would help to test the symbolic response argument directly, in the way that installation-level data from emissions trading systems now allow (Andreou, Anyfantaki, Cabolis and Dellis, 2026). Two cheaper additions would also help: a formal equivalence test with a pre-specified region for the emission coefficients, and a constant-coverage subsample that holds the set of rated firms fixed and tests the composition explanation for the event study pre-trends.

## References

Abadie, A., Athey, S., Imbens, G. W., Wooldridge, J. M. (2023). When should you adjust standard errors for clustering? Quarterly Journal of Economics, 138(1), 1-35.

Amel-Zadeh, A., Serafeim, G. (2018). Why and how investors use ESG information: Evidence from a global survey. Financial Analysts Journal, 74(3), 87-103.

Andreou, P. C., Anyfantaki, S., Cabolis, C., Dellis, K. (2026). Institutional and capability enablers of firm-level emissions abatement under the EU Emissions Trading System. Research Policy, 55(4), 105432.

Azar, J., Duro, M., Kadach, I., Ormazabal, G. (2021). The Big Three and corporate carbon emissions around the world. Journal of Financial Economics, 142(2), 674-696.

Bansal, P., Clelland, I. (2004). Talking trash: Legitimacy, impression management, and unsystematic risk in the context of the natural environment. Academy of Management Journal, 47(1), 93-103.

Bättig, M. B., Bernauer, T. (2009). National institutions and global public goods: Are democracies more cooperative in climate change policy? International Organization, 63(2), 281-308.

Bellemare, M. F., Masaki, T., Pepinsky, T. B. (2017). Lagged explanatory variables and the estimation of causal effect. Journal of Politics, 79(3), 949-963.

Berg, F., Kölbel, J. F., Rigobon, R. (2022). Aggregate confusion: The divergence of ESG ratings. Review of Finance, 26(6), 1315-1344.

Besley, T., Persson, T. (2010). State capacity, conflict, and development. Econometrica, 78(1), 1-34.

Bolton, P., Kacperczyk, M. (2021). Do investors care about carbon risk? Journal of Financial Economics, 142(2), 517-549.

Busch, T., Johnson, M., Pioch, T. (2022). Corporate carbon performance data: Quo vadis? Journal of Industrial Ecology, 26(1), 350-363.

Cai, Y., Pan, C. H., Statman, M. (2016). Why do countries matter so much in corporate social performance? Journal of Corporate Finance, 41, 591-609.

Cameron, A. C., Gelbach, J. B., Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. Review of Economics and Statistics, 90(3), 414-427.

Chatterji, A. K., Toffel, M. W. (2010). How firms respond to being rated. Strategic Management Journal, 31(9), 917-945.

Christensen, D. M., Serafeim, G., Sikochi, A. (2022). Why is corporate virtue in the eye of the beholder? The case of ESG ratings. The Accounting Review, 97(1), 147-175.

Christensen, H. B., Hail, L., Leuz, C. (2021). Mandatory CSR and sustainability reporting: Economic analysis and literature review. Review of Accounting Studies, 26(3), 1176-1248.

Delmas, M. A., Burbano, V. C. (2011). The drivers of greenwashing. California Management Review, 54(1), 64-87.

DiMaggio, P. J., Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. American Sociological Review, 48(2), 147-160.

Dixit, A. K., Pindyck, R. S. (1994). Investment under Uncertainty. Princeton University Press.

Downar, B., Ernstberger, J., Reichelstein, S., Schwenen, S., Zaklan, A. (2021). The impact of carbon disclosure mandates on emissions and financial operating performance. Review of Accounting Studies, 26(3), 1137-1175.

Drempetic, S., Klein, C., Zwergel, B. (2020). The influence of firm size on the ESG score: Corporate sustainability ratings under review. Journal of Business Ethics, 167(2), 333-360.

Frank, K. A. (2000). Impact of a confounding variable on a regression coefficient. Sociological Methods and Research, 29(2), 147-194.

Frank, K. A., Maroulis, S. J., Duong, M. Q., Kelcey, B. M. (2013). What would it take to change an inference? Using Rubin's causal model to interpret the robustness of causal inferences. Educational Evaluation and Policy Analysis, 35(4), 437-460.

Fredriksson, P. G., Svensson, J. (2003). Political instability, corruption and policy formation: The case of environmental policy. Journal of Public Economics, 87(7-8), 1383-1405.

Gulen, H., Ion, M. (2016). Policy uncertainty and corporate investment. Review of Financial Studies, 29(3), 523-564.

Hainmueller, J. (2012). Entropy balancing for causal effects: A multivariate reweighting method to produce balanced samples in observational studies. Political Analysis, 20(1), 25-46.

Hong, H., Kubik, J. D., Scheinkman, J. A. (2012). Financial constraints on corporate goodness. NBER Working Paper 18476.

Ioannou, I., Serafeim, G. (2012). What drives corporate social performance? The role of nation-level institutions. Journal of International Business Studies, 43(9), 834-864.

Krueger, P., Sautner, Z., Tang, D. Y., Zhong, R. (2024). The effects of mandatory ESG disclosure around the world. Journal of Accounting Research, 62(5), 1795-1847.

Lakens, D. (2017). Equivalence tests: A practical primer for t tests, correlations, and meta-analyses. Social Psychological and Personality Science, 8(4), 355-362.

Lee, C.-C., Wang, C.-W., Hu, T.-Y., Lin, W., Le, A. N. N. (2026). Carbon emissions and financial flexibility: International evidence. Energy Economics, 161, 109501.

Lewbel, A. (2012). Using heteroscedasticity to identify and estimate mismeasured and endogenous regressor models. Journal of Business and Economic Statistics, 30(1), 67-80.

Liang, H., Renneboog, L. (2017). On the foundations of corporate social responsibility. Journal of Finance, 72(2), 853-910.

Lyon, T. P., Montgomery, A. W. (2015). The means and end of greenwash. Organization & Environment, 28(2), 223-249.

Machado, J. A. F., Santos Silva, J. M. C. (2019). Quantiles via moments. Journal of Econometrics, 213(1), 145-173.

Marquis, C., Toffel, M. W., Zhou, Y. (2016). Scrutiny, norms, and selective disclosure: A global study of greenwashing. Organization Science, 27(2), 483-504.

Matsumura, E. M., Prakash, R., Vera-Muñoz, S. C. (2014). Firm-value effects of carbon emissions and carbon disclosures. The Accounting Review, 89(2), 695-724.

Meyer, J. W., Rowan, B. (1977). Institutionalized organizations: Formal structure as myth and ceremony. American Journal of Sociology, 83(2), 340-363.

MSCI ESG Research LLC (2023). MSCI ESG Ratings methodology: Carbon emissions key issue (October 2023). MSCI Inc.

MSCI ESG Research LLC (n.d.). MSCI ESG Ratings [Database]. MSCI Inc.

Muttakin, M. B., Mihret, D. G., Rana, T. (2021). Electoral system, corporate political donation, and carbon emission intensity: Cross-country evidence. Business Strategy and the Environment, 30(4), 1767-1779.

Muttakin, M. B., Rana, T., Mihret, D. G. (2022). Democracy, national culture and greenhouse gas emissions: An international study. Business Strategy and the Environment, 31(7), 2978-2991.

Oster, E. (2019). Unobservable selection and coefficient stability: Theory and evidence. Journal of Business and Economic Statistics, 37(2), 187-204.

PRS Group (n.d.). International Country Risk Guide [Database]. East Syracuse, NY: The PRS Group.

Reid, E. M., Toffel, M. W. (2009). Responding to public and private politics: Corporate disclosure of climate change strategies. Strategic Management Journal, 30(11), 1157-1178.

Ren, X., Li, W., Cheng, X., Zheng, X. (2024). Economic freedom and corporate carbon emissions: International evidence. Business Strategy and the Environment, 33(8), 8388-8412.

S&P Global Market Intelligence (n.d.). Compustat Global [Database]. S&P Global.

Sautner, Z., van Lent, L., Vilkov, G., Zhang, R. (2023). Firm-level climate change exposure. Journal of Finance, 78(3), 1449-1498.

Suchman, M. C. (1995). Managing legitimacy: Strategic and institutional approaches. Academy of Management Review, 20(3), 571-610.

Tee, C.-M., Wong, W.-Y., Hooy, C.-W. (2023). Economic policy uncertainty and carbon footprint: International evidence. Journal of Multinational Financial Management, 67, 100785.

Vasi, I. B., King, B. G. (2012). Social movements, risk perceptions, and economic outcomes: The effect of primary and secondary stakeholder activism on firms' perceived environmental risk and financial performance. American Sociological Review, 77(4), 573-596.

Walker, K., Wan, F. (2012). The harm of symbolic actions and green-washing: Corporate actions and communications on environmental performance and their financial implications. Journal of Business Ethics, 109(2), 227-242.

World Bank (n.d.). World Development Indicators [Database]. Washington, DC: The World Bank. [https://databank.worldbank.org/source/world-development-indicators](https://databank.worldbank.org/source/world-development-indicators)

## Appendix

### Table A1. Variable definitions

| Variable | Definition | Source |

|---|---|---|

| ces | MSCI Carbon Emissions Score, 0 to 10, higher = better management of carbon risk | MSCI ESG Ratings |

| ces_m | Alternative version of the carbon score (definition unverified) | MSCI ESG Ratings |

| env | MSCI environmental pillar score (includes `ces`) | MSCI ESG Ratings |

| ghg | Total GHG emissions (source definition ambiguous; treated as a level) | MSCI ESG Ratings |

| ln_ghg | ln(1 + ghg) | Constructed |

| ln_ghg_int | ln(1 + ghg) minus ln(sales) | Constructed |

| icrg_govstab | Government stability, 0 to 12 (sum of government unity, legislative strength, popular support); higher = lower risk | PRS Group ICRG |

| icrg_govunity | Government unity, 0 to 4 | PRS Group ICRG |

| icrg_legis | Legislative strength, 0 to 4 | PRS Group ICRG |

| icrg_popsup | Popular support, 0 to 4, derived as govstab minus govunity minus legis | Constructed from ICRG |

| icrg_civdis | Civil disorder, 0 to 4 (subcomponent of internal conflict) | PRS Group ICRG |

| icrg_forpress | Foreign pressures, 0 to 4 (subcomponent of external conflict) | PRS Group ICRG |

| icrg_fx | Exchange rate stability, 0 to 10 | PRS Group ICRG |

| icrg_fdebt | Foreign debt, 0 to 10 | PRS Group ICRG |

| icrg_gdpg | Real GDP growth, 0 to 10 | PRS Group ICRG |

| size | ln(total assets) | Compustat Global |

| lev | Total liabilities over total assets | Compustat Global |

| roa | Return on assets | Compustat Global |

| cash | Cash holdings (scaled as in source file) | Compustat Global |

| capx | Capital expenditure over sales | Compustat Global |

| ocf | Operating cash flow (scaled as in source file) | Compustat Global |

| wdi_infl | Inflation | World Bank WDI |

| wdi_unemp | Unemployment | World Bank WDI |

| ln_intan | ln(1 + intangible assets) | Compustat Global |

| sgrowth | Change in ln(sales) | Constructed |

| Large firm (big) | `size` at or above the base-sample median | Constructed |

| Carbon-intensive (cint) | SIC 2-digit codes 10, 12, 13, 14, 26, 28, 29, 32, 33 | Constructed |

| EU | Headquartered in an EU or EEA country (list in the estimation code) | Constructed |

| Crisis | Fiscal years 2007 to 2012, 2020 and 2021 (2021 does not occur in the base sample) | Constructed |

| High intangibles (hintan) | `ln_intan` at or above the base-sample median | Constructed |

*Note: The scaling of* `cash` *and* `ocf` *follows the source file and was not verified here.*

### Table A2. Countries in the base sample (headquarters, number of firm-year observations)

| Country | N | Country | N | Country | N | Country | N |

|---|---|---|---|---|---|---|---|

| JPN | 4,203 | CHE | 558 | PHL | 112 | EGY | 18 |

| GBR | 1,932 | ZAF | 400 | IRL | 110 | ZMB | 17 |

| CHN | 1,483 | MYS | 309 | POL | 94 | PNG | 15 |

| AUS | 1,284 | ITA | 303 | NZL | 85 | QAT | 15 |

| FRA | 895 | FIN | 278 | PRT | 70 | KEN | 11 |

| DEU | 857 | BRA | 261 | SAU | 70 | LKA | 10 |

| IND | 725 | ESP | 259 | USA | 45 | ROU | 9 |

| SWE | 613 | NLD | 241 | PAK | 39 | KAZ | 8 |

| HKG | 591 | NOR | 209 | PER | 39 | SRB | 7 |

| THA | 185 | SGP | 183 | MAR | 38 | SVK | 7 |

| MEX | 169 | BEL | 158 | NGA | 38 | CZE | 6 |

| DNK | 146 | TUR | 132 | LUX | 37 | GAB | 6 |

| ISR | 116 | AUT | 115 | IDN | 34 | BGD | 5 |

| CHL | 31 | GRC | 29 | UKR | 5 | COL | 3 |

| EST | 3 | JOR | 3 | MLT | 3 | TUN | 3 |

| SVN | 2 | ZWE | 2 | KWT | 1 | MNG | 1 |

*Note: Counts are for the base sample of 17,636 observations in 64 countries.*

### Table A3. Government stability components

| | (1) icrg_govunity | (2) icrg_popsup |

|---|---|---|

| icrg_govunity | 0.1277** | |

| | (2.23) | |

| icrg_popsup | | 0.2413*** |

| | | (4.85) |

| Firm and country controls | Yes | Yes |

| Observations | 17,008 | 17,008 |

| Firm and year fixed effects | Yes | Yes |

| Within R-squared | 0.00446 | 0.00558 |

*Note: The dependent variable is* `ces`*. Robust t-statistics are in parentheses.*  **p&lt;0.01,**  p&lt;0.05,  *p&lt;0.1.*

---

# NOTES FOR THE AUTHOR (not part of the paper; delete before submission)

**Target journal:** Business Strategy and the Environment (adapt the paper to its template and word limit). Seven of the new references are from BSE or from journals that BSE readers follow, which is deliberate.

**Affiliation numbers:** the byline lists the three affiliations in the [CLAUDE.md](http://CLAUDE.md) order. Please assign numbers to each author.

**Replication note.** The estimation code needed one mechanical fix. In the robustness section, the lag operator failed because earlier steps had re-sorted the data, so the panel structure was declared again `xtset firm_id year`) before creating the lagged variables. No variable, sample, control set, fixed effect, standard error choice or quantile changed. The Lewbel routine failed for `icrg_legis` and `icrg_civdis` (return code 198) and was left unchanged. Both points are logged in output/[CHANGELOG.md](http://CHANGELOG.md) and output/run_[report.md](http://report.md). Include a replication note in the paper only if the journal asks for one.

## Revision log for this pass

No new estimation was run. Every coefficient, t-statistic and diagnostic in the paper is unchanged. The changes are: (i) 24 new references, integrated into the text; (ii) new analysis that uses only numbers already reported in the tables; (iii) a rewritten Section 6; (iv) updated abstract, introduction, conclusion and notes.

### (i) New references, and where they are used

| # | Reference | Used in | Purpose |
|---|---|---|---|
| 1 | Abadie, Athey, Imbens & Wooldridge (2023, QJE) | 4.1, 6.7 | clustered SEs can be inflated when clusters are a large share of the population |
| 2 | Amel-Zadeh & Serafeim (2018, FAJ) | 1, 6.6 | why investors use ESG information |
| 3 | Andreou, Anyfantaki, Cabolis & Dellis (2026, Research Policy) | 2.2, 6.3, 6.6, 7 | institutions as a boundary condition on abatement |
| 4 | Azar, Duro, Kadach & Ormazabal (2021, JFE) | 2.6, 6.5, 6.6 | engagement concentrates on large emitters and is followed by lower emissions |
| 5 | Bättig & Bernauer (2009, IO) | 2.1 | national institutions and climate policy commitment |
| 6 | Besley & Persson (2010, Econometrica) | 2.4, 6.4 | **resolves flag 1**: state capacity, internal conflict and the incentive to invest in enforcement |
| 7 | Busch, Johnson & Pioch (2022, JIE) | 6.6 | firm-level carbon data quality |
| 8 | Cameron, Gelbach & Miller (2008, REStat) | 4.1, 6.7 | wild cluster bootstrap for few clusters |
| 9 | Chatterji & Toffel (2010, SMJ) | 1, 2.5, 6.1 | ratings are reactive |
| 10 | Christensen, Serafeim & Sikochi (2022, TAR) | 1, 2.5, 6.1 | more disclosure raises rater disagreement |
| 11 | Christensen, Hail & Leuz (2021, RAS) | 2.5, 6.2, 6.6 | real effects of disclosure mandates need enforcement |
| 12 | Drempetic, Klein & Zwergel (2020, JBE) | 1, 2.6, 6.1, 6.5 | firm size drives ESG scores (rating-construction alternative) |
| 13 | Downar, Ernstberger, Reichelstein, Schwenen & Zaklan (2021, RAS) | 2.5, 6.2, 6.6 | a disclosure mandate with enforcement reduces emissions |
| 14 | Fredriksson & Svensson (2003, JPubE) | 2.4, 6.4 | **resolves flag 1**: political instability weakens environmental policy stringency |
| 15 | Krueger, Sautner, Tang & Zhong (2024, JAR) | 2.5, 6.2 | effects of mandatory ESG disclosure around the world |
| 16 | Lakens (2017, SPPS) | 5.2.2, 5.10, 7 | equivalence testing: a null is not an equivalence claim |
| 17 | Lyon & Montgomery (2015, O&E) | 2.5, 6.2 | greenwashing review |
| 18 | Muttakin, Mihret & Rana (2021, BSE) | 1, 2.1, 6.3, 6.7 | electoral system and carbon intensity, cross-country |
| 19 | Muttakin, Rana & Mihret (2022, BSE) | 1, 2.1, 6.3, 6.7 | democracy and corporate GHG intensity |
| 20 | Reid & Toffel (2009, SMJ) | 2.4, 6.4 | **resolves flag 2**: public and private politics drive climate disclosure |
| 21 | Ren, Li, Cheng & Zheng (2024, BSE) | 1, 2.1, 6.3 | economic freedom and corporate carbon emissions |
| 22 | Sautner, van Lent, Vilkov & Zhang (2023, JF) | 1, 6.6 | text-based firm-level climate exposure |
| 23 | Tee, Wong & Hooy (2023, JMFM) | 2.2, 6.3, 6.6 | policy uncertainty raises carbon footprint; institutions moderate it |
| 24 | Vasi & King (2012, ASR) | 2.4, 6.4 | **resolves flag 2**: activism raises perceived environmental risk |

All 24 were checked against publisher or repository pages in this pass. One correction to note: Azar et al. is 2021 (JFE 142(2), 674-696), not 2023; Sautner et al. is Journal of Finance 78(3), 1449-1498, not JFE.

### (ii) New analysis (no new estimation, derived from reported numbers)

| Item | Where | What it does | Verify before submission |
|---|---|---|---|
| Table 4b | 5.2.1 | Standardizes each coefficient by the SD of its own outcome, so the score and emission associations can be compared; also gives the change in outcome SD for a one within-firm SD change | SDs come from Table 1 (base sample), not from the Table 4 sample of 15,753. Recompute on the exact sample, ideally with within-firm SDs of the outcomes |
| Table 4c | 5.2.2 | Converts each emission coefficient and t-statistic into a 95% interval, in log points and percent, and states what the data exclude | Intervals are `b ± 1.96 × (b/t)`. Replace with intervals from the estimation output |
| Pillar weight calculation | 5.6 | Shows the `env` result is not simple dilution: the CI upper bound (0.0467) implies a carbon weight in the pillar of at most about 0.18 | Requires the actual MSCI key issue weights for the sample |
| Multiplicity check | 5.10 | Bonferroni and Benjamini-Hochberg across the 15 interaction tests in Table 13 | p-values computed from reported t-statistics with a normal approximation |
| MSCI formula and country input | 3.2, 6.1 | States `KI = 7 − (max(EXP,2) − MGT)`, the geographic exposure input based on national target ambition, and the peer-relative performance component | Confirm whether `ces` is the key issue score or the management score (existing open flag) |

Key numbers to check: score association 5 to 8 times the emission association in SD units where the latter is non-negligible (5.2.1); ±3.5 percent for total emissions and -0.6 percent for intensity (5.2.2); implied carbon weight at most 0.18 (5.6); seven tests pass Benjamini-Hochberg, five pass Bonferroni (5.10).

### (iii) Rewritten discussion (Section 6)

Six subsections: (6.1) the gap between scores and emissions, with three mechanisms and the rating-practice channel made concrete; (6.2) what the disclosure literature adds, and why a mandate with enforcement is not the same comparison as a slow-moving institutional rating; (6.3) which institutions matter and as what, using the emissions-outcome literature as a contrast; (6.4) civil disorder, with both theory channels and the honest width of the interval; (6.5) size, coverage and the rating-construction alternative; (6.6) implications for researchers, managers and investors, and for policy; (6.7) limitations, now including clustering, multiplicity, the bounded score and the composition explanation.

### (iv) Other text changes

- Abstract: adds the standardized comparison, the exclusion bound, and the point that part of the score's country variation may come from how the rating is built.
- Keywords: adds "ESG ratings" and "symbolic versus substantive responses".
- Section 1: a new paragraph on three features of rating data (reactivity, disclosure raising disagreement, size in scores); the literature paragraph now covers the emissions-outcome side as well; a new paragraph announcing the two pieces of added analysis; H5 in the contributions is now qualified by the multiplicity result.
- Section 2.2: adds the policy-uncertainty evidence and the boundary-condition evidence.
- Section 3.2: adds the three properties of the MSCI score.
- Section 4.1: adds the clustering discussion; Section 4.5: adds the caveats on the group indicators and on multiplicity.
- Section 5.6: adds the pillar weight calculation.
- Section 5.9: updated to reflect the new material.
- Section 7: adds the standardized comparison, the exclusion bound, the multiplicity qualification on H5, and three new limitations (rating construction, multiplicity, no formal equivalence test).

## Open reference flags

- **Resolved in this revision:** Section 2.4 flag 1 (low disorder risk and enforcement) now cites Fredriksson and Svensson (2003) and Besley and Persson (2010). Section 2.4 flag 2 (unrest raises attention) now cites Vasi and King (2012) and Reid and Toffel (2009), and the text states that the two arguments predict opposite signs.
- **Resolved earlier:** the MSCI exposure and management claim (Section 2.3) cites MSCI ESG Research LLC (2023); Dixit and Pindyck (1994) is cleared.
- Data sources (lines around the reference list): the entries use "n.d." because the retrieval years and database versions are not in the project files. Please add the access year and version for MSCI, Compustat Global, ICRG and WDI. The Compustat Global entry was not checked online; the ICRG, WDI and MSCI entries were checked against the publishers' public pages.
- The `ces` field may or may not equal MSCI's carbon emissions key issue score. This now matters more than before, because the key issue score and the management score have different interpretations: the key issue score is exposure-adjusted, and the geographic exposure input is country-specific. Please confirm from the data documentation.
- The MSCI (2023) methodology document is cited for the formula, the geographic exposure input and the peer-relative performance component. The current public URL should be re-checked before submission; the version used here is dated October 2023.

## Decisions that need the author (no new estimation was run)

1. `capx` channel: `capx` is already a control, so Table 6 columns (3) and (4) reproduce the baseline and are not a mediation test (stated in Sections 4.2 and 5.3 and in the Table 6 note). A real test needs the baseline without `capx` among the controls, which is a new run. Please approve or drop it.
2. Figure 1 axis label: the file says "Effect on carbon emissions score". Suggested label: "Coefficient on legislative strength x year, carbon score (ces)". This needs a rerun of the figure command only. The figure note in the paper already warns readers.
3. Sample period: the paper states fiscal years 2007 to 2020 (from the log). [CLAUDE.md](http://CLAUDE.md) says 2007 to 2024. Please confirm which variable (ICRG, WDI or Compustat) ends in 2020, so that Section 3.1 can name it. Base-sample counts by year `tab year if s_base`) would also be useful; the paper currently uses counts from the deduplicated file (586 in 2007, 3,121 in 2020).
4. The `crisis` dummy includes 2021, which does not occur in the base sample. Consider removing 2021 from the definition (a change to the do-file).
5. Referee-style questions that would need new estimation, in the order we would rank them: (a) wild-cluster bootstrap and leave-one-country-out for legislative strength, both cheap and both likely to be asked; (b) a formal equivalence test on the two emission coefficients with a pre-specified region, which is what the title claims; (c) a lagged-emissions specification, which tests the "abatement takes time" objection in Section 2.5; (d) a constant-coverage subsample, which tests the composition explanation for the event study pre-trends; (e) a fractional-response or censored specification for the bounded score; (f) a formal equality test of standardized score and emission coefficients.
6. The title keeps "Same Emissions"; the abstract and text define it as "no detectable association within these bounds".
7. Government unity is significant (0.1277), contrary to the outline's expectation; contribution 1 was rewritten accordingly.

## Table-number crosswalk (paper table to output file)

| Paper | Output file |

|---|---|

| Table 1 | Table1_descriptives |

| Table 2 | Table2_baseline |

| Table 3 | Table2b_magnitudes |

| Table 4 | Table3_score_vs_emissions |

| Table 4b | new, derived from Table 4 and Table 1 |

| Table 4c | new, derived from Table 4 |

| Table 5 | Table4_channel_intangibles |

| Table 6 | Table4b_channel_growth |

| Table 7 | analysis.log (ITCV, Oster) and Table5_entropy_balancing |

| Table 8 | Table6_iv and analysis.log (Anderson-Rubin, confidence intervals) |

| Table 9 | Table6b_did |

| Table 10 and Figure 1 | Table6c_event_study and Fig1_event_study_legis |

| Table 11 | Table7_robustness |

| Table 12 | Table7b_alt_outcomes |

| Table 13 | Table8_heterogeneity |

| Table 14 | Table9_mmqr |

| Table A1 | variable definitions (constructed from the do-file and [CLAUDE.md](http://CLAUDE.md)) |

| Table A2 | analysis.log `tab iso3 if s_base`) |

| Table A3 | TableA1_gov_components (called Table A1 in the outline) |
