# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/httperror
%global commit          86b7830d14cca73aeceaaf08bd620c49a148dd7b

%global common_description %{expand:
Common basic building blocks for custom HTTP frameworks.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Common basic building blocks for custom HTTP frameworks
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git86b7830
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420git86b7830
- First package for Fedora

