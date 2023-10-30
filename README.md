# parseLATTESxml

<!--- Syntax summary in https://www.markdownguide.org/basic-syntax/ -->

This script parses XML files from [LATTES](https://lattes.cnpq.br/>LATTES) curriculum plataform -- \
Federal Government of Brazil -- to compile bibliographic production.

It will output the file **compiled_lattes.xlsx** containing unique entries for scientific articles, \
books, and chapters for the last 5 years.


## Help instuctions
### System requirements:
1. Python3
2. Python mudules:
  - elementpath
  - pandas
  - XlsxWriter

### Usage:
Your working directory should contain:
- The script **parse_lattes4multiple_xml.py**
- The directory **qualis_2017_2020** containing the QUALIS modules 
- The directory **lattes** containing LATTES curricula in XML format

Before executing the script, make sure you defined the appropriated \
QUALIS module for the area of the Graduate Program.

By default, the script is set for the area of Biodiversidade:
```python:
##
# SELECT APPROPRIATE QUALIS FOR THE AREA
##

from qualis_2017_2020.qualis_biodiversidade import get_qualis
```

If all requeriments ans setting are in place, execute the script in the terminal:
```bash:
$ ./parse_lattes4multiple_xml.py
```
