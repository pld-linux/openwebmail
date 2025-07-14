#
# TODO:
# - move from /home/services to /usr/share (upgrade-trigger)
# - main package should be non-suid, it can work as regular imap client
# - prepare second, suid subpackage
# - update to webapps framework
#
# Conditional build:
# _with_ispell - toggle ispell support
# _with_quota  - toggle quota support
# (it's only needed for automagical depenednces)
#
Summary:	Open Webmail
Summary(pl.UTF-8):	Otwarta poczta przez przeglądarkę
Name:		openwebmail
Version:	2.53
Release:	1
License:	GPL
Group:		Applications/WWW
Source0:	http://openwebmail.org/openwebmail/download/release/%{name}-%{version}.tar.gz
# Source0-md5:	a7b6c55c5a9a437d003fbb6c74b0c468
Patch0:		%{name}-conf-PLD.patch
Patch1:		%{name}-auth.patch
URL:		http://openwebmail.org/
Requires:	perl-modules >= 5.8
Requires:	iconv
Requires:	perl-CGI
Requires:	perl-MIME-Base64
Requires:	perl-libnet
Requires:	perl-Text-Iconv
Requires:	sperl >= 5.8
%{?_with_ispell:Requires:	ispell}
%{?_with_quota:Requires:	quota}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Open WebMail to system poczty przez WWW zaprojektowany do zarządzania
bardzo dużymi plikami folderów pocztowych w sposób wydajny pamięciowo.
Ma także własności pomagające użytkownikom gładko przejść z Microsoft
Outlooka na Open WebMail. Open WebMail ma następujące możliwości:
wiele języków, wiele zestawów ikon i styli, silne wsparcie dla MIME,
wirtualne aliasy host/login, obsługę PAM, zmianę hasła online, wygodne
operacje na folderach i wiadomościach, folder szkiców, obsługę
potwierdzenia przeczytania, pełnotekstowe przeszukiwanie, kontrolę
pisowni, automatyczne odpowiadanie, filtrowanie poczty, obsługę POP3
oraz podglądanie liczby wiadomości.

%prep
%setup -q -c
%patch -P0 -p1
%patch -P1 -p1

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
%{_cgidir}/%{name}
%{_httpdir}/html/%{name}
%{_sysconfdir}/smrsh/vacation.pl
