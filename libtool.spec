Summary:     GNU libtool, a shared library generation tool.
Name:        libtool
Version:     1.2b
Release:     2
Copyright:   GPL
Group:       Development/Building
Source:      ftp://alpha.gnu.org/gnu/%{name}-%{version}.tar.gz
PreReq:      /sbin/install-info
BuildRoot:   /tmp/%{name}-%{version}-root
URL:         http://www.profitpress.com/libtool/
BuildArchitectures: noarch

%description
GNU libtool is a set of shell scripts to automatically configure
UNIX architectures to build shared libraries in generic fashion.

%prep
%setup -q

%build
./configure --prefix=/usr
(cd doc && make -k)
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr
make prefix=$RPM_BUILD_ROOT/usr install
gzip -9 $RPM_BUILD_ROOT/usr/info/*.info*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/libtool.info.gz /usr/info/dir --entry \
"* Libtool: (libtool).                           Generic shared library support script."

%preun
/sbin/install-info --delete /usr/info/libtool.info.gz /usr/info/dir \
"* Libtool: (libtool).                           Generic shared library support script."

%files
%defattr(644, root, root, 755)
%doc AUTHORS NEWS README THANKS TODO ChangeLog demo
%attr(755, root, root) /usr/bin/*
/usr/info/libtool.info*
%dir /usr/share/libtool
%attr(755, root, root) /usr/share/libtool/config.guess
%attr(755, root, root) /usr/share/libtool/config.sub
%attr(755, root, root) /usr/share/libtool/ltconfig
/usr/share/libtool/ltmain.sh
/usr/share/aclocal/libtool.m4

%changelog
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
- added %attr and %defattr macros in %files (allow build package from
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
