Summary: A decimal, hexadecimal, octal and binary calculator
Name: hexcalc
Version: 1.11
Release: %mkrel 20
License: GPL like
Group: Sciences/Mathematics
Source: ftp://ftp.x.org/R5contrib/hexcalc.tar.bz2
Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png
Buildroot: %_tmppath/%name-buildroot
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xaw7)
BuildRequires: pkgconfig(xt)
BuildRequires: imake

%description
Hexcalc is a simple multi-radix calculator for programmers. The
calculator operates in four modes (decimal, hexadecimal, octal and
binary).

%prep
%setup -q -n %name

%build
xmkmf
%make CCOPTIONS="%optflags" EXTRA_LDOPTIONS="%ldflags"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%_bindir
install -d $RPM_BUILD_ROOT%_mandir/man1

install -c -s hexcalc $RPM_BUILD_ROOT%_bindir
install -c hexcalc.man $RPM_BUILD_ROOT%_mandir/man1/hexcalc.1x

# Menu stuff
install -d %buildroot%_miconsdir
install -d %buildroot%_iconsdir
install -d %buildroot%_liconsdir

install -m 644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot%_iconsdir/%name.png
install -m 644 %SOURCE3 %buildroot%_liconsdir/%name.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Hexcalc
Comment=Hexadecimal calculator
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Science;Math;
EOF

%clean 
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%_bindir/hexcalc
%_mandir/*/*
%_miconsdir/%name.png
%_iconsdir/%name.png
%_liconsdir/%name.png
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 1.11-20mdv2011.0
+ Revision: 636003
- update desktop category
- tighten BR

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.11-19mdv2011.0
+ Revision: 619361
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.11-18mdv2010.0
+ Revision: 429393
- rebuild

* Sat Sep 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.11-17mdv2009.0
+ Revision: 286173
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Oct 24 2007 Olivier Thauvin <nanardon@mandriva.org> 1.11-14mdv2008.1
+ Revision: 101895
- rebuild, avoid useless brequires

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character


* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 21:24:39 (53681)
- xdg menu

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 21:18:06 (53676)
Import hexcalc

* Mon Oct 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.11-12mdk
- BuildRequires fix

* Fri Apr 08 2005 Olivier Thauvin <nanardon@mandrake.org> 1.11-11mdk
- fix buildrequires for 64 bits

* Fri Feb 04 2005 Sylvie Terjan <erinmargault@mandrake.org> 1.11-9mdk
- birthday release

* Fri Jan 23 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.11-8mdk
- 1st mdk package

