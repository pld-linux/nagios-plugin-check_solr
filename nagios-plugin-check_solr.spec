%define		plugin	check_solr
Summary:	This is a nagios plugin that checks Apache Solr host
Name:		nagios-plugin-%{plugin}
Version:	2010.10.11
Release:	1
License:	Open Source (other)
Group:		Networking
Source0:	http://nagios-plugins-shamil.googlecode.com/svn/trunk/by_me/check_solr.sh
# Source0-md5:	c53cf19008597b4d9a352ae28ad7127b
Source1:	%{plugin}.cfg
Patch0:		bashism.patch
URL:		https://code.google.com/p/nagios-plugins-shamil/
Requires:	curl
Requires:	nagios-common
Requires:	which
Requires:	xmlstarlet
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
The plugin is capable of check couple aspects of Apache Solr server.
Supported checks are ping, replication and number of documents. Check
usage for info.

%prep
%setup -qcT
cp -p %{SOURCE0} .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin}.sh $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
