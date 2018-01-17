# shellson
JSON command line parser

## Usage
`$ echo '{"key1": "value1"}' | shellson get key1`  
`"value1"`  

`$ cat data.json | shellson get key1`  
`"value1`

`$ echo '{"key1": {"key2": "value1"}}' | shellson get key1 | get key2`  
`"value1"`

## Install
`$ pip install shellson`
