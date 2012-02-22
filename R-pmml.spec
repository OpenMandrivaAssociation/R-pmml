%global packname  pmml
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.2.29
Release:          1
Summary:          Generate PMML for various models
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-XML R-arules R-nnet R-rpart R-randomSurvivalForest
Requires:         R-randomForest R-kernlab
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-XML R-arules R-nnet R-rpart R-randomSurvivalForest
BuildRequires:    R-randomForest R-kernlab

%description
The Predictive Modelling Markup Language (PMML) is a language for
representing models using XML in an application independent way. Such
models can then be shared with other applications that support PMML (see
http://www.dmg.org/products.html). The generic pmml() function takes an R
model as its argument and returns the corresponding PMML.  Currently
supported models for export include linear regression (lm and glm),
support vector machines (ksvm), decision trees (rpart), neural networks
(nnet, multinom), association rules (arules), survival models (coxph,
survreg), random survival forests (randomSurvivalForest), and clusters
(kmeans, hclust).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
