%define		snap 20021218
Summary:	GNU libtool, a shared library generation tool
Summary(es):	GNU libtool, una herramienta de creación de bibliotecas compartidas
Summary(pl):	GNU libtool - narzêdzie do generowania bibliotek wspó³dzielonych
Summary(pt_BR):	GNU libtool, uma ferramenta de geração de bibliotecas compartilhadas
Name:		libtool
Version:	1.4e
Release:	0.%{snap}.2
Epoch:		2
License:	GPL
Group:		Development/Tools
# source from Libtool CVS
Source0:	%{name}-%{version}.%{snap}.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-man-pages.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-mktemp.patch
Patch2:		%{name}-relink.patch
URL:		http://www.gnu.org/software/libtool/
Requires:	mktemp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU libtool is a set of shell scripts to automatically configure UNIX
architectures to build shared libraries in generic fashion.

%description -l es
GNU libtool es un conjunto de scripts shell para configurar
automáticamente la creación de bibliotecas compartidas para varias
arquitecturas UNIX de una manera genérica.

%description -l pl
GNU libtool jest zbiorem skryptów shellowych do automatycznego
generowania bibliotek wspó³dzielonych niezale¿nie od typu platformy
systemowej.

%description -l pt_BR
GNU libtool é um conjunto de scripts shell para configurar
automaticamente a geração de bibliotecas compartilhadas para várias
arquiteturas UNIX de uma maneira genérica.

%package -n libltdl
Summary:	System independent dlopen wrapper for GNU libtool
Summary(pl):	Biblioteka ogólnych wywo³añ dlopen
Summary(pt_BR):	GNU libltdl, um wrapper dlopen para o GNU libtool
Group:		Libraries
Obsoletes:	libtool-libs

%description -n libltdl
System independent dlopen wrapper for GNU libtool.

%description -n libltdl -l pl
Biblioteka ogólnych wywo³añ dlopen.

%description -n libltdl -l pt_BR
GNU libltdl, um wrapper dlopen para o GNU libtool.

%package -n libltdl-devel
Summary:	Development components for libltdl
Summary(pl):	Czê¶æ libltdl przeznaczona dla programistów
Summary(pt_BR):	Componentes de desenvolvimento para a libltdl
Group:		Development/Libraries
Requires:	libltdl = %{version}

%description -n libltdl-devel
System independent dlopen wrapper for GNU libtool - development part.
Install this package if you want to develop for libltdl.

%description -n libltdl-devel -l pl
Biblioteka ogólnych wywo³añ dlopen - czê¶æ dla programistów.

%description -n libltdl-devel -l pt_BR
Instale este pacote se você deseja desenvolver para a libltdl.

%package -n libltdl-static
Summary:	Static system independent dlopen wrapper for GNU libtool
Summary(pl):	Statyczna biblioteka ogólnych wywo³añ dlopen
Summary(pt_BR):	Componentes de desenvolvimento para a libltdl
Group:		Development/Libraries
Requires:	libltdl-devel = %{version}

%description -n libltdl-static
Static system independent dlopen wrapper for GNU libtool. Install this
package if you want to develop for libltdl, but using static
components (seldom used).

%description -n libltdl-static -l pl
Statyczna biblioteka ogólnych wywo³añ dlopen.

%description -n libltdl-static -l pt_BR
Instale este pacote se você deseja desenvolver para a libltdl,
utilizando componentes estáticos (raramente necessário).

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure
%{__make} -C doc -k
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post   -n libltdl -p /sbin/ldconfig
%postun -n libltdl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO ChangeLog demo
%attr(755,root,root) %{_bindir}/*

%dir %{_datadir}/libtool
%attr(755,root,root) %{_datadir}/libtool/config.guess
%attr(755,root,root) %{_datadir}/libtool/config.sub
%attr(755,root,root) %{_datadir}/libtool/ltmain.sh
%attr(755,root,root) %{_datadir}/libtool/install-sh
%attr(755,root,root) %{_datadir}/libtool/missing
%attr(755,root,root) %{_datadir}/libtool/mkinstalldirs

%{_infodir}/libtool.info*
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%{_aclocaldir}/libtool.m4

%files -n libltdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files -n libltdl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/ltdl.m4

%dir %{_datadir}/libtool/libltdl
%{_datadir}/libtool/libltdl/[CMRal]*
%{_datadir}/libtool/libltdl/config-h.in
%attr(755,root,root) %{_datadir}/libtool/libltdl/configure
%{_datadir}/libtool/libltdl/configure.ac

%files -n libltdl-static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
