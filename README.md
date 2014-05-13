# iaupload

## NAME

`iaupload` - Upload files to [Internet Archive](http://archive.org).

## SYNOPSIS

`iaupload`

## DESCRIPTION

`iaupload` is a Python script I'm using to upload files to the [San Francisco Perl Mongers Collection on Internet Archive](http://archive.org/details/sfperlmongers).

This script uses the [internetarchive Python Library](https://github.com/jjjake/ia-wrapper).

As of the initial commit of this script, many important bits of information are hardcoded:

* Item identifier
* Files to upload
* Location/name of the configuration file
* Location/name of the metadata file
* Etc.

Eventually these will all be parameterized and configurable at the command line. Please check the issues in this repo if you'd like to help with that work.

## EXAMPLE

Edit script to set variables accordingly…then:

```
iaupload
```

## AUTHOR

This script is written and maintained by [VM Brasseur](http://vmbrasseur.com).

## REPORTING BUGS

If you use this script and would like to report bugs or suggest enhancements, please use the issues on this repo.

## CONTRIBUTING

If you'd like to contribute to this project (docs, code, tests, etc.), please send a pull request.

## COPYRIGHT AND LICENSE

All work on this project is copyright the authors of said work.

The source code for this project is licensed under the Apache License v2.0.

All documentation, web or other content are licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.

Please see the `LICENSE` file for copies of these licenses.

## SEE ALSO

* [ia-wrapper](https://github.com/jjjake/ia-wrapper)
* [IAS3API Documentation](https://github.com/vmbrasseur/IAS3API)
