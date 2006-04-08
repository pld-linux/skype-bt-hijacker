#
Summary:	skype_bt_hijacker
Summary(pl):	skype_bt_hijacker
Name:		skype_bt_hijacker
Version:	0.1b
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.acs.uni-duesseldorf.de/~becka/download/skype/%{name}-%{version}.tgz
# Source0-md5:	63114d0ec023bb86a7e997ca5bbb5163
#Patch0:		%{name}-DESTDIR.patch
URL:		http://www.acs.uni-duesseldorf.de/~becka/download/skype/
#BuildRequires:	-
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	intltool
#BuildRequires:	libtool
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Provides:	group(foo)
#Provides:	user(foo)
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
skype script for making the headset button answer an incoming call

%description -l pl


%prep
%setup -q
#%patch0 -p1


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

%pre

%post

%preun

%postun

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
