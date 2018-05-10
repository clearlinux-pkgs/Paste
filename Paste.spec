#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Paste
Version  : 2.0.3
Release  : 34
URL      : http://pypi.debian.net/Paste/Paste-2.0.3.tar.gz
Source0  : http://pypi.debian.net/Paste/Paste-2.0.3.tar.gz
Summary  : Tools for using a Web Server Gateway Interface stack
Group    : Development/Tools
License  : MIT
Requires: Paste-python3
Requires: Paste-python
Requires: six
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
Requires: Paste-python3
Provides: paste-python

%description python
python components for the Paste package.


%package python3
Summary: python3 components for the Paste package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Paste package.


%prep
%setup -q -n Paste-2.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523296736
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
