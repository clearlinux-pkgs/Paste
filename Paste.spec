#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Paste
Version  : 3.4.5
Release  : 75
URL      : https://files.pythonhosted.org/packages/49/5c/5dc9f1a1ae5c0fb966530c2ea663594339cbb0586b95b5d174389bb6d548/Paste-3.4.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/49/5c/5dc9f1a1ae5c0fb966530c2ea663594339cbb0586b95b5d174389bb6d548/Paste-3.4.5.tar.gz
Summary  : Tools for using a Web Server Gateway Interface stack
Group    : Development/Tools
License  : MIT
Requires: Paste-license = %{version}-%{release}
Requires: Paste-python = %{version}-%{release}
Requires: Paste-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
Paste provides several pieces of "middleware" (or filters) that can be nested
to build web applications. Each piece of middleware uses the WSGI (PEP 333)
interface, and should be compatible with other middleware based on those
interfaces.

%package license
Summary: license components for the Paste package.
Group: Default

%description license
license components for the Paste package.


%package python
Summary: python components for the Paste package.
Group: Default
Requires: Paste-python3 = %{version}-%{release}
Provides: paste-python

%description python
python components for the Paste package.


%package python3
Summary: python3 components for the Paste package.
Group: Default
Requires: python3-core
Provides: pypi(paste)
Requires: pypi(setuptools)
Requires: pypi(six)

%description python3
python3 components for the Paste package.


%prep
%setup -q -n Paste-3.4.5
cd %{_builddir}/Paste-3.4.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1601051505
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Paste
cp %{_builddir}/Paste-3.4.5/docs/license.txt %{buildroot}/usr/share/package-licenses/Paste/391729571488896efa70494919f96aab67116ad1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Paste/391729571488896efa70494919f96aab67116ad1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
