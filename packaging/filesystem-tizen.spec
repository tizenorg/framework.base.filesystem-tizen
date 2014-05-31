%define disable_docs_package 1
Summary: The basic directory layout for Tizen system
Name: filesystem-tizen
Version: 0.0.1
Release: 1
License: Apache License v2
Group: System/Base
BuildArch: noarch
Source0: %{name}-%{version}.tar.gz
Source1: issue
Source2: issue.net
Source1001: filesystem-tizen.manifest
Requires(post): coreutils
Requires(post): filesystem

Provides: default-files
Provides: default-files-tizen

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
mkdir -p csa mnt \
    etc/{rc.d/init.d,ssl} \
    lib/modules \
    opt/{data,driver,home/{app,developer},share/icons/default/small,storage/{sdcard,PersonalStorage},usr/{apps,data,dbspace,devel/{bin,sbin,usr/{bin,sbin}},live,media,share,ug,.personalpage},var/{cache,lib,log/apt}} \
    usr/{apps,lib/{debug,locale},share/icons/default/small,ug}

ln -sf /opt/home home
ln -sf /mnt/mmc sdcard
ln -sf /opt/storage/sdcard mnt/mmc
ln -sf /opt/media mnt/ums
ln -sf /opt/etc/ssl/certs/ etc/ssl/certs

# legacy sysvinit rc script directory
ln -snf rc.d/init.d etc/init.d

ln -sf usr/ug opt/ug

install -m644 %SOURCE1 %SOURCE2 etc

%post
[ -d /opt/home ] || mkdir -p /opt/home
if [ -d /root ]; then
# mv can't work because when creating image, / and /opt are different device
        cp -a /root /opt/home
        rm -rf /root
else
        [ -d /opt/home/root ] || mkdir -p /opt/home/root
fi
ln -sf /opt/home/root /root

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%manifest filesystem-tizen.manifest
/csa
%dir /lib/modules
%dir /mnt
/mnt/mmc
/mnt/ums
/sdcard
%dir /usr
/usr/apps
%dir /usr/lib
/usr/lib/debug
/usr/lib/locale/
%dir /usr/share/icons/default
/usr/share/icons/default/small
/usr/ug
/home
%dir /etc
/etc/init.d
/etc/rc.d/init.d/
%dir /etc/ssl
/etc/ssl/certs
/etc/issue.net
/etc/issue
%dir /opt
/opt/data
/opt/driver
%dir /opt/usr
/opt/usr/.personalpage
/opt/usr/apps
/opt/usr/data
/opt/usr/dbspace
/opt/usr/live
/opt/usr/share
%dir /opt/usr/devel
/opt/usr/devel/bin
/opt/usr/devel/sbin
/opt/usr/devel/usr
/opt/usr/devel/usr/bin
/opt/usr/devel/usr/sbin
%attr(777,app,app) /opt/usr/media
/opt/usr/ug
%dir /opt/home
/opt/home/app
/opt/home/developer
%dir /opt/share/icons/default
/opt/share/icons/default/small
%dir /opt/storage
/opt/storage/PersonalStorage
/opt/storage/sdcard
/opt/ug
/opt/var/cache
/opt/var/lib
/opt/var/log/apt
