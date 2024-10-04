#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v20
# autospec commit: f35655a
#
# Source0 file verified with key 0x6FFC33439B0D04DF (erik.winkels@open-xchange.com)
#
Name     : pdns
Version  : 4.9.2
Release  : 34
URL      : https://downloads.powerdns.com/releases/pdns-4.9.2.tar.bz2
Source0  : https://downloads.powerdns.com/releases/pdns-4.9.2.tar.bz2
Source1  : https://downloads.powerdns.com/releases/pdns-4.9.2.tar.bz2.asc
Source2  : 6FFC33439B0D04DF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause GPL-2.0 ISC MIT
Requires: pdns-bin = %{version}-%{release}
Requires: pdns-lib = %{version}-%{release}
Requires: pdns-license = %{version}-%{release}
Requires: pdns-man = %{version}-%{release}
Requires: pdns-services = %{version}-%{release}
Requires: pdns-doc
BuildRequires : LuaJIT-dev
BuildRequires : bison
BuildRequires : boost-dev
BuildRequires : buildreq-configure
BuildRequires : curl-dev
BuildRequires : file
BuildRequires : flex
BuildRequires : gnupg
BuildRequires : lua-dev
BuildRequires : mariadb-dev
BuildRequires : nghttp2-dev
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : postgresql-dev
BuildRequires : protobuf-dev
BuildRequires : pypi-virtualenv
BuildRequires : ragel
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Use-pdns-uid-gid-and-enable-syslogging.patch
Patch2: 0001-Disable-SHA384-test.patch

%description
PowerDNS is copyright © by PowerDNS.COM BV and lots of
contributors, using the GNU GPLv2 license (see NOTICE for the
exact license and exception used).

%package bin
Summary: bin components for the pdns package.
Group: Binaries
Requires: pdns-license = %{version}-%{release}
Requires: pdns-services = %{version}-%{release}

%description bin
bin components for the pdns package.


%package doc
Summary: doc components for the pdns package.
Group: Documentation
Requires: pdns-man = %{version}-%{release}

%description doc
doc components for the pdns package.


%package lib
Summary: lib components for the pdns package.
Group: Libraries
Requires: pdns-license = %{version}-%{release}

%description lib
lib components for the pdns package.


%package license
Summary: license components for the pdns package.
Group: Default

%description license
license components for the pdns package.


%package man
Summary: man components for the pdns package.
Group: Default

%description man
man components for the pdns package.


%package services
Summary: services components for the pdns package.
Group: Systemd services
Requires: systemd

