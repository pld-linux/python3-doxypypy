%define		module	doxypypy
Summary:	Doxygen filter for Python
Summary(pl.UTF-8):	Filtr Doxygena dla Pythona
# Name must match the python module/package name (as on pypi or in 'import' statement)
Name:		python3-%{module}
Version:	0.8.8.6
Release:	6
License:	GPL v2
Group:		Libraries/Python
# git version from 2021-08-02
Source0:	doxypypy.tar.xz
# Source0-md5:	d411db113b779e34b26bc5178819ed16
Source1:	py_filter
URL:		https://github.com/Feneric/doxypypy
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A more Pythonic version of doxypy, a Doxygen filter for Python.

%description -l pl.UTF-8
Bardziej Pythonowa wersja doxypy, filtra Doxygena dla Pythona.

%package apidocs
Summary:	API documentation for Python %{module} module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona %{module}
Group:		Documentation

%description apidocs
API documentation for Python %{module} module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona %{module}.

%prep
%setup -q -n %{module}

%build
%py3_build

%if %{with tests}
%{__python3} setup.py test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

install %SOURCE1 $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{_bindir}/doxypypy
%{_bindir}/py_filter
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
