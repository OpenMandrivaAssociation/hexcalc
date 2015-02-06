Summary:	A decimal, hexadecimal, octal and binary calculator
Name:		hexcalc
Version:	1.11
Release:	23
License:	GPL-like
Group:		Sciences/Mathematics
Source0:	ftp://ftp.x.org/R5contrib/hexcalc.tar.bz2
Source1:	%{name}-16.png
Source2:	%{name}-32.png
Source3:	%{name}-48.png
BuildRequires:	imake
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xt)

%description
Hexcalc is a simple multi-radix calculator for programmers. The calculator
operates in four modes (decimal, hexadecimal, octal and binary).

%files
%{_bindir}/hexcalc
%{_mandir}/*/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}

%build
xmkmf
%make CCOPTIONS="%{optflags}" EXTRA_LDOPTIONS="%{ldflags}"

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -c hexcalc %{buildroot}%{_bindir}
install -c hexcalc.man %{buildroot}%{_mandir}/man1/hexcalc.1x

# Menu stuff
install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_liconsdir}

install -m 644 %{SOURCE1} %{buildroot}%{_miconsdir}/%{name}.png
install -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png
install -m 644 %{SOURCE3} %{buildroot}%{_liconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
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

