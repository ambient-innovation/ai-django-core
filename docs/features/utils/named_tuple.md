## Named tuple

### get_namedtuple_choices()

// todo tbr

### Get value from tuple by key

If you have a tuple ``my_tuple`` and you want to get the value for the key `my_key`, you can use the
straight-forward helper function ``get_value_from_tuple_by_key()``:

```
my_tuple = (
    1, 'Value One',
    2, 'Value Two',
)

my_value = get_value_from_tuple_by_key(my_tuple, 1)
# my_value = 'Value One'
```

### Get key from tuple by value

If you have a tuple ``my_tuple`` and you want to get the key for the value `my_key`, you can use the
straight-forward helper function ``get_key_from_tuple_by_value()``:

```
my_tuple = (
    1, 'Value One',
    2, 'Value Two',
)

my_value = get_key_from_tuple_by_value(my_tuple, 'Value One')
# my_value = 1
```
