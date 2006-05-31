Summary:	GNU libtool, a shared library generation tool
Summary(es):	GNU libtool, una herramienta de creación de bibliotecas compartidas
Summary(pl):	GNU libtool - narzêdzie do generowania bibliotek wspó³dzielonych
Summary(pt_BR):	GNU libtool, uma ferramenta de geração de bibliotecas compartilhadas
Summary(ru):	GNU libtool, ÎÁÂÏÒ ÕÔÉÌÉÔ ÄÌÑ ÇÅÎÅÒÁÃÉÉ ÒÁÚÄÅÌÑÅÍÙÈ ÂÉÂÌÉÏÔÅË
Summary(uk):	GNU libtool, ÎÁÂ¦Ò ÕÔÉÌ¦Ô ÄÌÑ ÇÅÎÅÒÁÃ¦§ ÄÉÎÁÍ¦ÞÎÉÈ Â¦ÂÌ¦ÏÔÅË
Name:		libtool
Version:	1.5.22
Release:	4
Epoch:		2
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/libtool/%{name}-%{version}.tar.gz
# Source0-md5:	8e0ac9797b62ba4dcc8a2fb7936412b0
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-man-pages.tar.bz2
# Source1-md5:	b95e215961860c66f0868b0d551358c9
Patch0:		%{name}-info.patch
Patch1:		%{name}-relink.patch
Patch2:		%{name}-libdirs.patch
Patch3:		%{name}-multilib.patch
URL:		http://www.gnu.org/software/libtool/
BuildRequires:	/usr/bin/which
BuildRequires:	autoconf >= 2.57
%ifarch %{x8664}
BuildRequires:	automake >= 1:1.7.9-2
%else
BuildRequires:	automake >= 1:1.7.3
%endif
BuildRequires:	gcc-c++ >= 5:3.3.3
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	texinfo
%requires_eq	gcc
Requires:	%(which %{__cc})
Requires:	coreutils
Requires:	grep
Requires:	mktemp
Requires:	sed
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

%description -l ru
GNU libtool - ÜÔÏ ÎÁÂÏÒ ÓËÒÉÐÔÏ× ÄÌÑ Á×ÔÏÍÁÔÉÞÅÓËÏÊ ÇÅÎÅÒÁÃÉÉ
ÄÉÎÁÍÉÞÅÓËÉÈ ÒÁÚÄÅÌÑÅÍÙÈ ÂÉÂÌÉÏÔÅË ÎÁ ÒÁÚÌÉÞÎÙÈ ÁÒÈÉÔÅËÔÕÒÁÈ UNIX.

%description -l uk
GNU libtool - ÃÅ ÎÁÂ¦Ò ÓËÒÉÐÔ¦× ÄÌÑ Á×ÔÏÍÁÔÉÞÎÏ§ ÇÅÎÅÒÁÃ¦§ ÄÉÎÁÍ¦ÞÎÉÈ
Â¦ÂÌ¦ÏÔÅË ÎÁ Ò¦ÚÎÉÈ ÁÒÈ¦ÔÅËÔÕÒÁÈ UNIX.

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
Summary(ru):	æÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó libltdl
Summary(uk):	æÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú libltdl
Group:		Development/Libraries
Requires:	libltdl = %{epoch}:%{version}-%{release}

%description -n libltdl-devel
System independent dlopen wrapper for GNU libtool - development part.
Install this package if you want to develop for libltdl.

%description -n libltdl-devel -l pl
Biblioteka ogólnych wywo³añ dlopen - czê¶æ dla programistów.

%description -n libltdl-devel -l pt_BR
Instale este pacote se você deseja desenvolver para a libltdl.

%description -n libltdl-devel -l uk
æÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú libltdl.

%description -n libltdl-devel -l ru
æÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó libltdl.

%package -n libltdl-static
Summary:	Static system independent dlopen wrapper for GNU libtool
Summary(pl):	Statyczna biblioteka ogólnych wywo³añ dlopen
Summary(pt_BR):	Componentes de desenvolvimento para a libltdl
Summary(ru):	óÔÁÔÉÞÅÓËÁÑ ÂÉÂÌÉÏÔÅËÁ libltdl ÉÚ libltdl
Summary(uk):	óÔÁÔÉÞÎÁ Â¦ÂÌ¦ÏÔÅËÁ libltdl Ú libltdl
Group:		Development/Libraries
Requires:	libltdl-devel = %{epoch}:%{version}-%{release}

%description -n libltdl-static
Static system independent dlopen wrapper for GNU libtool. Install this
package if you want to develop for libltdl, but using static
components (seldom used).

%description -n libltdl-static -l pl
Statyczna biblioteka ogólnych wywo³añ dlopen.

%description -n libltdl-static -l pt_BR
Instale este pacote se você deseja desenvolver para a libltdl,
utilizando componentes estáticos (raramente necessário).

%description -n libltdl-static -l ru
üÔÏ ÏÔÄÅÌØÎÙÊ ÐÁËÅÔ ÓÏ ÓÔÁÔÉÞÅÓËÉÍÉ ÂÉÂÌÉÏÔÅËÁÍÉ, ËÏÔÏÒÙÅ ÂÏÌØÛÅ ÎÅ
×ÈÏÄÑÔ × libltdl.

%description -n libltdl-static -l uk
ãÅ ÏËÒÅÍÉÊ ÐÁËÅÔ Ú¦ ÓÔÁÔÉÞÎÉÍÉ Â¦ÂÌ¦ÏÔÅËÁÍÉ, ÝÏ Â¦ÌØÛÅ ÎÅ ×ÈÏÄÑÔØ ÄÏ
ÓËÌÁÄÕ libltdl.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# it's the same - copy so patching only libtool.m4 is sufficient
cp -f libtool.m4 acinclude.m4
cat libtool.m4 ltdl.m4 > libltdl/acinclude.m4

%build
%{__aclocal}
%{__autoconf}
%{__automake}

cd libltdl
%{__aclocal}
%{__autoconf}
cp -f ../config.sub .
automake -a -c --foreign
cd ..

%configure

%{__make} -C doc -k
%{__make} libtoolize
%{__make} acinclude.m4 cdemo/acinclude.m4 pdemo/acinclude.m4 \
	demo/acinclude.m4 depdemo/acinclude.m4 mdemo/acinclude.m4 \
	tagdemo/acinclude.m4 f77demo/acinclude.m4
%{__make} -C libltdl Makefile.in
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_datadir}/libtool/install-sh
%attr(755,root,root) %{_datadir}/libtool/ltmain.sh

%{_infodir}/libtool.info*
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%{_aclocaldir}/libtool.m4

%files -n libltdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libltdl.so.*.*.*

%files -n libltdl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libltdl.so
%{_libdir}/libltdl.la
%{_includedir}/ltdl.h
%{_aclocaldir}/ltdl.m4

%dir %{_datadir}/libtool
%dir %{_datadir}/libtool/libltdl
%{_datadir}/libtool/libltdl/[CMRal]*
%{_datadir}/libtool/libltdl/config-h.in
%attr(755,root,root) %{_datadir}/libtool/libltdl/configure
%{_datadir}/libtool/libltdl/configure.ac
%attr(755,root,root) %{_datadir}/libtool/libltdl/install-sh
%attr(755,root,root) %{_datadir}/libtool/libltdl/missing
%attr(755,root,root) %{_datadir}/libtool/libltdl/config.guess
%attr(755,root,root) %{_datadir}/libtool/libltdl/config.sub

%files -n libltdl-static
%defattr(644,root,root,755)
%{_libdir}/libltdl.a
