%include	/usr/lib/rpm/macros.perl
Summary:	jdresolve resolves IP addresses into hostnames with recursion
Summary(pl):	T�umaczenie adres�w IP na nazwy z rekurencj�
Name:		jdresolve
Version:	0.6.1
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://www.jdrowell.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	916a1e0023d2d18e2b2e8efd4efe23c5
Patch0:		%{name}-noroot.patch
URL:		http://www.jdrowell.com/Linux/Projects/jdresolve/
Requires:	perl >= 5.004
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

%description -l pl
Program jdresolve t�umaczy adresy IP na nazwy komputer�w. Aby
zmniejszy� czas potrzebny na przet�umaczenie du�ych partii adres�w,
jdresolve otwiera wiele jednoczesnych po��cze� do serwer�w DNS,
trzymaj�c wiele linii tekstu w pami�ci. Te linie mog� mie� dowoln�
zawarto��, pod warunkiem, �e adresy IP s� pierwszym polem od lewej.
Tak jest zazwyczaj w przypadku wi�kszo�ci format�w log�w HTTP i FTP.

Dla adres�w, kt�re nie mog� by� przet�umaczone z powodu timeout�w lub
�le skonfigurowanych stref odwrotnych, dost�pny jest algorytm
rekurencyjny: szukane s� domeny nadrz�dne (klasy C, B, A) adresu IP, a
te nazwy domen s� u�ywane do tworzenia fa�szywych nazw host�w, z
u�yciem maski zdefiniowanej przez u�ytkownika.

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
