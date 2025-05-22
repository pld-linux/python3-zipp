#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	pathlib-compatible Zipfile object wrapper
Summary(pl.UTF-8):	Obiektowe obudowanie Zipfile zgodne z pathlib
Name:		python3-zipp
Version:	3.21.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zipp/
Source0:	https://files.pythonhosted.org/packages/source/z/zipp/zipp-%{version}.tar.gz
# Source0-md5:	a758089a5cbb8fab61d73c8ff345eee2
URL:		https://pypi.org/project/zipp/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools >= 1:61.2
BuildRequires:	python3-setuptools_scm >= 3.4.1
BuildRequires:	python3-toml
%if %{with tests}
# optional
#BuildRequires:	python3-big_o
#BuildRequires:	python3-cov
BuildRequires:	python3-func_timeout
BuildRequires:	python3-jaraco.functools
BuildRequires:	python3-jaraco.itertools
BuildRequires:	python3-more_itertools
BuildRequires:	python3-pytest >= 6
#BuildRequires:	python3-pytest-black >= 0.3.7
#BuildRequires:	python3-pytest-checkdocs >= 2.4
#BuildRequires:	python3-pytest-enabler >= 2.2
#BuildRequires:	python3-pytest-flake8
#BuildRequires:	python3-pytest-ignore-flaky
#BuildRequires:	python3-pytest-mypy >= 0.9.1
#BuildRequires:	python3-pytest-ruff
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
BuildRequires:	python3-furo
BuildRequires:	python3-jaraco.packaging >= 9.3
BuildRequires:	python3-jaraco.tidelift >= 1.4
BuildRequires:	python3-rst.linker >= 1.9
#BuildRequires:	python3-sphinx-lint
BuildRequires:	sphinx-pdg-3 >= 3.5
%endif
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pathlib-compatible Zipfile object wrapper - backport from Python 3.12
zipfile module.

%description -l pl.UTF-8
Obiektowe obudowanie Zipfile zgodne z pathlib - backport z modułu
zipfile Pythona 3.12.

%package apidocs
Summary:	API documentation for Python zipp module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona zipp
Group:		Documentation

%description apidocs
API documentation for Python zipp module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona zipp.

%prep
%setup -q -n zipp-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%if %{with doc}
sphinx-build-3 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS.rst README.rst SECURITY.md
%{py3_sitescriptdir}/zipp
%{py3_sitescriptdir}/zipp-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
