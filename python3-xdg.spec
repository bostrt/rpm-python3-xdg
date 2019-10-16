%global debug_package %{nil}

Name:		python3-xdg
Version:	4.0.1
Release:	0
Summary:	XDG Base Directory Specification for Python


License:	GPLv3
URL:		https://github.com/srstevenson/xdg
Source0:	https://github.com/srstevenson/xdg/archive/%{version}.tar.gz

BuildRequires:	python3-devel

%description
xdg is a tiny Python module which provides the variables defined by the XDG Base Directory Specification, to save you from duplicating the same snippet of logic in every Python utility you write that deals with user cache, configuration, or data files. It has no external dependencies.
%prep
%setup -q -n xdg-%{version}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{python3_sitelib}/xdg/
cp src/xdg/__init__.py $RPM_BUILD_ROOT%{python3_sitelib}/xdg/__init__.py

%files
%doc README.md
%license LICENCE
%{python3_sitelib}/xdg

%changelog


