#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : TLP
Version  : 1.2.2
Release  : 1
URL      : https://github.com/linrunner/TLP/archive/1.2.2.tar.gz
Source0  : https://github.com/linrunner/TLP/archive/1.2.2.tar.gz
Summary  : Advanced Power Management for Linux
Group    : Development/Tools
License  : GPL-2.0
Requires: TLP-autostart = %{version}-%{release}
Requires: TLP-bin = %{version}-%{release}
Requires: TLP-data = %{version}-%{release}
Requires: TLP-license = %{version}-%{release}
Requires: TLP-services = %{version}-%{release}

%description
# TLP - Linux Advanced Power Management
TLP saves laptop battery power on Linux without the need to understand every
technical detail.

%package autostart
Summary: autostart components for the TLP package.
Group: Default

%description autostart
autostart components for the TLP package.


%package bin
Summary: bin components for the TLP package.
Group: Binaries
Requires: TLP-data = %{version}-%{release}
Requires: TLP-license = %{version}-%{release}
Requires: TLP-services = %{version}-%{release}

%description bin
bin components for the TLP package.


%package data
Summary: data components for the TLP package.
Group: Data

%description data
data components for the TLP package.


%package license
Summary: license components for the TLP package.
Group: Default

%description license
license components for the TLP package.


%package services
Summary: services components for the TLP package.
Group: Systemd services

%description services
services components for the TLP package.


%prep
%setup -q -n TLP-1.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565201097
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags} TLP_ULIB=/usr/lib/udev \
TLP_CONF=/usr/share/defaults/tlp \
TLP_SYSD=/usr/lib/systemd/system \
TLP_WITH_ELOGIND=0


%install
export SOURCE_DATE_EPOCH=1565201097
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/TLP
cp COPYING %{buildroot}/usr/share/package-licenses/TLP/COPYING
cp LICENSE %{buildroot}/usr/share/package-licenses/TLP/LICENSE
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -sf ../tlp.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
## install_append end

%files
%defattr(-,root,root,-)
/lib/elogind/system-sleep/49-tlp-sleep
/lib/udev/rules.d/85-tlp-rdw.rules
/lib/udev/rules.d/85-tlp.rules
/lib/udev/tlp-rdw-udev
/lib/udev/tlp-usb-udev

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/tlp.service

%files bin
%defattr(-,root,root,-)
/usr/bin/bluetooth
/usr/bin/run-on-ac
/usr/bin/run-on-bat
/usr/bin/tlp
/usr/bin/tlp-pcilist
/usr/bin/tlp-rdw
/usr/bin/tlp-stat
/usr/bin/tlp-usblist
/usr/bin/wifi
/usr/bin/wwan

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/bluetooth
/usr/share/bash-completion/completions/tlp
/usr/share/bash-completion/completions/tlp-rdw
/usr/share/bash-completion/completions/tlp-stat
/usr/share/bash-completion/completions/wifi
/usr/share/bash-completion/completions/wwan
/usr/share/metainfo/de.linrunner.tlp.metainfo.xml
/usr/share/tlp/func.d/05-tlp-func-pm
/usr/share/tlp/func.d/10-tlp-func-cpu
/usr/share/tlp/func.d/15-tlp-func-disk
/usr/share/tlp/func.d/20-tlp-func-usb
/usr/share/tlp/func.d/25-tlp-func-rf
/usr/share/tlp/func.d/30-tlp-func-rf-sw
/usr/share/tlp/func.d/35-tlp-func-batt
/usr/share/tlp/func.d/40-tlp-func-bay
/usr/share/tlp/func.d/45-tlp-func-gpu
/usr/share/tlp/func.d/tlp-func-stat
/usr/share/tlp/tlp-func-base
/usr/share/tlp/tpacpi-bat

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/TLP/COPYING
/usr/share/package-licenses/TLP/LICENSE

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/tlp.service
/lib/systemd/system/tlp-sleep.service
/lib/systemd/system/tlp.service
