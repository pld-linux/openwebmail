Summary:	Open Webmail
Summary(pl):	Otwarta poczta przez przegl�dark�
Name:		openwebmail
Version:	1.90
Release:	0.1
License:	GPL
Group:		Applications/Mail
Source0:	http://openwebmail.org/openwebmail/download/%{name}-%{version}.tgz
URL:		http://openwebmail.org/
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		httpdir		/home/services/httpd
%define		htmldir		%{httpdir}/html
%define		cgidir		%{httpdir}/cgi-bin

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
Open WebMail to system poczty przez WWW zaprojektowany do zarz�dzania
bardzo du�ymi plikami folder�w pocztowych w spos�b wydajny pami�ciowo.
Ma tak�e w�asno�ci pomagaj�ce u�ytkownikom g�adko przej�� z Microsoft
Outlooka na Open WebMail. Open WebMail ma nast�puj�ce mo�liwo�ci:
wiele j�zyk�w, wiele zestaw�w ikon i styli, silne wsparcie dla MIME,
wirtualne aliasy host/login, obs�ug� PAM, zmian� has�a online, wygodne
operacje na folderach i wiadomo�ciach, folder szkic�w, obs�ug�
potwierdzenia przeczytania, pe�notekstowe przeszukiwanie, kontrol�
pisowni, automatyczne odpowiadanie, filtrowanie poczty, obs�ug� POP3
oraz podgl�danie liczby wiadomo�ci.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
#tar -zxvBpf %{SOURCE0} --directory=%{httpdir}
#cp -rf $RPM_SOURCE_DIR/auth_unix.pl %{cgidir}/openwebmail/auth_unix.pl
#cp -rf $RPM_SOURCE_DIR/openwebmail.conf %{cgidir}/openwebmail%{_sysconfdir}/openwebmail.conf
#ln -sf %{httpdir}/data %{htmldir}/data
#ln -sf %{cgidir}/openwebmail/vacation.pl %{_sysconfdir}/smrsh/vacation.pl

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo
echo "You may login with non-root account from"
echo "http://$HOSTNAME/cgi-bin/openwebmail/openwebmail.pl"
echo

%files
%defattr(644,root,root,755)
%{cgidir}/openwebmail
# NOTE: %{httpdir}/data dir doesn't exist
%{httpdir}/data/openwebmail
%{htmldir}/data
%{_sysconfdir}/smrsh/vacation.pl
