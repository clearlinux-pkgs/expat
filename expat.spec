#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : expat
Version  : 2.2.0
Release  : 24
URL      : http://downloads.sourceforge.net/expat/expat-2.2.0.tar.bz2
Source0  : http://downloads.sourceforge.net/expat/expat-2.2.0.tar.bz2
Summary  : expat XML parser
Group    : Development/Tools
License  : MIT
Requires: expat-bin
Requires: expat-lib
Requires: expat-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
Patch1: cve-2016-4472.nopatch

%description
Expat, Release 2.2.0
This is Expat, a C library for parsing XML, written by James Clark.
Expat is a stream-oriented XML parser.  This means that you register
handlers with the parser before starting the parse.  These handlers
are called when the parser discovers the associated structures in the
document being parsed.  A start tag is an example of the kind of
structures for which you may register handlers.

%package bin
Summary: bin components for the expat package.
Group: Binaries

%description bin
bin components for the expat package.


%package dev
Summary: dev components for the expat package.
Group: Development
Requires: expat-lib
Requires: expat-bin
Provides: expat-devel

%description dev
dev components for the expat package.


%package dev32
Summary: dev32 components for the expat package.
Group: Default
Requires: expat-lib32
Requires: expat-bin

%description dev32
dev32 components for the expat package.


%package doc
Summary: doc components for the expat package.
Group: Documentation

%description doc
doc components for the expat package.


%package lib
Summary: lib components for the expat package.
Group: Libraries

%description lib
lib components for the expat package.


%package lib32
Summary: lib32 components for the expat package.
Group: Default

%description lib32
lib32 components for the expat package.


%prep
%setup -q -n expat-2.2.0
pushd ..
cp -a expat-2.2.0 build32
popd

%build
export LANG=C
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xmlwf

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libexpat.so
/usr/lib64/pkgconfig/expat.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libexpat.so
/usr/lib32/pkgconfig/32expat.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libexpat.so.1
/usr/lib64/libexpat.so.1.6.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libexpat.so.1
/usr/lib32/libexpat.so.1.6.2
