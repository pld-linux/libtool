Summary:	GNU libtool, a shared library generation tool.
Summary(pl):	GNU libtool - narzêdzie do generowania bibliotek wspó³dzielonych
Name:		libtool
Version:	1.3
Release:	2
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Source:		ftp://alpha.gnu.org/gnu/%{name}-%{version}.tar.gz
Patch0:		libtool-info.patch
Patch2:		libtool-cache.patch
Patch3:		libtool-egrep.patch
URL:		http://www.profitpress.com/libtool/
PreReq:		/sbin/install-info
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GNU libtool is a set of shell scripts to automatically configure
UNIX architectures to build shared libraries in generic fashion.

%description -l pl
GNU libtool jest zbiorem skryptów shellowych do automatycznego gemnerowania
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
%patch2 -p1
%patch3 -p1

%build
aclocal
./configure %{_target} --prefix=/usr
(cd doc && make -k)
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr

make prefix=$RPM_BUILD_ROOT/usr install

gzip -9nf $RPM_BUILD_ROOT/usr/info/*.info* \
	AUTHORS NEWS README THANKS TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/libtool.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete /usr/info/libtool.info.gz /etc/info-dir
fi

%files
%defattr(644,root,root,755)
%doc {AUTHORS,NEWS,README,THANKS,TODO,ChangeLog}.gz demo
%attr(755,root,root) /usr/bin/*

/usr/info/libtool.info*

%dir /usr/share/libtool
%attr(755,root,root) /usr/share/libtool/config.guess
%attr(755,root,root) /usr/share/libtool/config.sub
%attr(755,root,root) /usr/share/libtool/ltconfig
/usr/share/libtool/ltmain.sh

/usr/share/aclocal/libtool.m4

%files -n libltdl
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/lib*.so.*.*

%files -n libltdl-devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/lib*.so
%attr(755,root,root) /usr/lib/lib*.la
/usr/include/*
%attr(-,root,root) /usr/share/libtool/libltdl

%files -n libltdl-static
%defattr(644,root,root,755)
/usr/lib/lib*.a

%changelog
* Fri Apr 30 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.3-2]
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
  non-root account).

* Thu May 07 1998 Donnie Barnes <djb@redhat.com>
- fixed busted group

* Sat Jan 24 1998 Marc Ewing <marc@redhat.com>
- Update to 1.0h
- added install-info support

* Tue Nov 25 1997 Elliot Lee <sopwith@redhat.com>
- Update to 1.0f
- BuildRoot it
- Make it a noarch package
