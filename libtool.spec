Summary:	GNU libtool, a shared library generation tool.
Summary(pl):	GNU libtool - narzêdzie do generowania bibliotek wspó³dzielonych
Name:		libtool
Version:	1.3.3
Release:	2
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Source:		ftp://ftp.gnu.org/gnu/libtool/%{name}-%{version}.tar.gz
Patch0:		libtool-info.patch
Patch1:		libtool-cache.patch
Patch2:		libtool-arm.patch
URL:		http://www.gnu.org/software/libtool/
PreReq:		/usr/sbin/fix-info-dir
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GNU libtool is a set of shell scripts to automatically configure
UNIX architectures to build shared libraries in generic fashion.

%description -l pl
GNU libtool jest zbiorem skryptów shellowych do automatycznego generowania
bibliotek wspó³dzielonych niezale¿nie od typu platformy systemowej.

%package -n libltdl
Summary:	System independent dlopen wrapper for GNU libtool
Summary(pl):	Biblioteka ogólnych wywo³añ dlopen
Group:		Libraries
Group(pl):	Biblioteki

%description -n libltdl
System independent dlopen wrapper for GNU libtool

%description -n libltdl -l pl
Biblioteka ogólnych wywo³añ dlopen

%package -n libltdl-devel
Summary:	System independent dlopen wrapper for GNU libtool
Summary(pl):	Biblioteka ogólnych wywo³añ dlopen
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	libltdl = %{version}

%description -n libltdl-devel
System independent dlopen wrapper for GNU libtool

%description -n libltdl-devel -l pl
Biblioteka ogólnych wywo³añ dlopen

%package -n libltdl-static
Summary:	Static system independent dlopen wrapper for GNU libtool
Summary(pl):	Statyczna biblioteka ogólnych wywo³añ dlopen
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	libltdl-devel = %{version}

%description -n libltdl-static
Static system independent dlopen wrapper for GNU libtool

%description -n libltdl-static -l pl
Statyczna biblioteka ogólnych wywo³añ dlopen

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch1 -p1

%build
%configure 

make -C doc -k
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info* \
	AUTHORS NEWS README THANKS TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post   -n libltdl -p /sbin/ldconfig
%postun -n libltdl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {AUTHORS,NEWS,README,THANKS,TODO,ChangeLog}.gz demo
%attr(755,root,root) %{_bindir}/*

%dir %{_datadir}/libtool
%attr(755,root,root) %{_datadir}/libtool/config.guess
%attr(755,root,root) %{_datadir}/libtool/config.sub
%attr(755,root,root) %{_datadir}/libtool/ltconfig
%{_datadir}/libtool/ltmain.sh

%{_infodir}/libtool.info*
%{_datadir}/aclocal/libtool.m4

%files -n libltdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files -n libltdl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%dir %{_datadir}/libtool/libltdl
%{_datadir}/libtool/libltdl/Makefile.am
%{_datadir}/libtool/libltdl/Makefile.in
%{_datadir}/libtool/libltdl/README
%{_datadir}/libtool/libltdl/COPYING.LIB
%{_datadir}/libtool/libltdl/acconfig.h
%{_datadir}/libtool/libltdl/acinclude.m4
%{_datadir}/libtool/libltdl/aclocal.m4
%{_datadir}/libtool/libltdl/config.h.in
%{_datadir}/libtool/libltdl/configure.in
%{_datadir}/libtool/libltdl/ltdl.c
%{_datadir}/libtool/libltdl/ltdl.h
%{_datadir}/libtool/libltdl/stamp-h.in
%attr(755,root,root) %{_datadir}/libtool/libltdl/configure

%files -n libltdl-static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
