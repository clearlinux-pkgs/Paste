#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Paste
Version  : 2.0.3
Release  : 27
URL      : http://pypi.debian.net/Paste/Paste-2.0.3.tar.gz
Source0  : http://pypi.debian.net/Paste/Paste-2.0.3.tar.gz
Summary  : Tools for using a Web Server Gateway Interface stack
Group    : Development/Tools
License  : MIT
Requires: Paste-python
Requires: six
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
to build web applications.  Each piece of middleware uses the WSGI (`PEP 333`_)
        interface, and should be compatible with other middleware based on those
        interfaces.

%package python
Summary: python components for the Paste package.
Group: Default
Provides: paste-python

%description python
python components for the Paste package.


%prep
%setup -q -n Paste-2.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503125716
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1503125716
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
