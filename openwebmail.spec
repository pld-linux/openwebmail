Summary:	Open Webmail
Summary(pl):	Otwarta poczta przez przegl±darkê
Name:		openwebmail
Version:	2.01
Release:	0.2
License:	GPL
Group:		Applications/Mail
Source0:	http://openwebmail.com/openwebmail/download/%{name}-%{version}.tgz
Patch0:		%{name}-conf-PLD.patch
URL:		http://openwebmail.com/
Requires:	perl >= 5.8
Requires:	iconv
Requires:	perl-CGI
Requires:	perl-MIME-Base64
Requires:	perl-libnet
Requires:	perl-Text-Iconv
Requires:	sperl >= 5.8
Requires:	ispell
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_httpdir	/home/services/httpd
%define		_htmldir	%{_httpdir}/html
%define		_cgidir		%{_httpdir}/cgi-bin

%description
Open WebMail is a webmail system designed to manage very large mail
folder files in a memory efficient way. It also provides a range of
features to help users migrate smoothly from Microsoft Outlook to Open
WebMail. Open WebMail has the following features: multiple languages,
multiple iconsets/styles, strong MIME support, virtual host/login
alias, PAM support, online password changing, convenient
folder/message operations, draft folder, confirmed reading support,
full content search, a spelling checker, auto reply, mail filtering,
POP3 support, and message count previewing.

%description -l pl
Open WebMail to system poczty przez WWW zaprojektowany do zarz±dzania
bardzo du¿ymi plikami folderów pocztowych w sposób wydajny pamiêciowo.
Ma tak¿e w³asno¶ci pomagaj±ce u¿ytkownikom g³adko przej¶æ z Microsoft
Outlooka na Open WebMail. Open WebMail ma nastêpuj±ce mo¿liwo¶ci:
wiele jêzyków, wiele zestawów ikon i styli, silne wsparcie dla MIME,
wirtualne aliasy host/login, obs³ugê PAM, zmianê has³a online, wygodne
operacje na folderach i wiadomo¶ciach, folder szkiców, obs³ugê
potwierdzenia przeczytania, pe³notekstowe przeszukiwanie, kontrolê
pisowni, automatyczne odpowiadanie, filtrowanie poczty, obs³ugê POP3
oraz podgl±danie liczby wiadomo¶ci.

%prep
%setup -q -c
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_cgidir},%{_htmldir},%{_sysconfdir}/smrsh}

cp -a cgi-bin/%{name} $RPM_BUILD_ROOT%{_cgidir}
cp -a data/%{name} $RPM_BUILD_ROOT%{_htmldir}
ln -sf %{_cgidir}/openwebmail/vacation.pl $RPM_BUILD_ROOT%{_sysconfdir}/smrsh/vacation.pl

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo
echo "You may login with non-root account from"
echo "http://$HOSTNAME/cgi-bin/openwebmail/openwebmail.pl"
echo

%files
%defattr(644,root,root,755)
%{_cgidir}/%{name}/*
%{_httpdir}/html/%{name}/*
%{_sysconfdir}/smrsh/vacation.pl
