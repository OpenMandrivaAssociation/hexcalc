%define release %mkrel 14

Summary: A decimal, hexadecimal, octal and binary calculator
Name: hexcalc
Version: 1.11
Release: %release
License: GPL like
Group: Sciences/Mathematics
Source: ftp://ftp.x.org/R5contrib/hexcalc.tar.bz2
Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png
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
mkdir -p %buildroot{%_menudir,%_miconsdir,%_iconsdir,%_liconsdir}

install -m 644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot%_iconsdir/%name.png
install -m 644 %SOURCE3 %buildroot%_liconsdir/%name.png

cat > %buildroot%_menudir/%name <<EOF
?package(%{name}):\
        command="%{_bindir}/%{name}"\
        title="Hexcalc"\
        longtitle="Hexadecimal calculator"\
        needs="x11"\
        section="More Applications/Sciences/Mathematics"\
        icon="%{name}.png" \
        xdg="true"
EOF

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

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%_bindir/hexcalc
%_mandir/*/*
%_miconsdir/%name.png
%_iconsdir/%name.png
%_liconsdir/%name.png
%_menudir/%name
%{_datadir}/applications/mandriva-%{name}.desktop

