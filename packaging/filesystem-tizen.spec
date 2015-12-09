%define disable_docs_package 1
Summary: The basic directory layout for Tizen system
Name: filesystem-tizen
Version: 0.0.1
Release: 1
License: Apache-2.0
Group: System/Base
BuildArch: noarch
Source0: %{name}-%{version}.tar.gz
Source1: issue
Source2: issue.net
Source1001: filesystem-tizen.manifest
Source1002: LICENSE.Apache-2.0

%define debug_package %{nil}

%description
The filesystem-tizen package is one of the basic packages. That is
installed on Tizen system. It is very similar with origin filesystem
package. filesystem-tizen contains basic directory layout for Tizen
system. Basically, filesystem-tizen only contains directories what is
not installed by origin filesystem.

%prep
%setup -q
cp %{SOURCE1001} .

%build

%install
rm -rf %{buildroot}
mkdir %{buildroot}
cd %{buildroot}
mkdir -p csa etc
mkdir -p %{buildroot}/usr/share/license
install -m 0644 %SOURCE1002 %{buildroot}/usr/share/license/%{name}

install -m644 %SOURCE1 %SOURCE2 etc

%post

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
%manifest filesystem-tizen.manifest
/csa
/etc/issue.net
/etc/issue
