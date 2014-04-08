%define patches_087d  /usr/share/cacti/plugins/autom8/patches-087d
%define patches_087e  /usr/share/cacti/plugins/autom8/patches-087e
%define patches_087g  /usr/share/cacti/plugins/autom8/patches-087g

Summary:	Plugin CACTI aggregate
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

/usr/share/cacti/plugins/autom8/setup.php
/usr/share/cacti/plugins/autom8/autom8_graph_rules.php
/usr/share/cacti/plugins/autom8/autom8_functions.php
/usr/share/cacti/plugins/autom8/autom8_sql.php
/usr/share/cacti/plugins/autom8/autom8_tree_rules.php
/usr/share/cacti/plugins/autom8/autom8_utilities.php
/usr/share/cacti/plugins/autom8/autom8_actions.php


/usr/share/cacti/plugins/autom8/patches-087e/lib_api_device.php.patch
/usr/share/cacti/plugins/autom8/patches-087e/lib_html_utility.patch
/usr/share/cacti/plugins/autom8/patches-087e/lib_template.php.patch
/usr/share/cacti/plugins/autom8/patches-087e/lib_api_tree.php.patch
/usr/share/cacti/plugins/autom8/patches-087e/host.php.patch
/usr/share/cacti/plugins/autom8/patches-087e/lib_data_query.php.patch
/usr/share/cacti/plugins/autom8/patches-087e/lib_api_automation_tools.php.patch
/usr/share/cacti/plugins/autom8/patches-087e/cli.patch


/usr/share/cacti/plugins/autom8/patches-087d/lib_api_device.php.patch
/usr/share/cacti/plugins/autom8/patches-087d/lib_html_utility.patch
/usr/share/cacti/plugins/autom8/patches-087d/lib_template.php.patch
/usr/share/cacti/plugins/autom8/patches-087d/cli.patch
/usr/share/cacti/plugins/autom8/patches-087d/lib_api_tree.php.patch
/usr/share/cacti/plugins/autom8/patches-087d/host.php.patch
/usr/share/cacti/plugins/autom8/patches-087d/lib_data_query.php.patch
/usr/share/cacti/plugins/autom8/patches-087d/lib_api_automation_tools.php.patch

/usr/share/cacti/plugins/autom8/patches-087g/cacti087g_autom8.patch


%changelog
* Tue Apr 8 2014 Pietro Moretti <MORETTI.PIETRO@ac.bankit.it> 0.35-1
- Add %doc flag
