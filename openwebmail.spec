#
# Spec file for Open Webmail
#
Summary:	Open Webmail 1.90
Name:		openwebmail
Version:	1.90
Release:	20030313
License:	GPL
Group:		Applications/Mail
Source0:	ftp://ftp.openwebmail.org/pub/%{name}-current.tgz
URL:		http://openwebmail.org
Vendor:		Open Webmail Project

%description
Open Webmail 1.90

Open WebMail is a webmail system based on the Neomail version 1.14
from Ernie Miller. Open WebMail is designed to manage very large mail
folder files in a memory efficient way. It also provides a range of
features to help users migrate smoothly from Microsoft Outlook to Open
WebMail.

Homepage : http://openwebmail.org Credit : Chung-Kie Tung
<tung@turtle.ee.ncku.edu.tw> Nai-Jung Kuo
<ebola@turtle.ee.ncku.edu.tw> Chao-Chiu Wang
<eddie@turtle.ee.ncku.edu.tw> Emir Litric <elitric@yahoo.com> Thomas
Chung <tchung@openwebmail.org> Filippo Dattola <filippo@sms.it> Bernd
Bass <owm@adminsquare.de>

Special Thanks to Daniel Pentecost <daniel@davoice.net> who has
donated a dedicated web server in his datacenter for openwebmail.org

%prep
rm -rf /usr/src/redhat/RPMS/i386/*
rm -rf /usr/src/redhat/SRPMS/*

%install
rm -rf $RPM_BUILD_ROOT
tar -zxvBpf $RPM_SOURCE_DIR/openwebmail-current.tgz --directory=/var/www
cp -rf $RPM_SOURCE_DIR/auth_unix.pl /var/www/cgi-bin/openwebmail/auth_unix.pl
cp -rf $RPM_SOURCE_DIR/openwebmail.conf /var/www/cgi-bin/openwebmail%{_sysconfdir}/openwebmail.conf
ln -sf /var/www/data /var/www/html/data
ln -sf /var/www/cgi-bin/openwebmail/vacation.pl %{_sysconfdir}/smrsh/vacation.pl

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
