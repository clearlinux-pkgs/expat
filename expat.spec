#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v4
# autospec commit: 213bb01
#
# Source0 file verified with key 0x96262ACFFBD3AEC6 (sping@gentoo.org)
#
Name     : expat
Version  : 2.6.0
Release  : 74
URL      : https://sourceforge.net/projects/expat/files/expat/2.6.0/expat-2.6.0.tar.xz
Source0  : https://sourceforge.net/projects/expat/files/expat/2.6.0/expat-2.6.0.tar.xz
Source1  : https://sourceforge.net/projects/expat/files/expat/2.6.0/expat-2.6.0.tar.xz.asc
Summary  : expat XML parser
Group    : Development/Tools
License  : MIT
Requires: expat-bin = %{version}-%{release}
Requires: expat-lib = %{version}-%{release}
Requires: expat-license = %{version}-%{release}
Requires: expat-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : xmlto
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: cve-2016-4472.nopatch

%description
[![Run Linux CI tasks](https://github.com/libexpat/libexpat/actions/workflows/linux.yml/badge.svg)](https://github.com/libexpat/libexpat/actions/workflows/linux.yml)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/libexpat/libexpat?svg=true)](https://ci.appveyor.com/project/libexpat/libexpat)
[![Packaging status](https://repology.org/badge/tiny-repos/expat.svg)](https://repology.org/metapackage/expat/versions)
[![Downloads SourceForge](https://img.shields.io/sourceforge/dt/expat?label=Downloads%20SourceForge)](https://sourceforge.net/projects/expat/files/)
[![Downloads GitHub](https://img.shields.io/github/downloads/libexpat/libexpat/total?label=Downloads%20GitHub)](https://github.com/libexpat/libexpat/releases)

%package bin
Summary: bin components for the expat package.
Group: Binaries
Requires: expat-license = %{version}-%{release}

%description bin
bin components for the expat package.


%package dev
Summary: dev components for the expat package.
Group: Development
Requires: expat-lib = %{version}-%{release}
Requires: expat-bin = %{version}-%{release}
Provides: expat-devel = %{version}-%{release}
Requires: expat = %{version}-%{release}

%description dev
dev components for the expat package.


%package dev32
Summary: dev32 components for the expat package.
Group: Default
Requires: expat-lib32 = %{version}-%{release}
Requires: expat-bin = %{version}-%{release}
Requires: expat-dev = %{version}-%{release}

%description dev32
dev32 components for the expat package.


%package doc
Summary: doc components for the expat package.
Group: Documentation
Requires: expat-man = %{version}-%{release}

%description doc
doc components for the expat package.


%package lib
Summary: lib components for the expat package.
Group: Libraries
Requires: expat-license = %{version}-%{release}

%description lib
lib components for the expat package.


%package lib32
Summary: lib32 components for the expat package.
Group: Default
Requires: expat-license = %{version}-%{release}

%description lib32
lib32 components for the expat package.


%package license
Summary: license components for the expat package.
Group: Default

%description license
license components for the expat package.


%package man
Summary: man components for the expat package.
Group: Default

%description man
man components for the expat package.


%prep
%setup -q -n expat-2.6.0
cd %{_builddir}/expat-2.6.0
pushd ..
cp -a expat-2.6.0 build32
popd
pushd ..
cp -a expat-2.6.0 buildavx2
popd
pushd ..
cp -a expat-2.6.0 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707252432
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static DOCBOOK_TO_MAN="xmlto man --skip-validation"
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static DOCBOOK_TO_MAN="xmlto man --skip-validation"   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static DOCBOOK_TO_MAN="xmlto man --skip-validation"
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
GOAMD64=v4
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v4 -mprefer-vector-width=256 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v4 "
%configure --disable-static DOCBOOK_TO_MAN="xmlto man --skip-validation"
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :
cd ../buildavx512;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707252432
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/expat
cp %{_builddir}/expat-%{version}/COPYING %{buildroot}/usr/share/package-licenses/expat/39e6f567a10e36b2e77727e98e60bbcb3eb3af0b || :
export GOAMD64=v2
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v4
pushd ../buildavx512/
%make_install_v4
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/xmlwf
/V4/usr/bin/xmlwf
/usr/bin/xmlwf

%files dev
%defattr(-,root,root,-)
/usr/include/expat.h
/usr/include/expat_config.h
/usr/include/expat_external.h
/usr/lib64/cmake/expat-2.6.0/expat-config-version.cmake
/usr/lib64/cmake/expat-2.6.0/expat-config.cmake
/usr/lib64/cmake/expat-2.6.0/expat-noconfig.cmake
/usr/lib64/cmake/expat-2.6.0/expat.cmake
/usr/lib64/libexpat.so
/usr/lib64/pkgconfig/expat.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/cmake/expat-2.6.0/expat-config-version.cmake
/usr/lib32/cmake/expat-2.6.0/expat-config.cmake
/usr/lib32/cmake/expat-2.6.0/expat-noconfig.cmake
/usr/lib32/cmake/expat-2.6.0/expat.cmake
/usr/lib32/libexpat.so
/usr/lib32/pkgconfig/32expat.pc
/usr/lib32/pkgconfig/expat.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/expat/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libexpat.so.1.9.0
/V4/usr/lib64/libexpat.so.1.9.0
/usr/lib64/libexpat.so.1
/usr/lib64/libexpat.so.1.9.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libexpat.so.1
/usr/lib32/libexpat.so.1.9.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/expat/39e6f567a10e36b2e77727e98e60bbcb3eb3af0b

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xmlwf.1
