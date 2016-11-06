Name:           sshguard
Version:        1.7.1
Release:        1.el6
Summary:        Protects from brute force attacks against ssh
Group:          System Environment/Daemons
License:        ISC
URL:            http://www.sshguard.net
Source0:        https://sourceforge.net/projects/sshguard/files/sshguard/1.7.1/sshguard-1.7.1.tar.gz/download

BuildRequires: gcc make

%description
 Protects from brute force attacks against ssh
 Protects networked hosts from the today's widespread
 brute force attacks against ssh servers. It detects such attacks
 and blocks the author's address with a firewall rule.

%prep
%setup -q


%build
%configure --with-firewall=iptables
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
mkdir -p ${RPM_BUILD_ROOT}/etc/init.d
mkdir -p ${RPM_BUILD_ROOT}/etc/sshguard
mkdir -p ${RPM_BUILD_ROOT}/etc/sysconfig
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/sshguard
mkdir -p ${RPM_BUILD_ROOT}/usr/share/doc/sshguard/examples
cp -a ${RPM_BUILD_ROOT}/../../SOURCES/etc/init.d/sshguard ${RPM_BUILD_ROOT}/etc/init.d/sshguard
cp -a ${RPM_BUILD_ROOT}/../../SOURCES/etc/sshguard/whitelist ${RPM_BUILD_ROOT}/etc/sshguard/whitelist
cp -a ${RPM_BUILD_ROOT}/../../SOURCES/etc/sysconfig/sshguard ${RPM_BUILD_ROOT}/etc/sysconfig/sshguard
cp -a ${RPM_BUILD_ROOT}/../../SOURCES/usr/lib/sshguard/firewall ${RPM_BUILD_ROOT}/usr/lib/sshguard/firewall
cp -a ${RPM_BUILD_ROOT}/../../SOURCES/usr/share/doc/sshguard/examples/whitelistfile.example ${RPM_BUILD_ROOT}/usr/share/doc/sshguard/examples/whitelistfile.example
cp -a ${RPM_BUILD_ROOT}/../../SOURCES/usr/share/doc/sshguard/copyright ${RPM_BUILD_ROOT}/usr/share/doc/sshguard/copyright

%files
%doc

/etc/init.d/sshguard
/etc/sshguard/whitelist
/etc/sysconfig/sshguard
/usr/lib/sshguard/firewall
/usr/libexec/sshg-fw
/usr/libexec/sshg-logtail
/usr/libexec/sshg-parser
/usr/sbin/sshguard
/usr/share/doc/sshguard/examples/whitelistfile.example
/usr/share/doc/sshguard/copyright
/usr/share/man/man8/sshguard.8.gz

%post
/sbin/chkconfig --add sshguard
/sbin/service sshguard start > /dev/null 2>&1 || :

%preun
if [ $1 = 0 ]
then
	/sbin/service sshguard stop > /dev/null 2>&1 || :
	/sbin/chkconfig --del sshguard
fi

%postun
if [ $1 = 1 ]
then
	/sbin/service sshguard restart > /dev/null 2>&1 || :
fi

%changelog
* Sat Nov 05 2016 Bryce Larson <brycelarsn@gmail.com>
- Initial build using version 1.7.1 from sourceforge.net as well as systemd
  and environment files from the ubuntu package sshguard_1.6.0-1_amd64.deb
