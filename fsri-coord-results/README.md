# Coordinated Attack Results

Welcome to Coordinated Attack Results!  This text is placeholder and should be updated by the project maintainer.

This project uses [jekyll](https://jekyllrb.com/) to build your project site.

## Running

### Setup

- Need to have ruby/bundler/bower installed - `\curl -sSL https://get.rvm.io | bash -s stable --ruby`
- To install `bundler`: `gem install bundler`
- To install `bower`: `npm install -g bower`

### Running locally

```bash
rvm use 2  # tested with Ruby 2.3+
bundle install
bower install
bundle exec jekyll serve  # to serve content locally on localhost:4000
```

## Building

```bash
JEKYLL_ENV=production bundle exec jekyll build --config "_config.yml,_config.prod.yml"  # builds the complete site to the `_site` folder, minifying CSS/JS in the process
```


## Windows development

For information about developing for this project using a Windows machine, see <https://ulfirefightersafety.org/private/docs/windows-development/index.html>.


## Increasing ulimit
```bash
echo ulimit -n 1024 >> ~/.profile #Edits .profile to include new ulimit. Only required once.
source ~/.profile #Needs to be run after computer restart.
```
