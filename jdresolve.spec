%include	/usr/lib/rpm/macros.perl
Summary:	jdresolve resolves IP addresses into hostnames with recursion
Summary(pl.UTF-8):   Tłumaczenie adresów IP na nazwy z rekurencją
Name:		jdresolve
Version:	0.6.1
Release:	4
License:	GPL
Group:		Development/Languages
Source0:	http://www.jdrowell.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	916a1e0023d2d18e2b2e8efd4efe23c5
Patch0:		%{name}-noroot.patch
URL:		http://www.jdrowell.com/Linux/Projects/jdresolve/
BuildRequires:	perl-Net-DNS 
BuildRequires:	rpm-perlprov
Requires:	perl-DB_File
Requires:	perl-Net-DNS >= 0.12
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Program jdresolve tłumaczy adresy IP na nazwy komputerów. Aby
zmniejszyć czas potrzebny na przetłumaczenie dużych partii adresów,
jdresolve otwiera wiele jednoczesnych połączeń do serwerów DNS,
trzymając wiele linii tekstu w pamięci. Te linie mogą mieć dowolną
zawartość, pod warunkiem, że adresy IP są pierwszym polem od lewej.
Tak jest zazwyczaj w przypadku większości formatów logów HTTP i FTP.

Dla adresów, które nie mogą być przetłumaczone z powodu timeoutów lub
źle skonfigurowanych stref odwrotnych, dostępny jest algorytm
rekurencyjny: szukane są domeny nadrzędne (klasy C, B, A) adresu IP, a
te nazwy domen są używane do tworzenia fałszywych nazw hostów, z
użyciem maski zdefiniowanej przez użytkownika.

%prep
%setup  -q
%patch0 -p1

%build
sh configure

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	USER=`id -u` \
	GROUP=`id -g`

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS README TODO
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
