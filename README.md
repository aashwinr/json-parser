# json-parser
A simple JSON Parser written in python

> ### How to run?
- Import the `JSON` module
- Pass the JSON file contents to the constructor 
- The instance now acts as whateven the root element in the JSON file is (eg. If the top level element is a string, the instance will be a string)

> ### Object Mapping
| **JSON Representation** | **Resulting Python Object** |
|-------------------------|-----------------------------|
| `Object`                | Dictionary `dict`           |
| `Array`                 | List `list`                 |
| `String`                | String `str`                |
| `Number`                | Float `float`               |
| `true`                  | Boolean True `True`         |
| `false`                 | Boolean False `False`       |
| `null`                  | None `None`                 |
