%define	oname	archive-tar-minitar

Summary:	Provides POSIX archive management from Ruby programs
Name:		rubygem-%{oname}
Version:	0.5.2
Release:	%mkrel 1
License:	GPLv2+ or Ruby
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
BuildArch:	noarch

%description
Archive::Tar::Minitar is a pure-Ruby library and command-line utility that
provides the ability to deal with POSIX tar(1) archive files. The
implementation is based heavily on Mauricio Ferna'ndez's implementation in
rpa-base, but has been reorganised to promote reuse in other projects.

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

mv %{buildroot}%{ruby_gemdir}/bin %{buildroot}%{_prefix}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{_bindir}/minitar

