#
# Conditional build:
# _without_dist_kernel          without distribution kernel
#
%define		_orig_name	3c940

Summary:	Linux driver for the 3Com 3C990 Network Interface Cards
Summary(pl):	Sterownik dla Linuksa do kart sieciowych 3Com 3C990
Name:		kernel-net-%{_orig_name}
Version:	1.0.0a
%define	_rel	10
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.asus.com.tw/pub/ASUS/lan/3com/3c940/046_Linux.zip
# Source0-md5:	38b555a929576527b034c14585b507d0
%{!?_without_dist_kernel:BuildRequires:	kernel-headers }
BuildRequires:	%{kgcc_package}
BuildRequires:	rpmbuild(macros) >= 1.118
%{!?_without_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
empty

%package -n kernel-smp-net-%{_orig_name}
Summary:	Linux SMP driver for the 3Com 3C990 Network Interface Cards
Summary(pl):	Sterownik dla Linuksa SMP dla kart sieciowych 3Com 3C990
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{!?_without_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-net-%{_orig_name}
This driver (3c990.c) has been written to work with the 3c990 product
line of network cards, manufactured by 3Com Corp on SMP systems.

This driver is not intended for any other product line, including the
3c59x or 3c90x product lines (although drivers with both of these
names, and for both of these product lines, are available).

%description -n kernel-smp-net-%{_orig_name} -l pl
Sterownik dla Linuksa SMP do kart sieciowych 3Com 3c990.

Nie obs�uguje kart serii 3c59x i 3c90x, istniej� inne sterowniki do
tych linii produkt�w.

%prep
%setup -q -n 3c940 -c
cd Linux/
tar -zxvf 3c2000.tar.gz

%build
cd Linux/3c2000

rm -f 3c2000.o
%{__make}
mv -f 3c2000.o %{_orig_name}-smp.o
%{__make}
mv -f 3c2000.o %{_orig_name}.o

%install
cd Linux/3c2000
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/misc

install %{_orig_name}-smp.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/%{_orig_name}.o
install %{_orig_name}.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/%{_orig_name}.o

%clean
rm -rf $RPM_BUILD_ROOT

%post
%depmod %{_kernel_ver}

%postun
%depmod %{_kernel_ver}

%post	-n kernel-smp-net-%{_orig_name}
%depmod %{_kernel_ver}smp

%postun -n kernel-smp-net-%{_orig_name}
%depmod %{_kernel_ver}smp

%files
%defattr(644,root,root,755)
%doc README
/lib/modules/%{_kernel_ver}/misc/*

%files -n kernel-smp-net-%{_orig_name}
%defattr(644,root,root,755)
%doc README
/lib/modules/%{_kernel_ver}smp/misc/*
