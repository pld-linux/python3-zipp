#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	pathlib-compatible Zipfile object wrapper
Summary(pl.UTF-8):	Obiektowe obudowanie Zipfile zgodne z pathlib
Name:		python3-zipp
Version:	3.7.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zipp/
Source0:	https://files.pythonhosted.org/packages/source/z/zipp/zipp-%{version}.tar.gz
# Source0-md5:	5a1fc692b57b348d1e259484b405ddf6
URL:		https://pypi.org/project/zipp/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:31.0.1
BuildRequires:	python3-setuptools_scm >= 3.4.1
BuildRequires:	python3-toml
%if %{with tests}
BuildRequires:	python3-func_timeout
BuildRequires:	python3-jaraco.itertools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-jaraco.packaging >= 8.2
BuildRequires:	python3-rst.linker >= 1.9
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pathlib-compatible Zipfile object wrapper - backport from Python 3.8
zipfile module.

%description -l pl.UTF-8
Obiektowe obudowanie Zipfile zgodne z pathlib - backport z modułu
zipfile Pythona 3.8.

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
%py3_build

%if %{with tests}
%{__python3} -m unittest test_zipp
%endif

%if %{with doc}
sphinx-build-3 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/zipp.py
%{py3_sitescriptdir}/__pycache__/zipp.cpython-*.py[co]
%{py3_sitescriptdir}/zipp-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
