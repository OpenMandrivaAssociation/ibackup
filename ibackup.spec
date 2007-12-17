Summary: 	Automated backups (even remote) of machine configurations
Name: 		ibackup
Version: 	2.27
Release: 	%mkrel 4
License: 	GPL
Group:		Archiving/Backup
Source:		%{name}-%{version}.tar.bz2
Patch0:		%{name}-2.27-make-rpm.patch
URL:		http://www.linuks.mine.nu/ibackup/
BuildArch:	noarch

%description
This software simplifies the task of backing up the system
configuration files (those under /etc) for UNIX systems
(Solaris, *BSD, Linux). You can run the program from any directory
and it will by default save the (maybe compressed) tarball to /root.
.
It is possible to encrypt the tarball, to upload the tarball to some
other host and run the backup automated in a cronjob.
       
%prep
%setup -q
%patch0 -p1

%build

%install
[ -d %{buildroot} -a "%{buildroot}" != "" ] && rm -rf  %{buildroot}

make DESTDIR=%{buildroot} MANDIR=%{buildroot}%{_mandir} install
make DESTDIR=%{buildroot} install-config

%clean
[ -d %{buildroot} -a "%{buildroot}" != "" ] && rm -rf  %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING changelog *.html *.png *.jpg
%{_bindir}/ibackup
%{_bindir}/sysconf
%config(noreplace) /etc/ibackup.conf
%{_mandir}/man1/*


