#
# Conditional build:
%bcond_without	dist_kernel	# without distribution kernel
#
%define		_orig_name	3c940

Summary:	Linux driver for the 3Com 3C940/3C2000 Network Interface Cards
Summary(pl):	Sterownik dla Linuksa do kart sieciowych 3Com 3C940/3C2000
Name:		kernel-net-%{_orig_name}
Version:	6.01
%define	_rel	0.beta01.1
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.asus.com.tw/pub/ASUS/lan/3com/3c940/046_Linux.zip
# Source0-md5:	38b555a929576527b034c14585b507d0
%{?with_dist_kernel:BuildRequires:	kernel-headers}
BuildRequires:	%{kgcc_package}
BuildRequires:	rpmbuild(macros) >= 1.118
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux driver for the 3Com 3C940/3C2000 Gigabit Network Interface
Cards.

%description -l pl
Sterownik dla Linuksa do gigabitowych kart sieciowych 3Com
3C940/3C2000.

%package -n kernel-smp-net-%{_orig_name}
Summary:	Linux SMP driver for the 3Com 3C940/3C2000 Network Interface Cards
Summary(pl):	Sterownik dla Linuksa SMP dla kart sieciowych 3Com 3C940/3C2000
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-net-%{_orig_name}
Linux SMP driver for the 3Com 3C940/3C2000 Gigabit Network Interface
Cards.

%description -n kernel-smp-net-%{_orig_name} -l pl
Sterownik dla Linuksa SMP dla gigabitowych kart sieciowych 3Com
3C940/3C2000.

%prep
%setup -q -c
cd Linux
tar xzf 3c2000.tar.gz

%build
cd Linux/3c2000

rm -f 3c2000.o
%{__make}
mv -f 3c2000.o %{_orig_name}-smp.o
%{__make}
mv -f 3c2000.o %{_orig_name}.o

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/misc

cd Linux/3c2000
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
%doc Linux/readme
/lib/modules/%{_kernel_ver}/misc/*

%files -n kernel-smp-net-%{_orig_name}
%defattr(644,root,root,755)
%doc Linux/readme
/lib/modules/%{_kernel_ver}smp/misc/*
