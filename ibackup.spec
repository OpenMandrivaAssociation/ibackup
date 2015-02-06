Summary: 	Automated backups (even remote) of machine configurations
Name: 		ibackup
Version: 	2.27
Release: 	9
License: 	GPL
Group:		Archiving/Backup
Source:		%{name}-%{version}.tar.bz2
Patch0:		%{name}-2.27-make-rpm.patch
URL:		http://www.linuks.mine.nu/ibackup/
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
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




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.27-8mdv2011.0
+ Revision: 619538
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.27-7mdv2010.0
+ Revision: 429487
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.27-6mdv2009.0
+ Revision: 247143
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.27-4mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 05 2007 Stew Benedict <sbenedict@mandriva.com> 2.27-4mdv2007.0
+ Revision: 104602
- Import ibackup

* Fri Jan 05 2007 Stew Benedict <sbenedict@mandriva.com> 2.27-4mdv2007.1
- rebuild

* Tue Dec 27 2005 Stew Benedict <sbenedict@mandrakesoft.com> 2.27-3mdk
- rebuild

* Fri Nov 19 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.27-2mdk
- rebuild

