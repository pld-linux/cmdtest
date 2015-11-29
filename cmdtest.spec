Summary:	Black-box testing for Unix command line tools
Name:		cmdtest
Version:	0.9
Release:	1
License:	GPL v3+
Group:		Development/Building
Source0:	http://code.liw.fi/debian/pool/main/c/cmdtest/%{name}_%{version}.orig.tar.gz
# Source0-md5:	5fff5c87c8b01b261f73bd4ae1277ed5
URL:		http://liw.fi/cmdtest/
BuildRequires:	python-cliapp
BuildRequires:	python-coverage-test-runner
BuildRequires:	python-markdown
BuildRequires:	python-ttystatus
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-cliapp
Requires:	python-ttystatus
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cmdtest black box tests Unix command line tools. Roughly, it is given
a command line and input files, and the expected output, and it
verifies that the command line produces the expected output. If not,
it reports a problem, and shows the differences.

%prep
%setup -q

%build
%if %{with tests}
# CoverageTestRunner trips up on build directory;
# remove it first
rm -rf build
%{__python} setup.py check
%endif

%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/yarnlib/*_tests.py*

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README README.yarn
%attr(755,root,root) %{_bindir}/cmdtest
%attr(755,root,root) %{_bindir}/yarn
%{_mandir}/man1/cmdtest.1*
%{_mandir}/man1/yarn.1*
%{py_sitescriptdir}/cmdtestlib.py[co]
%{py_sitescriptdir}/cmdtest-%{version}-py*.egg-info
%dir %{py_sitescriptdir}/yarnlib
%{py_sitescriptdir}/yarnlib/*.py[co]
