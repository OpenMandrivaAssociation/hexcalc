Summary: A decimal, hexadecimal, octal and binary calculator
Name: hexcalc
Version: 1.11
Release: %mkrel 17
License: GPL like
Group: Sciences/Mathematics
Source: ftp://ftp.x.org/R5contrib/hexcalc.tar.bz2
Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png
Buildroot: %_tmppath/%name-buildroot
BuildRequires: X11-devel
BuildRequires: imake

%description
Hexcalc is a simple multi-radix calculator for programmers. The
calculator operates in four modes (decimal, hexadecimal, octal and
binary).

%prep
%setup -q -n %name

%build
xmkmf
%make

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
Categories=X-MandrivaLinux-MoreApplications-Sciences-Mathematics;
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