%description services
services components for the pdns package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 6FFC33439B0D04DF' gpg.status
%setup -q -n pdns-4.9.2
cd %{_builddir}/pdns-4.9.2
%patch -P 1 -p1
%patch -P 2 -p1
pushd ..
cp -a pdns-4.9.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728000640
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_CXXFLAGS=$CLEAR_INTERMEDIATE_CFLAGS
CLEAR_INTERMEDIATE_FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_FCFLAGS=$CLEAR_INTERMEDIATE_FFLAGS
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --enable-unit-tests \
--enable-backend-unit-tests \
--enable-reproducible \
--enable-tools \
--enable-systemd \
--with-luajit \
--with-sqlite3 \
--with-dynmodules="bind gmysql gsqlite3 gpgsql pipe" \
--with-socketdir=/run
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --enable-unit-tests \
--enable-backend-unit-tests \
--enable-reproducible \
--enable-tools \
--enable-systemd \
--with-luajit \
--with-sqlite3 \
--with-dynmodules="bind gmysql gsqlite3 gpgsql pipe" \
--with-socketdir=/run
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_CXXFLAGS=$CLEAR_INTERMEDIATE_CFLAGS
CLEAR_INTERMEDIATE_FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_FCFLAGS=$CLEAR_INTERMEDIATE_FFLAGS
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1728000640
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pdns
cp %{_builddir}/pdns-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pdns/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8 || :
cp %{_builddir}/pdns-%{version}/NOTICE %{buildroot}/usr/share/package-licenses/pdns/b0546213f9970e01098f0ec919c828d83790eb9a || :
cp %{_builddir}/pdns-%{version}/ext/ipcrypt/LICENSE %{buildroot}/usr/share/package-licenses/pdns/8f5d9d5ea232b642dd53df820acf167e9086d119 || :
cp %{_builddir}/pdns-%{version}/ext/protozero/LICENSE.from_folly %{buildroot}/usr/share/package-licenses/pdns/598f87f072f66e2269dd6919292b2934dbb20492 || :
cp %{_builddir}/pdns-%{version}/ext/protozero/LICENSE.md %{buildroot}/usr/share/package-licenses/pdns/c90134f68ba9b55008f8dc3dd3100e2e632d55bf || :
cp %{_builddir}/pdns-%{version}/ext/yahttp/LICENSE %{buildroot}/usr/share/package-licenses/pdns/cd4a6679c43eb8c0331ebc91648b27b6fd747252 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/calidns
/V3/usr/bin/dnsbulktest
/V3/usr/bin/dnsgram
/V3/usr/bin/dnspcap2calidns
/V3/usr/bin/dnspcap2protobuf
/V3/usr/bin/dnsreplay
/V3/usr/bin/dnsscan
/V3/usr/bin/dnsscope
/V3/usr/bin/dnstcpbench
/V3/usr/bin/dnswasher
/V3/usr/bin/dumresp
/V3/usr/bin/ixplore
/V3/usr/bin/nproxy
/V3/usr/bin/nsec3dig
/V3/usr/bin/pdns_control
/V3/usr/bin/pdns_notify
/V3/usr/bin/pdns_server
/V3/usr/bin/pdnsutil
/V3/usr/bin/saxfr
/V3/usr/bin/sdig
/V3/usr/bin/stubquery
/V3/usr/bin/zone2json
/V3/usr/bin/zone2sql
/usr/bin/calidns
/usr/bin/dnsbulktest
/usr/bin/dnsgram
/usr/bin/dnspcap2calidns
/usr/bin/dnspcap2protobuf
/usr/bin/dnsreplay
/usr/bin/dnsscan
/usr/bin/dnsscope
/usr/bin/dnstcpbench
/usr/bin/dnswasher
/usr/bin/dumresp
/usr/bin/ixplore
/usr/bin/nproxy
/usr/bin/nsec3dig
/usr/bin/pdns_control
/usr/bin/pdns_notify
/usr/bin/pdns_server
/usr/bin/pdnsutil
/usr/bin/saxfr
/usr/bin/sdig
/usr/bin/stubquery
/usr/bin/zone2json
/usr/bin/zone2sql

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/pdns/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/pdns/libbindbackend.so
/V3/usr/lib64/pdns/libgmysqlbackend.so
/V3/usr/lib64/pdns/libgpgsqlbackend.so
/V3/usr/lib64/pdns/libgsqlite3backend.so
/V3/usr/lib64/pdns/libpipebackend.so
/usr/lib64/pdns/libbindbackend.so
/usr/lib64/pdns/libgmysqlbackend.so
/usr/lib64/pdns/libgpgsqlbackend.so
/usr/lib64/pdns/libgsqlite3backend.so
/usr/lib64/pdns/libpipebackend.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pdns/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
/usr/share/package-licenses/pdns/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/pdns/8f5d9d5ea232b642dd53df820acf167e9086d119
/usr/share/package-licenses/pdns/b0546213f9970e01098f0ec919c828d83790eb9a
/usr/share/package-licenses/pdns/c90134f68ba9b55008f8dc3dd3100e2e632d55bf
/usr/share/package-licenses/pdns/cd4a6679c43eb8c0331ebc91648b27b6fd747252

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/calidns.1
/usr/share/man/man1/dnsbulktest.1
/usr/share/man/man1/dnsgram.1
/usr/share/man/man1/dnspcap2calidns.1
/usr/share/man/man1/dnspcap2protobuf.1
/usr/share/man/man1/dnsreplay.1
/usr/share/man/man1/dnsscan.1
/usr/share/man/man1/dnsscope.1
/usr/share/man/man1/dnstcpbench.1
/usr/share/man/man1/dnswasher.1
/usr/share/man/man1/dumresp.1
/usr/share/man/man1/ixplore.1
/usr/share/man/man1/nproxy.1
/usr/share/man/man1/nsec3dig.1
/usr/share/man/man1/pdns_control.1
/usr/share/man/man1/pdns_notify.1
/usr/share/man/man1/pdns_server.1
/usr/share/man/man1/pdnsutil.1
/usr/share/man/man1/saxfr.1
/usr/share/man/man1/sdig.1
/usr/share/man/man1/zone2json.1
/usr/share/man/man1/zone2sql.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/pdns.service
/usr/lib/systemd/system/pdns@.service
