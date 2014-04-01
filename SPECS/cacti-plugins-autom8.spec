Name:		cacti-plugins-autom8	
Version:	0.35
Release:    	0	
Summary:	Plugin CACTI aggregate
Group:		System/Monitoring
License:	GPLv2
Source0:    	cacti-plugins-autom8-0.35.tgz
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
mkdir -p %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/
mkdir -p %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/
mkdir -p %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/
mkdir -p %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087g/

cp -p   autom8_graph_rules.php  %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/autom8_graph_rules.php                
cp -p   autom8_functions.php    %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/autom8_functions.php              
cp -p   setup.php   %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/setup.php             
cp -p   README  %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/README                
cp -p   autom8_sql.php  %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/autom8_sql.php                
cp -p   autom8_tree_rules.php   %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/autom8_tree_rules.php             
cp -p   LICENSE %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/LICENSE               
cp -p   autom8_utilities.php    %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/autom8_utilities.php              
cp -p   autom8_actions.php  %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/autom8_actions.php                
cp -p   automate_manual.pdf  %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/automate_manual.pdf

cp -p   patches-087e/lib_api_device.php.patch %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/lib_api_device.php.patch               
cp -p   patches-087e/lib_html_utility.patch %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/lib_html_utility.patch               
cp -p   patches-087e/lib_template.php.patch %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/lib_template.php.patch               
cp -p   patches-087e/lib_api_tree.php.patch %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/lib_api_tree.php.patch               
cp -p   patches-087e/host.php.patch %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/host.php.patch               
cp -p   patches-087e/lib_data_query.php.patch   %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/lib_data_query.php.patch             
cp -p   patches-087e/lib_api_automation_tools.php.patch %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/lib_api_automation_tools.php.patch               
cp -p   patches-087e/cli.patch   %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/cli.patch


cp -p   patches-087d/lib_api_device.php.patch   %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/lib_api_device.php.patch             
cp -p   patches-087d/lib_html_utility.patch %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/lib_html_utility.patch               
cp -p   patches-087d/lib_template.php.patch %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/lib_template.php.patch               
cp -p   patches-087d/cli.patch  %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/cli.patch                
cp -p   patches-087d/lib_api_tree.php.patch %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/lib_api_tree.php.patch               
cp -p   patches-087d/host.php.patch %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/host.php.patch               
cp -p   patches-087d/lib_data_query.php.patch   %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/lib_data_query.php.patch             
cp -p   patches-087d/lib_api_automation_tools.php.patch  %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/lib_api_automation_tools.php.patch

cp -p   patches-087g/cacti087g_autom8.patch %{buildroot}/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087g/cacti087g_autom8.patch               



%clean
rm -rf %{buildroot}


%files
%defattr(0664,cacti,cacti,0664)
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/autom8_graph_rules.php
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/autom8_functions.php
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/setup.php
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/README
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/autom8_sql.php
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/autom8_tree_rules.php
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/LICENSE
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/autom8_utilities.php
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/autom8_actions.php
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/automate_manual.pdf


/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/lib_api_device.php.patch
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/lib_html_utility.patch
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/lib_template.php.patch
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/lib_api_tree.php.patch
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/host.php.patch
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/lib_data_query.php.patch
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/lib_api_automation_tools.php.patch
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087e/cli.patch


/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/lib_api_device.php.patch
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/lib_html_utility.patch
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/lib_template.php.patch
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/cli.patch
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/lib_api_tree.php.patch
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/host.php.patch
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/lib_data_query.php.patch
/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087d/lib_api_automation_tools.php.patch

/usr/share/cacti/plugins/cacti-plugins-autom8-0.35/patches-087g/cacti087g_autom8.patch


%changelog
