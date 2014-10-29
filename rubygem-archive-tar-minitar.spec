%define	oname	archive-tar-minitar

Summary:	Provides POSIX archive management from Ruby programs
Name:		rubygem-%{oname}
Version:	0.5.2
Release:	4
License:	GPLv2+ or Ruby
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
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
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

mv %{buildroot}%{ruby_gemdir}/bin %{buildroot}%{_prefix}


%clean

%files
%doc %{gem_dir}/doc/%{oname}-%{version}
%{gem_dir}/cache/%{oname}-%{version}.gem
%{gem_dir}/gems/%{oname}-%{version}
%{gem_dir}/specifications/%{oname}-%{version}.gemspec
%{_bindir}/minitar



