# iaupload

## NAME

`iaupload` - Upload files to [Internet Archive](http://archive.org).

## SYNOPSIS

```
usage: iaupload.py [-h] [--config CONFIG] [--metadata METADATA]
       --identifier IDENTIFIER file [file ...]
```

## DESCRIPTION

`iaupload` is a Python script I'm using to upload files to the [San Francisco Perl Mongers Collection on Internet Archive](http://archive.org/details/sfperlmongers).

This script uses the [internetarchive Python Library](https://github.com/jjjake/ia-wrapper).

## OPTIONS

### --config

Defines the configuration file for the script.

This file contains your Internet Archive S3 API credentials. You may retrieve your credentials from [your Internet Archive patron record](http://www.archive.org/account/s3.php).

The configuration file must be a [YAML](http://www.yaml.org) file containing two elements:

```
aws_access_key_id: 00000000000000000
aws_secret_access_key: 00000000000000000
```

Both elements are required for the script to operate.

An [example configuration file](./iaupload.yaml.example) is included in this repository.

If this option is not defined at the command line, it will default to a value of `./iaupload.yaml`.

### --identifier

Defines the [identifier](https://github.com/vmbrasseur/IAS3API/blob/master/appendices/terminology.md#identifier) for your Internet Archive item.

This identifier must be unique across the entire Internet Archive.

This is a required option.

### --metadata

Defines the file containing the metadata for the item. [See here](https://github.com/vmbrasseur/IAS3API/blob/master/metadata.md) to learn more about the metadata options for Internet Archive items.

This metadata file must be a [YAML](http://www.yaml.org) file and can contain as many elements as you need to describe your item.

An [example metadata file](./md.yaml.example) is included in this repository

If this options is not defined at the command line, it will default to a value of `./md.yaml'.

## EXAMPLE

```
./iaupload.py --identifier=mytestitem --config=./iauploadconfig.yaml --metadata=mytestitem_md.yaml \
~/Desktop/file1.jpg ~/Desktop/file2.jpg ~/Desktop/file3.jpg
```

## AUTHOR

This script is written and maintained by [VM Brasseur](http://vmbrasseur.com).

## REPORTING BUGS

If you use this script and would like to report bugs or suggest enhancements, please use the [issues](https://github.com/vmbrasseur/iaupload/issues) on this repo.

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
* [iadownload](https://github.com/vmbrasseur/iadownload)
