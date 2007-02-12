# TODO: Name vs filename
Summary:	Skype script for making the headset button answer an incoming call
Summary(pl.UTF-8):	Skrypt Skype'a do odbierania połączenia przyciskiem słuchawek
Name:		skype_bt_hijacker
Version:	0.1b
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.acs.uni-duesseldorf.de/~becka/download/skype/%{name}-%{version}.tgz
# Source0-md5:	63114d0ec023bb86a7e997ca5bbb5163
URL:		http://www.acs.uni-duesseldorf.de/~becka/download/skype/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skype script for making the headset button answer an incoming call.

%description -l pl.UTF-8
Skrypt Skype'a do odbierania połączenia przyciskiem słuchawek.

%prep
%setup -q

%build
%{__make}

rm *.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}
install libskype_bt_hijacker.so $RPM_BUILD_ROOT%{_libdir}
install skype_* $RPM_BUILD_ROOT%{_bindir}
install btscorunner $RPM_BUILD_ROOT%{_bindir}
 
%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libskype_bt_hijacker.so
