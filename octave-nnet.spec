%define	pkgname nnet
%define name	octave-%{pkgname}
%define version 0.1.13
%define release %mkrel 1

Summary:	Feedforward multi-layer neural network for Octave
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/nnet/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.0.0
BuildRequires:	octave-devel >= 3.0.0, MesaGL-devel, MesaGLU-devel
BuildArch:	noarch

%description
Feedforward multi-layer neural network for Octave

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
rm -rf %{buildroot}
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}/COPYING .
mv %{pkgname}/DESCRIPTION .

%clean
%__rm -rf %{buildroot}

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}
