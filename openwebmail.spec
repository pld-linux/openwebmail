#
# Spec file for Open Webmail
#
Summary:	Open Webmail
Summary(pl):	Otwarta poczta przez przegl±darkê
Name:		openwebmail
Version:	1.90
Release:	0.1
License:	GPL
Group:		Applications/Mail
Source0:	http://openwebmail.org/openwebmail/download/%{name}-%{version}.tgz
URL:		http://openwebmail.org/
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup

%install
rm -rf $RPM_BUILD_ROOT
#tar -zxvBpf $RPM_SOURCE_DIR/openwebmail-current.tgz --directory=/var/www
#cp -rf $RPM_SOURCE_DIR/auth_unix.pl /var/www/cgi-bin/openwebmail/auth_unix.pl
#cp -rf $RPM_SOURCE_DIR/openwebmail.conf /var/www/cgi-bin/openwebmail%{_sysconfdir}/openwebmail.conf
#ln -sf /var/www/data /var/www/html/data
#ln -sf /var/www/cgi-bin/openwebmail/vacation.pl %{_sysconfdir}/smrsh/vacation.pl

%files
%defattr(644,root,root,755)
/var/www/cgi-bin/openwebmail
/var/www/data/openwebmail
/var/www/html/data
%{_sysconfdir}/smrsh/vacation.pl

%post
echo
echo "You may login with non-root account from"
echo "http://$HOSTNAME/cgi-bin/openwebmail/openwebmail.pl"
echo

%clean
rm -rf $RPM_BUILD_ROOT
