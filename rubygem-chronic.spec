#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-chronic
Version  : 0.10.2
Release  : 5
URL      : https://rubygems.org/downloads/chronic-0.10.2.gem
Source0  : https://rubygems.org/downloads/chronic-0.10.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-activesupport
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-simplecov

%description
Chronic
=======
Chronic is a natural language date/time parser written in pure Ruby. See below
for the wide variety of formats Chronic will parse.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n chronic-0.10.2
gem spec %{SOURCE0} -l --ruby > rubygem-chronic.gemspec

%build
gem build rubygem-chronic.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
chronic-0.10.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/chronic-0.10.2
ruby -v -I.:lib:test test*/test_*.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/chronic-0.10.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/HISTORY.md
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/README.md
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/chronic.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/date.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/grabber.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/handler.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/handlers.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/mini_date.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/numerizer.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/ordinal.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/pointer.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeater.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_day.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_day_name.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_day_portion.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_fortnight.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_hour.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_minute.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_month.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_month_name.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_season.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_season_name.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_second.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_time.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_week.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_weekday.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_weekend.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/repeaters/repeater_year.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/scalar.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/season.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/separator.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/sign.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/span.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/tag.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/time.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/time_zone.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/lib/chronic/token.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_chronic.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_daylight_savings.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_handler.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_mini_date.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_numerizer.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_parsing.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_repeater_day_name.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_repeater_day_portion.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_repeater_fortnight.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_repeater_hour.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_repeater_minute.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_repeater_month.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_repeater_month_name.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_repeater_season.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_repeater_time.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_repeater_week.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_repeater_weekday.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_repeater_weekend.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_repeater_year.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_span.rb
/usr/lib64/ruby/gems/2.3.0/gems/chronic-0.10.2/test/test_token.rb
/usr/lib64/ruby/gems/2.3.0/specifications/chronic-0.10.2.gemspec
