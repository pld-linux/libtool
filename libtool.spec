Summary:	GNU libtool, a shared library generation tool.
Summary(pl):	GNU libtool - narzêdzie do generowania bibliotek wspó³dzielonych
Name:		libtool
Version:	1.3
Release:	3
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Source:		ftp://ftp.gnu.org/gnu/libtool/%{name}-%{version}.tar.gz
Patch0:		libtool-info.patch
Patch1:		libtool-cache.patch
URL:		http://www.gnu.org/software/libtool/
PreReq:		/sbin/install-info
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GNU libtool is a set of shell scripts to automatically configure
UNIX architectures to build shared libraries in generic fashion.

%description -l pl
GNU libtool jest zbiorem skryptów shellowych do automatycznego gemnerowania
bibliotek wspó³dzielonych niezale¿nie od typu platformy systemowej.

%package -n	libltdl
Summary:	System independent dlopen wrapper for GNU libtool
Summary(pl):	Biblioteka ogólnych wywo³añ dlopen
Group:		Libraries
Group(pl):	Biblioteki

%description -n libltdl
System independent dlopen wrapper for GNU libtool

%description -n libltdl -l pl
Biblioteka ogólnych wywo³añ dlopen

%package -n	libltdl-devel
Summary:	System independent dlopen wrapper for GNU libtool
Summary(pl):	Biblioteka ogólnych wywo³añ dlopen
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	libltdl = %{version}

%description -n libltdl-devel
System independent dlopen wrapper for GNU libtool

%description -n libltdl-devel -l pl
Biblioteka ogólnych wywo³añ dlopen

%package -n	libltdl-static
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

%build
aclocal
CFLAGS="$RPM_OPT_FLAGS" \
    ./configure \
	--prefix=%{_prefix} \
	%{_target_platform}

(cd doc && make -k)
make

%install
rm -rf $RPM_BUILD_ROOT

make \
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    install

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info* \
	AUTHORS NEWS README THANKS TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/libtool.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
    /sbin/install-info --delete %{_infodir}/libtool.info.gz /etc/info-dir
fi
%post -n libltdl
/sbin/ldconfig

%post -n libltdl-devel
/sbin/ldconfig

%postun -n libltdl
/sbin/ldconfig

%postun -n libltdl-devel
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {AUTHORS,NEWS,README,THANKS,TODO,ChangeLog}.gz demo

%attr(755,root,root) %{_bindir}/*

%{_infodir}/libtool.info*

%dir %{_datadir}/libtool
%attr(755,root,root) %{_datadir}/libtool/config.guess
%attr(755,root,root) %{_datadir}/libtool/config.sub
%attr(755,root,root) %{_datadir}/libtool/ltconfig

%{_datadir}/libtool/ltmain.sh
%{_datadir}/aclocal/libtool.m4

%files -n libltdl
%defattr(755,root,root,755)
%{_libdir}/lib*.so.*.*

%files -n libltdl-devel
%defattr(644,root,root,755)

%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%{_includedir}/*
%attr(-,root,root) %{_datadir}/libtool/libltdl

%files -n libltdl-static
%defattr(644,root,root,755)

%{_libdir}/lib*.a

%changelog
* Sun May 23 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3-3]
- added some macros,
- fixed %post & %postun,
- cosmetic.

* Wed May  5 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-2]
- added CFLAGS="$RPM_OPT_FLAGS" to ./configure enviroment,
- added stripping shared libraries.

* Fri Apr 30 1999 Artur Frysiak <wiget@pld.org.pl>
- added libltdl, libltdl-devel and libltdl-static subpackage
- removed BuildArch: noarch (added subpackage are system independent)
- added patch for work correct with grep 2.3

* Sun Mar 14 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [1.2d-3]
- added gzipping documentation

* Thu Mar 11 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2d-2]
- Group changed to Development/Tools,
- added Group(pl).

* Tue Dec 29 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2d-1]
- added pl translation,
- added libtool-info.patch.
- standarized {un}registering info pages.

* Wed Nov 25 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2b-2]
- added URL field,
- fixed --entry text on {un}registering info page for libtool in %post
  %preun in devel.

* Thu Sep  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- removed COPYING and INSTALL drom %doc,
- added %attr and %defattr macros in %files (allows build package from
  non-root account),
- start at RH spec.
