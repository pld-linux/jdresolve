%include	/usr/lib/rpm/macros.perl
Summary:	jdresolve resolves IP addresses into hostnames with recursion
Name:		jdresolve
Version:	0.5.2
Release:	2
License:	GPL
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Source0:	http://www.jdrowell.com/files/%{name}-%{version}.tar.gz
Patch0:		jdresolve-noroot.patch
Url:		http://www.jdrowell.com/Linux/Projects/jdresolve
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	perl >= 5.004
Requires:	perl-Net-DNS >= 0.12
BuildArch:	noarch

%description
The jdresolve application resolves IP addresses into hostnames. To
reduce the time necessary to resolve large batches of addresses,
jdresolve opens many concurrent connections to the DNS servers, and
keeps a large number of text lines in memory. These lines can have any
content, as long as the IP addresses are the first field to the left.
This is usually the case with most formats of HTTP and FTP log files.

For addresses that can't be resolved due to timeouts or incorrectly
configured reverse mappings, a recursive algorithm is available. A
search is made for the parent domains (classes C, B and A) of the IP
address and those domain names become available for composing a fake
hostname, thru a user defined mask.

%prep
%setup  -q
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	USER=`id -u` \
	GROUP=`id -g`

gzip -9nf CHANGELOG CREDITS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGELOG,CREDITS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/jdresolve
%attr(755,root,root) %{_bindir}/jdresolve-dumpdb
%attr(755,root,root) %{_bindir}/jdresolve-mergedb
%attr(755,root,root) %{_bindir}/jdresolve-unresolved
%attr(755,root,root) %{_bindir}/rhost
