#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	pathlib-compatible Zipfile object wrapper
Summary(pl.UTF-8):	Obiektowe obudowanie Zipfile zgodne z pathlib
Name:		python-zipp
Version:	0.6.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zipp/
Source0:	https://files.pythonhosted.org/packages/source/z/zipp/zipp-%{version}.tar.gz
# Source0-md5:	d4451a749d8a7c3c392a9edd1864a937
URL:		https://pypi.org/project/zipp/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 31.0.1
BuildRequires:	python-setuptools_scm >= 1.15.0
%if %{with tests}
BuildRequires:	python-contextlib2
BuildRequires:	python-linecache2
BuildRequires:	python-more_itertools
BuildRequires:	python-pathlib2
BuildRequires:	python-traceback2
BuildRequires:	python-unittest2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools >= 31.0.1
BuildRequires:	python3-setuptools_scm >= 1.15.0
%if %{with tests}
BuildRequires:	python3-more_itertools
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-jaraco.packaging >= 3.2
BuildRequires:	python-rst.linker >= 1.9
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pathlib-compatible Zipfile object wrapper - backport from Python 3.8
zipfile module.

%description -l pl.UTF-8
Obiektowe obudowanie Zipfile zgodne z pathlib - backport z modułu
zipfile Pythona 3.8.

%package -n python3-zipp
Summary:	pathlib-compatible Zipfile object wrapper
Summary(pl.UTF-8):	Obiektowe obudowanie Zipfile zgodne z pathlib
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-zipp
pathlib-compatible Zipfile object wrapper - backport from Python 3.8
zipfile module.

%description -n python3-zipp -l pl.UTF-8
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
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
sphinx-build-3 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/zipp.py[co]
%{py_sitescriptdir}/zipp-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-zipp
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/zipp.py
%{py3_sitescriptdir}/__pycache__/zipp.cpython-*.py[co]
%{py3_sitescriptdir}/zipp-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
