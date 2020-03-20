# Packaging Test

## Shell scripting

Make the following changes to the greet.sh script:
- Include the user's username in the greeting.
- Include the current date in the greeting. Optionally, print only the weekday
  name instead of the full date.
- Handle an *optional* argument in the script. The argument is a number indicating
  how many times the user should be greeted. When omitted, the script behaviour
  remains the same (user is greeted once).

## Packaging

Create a debian or rpm (or both!) package for the greet.sh file from this
repository. The package should install greet.sh as an executable script.
(greet.sh doesn't need to have the changes you made above.)

Try to create all the packaging file(s) needed to generate the package.
Ideally, these could be used to create a functioning package.

If you're not sure where to start, check out the resources about debian or rpm
packaging in the links section below, or use a search engine. A good place to
start is also to take a look at some of the existing packages which are
similar. An example of a fairly simple package is lua-basexx.

## Bonus Tasks

### git repository

- Commit all the changes you make (including any packaging files) to your git
  repository.
- Push the repository somewhere where it's publicly accessible (e.g.
  gitlab.com, github.com).

### package demo_libuv

- Package the `demo_libuv.c` file - the created package should contain an
  executable `demo_libuv` binary.

### systemd unit file

- Create a systemd unit file that can be used to run the greet.sh script as a
  oneshot service.

## Resources

- Debian packaging: https://wiki.debian.org/Packaging
- Debian repository with packages: https://salsa.debian.org
- Debian Policy Manual: https://www.debian.org/doc/debian-policy/
- RPM packaging guide: https://rpm-packaging-guide.github.io
- Fedora repository with packages: https://src.fedoraproject.org/
- Fedora Packaging Guidelines: https://docs.fedoraproject.org/en-US/packaging-guidelines/
