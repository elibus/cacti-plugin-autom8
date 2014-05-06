%define patches_087d  /usr/share/cacti/plugins/autom8/patches-087d
%define patches_087e  /usr/share/cacti/plugins/autom8/patches-087e
%define patches_087g  /usr/share/cacti/plugins/autom8/patches-087g

Summary:	Plugin CACTI autom8
Name:		cacti-plugins-autom8	
Version:	0.35
Release:    	1.bdi6
Group:		System/Monitoring
License:	GPLv2
Source0:    	cacti-plugins-autom8-%{version}.tgz
BuildRoot:  	%(mktemp -ud %{_tmppath}/}%{name}-XXXXXX)
BuildArch:	noarch
Requires:	cacti

%description
Plugin CACTI autom8

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{patches_087d}
mkdir -p %{buildroot}%{patches_087e}
mkdir -p %{buildroot}%{patches_087g}

cp -pr  * %{buildroot}/usr/share/cacti/plugins/autom8/               


%clean
rm -rf %{buildroot}


%files
%defattr(-,cacti,cacti,-)
%doc /usr/share/cacti/plugins/autom8/README
%doc /usr/share/cacti/plugins/autom8/LICENSE
%doc /usr/share/cacti/plugins/autom8/automate_manual.pdf
/usr/share/cacti/plugins/autom8/*.php
/usr/share/cacti/plugins/autom8/patches-087d
/usr/share/cacti/plugins/autom8/patches-087e
/usr/share/cacti/plugins/autom8/patches-087g


%changelog
* Tue Apr 8 2014 Marco Tizzoni <marco.tizzoni@gmail.com> 0.35-1
- Add %doc flag
